"""
Backtest Engine - Core execution module
Implements vectorized parallel backtesting with VN market rules
"""

import pandas as pd
import numpy as np
from typing import Dict, Callable, List, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from data.vn_rules import enforce_price_band, calculate_vn_transaction_cost


@dataclass
class BacktestResult:
    """Container for backtest results"""
    strategy_name: str
    equity_curve: pd.Series
    trades: pd.DataFrame
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    profit_factor: float
    num_trades: int
    
    
def run_backtest(data: pd.DataFrame, 
                 signals: pd.Series,
                 strategy_name: str = "Strategy",
                 initial_capital: float = 100_000_000,
                 transaction_cost: float = 0.0015,
                 enforce_vn_rules: bool = True) -> BacktestResult:
    """
    Run backtest for a single strategy
    
    Args:
        data: Price data DataFrame
        signals: Trading signals (1=buy, -1=sell, 0=hold)
        strategy_name: Name of strategy
        initial_capital: Starting capital in VND
        transaction_cost: Transaction cost rate (default 0.15%)
        enforce_vn_rules: Apply VN market rules (default True)
    
    Returns:
        BacktestResult object with performance metrics
    """
    # Apply VN price limits if enabled
    if enforce_vn_rules:
        data = enforce_price_band(data.copy())
    
    # Initialize portfolio
    cash = initial_capital
    shares = 0
    equity = []
    trades_list = []
    
    # Debug: Track signal positions
    buy_signals = signals[signals == 1].index.tolist()
    sell_signals = signals[signals == -1].index.tolist()
    print(f"Backtest {strategy_name}:")
    print(f"  - Buy signals at: {buy_signals[:5]}... (total: {len(buy_signals)})")
    print(f"  - Sell signals at: {sell_signals[:5]}... (total: {len(sell_signals)})")
    
    # Simulate trading
    for i in range(len(data)):
        price = data['close'].iloc[i]
        signal = signals.iloc[i]
        
        # Check for NaN price
        if pd.isna(price) or price <= 0:
            portfolio_value = cash + (shares * (data['close'].iloc[i-1] if i > 0 else initial_capital))
            equity.append(portfolio_value)
            continue
        
        # Buy signal
        if signal == 1:
            if shares == 0:
                # Calculate shares to buy (account for transaction cost)
                # We need: shares * price + fee <= cash
                # fee = (shares * price) * transaction_cost
                # So: shares * price * (1 + transaction_cost) <= cash
                # shares <= cash / (price * (1 + transaction_cost))
                max_shares = int(cash / (price * (1 + transaction_cost + 0.001)))  # +0.001 for tax
                
                if max_shares > 0:
                    cost = max_shares * price
                    fee = calculate_vn_transaction_cost(cost, transaction_cost)
                    total_cost = cost + fee
                    
                    if cash >= total_cost:
                        shares = max_shares
                        cash -= total_cost
                        
                        trades_list.append({
                            'date': data.index[i],
                            'type': 'BUY',
                            'price': price,
                            'shares': shares,
                            'cost': total_cost
                        })
                        print(f"  - BUY at {data.index[i]}: {shares} shares @ {price:.2f}, cost: {total_cost:.2f}, cash left: {cash:.2f}")
                    else:
                        print(f"  - BUY SKIPPED at {data.index[i]}: not enough cash (need {total_cost:.2f}, have {cash:.2f})")
            else:
                # Already have shares, ignore buy signal
                pass
        
        # Sell signal
        elif signal == -1:
            if shares > 0:
                # Sell all shares
                proceeds = shares * price
                fee = calculate_vn_transaction_cost(proceeds, transaction_cost)
                
                cash += (proceeds - fee)
                
                trades_list.append({
                    'date': data.index[i],
                    'type': 'SELL',
                    'price': price,
                    'shares': shares,
                    'proceeds': proceeds - fee
                })
                
                profit = (proceeds - fee) - trades_list[-2]['cost'] if len(trades_list) >= 2 else 0
                print(f"  - SELL at {data.index[i]}: {shares} shares @ {price:.2f}, proceeds: {proceeds-fee:.2f}, profit: {profit:.2f}")
                
                shares = 0
            else:
                # No shares to sell, ignore sell signal
                pass
        
        # Record equity
        portfolio_value = cash + (shares * price)
        equity.append(portfolio_value)
    
    print(f"  - Total trades executed: {len(trades_list)}")
    print(f"  - Final cash: {cash:.2f}, Final shares: {shares}")
    
    # Create equity curve
    equity_curve = pd.Series(equity, index=data.index)
    trades_df = pd.DataFrame(trades_list)
    
    # Calculate metrics
    total_return = ((equity_curve.iloc[-1] - initial_capital) / initial_capital) * 100
    
    # Sharpe ratio (annualized, assume 252 trading days)
    returns = equity_curve.pct_change().dropna()
    if len(returns) > 0 and returns.std() > 0:
        sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)
    else:
        sharpe_ratio = 0.0
    
    # Maximum drawdown
    peak = equity_curve.expanding().max()
    drawdown = (equity_curve - peak) / peak
    max_drawdown = drawdown.min() * 100
    
    # Win rate and profit factor
    if len(trades_df) >= 2:
        # Pair buy/sell trades
        buy_trades = trades_df[trades_df['type'] == 'BUY']
        sell_trades = trades_df[trades_df['type'] == 'SELL']
        
        profits = []
        for idx in range(min(len(buy_trades), len(sell_trades))):
            buy_cost = buy_trades.iloc[idx]['cost']
            sell_proceeds = sell_trades.iloc[idx]['proceeds']
            profit = sell_proceeds - buy_cost
            profits.append(profit)
        
        if profits:
            wins = [p for p in profits if p > 0]
            losses = [abs(p) for p in profits if p < 0]
            
            win_rate = (len(wins) / len(profits)) * 100 if profits else 0
            
            if losses:
                profit_factor = sum(wins) / sum(losses)
            else:
                profit_factor = float('inf') if wins else 0
        else:
            win_rate = 0
            profit_factor = 0
    else:
        win_rate = 0
        profit_factor = 0
    
    return BacktestResult(
        strategy_name=strategy_name,
        equity_curve=equity_curve,
        trades=trades_df,
        total_return=total_return,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown,
        win_rate=win_rate,
        profit_factor=profit_factor,
        num_trades=len(trades_df)
    )


def run_parallel_backtests(data: pd.DataFrame,
                           strategies: Dict[str, Callable],
                           initial_capital: float = 100_000_000,
                           transaction_cost: float = 0.0015,
                           enforce_vn_rules: bool = True,
                           max_workers: int = 8) -> Dict[str, BacktestResult]:
    """
    Run multiple strategies in parallel
    
    Args:
        data: Price data DataFrame
        strategies: Dict of {strategy_name: strategy_function}
        initial_capital: Starting capital
        transaction_cost: Transaction cost rate
        enforce_vn_rules: Apply VN market rules
        max_workers: Max parallel threads
    
    Returns:
        Dict of {strategy_name: BacktestResult}
    """
    def run_single_strategy(name: str, strategy_func: Callable):
        try:
            signals = strategy_func(data)
            
            # Validate signals
            if signals is None or len(signals) == 0:
                raise ValueError(f"Strategy {name} returned empty signals")
            
            if not isinstance(signals, pd.Series):
                raise ValueError(f"Strategy {name} must return pd.Series, got {type(signals)}")
            
            # Debug: Check signals
            print(f"Strategy {name}:")
            print(f"  - Signals shape: {signals.shape}")
            print(f"  - Signals value counts: {signals.value_counts().to_dict()}")
            print(f"  - Buy signals: {(signals == 1).sum()}")
            print(f"  - Sell signals: {(signals == -1).sum()}")
            print(f"  - Hold signals: {(signals == 0).sum()}")
            
            # Check if signals match data index
            if not signals.index.equals(data.index):
                print(f"  - Warning: Signals index doesn't match data index, reindexing...")
                signals = signals.reindex(data.index, fill_value=0)
            
            result = run_backtest(
                data, signals, name, 
                initial_capital, transaction_cost, enforce_vn_rules
            )
            
            # Debug: Check result
            print(f"  - Total return: {result.total_return:.2f}%")
            print(f"  - Num trades: {result.num_trades}")
            print(f"  - Final equity: {result.equity_curve.iloc[-1]:,.0f}")
            
            return name, result
        except Exception as e:
            # Return empty result on error
            import traceback
            print(f"ERROR in strategy {name}: {e}")
            print(traceback.format_exc())
            # Return a result with zeros
            empty_equity = pd.Series([initial_capital] * len(data), index=data.index)
            empty_trades = pd.DataFrame(columns=['date', 'type', 'price', 'shares', 'cost'])
            from engine.backtest import BacktestResult
            return name, BacktestResult(
                strategy_name=name,
                equity_curve=empty_equity,
                trades=empty_trades,
                total_return=0.0,
                sharpe_ratio=0.0,
                max_drawdown=0.0,
                win_rate=0.0,
                profit_factor=0.0,
                num_trades=0
            )
    
    # Execute in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_single_strategy, name, func) 
                   for name, func in strategies.items()]
        results = {name: result for name, result in [f.result() for f in futures]}
    
    return results
