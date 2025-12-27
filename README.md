# 🚀 Multi-Strategy Backtesting Platform
## For Vietnamese Stock Market

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Deployed](https://img.shields.io/badge/deployed-Streamlit%20Cloud-brightgreen.svg)](https://multi-stragtegy-vnteam10.streamlit.app/)

---

## 🎯 Overview

A **specialized backtesting platform** designed for the **Vietnamese stock market** (VN-Index, VN30, HOSE/HNX) that enables **parallel testing of multiple trading strategies** under identical market conditions.

### 🌟 Key Innovation

Instead of testing strategies one-by-one (slow, biased), this platform runs them **in parallel** with:
- ✅ **Same market data** - Fair comparison
- ✅ **Same execution rules** - Consistent assumptions
- ✅ **Same cost assumptions** - Realistic fees
- ✅ **Same time period** - Identical conditions

→ **Fast, fair, and transparent** strategy comparison

---

## ⚡ Key Features

### 🇻🇳 Vietnamese Market Specialized

- **±7% daily price limit** (HOSE enforcement)
- **T+2 cash settlement** modeling
- **T+3 stock settlement** delays
- **VN trading hours** (9AM-3PM GMT+7)
- **Vietnamese transaction costs** (0.15% default)

### 🚀 Multi-Strategy Engine

- **Parallel execution** of multiple strategies
- **5-10× faster** than sequential testing
- **Vectorized backtest engine** (Pandas)
- **Multi-threaded** for speed
- **~12 seconds** for 10-year backtest (2 strategies)

### 📊 Built-in Strategies

| Strategy | Type | Default Parameters | Description |
|----------|------|-------------------|-------------|
| **MACD Crossover** | Momentum | Fast=12, Slow=26, Signal=9 | Buy when MACD crosses above signal line |
| **RSI Mean-Reversion** | Mean-Reversion | Period=14, Oversold=30, Overbought=70 | Buy when RSI < 30, sell when RSI > 70 |
| **Bollinger Bands** | Volatility | Window=20, σ=2 | Buy at lower band, sell at upper band |
| **SMA Crossover** | Trend | Short=50, Long=200 | Golden/Death Cross strategy |
| **Buy & Hold** | Benchmark | N/A | Buy at start, hold until end |
| **Combined Portfolio** | Portfolio | Equal-weight MACD + RSI | Combines momentum and mean-reversion |

### 📈 Advanced Analytics

- **Performance Metrics:**
  - Total Return (%)
  - Annualized Sharpe Ratio
  - Maximum Drawdown (%)
  - Win Rate (%)
  - Profit Factor
  - Number of Trades

- **Visualizations:**
  - Equity curve overlays
  - Drawdown charts
  - Returns distribution
  - Trade logs

- **Export Options:**
  - CSV export
  - PDF reports (planned)

---

## 🚀 Quick Start

### 🌐 Use Online (Recommended - No Installation!)

**Access the platform directly:**

🔗 **https://multi-stragtegy-vnteam10.streamlit.app/**

✅ **Advantages:**
- ✅ No local setup required
- ✅ Access from anywhere (computer, phone, tablet)
- ✅ Always up-to-date
- ✅ Share easily via link
- ✅ No Python installation needed

**Quick Steps:**
1. Open the link above
2. Click **CONFIGURE** → Select strategies
3. Click **BACKTEST** → Generate sample data → Run backtest
4. Click **RESULTS** → View charts
5. Click **COMPARE** → See leaderboard

> 📖 **Detailed Guide:** See [Streamlit Platform Guide](streamlit/STREAMLIT_GUIDE.md) for complete usage instructions.

---

### 💻 Run Locally (For Developers)

#### Prerequisites

- Python 3.8 or higher
- pip package manager

#### Installation

```bash
# 1. Clone repository
git clone <repository-url>
cd "6 new project"

# 2. Install dependencies
pip install -r requirements.txt
```

> 📖 **Detailed Installation:** See [Installation Guide](docs/INSTALLATION.md) for complete setup instructions, including optional dependencies.

#### Run Platform

```bash
# Launch Streamlit app
streamlit run streamlit/MAIN.py
```

Access at: **http://localhost:8501**

> 💡 **User Guide:** See [Streamlit Platform Guide](streamlit/STREAMLIT_GUIDE.md) for detailed usage instructions.

---

## 📊 Sample Results

Results from backtesting on VN-Index data (2015-2024):

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|--------------|
| **MACD (Momentum)** | 22.77% | 0.56 | -20.93% |
| **RSI (Mean-Reversion)** | 44.83% | 0.98 | -16.18% |
| **Combined Portfolio** | 10.51% | 0.34 | -19.52% |
| **Buy & Hold** | 58.25% | 0.90 | -25.51% |

**Key Insights:**
- ✅ RSI achieved the **best risk-adjusted returns** (Sharpe 0.98)
- ✅ Buy & Hold significantly outperformed (58.25% return) in this bullish market period
- ✅ Combined Portfolio underperformed due to signal conflicts between momentum and mean-reversion strategies
- ✅ Platform successfully enables **fair comparison** of strategies under identical conditions

> 📖 **Test Case Setup:** See [Test Case Setup Guide](docs/guides/TEST_CASE_SETUP.md) for how to replicate these results.

---

## 📐 Architecture

The platform uses a **4-layer architecture**:

```
┌─────────────────────────────────────────┐
│  Analytics Layer                         │
│  • Visualizations (Plotly)              │
│  • Leaderboards                          │
│  • CSV/PDF Export                        │
└─────────────────────────────────────────┘
              ↑
┌─────────────────────────────────────────┐
│  Backtest Engine                        │
│  • Parallel execution                   │
│  • VN market rules enforcement          │
│  • Transaction cost modeling            │
└─────────────────────────────────────────┘
              ↑
┌─────────────────────────────────────────┐
│  Strategy Layer                         │
│  • MACD, RSI, Bollinger, SMA            │
│  • Custom strategy SDK                   │
│  • Parameter optimization               │
└─────────────────────────────────────────┘
              ↑
┌─────────────────────────────────────────┐
│  Data Layer                             │
│  • VN market data (VNStock)            │
│  • CSV upload support                   │
│  • Data validation & cleaning           │
└─────────────────────────────────────────┘
```

### Component Details

1. **Data Layer** → Fetches & caches VN market data, enforces ±7% price limits
2. **Strategy Layer** → Defines trading rules via Python SDK, supports built-in and custom strategies
3. **Backtest Engine** → Executes parallel simulations with realistic market mechanics
4. **Analytics Layer** → Visualizes results, generates reports, creates leaderboards

See `docs/` for detailed documentation.

---

## 🎯 Research Questions

Based on our academic research, the platform addresses:

- **RQ1:** Does multi-strategy backtesting enable fair comparison of strategies?
  - ✅ **Answer:** Yes, by running strategies in parallel under identical conditions, the platform enables fair comparison. Results show RSI (Sharpe 0.98) outperformed combined portfolio (Sharpe 0.34) in this market regime.

- **RQ2:** How do Vietnam-specific constraints affect results?
  - ✅ **Answer:** Enforcing ±7% price limits and T+2 settlement produces more realistic results. Without limits, returns were artificially inflated (e.g., 28% vs 22.77% for MACD).

- **RQ3:** What is the execution speed?
  - ✅ **Answer:** Parallel execution achieves **5-10× speedup**. A 10-year backtest of 2 strategies takes ~12 seconds vs ~60 seconds for sequential execution.

---

## 📖 Usage Example

### Python API Usage

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
results = run_parallel_backtests(
    data, 
    strategies, 
    initial_capital=100000000,  # 100M VND
    transaction_cost=0.0015,    # 0.15%
    enforce_vn_rules=True       # ±7% limit, T+2 settlement
)

# 4. View leaderboard
from analytics.leaderboard import create_leaderboard
print(create_leaderboard(results))
```

### Streamlit Web Interface

1. **CONFIGURE** → Select strategies and adjust parameters
2. **BACKTEST** → Upload data or generate sample data → Run backtest
3. **RESULTS** → View detailed performance charts
4. **COMPARE** → See side-by-side leaderboard

> 📖 **Complete Guide:** See [Streamlit Platform Guide](streamlit/STREAMLIT_GUIDE.md) for detailed step-by-step instructions.

---

## 📁 Project Structure

```
6 new project/
├── data/                    # Data layer
│   ├── database.py          # Data caching
│   └── vn_rules.py          # VN market rules enforcement
│
├── strategies/              # Strategy definitions
│   ├── builtin/             # Built-in strategies
│   │   ├── macd.py          # MACD Crossover
│   │   ├── rsi.py           # RSI Mean-Reversion
│   │   ├── bollinger.py     # Bollinger Bands
│   │   ├── sma.py           # SMA Crossover
│   │   ├── buy_hold.py      # Buy & Hold
│   │   └── portfolio_combined.py  # Combined Portfolio
│   └── ai_generator.py      # AI strategy generator
│
├── engine/                   # Backtest engine
│   └── backtest.py           # Core backtesting logic
│
├── analytics/                # Visualization
│   ├── visualize.py          # Plotly charts
│   ├── leaderboard.py        # Strategy comparison
│   └── strategy_matrix.py    # Strategy matrix
│
├── streamlit/                # Streamlit application
│   ├── MAIN.py               # Main app (entry point)
│   ├── STREAMLIT_GUIDE.md    # User guide
│   └── app/                   # Streamlit UI components
│       ├── assets/            # Custom CSS & assets
│       ├── pages/             # Streamlit pages
│       │   ├── 1_CONFIGURE.py
│       │   ├── 2_BACKTEST.py
│       │   ├── 3_RESULTS.py
│       │   ├── 4_COMPARE.py
│       │   └── 5_AI_STRATEGY_GENERATOR.py
│       └── utils/              # UI helpers
│
├── tests/                     # Test files
│   ├── comparison_report.md   # Results comparison
│   └── TEST_RESULTS_LOG.md    # Test log
│
├── docs/                      # Documentation
│   ├── guides/                # User guides
│   │   ├── TEST_CASE_SETUP.md
│   │   ├── STRATEGY_MAPPING.md
│   │   ├── PARAMETER_TUNING.md
│   │   └── DEPLOYMENT.md
│   ├── features/              # Feature documentation
│   ├── analysis/              # Analysis & research
│   ├── INSTALLATION.md
│   ├── USER_GUIDE_VI.md
│   └── README.md
│
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🛠️ Technology Stack

- **Python 3.8+** - Core language
- **Pandas** - Data manipulation & analysis
- **NumPy** - Numerical computing
- **VNStock** - Vietnamese market data API
- **Streamlit** - Web interface framework
- **Plotly** - Interactive charts
- **Optuna** - Parameter optimization (optional)

---

## 📝 Documentation

### 📖 User Guides

- **[Installation Guide](docs/INSTALLATION.md)** - Complete setup instructions
- **[User Guide (Vietnamese)](docs/USER_GUIDE_VI.md)** - Hướng dẫn tiếng Việt
- **[Streamlit Platform Guide](streamlit/STREAMLIT_GUIDE.md)** - Detailed Streamlit usage
- **[Deployment Guide](docs/guides/DEPLOYMENT.md)** - Deploy to Streamlit Cloud
- **[Test Case Setup Guide](docs/guides/TEST_CASE_SETUP.md)** - How to replicate test case results
- **[Strategy Mapping Guide](docs/guides/STRATEGY_MAPPING.md)** - Strategy implementation details
- **[Parameter Tuning Guide](docs/guides/PARAMETER_TUNING.md)** - How to optimize strategy parameters

### ✨ Features

- **[New Features Guide](docs/features/FEATURES_GUIDE.md)** - Latest features and improvements
- **[AI Strategy Generator FAQ](docs/features/WHY_GOOGLE_GENERATIVEAI.md)** - AI strategy generator explanation

### 🔍 Analysis

- **[FC-Terminal Compatibility Analysis](docs/analysis/FC_TERMINAL_COMPATIBILITY.md)** - Compatibility analysis

---

## 🐛 Troubleshooting

### Common Issues

**Q: Backtest results show all zeros?**
- ✅ **Fixed in v1.0** - Transaction cost calculation bug fixed
- If still occurs, reload Streamlit Cloud app

**Q: Strategies not generating signals?**
- Check data has enough points (SMA 50/200 needs 200+ points)
- Adjust parameters in CONFIGURE page
- Try different date ranges

**Q: App not loading on Streamlit Cloud?**
- Check `Main file path: streamlit/MAIN.py` in settings
- Verify all dependencies in `requirements.txt`
- Check deployment logs

**Q: Import errors when running locally?**
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (need 3.8+)

> 📖 **More Troubleshooting:** See [Streamlit Guide - Troubleshooting](streamlit/STREAMLIT_GUIDE.md#-troubleshooting) section.

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone repository
git clone <repository-url>
cd "6 new project"

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run locally
streamlit run streamlit/MAIN.py
```

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- **VNStock** library for Vietnamese market data
- **Research paper:** "Multi-Strategy Backtesting Platform for Vietnamese Stock Market: Design and Evaluation"
- Inspired by **QuantConnect**, **Backtrader**, and other open-source backtesting platforms

---

## 📧 Contact & Support

- **Platform URL:** https://multi-stragtegy-vnteam10.streamlit.app/
- **Documentation:** See `docs/` folder
- **Issues:** Open an issue on GitHub

---

**Built for Vietnamese traders, students, and quant researchers** 🇻🇳📈

*Multi-Strategy Backtesting Platform v1.0*
