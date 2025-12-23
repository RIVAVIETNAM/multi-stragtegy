"""
Configure Strategies Page
Allow users to select and configure trading strategies
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from strategies.builtin import STRATEGIES

st.title("⚙️ Configure Strategies")

st.markdown("""
Select which strategies to test and configure their parameters.
All selected strategies will run in parallel using identical market data.
""")

st.markdown("---")

# Strategy selection
st.subheader("📊 Select Strategies")

if 'selected_strategies' not in st.session_state:
    st.session_state.selected_strategies = list(STRATEGIES.keys())

selected = []
cols = st.columns(2)

for idx, (name, info) in enumerate(STRATEGIES.items()):
    with cols[idx % 2]:
        if st.checkbox(f"**{name}** ({info['type']})", value=name in st.session_state.selected_strategies, key=f"select_{name}"):
            selected.append(name)
            
            with st.expander(f"Configure {name}"):
                st.markdown(f"**Description:** {info['description']}")
                st.markdown("**Parameters:**")
                
                params = info['params'].copy()
                for param, default_value in params.items():
                    if isinstance(default_value, int):
                        params[param] = st.number_input(
                            param.replace('_', ' ').title(),
                            value=default_value,
                            min_value=1,
                            key=f"{name}_{param}"
                        )
                    elif isinstance(default_value, float):
                        params[param] = st.number_input(
                            param.replace('_', ' ').title(),
                            value=default_value,
                            min_value=0.0,
                            step=0.1,
                            key=f"{name}_{param}"
                        )
                
                # Store configured params
                if f'params_{name}' not in st.session_state:
                    st.session_state[f'params_{name}'] = params

st.session_state.selected_strategies = selected

st.markdown("---")

# Backtest parameters
st.subheader("🎯 Backtest Parameters")

col1, col2 = st.columns(2)

with col1:
    initial_capital = st.number_input(
        "Initial Capital (VND)",
        value=100_000_000,
        min_value=1_000_000,
        step=10_000_000,
        format="%d"
    )
    st.session_state.initial_capital = initial_capital
    
    enforce_vn_rules = st.checkbox(
        "Enforce Vietnamese Market Rules",
        value=True,
        help="Apply ±7% price limit, T+2 settlement, etc."
    )
    st.session_state.enforce_vn_rules = enforce_vn_rules

with col2:
    transaction_cost = st.slider(
        "Transaction Cost (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.15,
        step=0.05
    ) / 100
    st.session_state.transaction_cost = transaction_cost
    
    st.write("")  # Spacing
    st.write("")
    
    if enforce_vn_rules:
        st.success("✅ VN rules active: ±7% limit, T+2 settlement")
    else:
        st.warning("⚠️ VN rules disabled - unrealistic results")

st.markdown("---")

# Summary
st.subheader("📋 Configuration Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Strategies Selected", len(selected))

with col2:
    st.metric("Initial Capital", f"{initial_capital:,.0f} VND")

with col3:
    st.metric("Transaction Cost", f"{transaction_cost*100:.2f}%")

if len(selected) > 0:
    st.success(f"✅ Ready to backtest: {', '.join(selected)}")
    st.info("👉 Go to **Backtest** page to run the simulation!")
else:
    st.warning("⚠️ Please select at least one strategy")
