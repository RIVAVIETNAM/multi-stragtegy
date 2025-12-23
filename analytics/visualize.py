"""
Visualization - Charts and Plots
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict
from engine.backtest import BacktestResult


def plot_equity_curves(results: Dict[str, BacktestResult], title: str = "Multi-Strategy Equity Curves") -> go.Figure:
    """
    Create overlay plot of all strategy equity curves with enhanced styling
    
    Args:
        results: Dict of BacktestResults
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure()
    
    # Color palette for strategies
    colors = px.colors.qualitative.Set2
    
    for idx, (name, res) in enumerate(results.items()):
        color = colors[idx % len(colors)]
        
        # Convert color to rgba safely
        # px.colors.qualitative.Set2 returns RGB strings like 'rgb(102,194,165)'
        try:
            if isinstance(color, str):
                if color.startswith('rgb('):
                    # Parse RGB string: 'rgb(102,194,165)' -> (102, 194, 165)
                    rgb_str = color.replace('rgb(', '').replace(')', '')
                    rgb = tuple(int(x.strip()) for x in rgb_str.split(','))
                    rgba_fill = f'rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 0.1)'
                elif color.startswith('#'):
                    # Hex color: '#66c2a5'
                    rgb = px.colors.hex_to_rgb(color)
                    rgba_fill = f'rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 0.1)'
                else:
                    # Named color or other format
                    rgba_fill = 'rgba(128, 128, 128, 0.1)'
            elif isinstance(color, (tuple, list)) and len(color) >= 3:
                # Already RGB tuple
                rgba_fill = f'rgba({color[0]}, {color[1]}, {color[2]}, 0.1)'
            else:
                rgba_fill = 'rgba(128, 128, 128, 0.1)'
        except (ValueError, TypeError, AttributeError, IndexError):
            # If conversion fails, use default gray
            rgba_fill = 'rgba(128, 128, 128, 0.1)'
        
        fig.add_trace(go.Scatter(
            x=res.equity_curve.index,
            y=res.equity_curve.values,
            name=name,
            mode='lines',
            line=dict(width=3, color=color),
            hovertemplate=f'<b>{name}</b><br>Date: %{{x}}<br>Value: %{{y:,.0f}} VND<extra></extra>',
            fill='tonexty' if idx > 0 else None,
            fillcolor=rgba_fill if idx > 0 else None
        ))
    
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=20, color='#1f77b4'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            showline=True,
            linecolor='rgba(128, 128, 128, 0.5)'
        ),
        yaxis=dict(
            title='Portfolio Value (VND)',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            showline=True,
            linecolor='rgba(128, 128, 128, 0.5)',
            tickformat=',.0f'
        ),
        hovermode='x unified',
        template='plotly_white',
        height=600,
        plot_bgcolor='rgba(255, 255, 255, 0.9)',
        paper_bgcolor='white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='rgba(128, 128, 128, 0.3)',
            borderwidth=1
        ),
        margin=dict(l=60, r=20, t=80, b=60)
    )
    
    return fig


def plot_drawdown(result: BacktestResult) -> go.Figure:
    """
    Plot drawdown chart for a single strategy with enhanced styling
    """
    equity = result.equity_curve
    peak = equity.expanding().max()
    drawdown = ((equity - peak) / peak) * 100
    
    fig = go.Figure()
    
    # Use gradient fill for drawdown
    fig.add_trace(go.Scatter(
        x=drawdown.index,
        y=drawdown.values,
        fill='tozeroy',
        name='Drawdown',
        line=dict(color='#d62728', width=2),
        fillcolor='rgba(214, 39, 40, 0.3)',
        hovertemplate=f'<b>{result.strategy_name}</b><br>Date: %{{x}}<br>Drawdown: %{{y:.2f}}%<extra></extra>'
    ))
    
    # Add max drawdown line
    max_dd = drawdown.min()
    max_dd_date = drawdown.idxmin()
    fig.add_annotation(
        x=max_dd_date,
        y=max_dd,
        text=f'Max DD: {max_dd:.2f}%',
        showarrow=True,
        arrowhead=2,
        arrowcolor='#d62728',
        bgcolor='rgba(214, 39, 40, 0.8)',
        bordercolor='#d62728',
        font=dict(color='white', size=12)
    )
    
    fig.update_layout(
        title=dict(
            text=f"Drawdown Analysis - {result.strategy_name}",
            font=dict(size=18, color='#d62728'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        yaxis=dict(
            title='Drawdown (%)',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        hovermode='x',
        template='plotly_white',
        height=450,
        plot_bgcolor='rgba(255, 255, 255, 0.9)',
        paper_bgcolor='white'
    )
    
    return fig


def plot_metrics_comparison(results: Dict[str, BacktestResult]) -> go.Figure:
    """
    Create radar chart comparing key metrics across strategies
    """
    strategies = list(results.keys())
    
    # Normalize metrics to 0-100 scale for radar chart
    metrics = {
        'Return': [res.total_return for res in results.values()],
        'Sharpe': [res.sharpe_ratio * 10 for res in results.values()],  # Scale up
        'Win Rate': [res.win_rate for res in results.values()],
        'Profit Factor': [min(res.profit_factor * 10, 100) for res in results.values()],  # Cap at 100
    }
    
    fig = go.Figure()
    
    for i, strategy in enumerate(strategies):
        values = [metrics[m][i] for m in metrics.keys()]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=list(metrics.keys()),
            fill='toself',
            name=strategy
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Strategy Performance Comparison",
        height=500
    )
    
    return fig


def plot_returns_distribution(result: BacktestResult) -> go.Figure:
    """
    Plot distribution of daily returns
    """
    returns = result.equity_curve.pct_change().dropna() * 100
    
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=returns,
        nbinsx=50,
        name='Returns',
        marker_color='steelblue'
    ))
    
    fig.update_layout(
        title=f"Returns Distribution - {result.strategy_name}",
        xaxis_title='Daily Return (%)',
        yaxis_title='Frequency',
        template='plotly_white',
        height=400
    )
    
    return fig
