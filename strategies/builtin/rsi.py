"""
RSI Mean-Reversion Strategy
Buy when RSI < 30 (oversold), sell when RSI > 70 (overbought)
"""

import pandas as pd
import numpy as np


def rsi_mean_reversion(data: pd.DataFrame, period: int = 14, 
                       oversold: int = 30, overbought: int = 70) -> pd.Series:
    """
    RSI Mean-Reversion Strategy
    
    Args:
        data: DataFrame with 'close' column
        period: RSI calculation period (default 14)
        oversold: Oversold threshold (default 30)
        overbought: Overbought threshold (default 70)
    
    Returns:
        Series with signals: 1 (buy), -1 (sell), 0 (hold)
    """
    # Calculate RSI
    rsi = calculate_rsi(data, period)
    
    # Generate signals
    signals = pd.Series(0, index=data.index)
    
    # Buy when RSI crosses below oversold threshold
    signals[(rsi < oversold) & (rsi.shift(1) >= oversold)] = 1
    
    # Sell when RSI crosses above overbought threshold
    signals[(rsi > overbought) & (rsi.shift(1) <= overbought)] = -1
    
    return signals


def calculate_rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculate RSI (Relative Strength Index)
    
    Args:
        data: DataFrame with 'close' column
        period: RSI period (default 14)
    
    Returns:
        Series with RSI values (0-100)
    """
    # Calculate price changes
    delta = data['close'].diff()
    
    # Separate gains and losses
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    
    # Calculate average gains and losses
    avg_gains = gains.rolling(window=period, min_periods=period).mean()
    avg_losses = losses.rolling(window=period, min_periods=period).mean()
    
    # Calculate RS and RSI
    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1 + rs))
    
    return rsi
