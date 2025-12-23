"""
MACD Crossover Strategy
Buy when MACD line crosses above signal line, sell when crosses below
"""

import pandas as pd
import numpy as np


def macd_crossover(data: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.Series:
    """
    MACD Crossover Strategy
    
    Args:
        data: DataFrame with 'close' column
        fast: Fast EMA period (default 12)
        slow: Slow EMA period (default 26)
        signal: Signal line period (default 9)
    
    Returns:
        Series with signals: 1 (buy), -1 (sell), 0 (hold)
    """
    # Calculate MACD
    ema_fast = data['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = data['close'].ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    
    # Generate signals
    signals = pd.Series(0, index=data.index)
    
    # Buy when MACD crosses above signal
    signals[(macd_line > signal_line) & (macd_line.shift(1) <= signal_line.shift(1))] = 1
    
    # Sell when MACD crosses below signal
    signals[(macd_line < signal_line) & (macd_line.shift(1) >= signal_line.shift(1))] = -1
    
    return signals


def calculate_macd(data: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    """
    Calculate MACD indicator values for visualization
    
    Returns:
        DataFrame with macd, signal, and histogram columns
    """
    ema_fast = data['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = data['close'].ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    
    result = pd.DataFrame({
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    }, index=data.index)
    
    return result
