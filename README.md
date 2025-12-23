# VN10: Multi-Strategy Backtesting Platform
## For Vietnamese Stock Market

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🎯 Overview

A specialized backtesting platform designed for the **Vietnamese stock market** (VN-Index, VN30, HOSE/HNX) that enables **parallel testing of multiple trading strategies** under identical market conditions.

### Key Innovation

Instead of testing strategies one-by-one, VN10 runs them **in parallel** with:
- ✅ Same market data
- ✅ Same execution rules  
- ✅ Same cost assumptions

→ **Fair, fast, and transparent** comparison

---

## ⚡ Key Features

### 🇻🇳 Vietnamese Market Specialized
- **±7% daily price limit** (HOSE enforcement)
- **T+2 cash settlement** modeling
- **T+3 stock settlement** delays
- **VN trading hours** (9AM-3PM GMT+7)
- **Vietnamese transaction costs** (0.15% default)

### 🚀 Multi-Strategy Engine
- Parallel execution of multiple strategies
- 5-10× faster than sequential testing
- Vectorized backtest engine (Pandas)
- Multi-threaded for speed

### 📊 Built-in Strategies
- MACD Crossover (12, 26, 9)
- RSI Mean-Reversion (Period 14)
- Bollinger Bands (20, σ=2)
- SMA Crossover (50/200)

### 📈 Advanced Analytics
- Sharpe ratio, Max drawdown, Win rate
- Side-by-side strategy leaderboards
- Equity curve overlays
- PDF/CSV export

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone <repository-url>
cd "6 new project"

# Install dependencies
pip install -r requirements.txt
```

### Run Platform

```bash
# Launch Streamlit app
streamlit run app/main.py
```

Access at: **http://localhost:8501**

---

## 📖 Usage Example

```python
from engine.backtest import run_parallel_backtests
from strategies.builtin import macd, rsi, bollinger
from data.fetcher import fetch_vn_data

# 1. Load VN-Index data
data = fetch_vn_data('VN-INDEX', '2020-01-01', '2024-12-31')

# 2. Define strategies
strategies = [
    ('MACD', macd.macd_crossover),
    ('RSI', rsi.rsi_mean_reversion),
    ('Bollinger', bollinger.bollinger_bands)
]

# 3. Run parallel backtest
results = run_parallel_backtests(data, strategies, costs=0.0015)

# 4. View leaderboard
from analytics.leaderboard import create_leaderboard
print(create_leaderboard(results))
```

---

## 📐 Architecture

VN10 uses a **4-layer architecture**:

1. **Data Layer** → Fetches & caches VN market data
2. **Strategy Layer** → Defines trading rules via Python SDK
3. **Backtest Engine** → Executes parallel simulations
4. **Analytics Layer** → Visualizes results

See `docs/` for detailed documentation.

---

## 🎯 Research Questions 

Based on our academic research, VN10 addresses:

- **RQ1:** Multi-strategy portfolio achieves **higher Sharpe** than individual strategies
- **RQ2:** VN market rules enforcement produces **realistic results**
- **RQ3:** Parallel execution achieves **5-10× speedup**

---

## 📊 Expected Results

| Test Case | Total Return | Sharpe | Max DD |
|-----------|--------------|--------|--------|
| MACD (Momentum) | ~30% | 1.05 | -15% |
| RSI (Mean-Rev) | ~28% | 1.00 | -18% |
| **Combined Portfolio** | **45%** | **1.30** | **-12%** |
| Buy & Hold VN-Index | 22% | 0.85 | -25% |

---

## 📁 Project Structure

```
6 new project/
├── data/              # Data layer
├── strategies/        # Strategy definitions
├── engine/            # Backtest engine
├── analytics/         # Visualization
├── app/               # Streamlit UI
├── tests/             # Unit tests
└── docs/              # Documentation
```

---

## 🛠️ Technology Stack

- **Python 3.8+**
- **Pandas** - Data manipulation
- **VNStock** - Vietnamese market data
- **Streamlit** - Web interface
- **Plotly** - Interactive charts
- **Optuna** - Parameter optimization

---

## 📝 Documentation

- [User Guide (Vietnamese)](docs/USER_GUIDE_VI.md)
- [API Documentation](docs/API_DOCS.md)
- [Research Paper](docs/RESEARCH_PAPER.md)

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- VNStock library for Vietnamese market data
- Research paper: "Multi-Strategy Backtesting Platform for Vietnamese Stock Market"
- Inspired by QuantConnect, Backtrader

---

**Built for Vietnamese traders, students, and quant researchers** 🇻🇳📈

