"""
Backtest Execution Page
Run parallel backtests on selected strategies
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from strategies.builtin import STRATEGIES
from engine.backtest import run_parallel_backtests

st.title("🚀 Run Backtest")

st.markdown("""
Load market data and execute parallel backtests on selected strategies.
All strategies will run simultaneously with identical assumptions.
""")

st.markdown("---")

# Data input section
st.subheader("📊 Market Data")

data_source = st.radio(
    "Select Data Source",
    ["Sample Data (Demo)", "Upload CSV", "VNStock API"],
    horizontal=True
)

data = None

if data_source == "Sample Data (Demo)":
    st.info("📝 Using simulated VN-Index data for demonstration")
    
    # Generate sample data
    if st.button("🎲 Generate Sample Data", type="primary"):
        with st.spinner("Generating sample data..."):
            # Create synthetic VN market data
            dates = pd.date_range(end=datetime.now(), periods=500, freq='D')
            np.random.seed(42)
            
            # Simulate realistic VN stock price movement
            returns = np.random.normal(0.001, 0.02, len(dates))
            prices = 100 * (1 + returns).cumprod()
            
            data = pd.DataFrame({
                'close': prices,
                'high': prices * (1 + np.abs(np.random.normal(0, 0.01, len(dates)))),
                'low': prices * (1 - np.abs(np.random.normal(0, 0.01, len(dates)))),
                'volume': np.random.randint(1000000, 5000000, len(dates))
            }, index=dates)
            
            st.session_state.market_data = data
            st.success(f"✅ Generated {len(data)} days of sample data!")
            
elif data_source == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file:
        data = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)
        st.session_state.market_data = data
        st.success(f"✅ Loaded {len(data)} rows from CSV")

elif data_source == "VNStock API":
    st.info("🚧 VNStock API integration coming soon...")

# Show data preview
if 'market_data' in st.session_state:
    data = st.session_state.market_data
    
    st.subheader("📈 Data Preview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Rows", len(data))
    with col2:
        st.metric("Start Date", data.index[0].strftime('%Y-%m-%d'))
    with col3:
        st.metric("End Date", data.index[-1].strftime('%Y-%m-%d'))
    
    with st.expander("View Data"):
        st.dataframe(data.tail(20), use_container_width=True)

st.markdown("---")

# Backtest execution
st.subheader("⚡ Execute Backtest")

# Check configuration
if 'selected_strategies' not in st.session_state or len(st.session_state.selected_strategies) == 0:
    st.warning("⚠️ No strategies selected. Go to **Configure** page first!")
    st.stop()

if 'market_data' not in st.session_state:
    st.warning("⚠️ No market data loaded. Please load data above!")
    st.stop()

# Show execution plan
with st.expander("📋 Execution Plan"):
    st.markdown(f"**Strategies:** {', '.join(st.session_state.selected_strategies)}")
    st.markdown(f"**Data Points:** {len(st.session_state.market_data)}")
    st.markdown(f"**Initial Capital:** {st.session_state.get('initial_capital', 100_000_000):,.0f} VND")
    st.markdown(f"**Transaction Cost:** {st.session_state.get('transaction_cost', 0.0015)*100:.2f}%")
    st.markdown(f"**VN Rules:** {'Enabled' if st.session_state.get('enforce_vn_rules', True) else 'Disabled'}")

# Run button
if st.button("🚀 RUN BACKTEST", type="primary", use_container_width=True):
    
    # Prepare strategies with configured params
    selected = st.session_state.selected_strategies
    strategies_to_run = {}
    
    for name in selected:
        strategy_func = STRATEGIES[name]['function']
        # Get configured params from session state, or use defaults
        params = st.session_state.get(f'params_{name}', STRATEGIES[name]['params'])
        
        # Wrap function to pass params (use default parameter to capture in closure)
        def make_strategy_wrapper(func, strategy_params):
            def wrapper(data, params=strategy_params):
                return func(data, **params)
            return wrapper
        
        strategies_to_run[name] = make_strategy_wrapper(strategy_func, params)
    
    # Execute
    with st.spinner("⏳ Running parallel backtests..."):
        results = run_parallel_backtests(
            data=st.session_state.market_data,
            strategies=strategies_to_run,
            initial_capital=st.session_state.get('initial_capital', 100_000_000),
            transaction_cost=st.session_state.get('transaction_cost', 0.0015),
            enforce_vn_rules=st.session_state.get('enforce_vn_rules', True)
        )
        
        # Store results
        st.session_state.backtest_results = results
        st.session_state.backtest_timestamp = datetime.now()
    
    st.success(f"✅ Backtest completed for {len(results)} strategies!")
    st.balloons()
    
    # Quick results preview
    st.subheader("🎯 Quick Results")
    
    from analytics.leaderboard import create_leaderboard
    leaderboard = create_leaderboard(results)
    
    st.dataframe(
        leaderboard.style.background_gradient(cmap='RdYlGn', subset=['Total Return (%)', 'Sharpe Ratio']),
        use_container_width=True
    )
    
    st.info("👉 Go to **Results** page for detailed analysis!")

# Show existing results
elif 'backtest_results' in st.session_state:
    st.info(f"ℹ️ Last backtest: {st.session_state.backtest_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("**Strategies tested:** " + ", ".join(st.session_state.backtest_results.keys()))
    st.success("👉 Go to **Results** or **Compare** pages to view analysis!")
