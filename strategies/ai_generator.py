"""
AI Strategy Generator
Uses Google Gemini API to generate trading strategies from natural language descriptions
"""

import os
import streamlit as st
from typing import Dict, Optional
from pathlib import Path
import re

# Optional import - only needed for AI Strategy Generator
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    genai = None


class AIStrategyGenerator:
    """Generate Python trading strategy code using AI"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize AI Strategy Generator
        
        Args:
            api_key: Google Gemini API key (if None, will try to get from env or st.secrets)
        
        Raises:
            ImportError: If google-generativeai is not installed
            ValueError: If API key is not provided
        """
        if not GEMINI_AVAILABLE:
            raise ImportError(
                "google-generativeai package is not installed. "
                "Install it with: pip install google-generativeai\n"
                "Note: This is only needed for AI Strategy Generator feature. "
                "The rest of the app works without it."
            )
        
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. Please set GEMINI_API_KEY environment variable "
                "or add it to Streamlit secrets (st.secrets.GEMINI_API_KEY)"
            )
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Strategy template
        self.strategy_template = """
def {function_name}(data: pd.DataFrame, **params) -> pd.Series:
    \"\"\"
    {description}
    
    Args:
        data: DataFrame with columns: open, high, low, close, volume
        **params: Strategy parameters
    
    Returns:
        pd.Series: Trading signals (1 = buy, -1 = sell, 0 = hold)
    \"\"\"
    import pandas as pd
    import numpy as np
    from ta.trend import MACD
    from ta.momentum import RSIIndicator
    from ta.volatility import BollingerBands
    
    signals = pd.Series(0, index=data.index)
    
    {code_body}
    
    return signals
"""
    
    def generate_strategy(self, description: str, strategy_name: str = None) -> Dict[str, str]:
        """
        Generate strategy code from natural language description
        
        Args:
            description: Natural language description of the strategy
            strategy_name: Optional strategy name (will be generated if not provided)
        
        Returns:
            Dictionary with 'code', 'function_name', 'description', 'params'
        """
        prompt = f"""
You are a Python trading strategy expert. Generate a complete trading strategy function based on this description:

DESCRIPTION: {description}

REQUIREMENTS:
1. The function must be named using snake_case (e.g., 'rsi_mean_reversion')
2. It must accept a pandas DataFrame 'data' with columns: open, high, low, close, volume
3. It must accept **params for strategy parameters
4. It must return a pandas Series with signals: 1 (buy), -1 (sell), 0 (hold)
5. Use the 'ta' library for technical indicators (MACD, RSI, Bollinger Bands, etc.)
6. The code must be production-ready and handle edge cases
7. Include proper comments explaining the logic
8. Only return the function body code (not the full function definition)

EXAMPLE OUTPUT FORMAT:
# Calculate RSI
rsi_indicator = RSIIndicator(data['close'], window=params.get('period', 14))
rsi = rsi_indicator.rsi()

# Generate signals
signals = pd.Series(0, index=data.index)
signals[rsi < params.get('oversold', 30)] = 1  # Buy when oversold
signals[rsi > params.get('overbought', 70)] = -1  # Sell when overbought

Now generate the code body for the described strategy:
"""
        
        try:
            response = self.model.generate_content(prompt)
            code_body = response.text.strip()
            
            # Clean up the code (remove markdown formatting if present)
            code_body = re.sub(r'```python\n?', '', code_body)
            code_body = re.sub(r'```\n?', '', code_body)
            code_body = code_body.strip()
            
            # Generate function name from description
            if not strategy_name:
                function_name = self._generate_function_name(description)
            else:
                function_name = strategy_name.lower().replace(' ', '_').replace('-', '_')
            
            # Extract parameters from code
            params = self._extract_parameters(code_body)
            
            # Build full function code
            full_code = self.strategy_template.format(
                function_name=function_name,
                description=description,
                code_body=code_body
            )
            
            return {
                'code': full_code,
                'function_name': function_name,
                'description': description,
                'params': params,
                'code_body': code_body
            }
            
        except Exception as e:
            raise Exception(f"Error generating strategy: {str(e)}")
    
    def _generate_function_name(self, description: str) -> str:
        """Generate function name from description"""
        # Simple heuristic: take first few words, make snake_case
        words = description.lower().split()[:3]
        # Remove common words
        words = [w for w in words if w not in ['a', 'an', 'the', 'buy', 'sell', 'when', 'if']]
        return '_'.join(words[:3]) if words else 'custom_strategy'
    
    def _extract_parameters(self, code: str) -> Dict[str, any]:
        """Extract parameter names and default values from code"""
        params = {}
        # Look for params.get() patterns
        pattern = r"params\.get\(['\"]([^'\"]+)['\"],\s*([^\)]+)\)"
        matches = re.findall(pattern, code)
        for param_name, default_value in matches:
            try:
                # Try to evaluate default value
                params[param_name] = eval(default_value)
            except:
                params[param_name] = default_value
        return params
    
    def validate_strategy_code(self, code: str) -> tuple[bool, str]:
        """
        Validate generated strategy code
        
        Returns:
            (is_valid, error_message)
        """
        try:
            # Try to compile the code
            compile(code, '<string>', 'exec')
            return True, "Code is valid"
        except SyntaxError as e:
            return False, f"Syntax error: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"


def save_strategy_to_file(code: str, function_name: str, output_dir: Path):
    """
    Save generated strategy to a Python file
    
    Args:
        code: Complete strategy code
        function_name: Function name
        output_dir: Directory to save the file
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / f"{function_name}.py"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    
    return file_path

