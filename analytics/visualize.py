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
    Create overlay plot of all strategy equity curves
    
    Args:
        results: Dict of BacktestResults
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure()
    
    for name, res in results.items():
        fig.add_trace(go.Scatter(
            x=res.equity_curve.index,
            y=res.equity_curve.values,
            name=name,
            mode='lines',
            line=dict(width=2),
            hovertemplate='%{y:,.0f} VND<extra></extra>'
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Portfolio Value (VND)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def plot_drawdown(result: BacktestResult) -> go.Figure:
    """
    Plot drawdown chart for a single strategy
    """
    equity = result.equity_curve
    peak = equity.expanding().max()
    drawdown = ((equity - peak) / peak) * 100
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=drawdown.index,
        y=drawdown.values,
        fill='tozeroy',
        name='Drawdown',
        line=dict(color='red', width=1),
        hovertemplate='%{y:.2f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title=f"Drawdown - {result.strategy_name}",
        xaxis_title='Date',
        yaxis_title='Drawdown (%)',
        hovermode='x',
        template='plotly_white',
        height=400
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
