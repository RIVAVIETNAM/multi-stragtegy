"""
Analytics - Leaderboard and Comparison Tools
"""

import pandas as pd
from typing import Dict
from engine.backtest import BacktestResult


def create_leaderboard(results: Dict[str, BacktestResult]) -> pd.DataFrame:
    """
    Create strategy comparison leaderboard
    
    Args:
        results: Dict of {strategy_name: BacktestResult}
    
    Returns:
        DataFrame sorted by Sharpe ratio
    """
    comparison = pd.DataFrame({
        name: {
            'Total Return (%)': round(res.total_return, 2),
            'Sharpe Ratio': round(res.sharpe_ratio, 2),
            'Max Drawdown (%)': round(res.max_drawdown, 2),
            'Win Rate (%)': round(res.win_rate, 2),
            'Profit Factor': round(res.profit_factor, 2),
            'Number of Trades': res.num_trades
        }
        for name, res in results.items()
    }).T
    
    # Sort by Sharpe Ratio (descending)
    comparison = comparison.sort_values('Sharpe Ratio', ascending=False)
    
    return comparison


def rank_strategies(results: Dict[str, BacktestResult], metric: str = 'sharpe_ratio') -> list:
    """
    Rank strategies by a specific metric
    
    Args:
        results: Dict of BacktestResults
        metric: Metric to rank by (total_return, sharpe_ratio, etc.)
    
    Returns:
        List of (strategy_name, metric_value) sorted by metric
    """
    rankings = [(name, getattr(res, metric)) for name, res in results.items()]
    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings


def get_best_strategy(results: Dict[str, BacktestResult], metric: str = 'sharpe_ratio') -> tuple:
    """
    Get the best performing strategy
    
    Returns:
        (strategy_name, BacktestResult)
    """
    best = max(results.items(), key=lambda x: getattr(x[1], metric))
    return best


def create_summary_stats(results: Dict[str, BacktestResult]) -> pd.DataFrame:
    """
    Create summary statistics table
    """
    stats = {
        'Best Return': f"{max(res.total_return for res in results.values()):.2f}%",
        'Best Sharpe': f"{max(res.sharpe_ratio for res in results.values()):.2f}",
        'Lowest Drawdown': f"{max(res.max_drawdown for res in results.values()):.2f}%",
        'Avg Win Rate': f"{sum(res.win_rate for res in results.values())/len(results):.2f}%",
        'Total Strategies': len(results)
    }
    
    return pd.DataFrame([stats])
