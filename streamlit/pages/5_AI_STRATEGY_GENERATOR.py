"""
AI Strategy Generator Page
Generate trading strategies using Google Gemini AI
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Try to import AI Generator (optional feature)
try:
    from strategies.ai_generator import AIStrategyGenerator, save_strategy_to_file
    AI_GENERATOR_AVAILABLE = True
except ImportError as e:
    AI_GENERATOR_AVAILABLE = False
    AIStrategyGenerator = None
    save_strategy_to_file = None

st.title("🤖 AI Strategy Generator")
st.markdown("### Generate Trading Strategies from Natural Language")

# Check if feature is available
if not AI_GENERATOR_AVAILABLE:
    st.error("""
    ❌ **AI Strategy Generator is not available**
    
    This feature requires the `google-generativeai` package.
    
    **To enable this feature:**
    ```bash
    pip install google-generativeai
    ```
    
    **Note:** This is an **optional** feature. The rest of the backtesting platform works perfectly without it!
    
    You can still:
    - ✅ Use all built-in strategies (MACD, RSI, Bollinger, SMA)
    - ✅ Create custom strategies manually
    - ✅ Run backtests
    - ✅ View results and comparisons
    - ✅ Use Performance Matrix
    """)
    st.stop()

st.info("""
💡 **How it works:** Describe your trading strategy in plain language, and AI will generate 
production-ready Python code using Google Gemini API.

**Example descriptions:**
- "Buy when RSI is below 30 and sell when RSI is above 70"
- "Use MACD crossover with fast period 12 and slow period 26"
- "Buy when price touches lower Bollinger Band and sell at upper band"
""")

st.markdown("---")

# API Key Configuration
st.subheader("🔑 API Configuration")

api_key_source = st.radio(
    "API Key Source",
    ["Environment Variable", "Enter Manually"],
    horizontal=True
)

api_key = None

if api_key_source == "Environment Variable":
    import os
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        st.success("✅ API key found in environment")
    else:
        st.warning("⚠️ GEMINI_API_KEY not found in environment variables")
        st.info("💡 You can set it using: `export GEMINI_API_KEY=your_key_here`")
else:
    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password",
        help="Get your API key from: https://makersuite.google.com/app/apikey"
    )

st.markdown("---")

# Strategy Generation
st.subheader("📝 Strategy Description")

strategy_description = st.text_area(
    "Describe your trading strategy",
    height=150,
    placeholder="Example: Buy when RSI indicator is below 30 (oversold) and sell when RSI is above 70 (overbought). Use a period of 14 for RSI calculation."
)

strategy_name = st.text_input(
    "Strategy Name (optional)",
    placeholder="e.g., rsi_mean_reversion",
    help="Leave empty to auto-generate from description"
)

col1, col2 = st.columns([1, 1])

with col1:
    generate_button = st.button("🚀 Generate Strategy", type="primary")

with col2:
    if st.button("📋 Load Example"):
        strategy_description = "Buy when RSI is below 30 and sell when RSI is above 70. Use period 14 for RSI calculation."
        strategy_name = "rsi_mean_reversion"
        st.rerun()

st.markdown("---")

# Generate and display
if generate_button:
    if not api_key:
        st.error("❌ Please configure your Gemini API key first!")
        st.stop()
    
    if not strategy_description:
        st.error("❌ Please enter a strategy description!")
        st.stop()
    
    try:
        with st.spinner("🤖 AI is generating your strategy..."):
            generator = AIStrategyGenerator(api_key=api_key)
            result = generator.generate_strategy(
                description=strategy_description,
                strategy_name=strategy_name if strategy_name else None
            )
            
            # Validate code
            is_valid, error_msg = generator.validate_strategy_code(result['code'])
            
            if not is_valid:
                st.error(f"❌ Generated code has errors: {error_msg}")
                st.code(result['code'], language='python')
            else:
                st.success("✅ Strategy generated successfully!")
                
                # Display results
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Function Name:** `{result['function_name']}`")
                    st.markdown(f"**Description:** {result['description']}")
                    
                    if result['params']:
                        st.markdown("**Parameters:**")
                        for param, default in result['params'].items():
                            st.code(f"{param} = {default}", language='python')
                
                with col2:
                    st.download_button(
                        label="💾 Download Code",
                        data=result['code'],
                        file_name=f"{result['function_name']}.py",
                        mime="text/python"
                    )
                
                # Code preview
                st.subheader("📄 Generated Code")
                st.code(result['code'], language='python')
                
                # Save to session state for potential use
                if 'generated_strategies' not in st.session_state:
                    st.session_state.generated_strategies = {}
                
                st.session_state.generated_strategies[result['function_name']] = result
                
                st.info("""
                💡 **Next Steps:**
                1. Review the generated code
                2. Download and save to `strategies/custom/` folder
                3. Import and test in the **Configure** page
                4. Run backtest to evaluate performance
                """)
                
    except Exception as e:
        st.error(f"❌ Error generating strategy: {str(e)}")
        st.info("""
        **Troubleshooting:**
        - Check your API key is correct
        - Ensure you have internet connection
        - Try a simpler description
        - Check API quota/limits
        """)

# Show previously generated strategies
if 'generated_strategies' in st.session_state and st.session_state.generated_strategies:
    st.markdown("---")
    st.subheader("📚 Previously Generated Strategies")
    
    for name, strategy_data in st.session_state.generated_strategies.items():
        with st.expander(f"🤖 {name}"):
            st.markdown(f"**Description:** {strategy_data['description']}")
            st.code(strategy_data['code'], language='python')
            
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label=f"💾 Download {name}",
                    data=strategy_data['code'],
                    file_name=f"{name}.py",
                    mime="text/python",
                    key=f"download_{name}"
                )
            with col2:
                if st.button(f"🗑️ Remove {name}", key=f"remove_{name}"):
                    del st.session_state.generated_strategies[name]
                    st.rerun()

st.markdown("---")
st.markdown("""
### 📖 Tips for Better Results

1. **Be Specific:** Include indicator names, periods, and threshold values
2. **Use Standard Indicators:** RSI, MACD, Bollinger Bands, SMA, EMA work best
3. **Describe Entry/Exit Rules:** Clearly state when to buy and sell
4. **Mention Parameters:** Specify any customizable values

### 🔗 Resources

- [Get Gemini API Key](https://makersuite.google.com/app/apikey)
- [Strategy Examples](https://github.com/your-repo/strategies)
- [Technical Indicators Guide](https://ta-lib.org/)
""")

