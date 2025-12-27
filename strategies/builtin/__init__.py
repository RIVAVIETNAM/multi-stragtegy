"""Built-in Strategies Package"""

import pandas as pd
from .macd import macd_crossover, calculate_macd
from .rsi import rsi_mean_reversion, calculate_rsi
from .bollinger import bollinger_bands, calculate_bollinger_bands
from .sma import sma_crossover, calculate_sma
from .buy_hold import buy_hold
from .portfolio_combined import portfolio_combined, create_combined_strategy

__all__ = [
    'macd_crossover',
    'rsi_mean_reversion',
    'bollinger_bands',
    'sma_crossover',
    'buy_hold',
    'portfolio_combined',
    'create_combined_strategy',
    'calculate_macd',
    'calculate_rsi',
    'calculate_bollinger_bands',
    'calculate_sma'
]

# Create combined portfolio strategy (MACD + RSI)
def momentum_mean_reversion_combined(data: pd.DataFrame) -> pd.Series:
    """Combined Portfolio: MACD (Momentum) + RSI (Mean-Reversion)"""
    return portfolio_combined(data, [macd_crossover, rsi_mean_reversion])

# Strategy metadata
STRATEGIES = {
    'MACD Crossover': {
        'function': macd_crossover,
        'params': {'fast': 12, 'slow': 26, 'signal': 9},
        'description': 'Buy when MACD crosses above signal line',
        'type': 'Momentum'
    },
    'RSI Mean-Reversion': {
        'function': rsi_mean_reversion,
        'params': {'period': 14, 'oversold': 30, 'overbought': 70},
        'description': 'Buy at RSI < 30, Sell at RSI > 70',
        'type': 'Mean-Reversion'
    },
    'Bollinger Bands': {
        'function': bollinger_bands,
        'params': {'window': 20, 'num_std': 2.0},
        'description': 'Buy at lower band, sell at upper band',
        'type': 'Volatility'
    },
    'SMA Crossover': {
        'function': sma_crossover,
        'params': {'short_window': 10, 'long_window': 30},
        'description': 'Golden/Death cross detection',
        'type': 'Trend'
    },
    'Buy & Hold': {
        'function': buy_hold,
        'params': {},
        'description': 'Buy at start, hold until end (benchmark)',
        'type': 'Benchmark'
    },
    'Combined Portfolio (Momentum + Mean-Reversion)': {
        'function': momentum_mean_reversion_combined,
        'params': {},
        'description': 'Equal-weight combination of MACD and RSI strategies',
        'type': 'Portfolio'
    }
}
