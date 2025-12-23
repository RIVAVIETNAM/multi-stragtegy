"""
SMA Crossover Strategy  
Golden Cross (buy) / Death Cross (sell)
"""

import pandas as pd
import numpy as np


def sma_crossover(data: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.Series:
    """
    SMA Crossover Strategy (Moving Average Crossover)
    
    Args:
        data: DataFrame with 'close' column
        short_window: Short-term MA period (default 50)
        long_window: Long-term MA period (default 200)
    
    Returns:
        Series with signals: 1 (buy), -1 (sell), 0 (hold)
    """
    # Calculate moving averages
    ma_short = data['close'].rolling(window=short_window).mean()
    ma_long = data['close'].rolling(window=long_window).mean()
    
    # Generate signals
    signals = pd.Series(0, index=data.index)
    
    # Golden Cross: Short MA crosses above Long MA (buy)
    signals[(ma_short > ma_long) & (ma_short.shift(1) <= ma_long.shift(1))] = 1
    
    # Death Cross: Short MA crosses below Long MA (sell)
    signals[(ma_short < ma_long) & (ma_short.shift(1) >= ma_long.shift(1))] = -1
    
    return signals


def calculate_sma(data: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.DataFrame:
    """
    Calculate Simple Moving Averages for visualization
    
    Returns:
        DataFrame with short and long MA columns
    """
    ma_short = data['close'].rolling(window=short_window).mean()
    ma_long = data['close'].rolling(window=long_window).mean()
    
    result = pd.DataFrame({
        f'ma_{short_window}': ma_short,
        f'ma_{long_window}': ma_long
    }, index=data.index)
    
    return result
