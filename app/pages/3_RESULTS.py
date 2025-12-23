"""
Results Dashboard Page
Detailed analysis of backtest results
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from analytics.visualize import plot_equity_curves, plot_drawdown, plot_returns_distribution

st.title("📈 Results Dashboard")

# Check if results exist
if 'backtest_results' not in st.session_state:
    st.warning("⚠️ No backtest results available. Run a backtest first!")
    st.info("👉 Go to **Backtest** page to execute strategies")
    st.stop()

results = st.session_state.backtest_results

st.markdown(f"**Backtest Date:** {st.session_state.backtest_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown(f"**Strategies Analyzed:** {len(results)}")

st.markdown("---")

# Multi-strategy equity curves
st.subheader("💹 Multi-Strategy Performance")

fig_equity = plot_equity_curves(results)
st.plotly_chart(fig_equity, use_container_width=True)

st.caption("📊 All strategies executed in parallel with identical market data and costs")

st.markdown("---")

# Individual strategy analysis
st.subheader("🔍 Individual Strategy Analysis")

strategy_name = st.selectbox(
    "Select Strategy",
    options=list(results.keys())
)

if strategy_name:
    result = results[strategy_name]
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Return",
            f"{result.total_return:.2f}%",
            delta=f"{result.total_return:.2f}%"
        )
    
    with col2:
        st.metric(
            "Sharpe Ratio",
            f"{result.sharpe_ratio:.2f}",
            delta="Good" if result.sharpe_ratio > 1.0 else "Poor"
        )
    
    with col3:
        st.metric(
            "Max Drawdown",
            f"{result.max_drawdown:.2f}%",
            delta=f"{result.max_drawdown:.2f}%",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "Win Rate",
            f"{result.win_rate:.1f}%",
            delta=f"{result.win_rate:.1f}%"
        )
    
    # Additional metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Profit Factor", f"{result.profit_factor:.2f}")
    with col2:
        st.metric("Number of Trades", result.num_trades)
    with col3:
        final_value = result.equity_curve.iloc[-1]
        st.metric("Final Portfolio", f"{final_value:,.0f} VND")
    
    # Charts
    tab1, tab2, tab3 = st.tabs(["📉 Drawdown", "📊 Returns Distribution", "📋 Trade Log"])
    
    with tab1:
        st.plotly_chart(plot_drawdown(result), use_container_width=True)
        st.caption("Drawdown shows peak-to-trough decline in portfolio value")
    
    with tab2:
        st.plotly_chart(plot_returns_distribution(result), use_container_width=True)
        st.caption("Distribution of daily returns")
    
    with tab3:
        if len(result.trades) > 0:
            st.dataframe(result.trades, use_container_width=True)
        else:
            st.info("No trades executed")

st.markdown("---")

# Performance interpretation
st.subheader("💡 Performance Interpretation")

best_return = max(results.values(), key=lambda x: x.total_return)
best_sharpe = max(results.values(), key=lambda x: x.sharpe_ratio)
lowest_dd = max(results.values(), key=lambda x: x.max_drawdown)  # Least negative

col1, col2, col3 = st.columns(3)

with col1:
    st.success(f"**Best Return**\n\n{best_return.strategy_name}\n\n{best_return.total_return:.2f}%")

with col2:
    st.success(f"**Best Risk-Adjusted**\n\n{best_sharpe.strategy_name}\n\n{best_sharpe.sharpe_ratio:.2f} Sharpe")

with col3:
    st.success(f"**Lowest Drawdown**\n\n{lowest_dd.strategy_name}\n\n{lowest_dd.max_drawdown:.2f}%")

st.info("💡 **Tip:** A good strategy balances return, risk (Sharpe), and drawdown. Check the **Compare** page for side-by-side rankings!")
