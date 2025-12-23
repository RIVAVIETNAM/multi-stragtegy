"""
Strategy Comparison Page
Side-by-side leaderboard and rankings
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from analytics.leaderboard import create_leaderboard, get_best_strategy, create_summary_stats
from analytics.visualize import plot_metrics_comparison

st.title("🏆 Strategy Leaderboard")

st.markdown("""
Fair comparison of all strategies tested in parallel.
**All strategies used:**
- Same market data
- Same execution rules
- Same transaction costs
""")

st.markdown("---")

# Check results
if 'backtest_results' not in st.session_state:
    st.warning("⚠️ No backtest results available. Run a backtest first!")
    st.stop()

results = st.session_state.backtest_results

# Summary stats
st.subheader("📊 Summary Statistics")

summary = create_summary_stats(results)
st.dataframe(summary, use_container_width=True)

st.markdown("---")

# Main leaderboard
st.subheader("🏅 Performance Leaderboard")

leaderboard = create_leaderboard(results)

# Apply conditional formatting
st.dataframe(
    leaderboard.style.background_gradient(
        cmap='RdYlGn',
        subset=['Total Return (%)', 'Sharpe Ratio', 'Win Rate (%)']
    ).background_gradient(
        cmap='RdYlGn_r',
        subset=['Max Drawdown (%)']
    ),
    use_container_width=True
)

st.caption("📌 Sorted by Sharpe Ratio (risk-adjusted returns)")
st.caption("🟩 Green = Better | 🟥 Red = Worse")

st.markdown("---")

# Rankings by different metrics
st.subheader("🎯 Rankings by Metric")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### By Total Return")
    sorted_by_return = sorted(
        [(name, res.total_return) for name, res in results.items()],
        key=lambda x: x[1],
        reverse=True
    )
    for rank, (name, value) in enumerate(sorted_by_return, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"#{rank}"
        st.write(f"{medal} **{name}**: {value:.2f}%")

with col2:
    st.markdown("#### By Sharpe Ratio")
    sorted_by_sharpe = sorted(
        [(name, res.sharpe_ratio) for name, res in results.items()],
        key=lambda x: x[1],
        reverse=True
    )
    for rank, (name, value) in enumerate(sorted_by_sharpe, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"#{rank}"
        st.write(f"{medal} **{name}**: {value:.2f}")

st.markdown("---")

# Radar chart comparison
st.subheader("📡 Multi-Metric Comparison")

if len(results) > 1:
    fig_radar = plot_metrics_comparison(results)
    st.plotly_chart(fig_radar, use_container_width=True)
    st.caption("Normalized radar chart showing relative performance across key metrics")

st.markdown("---")

# Winner announcement
st.subheader("🎉 Best Strategy")

best_name, best_result = get_best_strategy(results, metric='sharpe_ratio')

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.success(f"""
    ### 🏆 {best_name}
    
    **Sharpe Ratio:** {best_result.sharpe_ratio:.2f}  
    **Total Return:** {best_result.total_return:.2f}%  
    **Max Drawdown:** {best_result.max_drawdown:.2f}%  
    **Win Rate:** {best_result.win_rate:.1f}%  
    
    *Based on risk-adjusted returns (Sharpe Ratio)*
    """)

st.markdown("---")

# Export results
st.subheader("📥 Export Results")

col1, col2 = st.columns(2)

with col1:
    csv = leaderboard.to_csv()
    st.download_button(
        label="📊 Download Leaderboard (CSV)",
        data=csv,
        file_name=f"vn10_leaderboard_{st.session_state.backtest_timestamp.strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

with col2:
    st.info("📄 PDF export coming soon...")

st.success("✅ All comparisons are fair - strategies tested under identical conditions!")
