"""
Buy & Hold Strategy
Simple benchmark: Buy at the start, hold until the end
"""

import pandas as pd


def buy_hold(data: pd.DataFrame) -> pd.Series:
    """
    Buy & Hold Strategy (Benchmark)
    
    Args:
        data: DataFrame with 'close' column
    
    Returns:
        Series with signals: 1 (buy at start), -1 (sell at end), 0 (hold)
    """
    signals = pd.Series(0, index=data.index)
    
    # Buy at the first day
    if len(signals) > 0:
        signals.iloc[0] = 1
    
    # Sell at the last day (optional, for comparison)
    # signals.iloc[-1] = -1
    
    return signals

