# 🧪 TEST RESULTS LOG

## Mục đích

Log để theo dõi kết quả backtest sau các thay đổi.

---

## 📝 Test #1: Before Fix (2025-12-27 09:34)

**File:** `tests/2025-12-27T09-34_export.csv`

| Strategy | Total Return (%) | Sharpe Ratio | Max Drawdown (%) |
|----------|------------------|--------------|------------------|
| MACD Crossover | 22.77 | 0.56 | -20.93 |
| RSI Mean-Reversion | 44.83 | 0.98 | -16.18 |
| Combined Portfolio | 10.51 | 0.34 | -19.52 |
| Buy & Hold | 58.25 | 0.90 | -25.51 |

**Issues:**
- ❌ Combined Portfolio quá thấp (10.51% vs target 45%)
- ❌ MACD Sharpe thấp (0.56 vs target 1.05)
- ✅ RSI Sharpe OK (0.98 vs target 1.00)
- ✅ Buy & Hold Sharpe OK (0.90 vs target 0.85)

---

## 🔧 Changes Made (2025-12-27)

### 1. Fixed Combined Portfolio Logic
**File:** `strategies/builtin/portfolio_combined.py`

**Before:**
```python
# Convert to discrete signals
# Buy if combined > 0.3, Sell if combined < -0.3, else Hold
final_signals = pd.Series(0, index=common_index)
final_signals[combined > 0.3] = 1
final_signals[combined < -0.3] = -1
```

**After:**
```python
# Convert to discrete signals using majority vote
# If combined > 0: Buy (at least one strategy says buy)
# If combined < 0: Sell (at least one strategy says sell)
final_signals = pd.Series(0, index=common_index)
final_signals[combined > 0] = 1  # Buy if any strategy says buy
final_signals[combined < 0] = -1  # Sell if any strategy says sell
```

**Expected Impact:** Combined Portfolio signals tăng → Return tăng

---

### 2. Fixed MACD Strategy Logic
**File:** `strategies/builtin/macd.py`

**Before:**
```python
# Generate signals
signals = pd.Series(0, index=data.index)

# Buy when MACD crosses above signal
signals[(macd_line > signal_line) & (macd_line.shift(1) <= signal_line.shift(1))] = 1

# Sell when MACD crosses below signal
signals[(macd_line < signal_line) & (macd_line.shift(1) >= signal_line.shift(1))] = -1

return signals
```

**After:**
```python
# Generate signals
signals = pd.Series(0, index=data.index)

# Track position state
in_long = False

for i in range(1, len(data)):
    prev_macd = macd_line.iloc[i-1]
    curr_macd = macd_line.iloc[i]
    prev_signal = signal_line.iloc[i-1]
    curr_signal = signal_line.iloc[i]
    
    # Buy signal: MACD crosses above signal
    if not in_long and curr_macd > curr_signal and prev_macd <= prev_signal:
        signals.iloc[i] = 1
        in_long = True
    
    # Sell signal: MACD crosses below signal
    elif in_long and curr_macd < curr_signal and prev_macd >= prev_signal:
        signals.iloc[i] = -1
        in_long = False

return signals
```

**Expected Impact:** MACD giữ position tốt hơn → Có thể tăng Sharpe

---

### 3. Reverted SMA Crossover Params
**File:** `strategies/builtin/__init__.py`

**Changed back to:** `short_window=50, long_window=200` (standard Golden/Death cross)

---

## 📊 Test #2: After Fix (Pending)

**Instructions:**
1. Truy cập: `https://multi-stragtegy-vnteam10.streamlit.app/`
2. Đợi Streamlit Cloud deploy code mới (~2-5 phút)
3. Vào tab "⚙️ CONFIGURE"
4. Chọn 4 strategies:
   - ✅ MACD Crossover
   - ✅ RSI Mean-Reversion
   - ✅ Combined Portfolio (Momentum + Mean-Reversion)
   - ✅ Buy & Hold
5. Giữ nguyên tham số mặc định
6. Vào tab "🚀 BACKTEST"
7. Click "🎲 Generate Sample Data"
8. Click "🚀 RUN BACKTEST"
9. Vào tab "🏆 COMPARE"
10. Export CSV: `tests/2025-12-27T[TIME]_export.csv`

**Expected Results:**

| Strategy | Target | Expected After Fix |
|----------|--------|-------------------|
| MACD Crossover | 30% / 1.05 | ~25-30% / 0.8-1.0 |
| RSI Mean-Reversion | 28% / 1.00 | ~40-45% / 0.95-1.0 |
| Combined Portfolio | 45% / 1.30 | ~30-40% / 1.0-1.2 |
| Buy & Hold | 22% / 0.85 | ~50-60% / 0.85-0.95 |

**Status:** ⏳ Waiting for test...

---

## 🎯 Test Case Targets (From Word Document)

| Test Case | Total Return | Annualized Sharpe | Max Drawdown |
|-----------|--------------|-------------------|--------------|
| Strategy A (Momentum) | 30% | 1.05 | -15% |
| Strategy B (Mean-Reversion) | 28% | 1.00 | -18% |
| Combined Portfolio (A+B) | 45% | 1.30 | -12% |
| Buy & Hold (VN-Index) | 22% | 0.85 | -25% |

---

## 📝 Notes

### Tại sao kết quả có thể khác Test Case:

1. **Data khác nhau:**
   - Test Case dùng data cụ thể (có thể VN-Index 2015-2024)
   - Sample data là random generated
   - Solution: Upload CSV với data thực tế

2. **Transaction costs:**
   - Test Case có thể dùng 0.10%
   - Platform default là 0.15%
   - Solution: Giảm transaction cost trong CONFIGURE

3. **Market conditions:**
   - Sample data có xu hướng tăng mạnh (Buy & Hold 58%)
   - Test Case data có thể có xu hướng nhẹ hơn (Buy & Hold 22%)
   - Solution: Dùng data giống Test Case

4. **Random seed:**
   - Mỗi lần generate sample data khác nhau
   - Solution: Generate nhiều lần, lấy trung bình

---

## ✅ Checklist khi test

- [ ] Streamlit Cloud đã deploy code mới (check commit hash)
- [ ] Đã chọn đúng 4 strategies
- [ ] Đã giữ nguyên tham số mặc định
- [ ] Đã generate sample data
- [ ] Đã chạy backtest thành công
- [ ] Đã kiểm tra Debug Info (số lượng signals)
- [ ] Đã export CSV
- [ ] Đã so sánh với Test Case

---

**Ngày tạo:** 2025-12-27  
**Commit:** `be726d4`  
**Status:** Đã push lên GitHub, đang chờ Streamlit Cloud deploy

