"""
Combined Portfolio Strategy
Combines multiple strategies with equal weight allocation
"""

import pandas as pd
import numpy as np
from typing import List, Callable


def portfolio_combined(data: pd.DataFrame, 
                       strategies: List[Callable],
                       weights: List[float] = None) -> pd.Series:
    """
    Combined Portfolio Strategy
    
    Combines multiple strategies by averaging their signals.
    Each strategy gets equal weight by default.
    
    Args:
        data: DataFrame with 'close' column
        strategies: List of strategy functions (each takes data and returns signals)
        weights: Optional list of weights for each strategy (must sum to 1)
    
    Returns:
        Series with combined signals: 1 (buy), -1 (sell), 0 (hold)
    """
    if not strategies:
        return pd.Series(0, index=data.index)
    
    # Get signals from all strategies
    all_signals = []
    for strategy_func in strategies:
        try:
            signals = strategy_func(data)
            if isinstance(signals, pd.Series):
                all_signals.append(signals)
        except Exception as e:
            print(f"Warning: Strategy {strategy_func.__name__} failed: {e}")
            continue
    
    if not all_signals:
        return pd.Series(0, index=data.index)
    
    # Align all signals to same index
    common_index = data.index
    aligned_signals = [sig.reindex(common_index, fill_value=0) for sig in all_signals]
    
    # Combine signals
    if weights is None:
        # Equal weights
        weights = [1.0 / len(aligned_signals)] * len(aligned_signals)
    
    # Normalize weights
    total_weight = sum(weights)
    if total_weight > 0:
        weights = [w / total_weight for w in weights]
    
    # Weighted average of signals
    combined = pd.Series(0.0, index=common_index)
    for sig, weight in zip(aligned_signals, weights):
        combined += sig * weight
    
    # Convert to discrete signals
    # Buy if combined > 0.3, Sell if combined < -0.3, else Hold
    final_signals = pd.Series(0, index=common_index)
    final_signals[combined > 0.3] = 1
    final_signals[combined < -0.3] = -1
    
    return final_signals


def create_combined_strategy(strategy_funcs: List[Callable], 
                             weights: List[float] = None):
    """
    Factory function to create a combined strategy
    
    Usage:
        from strategies.builtin.macd import macd_crossover
        from strategies.builtin.rsi import rsi_mean_reversion
        
        combined = create_combined_strategy([macd_crossover, rsi_mean_reversion])
        signals = combined(data)
    """
    def combined_strategy(data: pd.DataFrame) -> pd.Series:
        return portfolio_combined(data, strategy_funcs, weights)
    
    return combined_strategy

