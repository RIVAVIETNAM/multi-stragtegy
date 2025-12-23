"""
Strategy Performance Matrix (RRG-like)
Relative Rotation Graph for strategies showing performance over time
Inspired by FC-Terminal's Institutional Sector Matrix
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from engine.backtest import BacktestResult


def calculate_relative_strength(strategy_returns: pd.Series, benchmark_returns: pd.Series, window: int = 20) -> pd.Series:
    """
    Calculate relative strength (RS) of strategy vs benchmark
    
    Args:
        strategy_returns: Strategy returns series
        benchmark_returns: Benchmark returns series
        window: Rolling window for calculation
    
    Returns:
        Relative strength series
    """
    strategy_cum = (1 + strategy_returns).rolling(window).apply(lambda x: x.prod(), raw=True)
    benchmark_cum = (1 + benchmark_returns).rolling(window).apply(lambda x: x.prod(), raw=True)
    
    rs = (strategy_cum / benchmark_cum) - 1
    return rs * 100  # Convert to percentage


def calculate_relative_strength_momentum(rs: pd.Series, window: int = 10) -> pd.Series:
    """
    Calculate momentum of relative strength (rate of change)
    
    Args:
        rs: Relative strength series
        window: Window for momentum calculation
    
    Returns:
        RS momentum series
    """
    return rs.diff(window)


def create_strategy_matrix(
    results: Dict[str, BacktestResult],
    benchmark_name: str = "Benchmark",
    window: int = 20,
    momentum_window: int = 10
) -> go.Figure:
    """
    Create Relative Rotation Graph (RRG) style visualization for strategies
    
    Args:
        results: Dictionary of BacktestResults
        benchmark_name: Name of benchmark strategy (used for relative calculation)
        window: Rolling window for RS calculation
        momentum_window: Window for momentum calculation
    
    Returns:
        Plotly Figure with RRG-style scatter plot
    """
    # Calculate benchmark (average of all strategies or specific one)
    if benchmark_name in results:
        benchmark_result = results[benchmark_name]
        benchmark_returns = benchmark_result.equity_curve.pct_change().dropna()
    else:
        # Use average of all strategies as benchmark
        all_equity = pd.DataFrame({
            name: res.equity_curve for name, res in results.items()
        })
        benchmark_equity = all_equity.mean(axis=1)
        benchmark_returns = benchmark_equity.pct_change().dropna()
    
    # Prepare data for each strategy
    strategy_data = []
    
    for name, result in results.items():
        if name == benchmark_name:
            continue
            
        strategy_returns = result.equity_curve.pct_change().dropna()
        
        # Align indices
        common_idx = strategy_returns.index.intersection(benchmark_returns.index)
        if len(common_idx) < window:
            continue
            
        strategy_returns = strategy_returns.loc[common_idx]
        bench_returns = benchmark_returns.loc[common_idx]
        
        # Calculate RS and RS Momentum
        rs = calculate_relative_strength(strategy_returns, bench_returns, window)
        rs_momentum = calculate_relative_strength_momentum(rs, momentum_window)
        
        # Get latest values
        latest_rs = rs.iloc[-1] if not rs.empty else 0
        latest_momentum = rs_momentum.iloc[-1] if not rs_momentum.empty else 0
        
        # Calculate quadrant
        quadrant = determine_quadrant(latest_rs, latest_momentum)
        
        strategy_data.append({
            'name': name,
            'rs': latest_rs,
            'rs_momentum': latest_momentum,
            'quadrant': quadrant,
            'total_return': result.total_return,
            'sharpe': result.sharpe_ratio,
            'max_dd': result.max_drawdown
        })
    
    if not strategy_data:
        # Fallback: create simple comparison
        return create_simple_matrix(results)
    
    df = pd.DataFrame(strategy_data)
    
    # Create figure
    fig = go.Figure()
    
    # Define quadrant colors
    quadrant_colors = {
        'Leading': '#2ca02c',      # Green
        'Weakening': '#ff7f0e',    # Orange
        'Lagging': '#d62728',      # Red
        'Improving': '#1f77b4'     # Blue
    }
    
    # Plot each quadrant
    for quadrant in ['Leading', 'Weakening', 'Lagging', 'Improving']:
        quadrant_data = df[df['quadrant'] == quadrant]
        if len(quadrant_data) > 0:
            fig.add_trace(go.Scatter(
                x=quadrant_data['rs'],
                y=quadrant_data['rs_momentum'],
                mode='markers+text',
                name=quadrant,
                text=quadrant_data['name'],
                textposition='middle right',
                marker=dict(
                    size=quadrant_data['sharpe'].abs() * 20 + 10,
                    color=quadrant_colors[quadrant],
                    line=dict(width=2, color='white'),
                    opacity=0.7
                ),
                hovertemplate=(
                    '<b>%{text}</b><br>' +
                    'RS: %{x:.2f}%<br>' +
                    'RS Momentum: %{y:.2f}%<br>' +
                    'Return: ' + quadrant_data['total_return'].astype(str) + '%<br>' +
                    'Sharpe: ' + quadrant_data['sharpe'].astype(str) + '<extra></extra>'
                )
            ))
    
    # Add quadrant lines
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    # Add quadrant labels
    fig.add_annotation(
        x=0.5, y=0.5, xref="paper", yref="paper",
        text="<b>LEADING</b>", showarrow=False,
        font=dict(size=14, color=quadrant_colors['Leading']),
        bgcolor="rgba(44, 160, 44, 0.1)", bordercolor=quadrant_colors['Leading'],
        borderwidth=2
    )
    fig.add_annotation(
        x=0.5, y=0.1, xref="paper", yref="paper",
        text="<b>WEAKENING</b>", showarrow=False,
        font=dict(size=14, color=quadrant_colors['Weakening']),
        bgcolor="rgba(255, 127, 14, 0.1)", bordercolor=quadrant_colors['Weakening'],
        borderwidth=2
    )
    fig.add_annotation(
        x=0.1, y=0.1, xref="paper", yref="paper",
        text="<b>LAGGING</b>", showarrow=False,
        font=dict(size=14, color=quadrant_colors['Lagging']),
        bgcolor="rgba(214, 39, 40, 0.1)", bordercolor=quadrant_colors['Lagging'],
        borderwidth=2
    )
    fig.add_annotation(
        x=0.1, y=0.5, xref="paper", yref="paper",
        text="<b>IMPROVING</b>", showarrow=False,
        font=dict(size=14, color=quadrant_colors['Improving']),
        bgcolor="rgba(31, 119, 180, 0.1)", bordercolor=quadrant_colors['Improving'],
        borderwidth=2
    )
    
    # Update layout
    fig.update_layout(
        title="Strategy Performance Matrix (RRG-style)",
        xaxis_title="Relative Strength (RS) vs Benchmark",
        yaxis_title="RS Momentum (Rate of Change)",
        hovermode='closest',
        template='plotly_white',
        height=700,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def determine_quadrant(rs: float, rs_momentum: float) -> str:
    """
    Determine which quadrant a strategy belongs to
    
    Args:
        rs: Relative strength value
        rs_momentum: RS momentum value
    
    Returns:
        Quadrant name: 'Leading', 'Weakening', 'Lagging', or 'Improving'
    """
    if rs >= 0 and rs_momentum >= 0:
        return 'Leading'
    elif rs >= 0 and rs_momentum < 0:
        return 'Weakening'
    elif rs < 0 and rs_momentum < 0:
        return 'Lagging'
    else:  # rs < 0 and rs_momentum >= 0
        return 'Improving'


def create_simple_matrix(results: Dict[str, BacktestResult]) -> go.Figure:
    """
    Create a simpler matrix visualization when RS calculation is not possible
    Uses Sharpe Ratio vs Total Return
    """
    data = []
    for name, result in results.items():
        data.append({
            'name': name,
            'sharpe': result.sharpe_ratio,
            'return': result.total_return,
            'max_dd': result.max_drawdown
        })
    
    df = pd.DataFrame(data)
    
    # Calculate quadrants based on median
    median_sharpe = df['sharpe'].median()
    median_return = df['return'].median()
    
    df['quadrant'] = df.apply(
        lambda row: determine_quadrant_simple(row['sharpe'], row['return'], median_sharpe, median_return),
        axis=1
    )
    
    fig = go.Figure()
    
    quadrant_colors = {
        'Leading': '#2ca02c',
        'Weakening': '#ff7f0e',
        'Lagging': '#d62728',
        'Improving': '#1f77b4'
    }
    
    for quadrant in ['Leading', 'Weakening', 'Lagging', 'Improving']:
        quadrant_data = df[df['quadrant'] == quadrant]
        if len(quadrant_data) > 0:
            fig.add_trace(go.Scatter(
                x=quadrant_data['return'],
                y=quadrant_data['sharpe'],
                mode='markers+text',
                name=quadrant,
                text=quadrant_data['name'],
                textposition='middle right',
                marker=dict(
                    size=abs(quadrant_data['max_dd']) * 2 + 10,
                    color=quadrant_colors[quadrant],
                    line=dict(width=2, color='white'),
                    opacity=0.7
                ),
                hovertemplate=(
                    '<b>%{text}</b><br>' +
                    'Return: %{x:.2f}%<br>' +
                    'Sharpe: %{y:.2f}<br>' +
                    'Max DD: ' + quadrant_data['max_dd'].astype(str) + '%<extra></extra>'
                )
            ))
    
    fig.add_hline(y=median_sharpe, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=median_return, line_dash="dash", line_color="gray", opacity=0.5)
    
    fig.update_layout(
        title="Strategy Performance Matrix (Sharpe vs Return)",
        xaxis_title="Total Return (%)",
        yaxis_title="Sharpe Ratio",
        hovermode='closest',
        template='plotly_white',
        height=600
    )
    
    return fig


def determine_quadrant_simple(sharpe: float, return_val: float, median_sharpe: float, median_return: float) -> str:
    """Determine quadrant for simple matrix"""
    if return_val >= median_return and sharpe >= median_sharpe:
        return 'Leading'
    elif return_val >= median_return and sharpe < median_sharpe:
        return 'Weakening'
    elif return_val < median_return and sharpe < median_sharpe:
        return 'Lagging'
    else:
        return 'Improving'

