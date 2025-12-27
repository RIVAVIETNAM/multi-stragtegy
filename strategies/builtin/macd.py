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
    
    # Track position state
    in_long = False
    
    for i in range(1, len(data)):
        prev_macd = macd_line.iloc[i-1]
        curr_macd = macd_line.iloc[i]
        prev_signal = signal_line.iloc[i-1]
        curr_signal = signal_line.iloc[i]
        
        # Buy signal: MACD crosses above signal
        if not in_long and curr_macd > curr_signal and prev_macd <= prev_signal:
            signals.iloc[i] = 1
            in_long = True
        
        # Sell signal: MACD crosses below signal
        elif in_long and curr_macd < curr_signal and prev_macd >= prev_signal:
            signals.iloc[i] = -1
            in_long = False
    
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
