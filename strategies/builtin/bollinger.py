"""
Bollinger Bands Strategy
Buy at lower band, sell at upper band
"""

import pandas as pd
import numpy as np


def bollinger_bands(data: pd.DataFrame, window: int = 20, num_std: float = 2.0) -> pd.Series:
    """
    Bollinger Bands Strategy
    
    Args:
        data: DataFrame with 'close' column
        window: Rolling window period (default 20)
        num_std: Number of standard deviations (default 2.0)
    
    Returns:
        Series with signals: 1 (buy), -1 (sell), 0 (hold)
    """
    # Calculate Bollinger Bands
    bb = calculate_bollinger_bands(data, window, num_std)
    
    # Generate signals
    signals = pd.Series(0, index=data.index)
    
    # Buy when price touches or crosses below lower band
    signals[(data['close'] <= bb['lower']) & (data['close'].shift(1) > bb['lower'].shift(1))] = 1
    
    # Sell when price touches or crosses above upper band
    signals[(data['close'] >= bb['upper']) & (data['close'].shift(1) < bb['upper'].shift(1))] = -1
    
    return signals


def calculate_bollinger_bands(data: pd.DataFrame, window: int = 20, num_std: float = 2.0) -> pd.DataFrame:
    """
    Calculate Bollinger Bands
    
    Args:
        data: DataFrame with 'close' column
        window: Rolling window period
        num_std: Number of standard deviations
    
    Returns:
        DataFrame with middle, upper, and lower bands
    """
    # Middle band (SMA)
    middle = data['close'].rolling(window=window).mean()
    
    # Standard deviation
    std = data['close'].rolling(window=window).std()
    
    # Upper and lower bands
    upper = middle + (std * num_std)
    lower = middle - (std * num_std)
    
    result = pd.DataFrame({
        'middle': middle,
        'upper': upper,
        'lower': lower
    }, index=data.index)
    
    return result
