"""
UI Helper Functions
Custom styling and UI components for Streamlit
"""

import streamlit as st
from pathlib import Path


def load_custom_css():
    """Load custom CSS file"""
    try:
        # Try relative to utils folder
        css_file = Path(__file__).parent.parent / "assets" / "custom.css"
        if not css_file.exists():
            # Try alternative path
            css_file = Path(__file__).parent.parent.parent / "app" / "assets" / "custom.css"
        if css_file.exists():
            with open(css_file, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        # Silently fail if CSS can't be loaded
        pass


def render_metric_card(label: str, value: str, delta: str = None, delta_color: str = "normal"):
    """
    Render a styled metric card
    
    Args:
        label: Metric label
        value: Metric value
        delta: Delta value (optional)
        delta_color: Delta color ("normal", "inverse", "off")
    """
    delta_html = ""
    if delta:
        delta_class = "positive" if delta_color == "normal" else "negative" if delta_color == "inverse" else ""
        delta_html = f'<div class="metric-delta {delta_class}">{delta}</div>'
    
    html = f"""
    <div class="metric-card fade-in">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        {delta_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_performance_badge(value: float, threshold_good: float = 0, threshold_excellent: float = 1.0):
    """
    Render a performance badge with color coding
    
    Args:
        value: Performance value
        threshold_good: Threshold for "good" performance
        threshold_excellent: Threshold for "excellent" performance
    """
    if value >= threshold_excellent:
        class_name = "excellent"
    elif value >= threshold_good:
        class_name = "good"
    else:
        class_name = "poor"
    
    html = f'<span class="performance-badge {class_name}">{value:.2f}</span>'
    st.markdown(html, unsafe_allow_html=True)


def render_strategy_card(name: str, description: str, metrics: dict):
    """
    Render a strategy information card
    
    Args:
        name: Strategy name
        description: Strategy description
        metrics: Dictionary of metrics to display
    """
    metrics_html = ""
    for key, value in metrics.items():
        metrics_html += f'<div><strong>{key}:</strong> {value}</div>'
    
    html = f"""
    <div class="strategy-card fade-in">
        <h3>{name}</h3>
        <p>{description}</p>
        <div class="strategy-metrics">
            {metrics_html}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def apply_custom_styling():
    """Apply all custom styling"""
    load_custom_css()
    
    # Additional inline styles if needed
    st.markdown("""
    <style>
        /* Additional dynamic styles can go here */
    </style>
    """, unsafe_allow_html=True)

