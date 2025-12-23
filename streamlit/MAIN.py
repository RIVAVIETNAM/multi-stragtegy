"""
Multi-Strategy Backtesting Platform
Main Streamlit Application
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Load custom CSS
from app.utils.ui_helpers import apply_custom_styling
apply_custom_styling()

# Page config
st.set_page_config(
    page_title="Multi-Strategy Backtesting Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page
st.title("🇻🇳 Multi-Strategy Backtesting Platform")
st.markdown("### For Vietnamese Stock Market (VN-Index, VN30, HOSE/HNX)")

st.markdown("---")

# Introduction
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## WELCOME
    
    A specialized backtesting platform that enables **parallel testing** of multiple 
    trading strategies under identical Vietnamese market conditions.
    
    ### Key Features:
    - ✅ **Multi-Strategy Execution** - Test many strategies simultaneously
    - ✅ **VN Market Rules** - ±7% price limit, T+2 settlement
    - ✅ **Fair Comparison** - All strategies use same data & assumptions
    - ✅ **5-10× Faster** - Vectorized parallel execution
    - ✅ **Advanced Analytics** - Sharpe, drawdown, win rate, leaderboards
    """)

with col2:
    st.info("""
    **Quick Start:**
    
    1. Configure strategies
    2. Run backtest
    3. View results
    4. Compare performance
    
    Use sidebar to navigate →
    """)

st.markdown("---")

# Sidebar navigation
st.sidebar.title("📊 Navigation")
st.sidebar.markdown("""
Navigate to:
- **⚙️ Configure** - Setup strategies
- **🚀 Backtest** - Run tests
- **📈 Results** - View dashboard
- **🏆 Compare** - Strategy leaderboard
""")


# Main content
st.markdown("## 🎯 Why This Platform?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Speed
    Parallel execution achieves **5-10× speedup** compared to sequential testing.
    """)

with col2:
    st.markdown("""
    ### Fairness
    All strategies tested with **identical** data, costs, and execution rules.
    """)

with col3:
    st.markdown("""
    ### Specialized
    Built specifically for **Vietnamese market** quirks and regulations.
    """)

st.markdown("---")

st.markdown("## 📚 Built-in Strategies")

strategies = {
    "MACD Crossover": {
        "desc": "Buy when MACD crosses above signal line",
        "params": "Fast=12, Slow=26, Signal=9",
        "type": "Momentum"
    },
    "RSI Mean-Reversion": {
        "desc": "Buy at RSI < 30, Sell at RSI > 70",
        "params": "Period=14",
        "type": "Mean-Reversion"
    },
    "Bollinger Bands": {
        "desc": "Buy at lower band, sell at upper band",
        "params": "Window=20, StdDev=2",
        "type": "Volatility"
    },
    "SMA Crossover": {
        "desc": "Golden/Death cross detection",
        "params": "Short=50, Long=200",
        "type": "Trend"
    }
}

for name, info in strategies.items():
    with st.expander(f"**{name}** ({info['type']})"):
        st.markdown(f"**Description:** {info['desc']}")
        st.markdown(f"**Parameters:** {info['params']}")

st.markdown("---")

st.markdown("## 🇻🇳 Vietnamese Market Rules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Price Limits
    - **HOSE:** ±7% daily limit
    - **HNX:** ±10% daily limit
    - **UPCOM:** ±15% daily limit
    
    Platform automatically enforces these limits.
    """)

with col2:
    st.markdown("""
    ### Settlement
    - **T+2:** Cash settlement (2 business days)
    - **T+3:** Stock settlement (3 business days)
    - **Trading Hours:** 9AM-3PM (GMT+7)
    
    All accurately modeled in backtests.
    """)

st.markdown("---")

st.success("""
👈 **Get Started:** Use the sidebar to navigate to different pages!

Start with **Configure** to set up your first backtest.
""")

