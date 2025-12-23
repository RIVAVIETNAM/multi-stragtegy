"""
Vietnamese Market Rules Enforcement
Implements ±7% price limit, T+2 settlement, and other VN-specific constraints
"""

import pandas as pd
import numpy as np


def enforce_price_band(data: pd.DataFrame, limit: float = 0.07) -> pd.DataFrame:
    """
    Enforce HOSE ±7% daily price limit
    
    Args:
        data: DataFrame with 'close' and 'prev_close' columns
        limit: Price band limit (default 0.07 for ±7%)
    
    Returns:
        DataFrame with prices clipped to allowed range
    """
    if 'prev_close' not in data.columns:
        data['prev_close'] = data['close'].shift(1)
    
    # Calculate floor and ceiling
    data['floor_price'] = data['prev_close'] * (1 - limit)
    data['ceiling_price'] = data['prev_close'] * (1 + limit)
    
    # Clip close price to allowed range
    data['close'] = data['close'].clip(
        lower=data['floor_price'],
        upper=data['ceiling_price']
    )
    
    # Also clip high/low if they exist
    if 'high' in data.columns:
        data['high'] = data['high'].clip(upper=data['ceiling_price'])
    if 'low' in data.columns:
        data['low'] = data['low'].clip(lower=data['floor_price'])
    
    return data


def model_t2_settlement(trades: pd.DataFrame) -> pd.DataFrame:
    """
    Model T+2 cash settlement delay
    Cash from selling stock arrives 2 business days later
    
    Args:
        trades: DataFrame with 'cash_received' column
    
    Returns:
        DataFrame with 'cash_available' column (T+2 delayed)
    """
    trades['cash_available'] = trades['cash_received'].shift(2)
    trades['cash_available'].fillna(0, inplace=True)
    return trades


def model_t3_settlement(trades: pd.DataFrame) -> pd.DataFrame:
    """
    Model T+3 stock settlement delay
    Can't sell newly purchased stock for 3 business days
    
    Args:
        trades: DataFrame with 'shares_bought' column
    
    Returns:
        DataFrame with 'shares_available' column (T+3 delayed)
    """
    trades['shares_available'] = trades['shares_bought'].shift(3)
    trades['shares_available'].fillna(0, inplace=True)
    return trades


def apply_vn_trading_hours(data: pd.DataFrame) -> pd.DataFrame:
    """
    Filter data to Vietnamese trading hours
    Morning: 9:00 AM - 11:30 AM
    Afternoon: 1:00 PM - 3:00 PM
    Timezone: GMT+7
    
    Args:
        data: DataFrame with datetime index
    
    Returns:
        Filtered DataFrame
    """
    if not isinstance(data.index, pd.DatetimeIndex):
        return data
    
    # Filter to trading hours
    morning = (data.index.hour >= 9) & (data.index.hour < 12)
    afternoon = (data.index.hour >= 13) & (data.index.hour < 15)
    trading_hours = morning | afternoon
    
    return data[trading_hours]


def calculate_vn_transaction_cost(trade_value: float, fee_rate: float = 0.0015) -> float:
    """
    Calculate Vietnamese transaction costs
    
    Args:
        trade_value: Value of trade in VND
        fee_rate: Brokerage fee rate (default 0.15%)
    
    Returns:
        Total transaction cost
    """
    # Brokerage fee (0.15% typical)
    brokerage = trade_value * fee_rate
    
    # Tax on sale (0.1% for stocks)
    tax = trade_value * 0.001
    
    # Total cost
    total_cost = brokerage + tax
    
    return total_cost
