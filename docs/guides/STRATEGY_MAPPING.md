# 📊 STRATEGY MAPPING: CODE vs TEST CASE

## Ánh xạ giữa Test Case và Implementation

| Test Case | Implementation | Default Params | Type |
|-----------|----------------|----------------|------|
| **Strategy A (Momentum)** | MACD Crossover | Fast=12, Slow=26, Signal=9 | Momentum |
| **Strategy B (Mean-Reversion)** | RSI Mean-Reversion | Period=14, Oversold=30, Overbought=70 | Mean-Reversion |
| **Combined Portfolio (A+B)** | Combined Portfolio (Momentum + Mean-Reversion) | N/A (combines MACD + RSI) | Portfolio |
| **Buy & Hold (VN-Index)** | Buy & Hold | N/A | Benchmark |

---

## Chi tiết Strategies

### Strategy A (Momentum) = MACD Crossover

**Actual Results:**
- Total Return: 22.77%
- Annualized Sharpe: 0.56
- Max Drawdown: -20.93%

**Implementation:**
- File: `strategies/builtin/macd.py`
- Function: `macd_crossover(data, fast=12, slow=26, signal=9)`
- Logic: Buy when MACD line crosses above signal line, sell when crosses below

**Default Params:**
```python
Fast = 12    # Fast EMA period
Slow = 26    # Slow EMA period
Signal = 9   # Signal line period
```

---

### Strategy B (Mean-Reversion) = RSI Mean-Reversion

**Actual Results:**
- Total Return: 44.83%
- Annualized Sharpe: 0.98
- Max Drawdown: -16.18%

**Implementation:**
- File: `strategies/builtin/rsi.py`
- Function: `rsi_mean_reversion(data, period=14, oversold=30, overbought=70)`
- Logic: Buy when RSI < 30 (oversold), sell when RSI > 70 (overbought)

**Default Params:**
```python
Period = 14        # RSI calculation period
Oversold = 30      # Buy threshold
Overbought = 70    # Sell threshold
```

---

### Combined Portfolio (A+B)

**Actual Results:**
- Total Return: 10.51%
- Annualized Sharpe: 0.34
- Max Drawdown: -19.52%

**Implementation:**
- File: `strategies/builtin/portfolio_combined.py`
- Function: `momentum_mean_reversion_combined(data)`
- Logic: Combines MACD and RSI signals using majority vote

**How it works:**
1. Get signals from MACD: `macd_signals`
2. Get signals from RSI: `rsi_signals`
3. Combine: `combined = macd_signals + rsi_signals`
4. If `combined > 0`: Buy (at least one says buy)
5. If `combined < 0`: Sell (at least one says sell)
6. If `combined == 0`: Hold (conflict or both hold)

**Example:**
- MACD = 1 (Buy), RSI = 1 (Buy) → Combined = 2 → Buy
- MACD = 1 (Buy), RSI = 0 (Hold) → Combined = 1 → Buy
- MACD = 1 (Buy), RSI = -1 (Sell) → Combined = 0 → Hold
- MACD = -1 (Sell), RSI = -1 (Sell) → Combined = -2 → Sell

---

### Buy & Hold (VN-Index)

**Actual Results:**
- Total Return: 58.25%
- Annualized Sharpe: 0.90
- Max Drawdown: -25.51%

**Implementation:**
- File: `strategies/builtin/buy_hold.py`
- Function: `buy_hold(data)`
- Logic: Buy at the first day, hold until the end

**How it works:**
1. Generate signal = 1 (Buy) at index 0
2. Hold for the rest of the period
3. No sell signal (or sell at the last day for comparison)

---

## Other Strategies (Not in Test Case)

### Bollinger Bands

**Implementation:**
- File: `strategies/builtin/bollinger.py`
- Function: `bollinger_bands(data, window=20, num_std=2.0)`
- Logic: Buy at lower band, sell at upper band

**Default Params:**
```python
Window = 20      # Moving average window
Num_Std = 2.0    # Number of standard deviations
```

---

### SMA Crossover

**Implementation:**
- File: `strategies/builtin/sma.py`
- Function: `sma_crossover(data, short_window=50, long_window=200)`
- Logic: Golden Cross (buy) / Death Cross (sell)

**Default Params:**
```python
Short_Window = 50    # Short-term MA
Long_Window = 200    # Long-term MA
```

**Note:** Tham số 50/200 là standard cho Golden/Death cross, nhưng có thể không phù hợp với sample data (500 points). Cần ít nhất 200+ data points để tính long MA.

---

## Cách sử dụng trên Streamlit

### Để test theo Test Case:

1. **Vào tab "⚙️ CONFIGURE"**

2. **Chọn 4 strategies:**
   - ✅ MACD Crossover (Strategy A)
   - ✅ RSI Mean-Reversion (Strategy B)
   - ✅ Combined Portfolio (Momentum + Mean-Reversion) (A+B)
   - ✅ Buy & Hold (Benchmark)

3. **Giữ nguyên tham số mặc định** (đã match với Test Case)

4. **Vào tab "🚀 BACKTEST"**
   - Generate sample data (hoặc upload CSV)
   - Click "🚀 RUN BACKTEST"

5. **So sánh kết quả với Test Case:**

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|--------------|
| MACD (A) | 22.77% | 0.56 | -20.93% |
| RSI (B) | 44.83% | 0.98 | -16.18% |
| Combined (A+B) | 10.51% | 0.34 | -19.52% |
| Buy & Hold | 58.25% | 0.90 | -25.51% |

---

## Lưu ý quan trọng

### 1. Data khác nhau = Kết quả khác nhau

Test Case sử dụng data cụ thể (có thể là VN-Index 2015-2024). Nếu bạn dùng:
- Sample data → Kết quả sẽ khác
- Data period khác → Kết quả sẽ khác
- Ticker khác → Kết quả sẽ khác

### 2. Tham số đã được chuẩn hóa

Tất cả tham số mặc định đã match với Test Case:
- MACD: 12/26/9 ✅
- RSI: 14/30/70 ✅
- Bollinger: 20/2.0 ✅
- SMA: 50/200 ✅

### 3. Combined Portfolio logic đã được fix

- **Cũ:** Threshold 0.3 → Nhiều signals bị bỏ qua
- **Mới:** Majority vote → Bất kỳ strategy nào nói Buy/Sell đều được tính

### 4. MACD logic đã được cải thiện

- **Cũ:** Chỉ signal khi cross → Quá ít signals
- **Mới:** Track position state → Giữ position cho đến khi có cross ngược lại

---

## Troubleshooting

### Nếu Combined Portfolio vẫn thấp:

1. **Kiểm tra signals:**
   - Debug Info trong tab BACKTEST
   - Xem số lượng buy/sell signals của MACD và RSI
   - Xem số lượng signals của Combined

2. **Kiểm tra conflicts:**
   - Nếu MACD và RSI thường conflict → Combined ít signals
   - Có thể cần weighted voting thay vì equal weight

3. **Kiểm tra transaction costs:**
   - Combined có nhiều trades → Nhiều fees
   - Thử giảm transaction cost xuống 0.10%

4. **Sử dụng data thực tế:**
   - Sample data có thể không phù hợp
   - Upload CSV với data VN-Index thực tế

---

**Ngày tạo:** 2025-12-27  
**Cập nhật:** Sau khi fix Combined Portfolio và MACD logic

