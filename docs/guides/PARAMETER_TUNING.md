# 🎛️ HƯỚNG DẪN ĐIỀU CHỈNH THAM SỐ STRATEGIES

## 📊 Ánh xạ Test Case → Implementation

| Test Case | Implementation | Default Params |
|-----------|----------------|----------------|
| **Strategy A (Momentum)** | MACD Crossover | Fast=12, Slow=26, Signal=9 |
| **Strategy B (Mean-Reversion)** | RSI Mean-Reversion | Period=14, Oversold=30, Overbought=70 |
| **Combined Portfolio (A+B)** | Combined Portfolio | Combines MACD + RSI |
| **Buy & Hold (VN-Index)** | Buy & Hold | N/A |

## 🎯 Mục tiêu: Khớp với Test Case

| Strategy | Test Case Target | CSV Export (Cũ) | Cần điều chỉnh |
|----------|------------------|----------------|----------------|
| **MACD (Strategy A)** | 30% return, 1.05 Sharpe | 22.77% return, 0.56 Sharpe | ⬆️ Tăng return |
| **RSI (Strategy B)** | 28% return, 1.00 Sharpe | 44.83% return, 0.98 Sharpe | ✅ Sharpe OK, return cao hơn |
| **Combined (A+B)** | 45% return, 1.30 Sharpe | 10.51% return, 0.34 Sharpe | ⬆️⬆️ Tăng mạnh |
| **Buy & Hold** | 22% return, 0.85 Sharpe | 58.25% return, 0.90 Sharpe | ✅ Sharpe OK, return cao hơn |

---

## 🔧 CÁC THAY ĐỔI ĐÃ THỰC HIỆN

### 1. ✅ Fixed Combined Portfolio Logic

**Vấn đề cũ:**
- Threshold quá cao (0.3) → Nhiều signals bị bỏ qua
- Khi MACD=1, RSI=-1 → Combined = 0 → Không có signal

**Giải pháp:**
- Dùng **majority vote**: `combined > 0` = Buy, `combined < 0` = Sell
- Bất kỳ strategy nào nói Buy/Sell thì sẽ có signal

**File:** `strategies/builtin/portfolio_combined.py`

---

### 2. ✅ Cải thiện MACD Strategy

**Vấn đề cũ:**
- Chỉ tạo signal khi cross → Quá ít signals
- Không giữ position giữa các crosses

**Giải pháp:**
- Thêm logic track position state
- Giữ position cho đến khi có cross ngược lại

**File:** `strategies/builtin/macd.py`

---

## 🎯 ĐIỀU CHỈNH THAM SỐ ĐỀ XUẤT

### MACD Crossover (Strategy A - Momentum)

**Mục tiêu:** Tăng return từ 22.77% → 30%, Sharpe từ 0.56 → 1.05

#### Option 1: Tham số nhạy hơn (Nhiều signals hơn)
```python
Fast = 8   # Giảm từ 12
Slow = 21  # Giảm từ 26
Signal = 5 # Giảm từ 9
```
**Lý do:** Tham số nhỏ hơn → Phản ứng nhanh hơn → Nhiều signals hơn

#### Option 2: Tham số chậm hơn (Ít signals, chất lượng cao)
```python
Fast = 15  # Tăng từ 12
Slow = 35  # Tăng từ 26
Signal = 12 # Tăng từ 9
```
**Lý do:** Tham số lớn hơn → Lọc nhiễu tốt hơn → Signals chất lượng cao hơn

#### Option 3: Giữ nguyên, test với data khác
- Có thể data hiện tại không phù hợp với MACD
- Thử với data VN-Index thực tế thay vì sample data

---

### RSI Mean-Reversion (Strategy B)

**Mục tiêu:** Giảm return từ 44.83% → 28% (Sharpe đã OK: 0.98 vs 1.00)

#### Option 1: Tăng threshold (Ít signals hơn)
```python
Period = 14      # Giữ nguyên
Oversold = 25    # Giảm từ 30 (khó trigger hơn)
Overbought = 75  # Tăng từ 70 (khó trigger hơn)
```
**Lý do:** Threshold khó hơn → Ít signals → Return thấp hơn

#### Option 2: Tăng period (Chậm hơn)
```python
Period = 20      # Tăng từ 14
Oversold = 30    # Giữ nguyên
Overbought = 70  # Giữ nguyên
```
**Lý do:** Period lớn hơn → Phản ứng chậm hơn → Ít signals

#### Option 3: Giữ nguyên
- Return cao hơn test case nhưng Sharpe tương đương → Có thể chấp nhận được

---

### Combined Portfolio

**Mục tiêu:** Tăng return từ 10.51% → 45%, Sharpe từ 0.34 → 1.30

**Đã fix logic** → Cần test lại. Nếu vẫn thấp, có thể do:

1. **MACD và RSI signals conflict:**
   - Khi MACD = Buy, RSI = Sell → Combined = 0 → Hold
   - Giải pháp: Dùng weighted voting hoặc priority

2. **Transaction costs quá cao:**
   - Combined có nhiều signals hơn → Nhiều trades → Nhiều fees
   - Thử giảm transaction cost xuống 0.10%

3. **Data không phù hợp:**
   - Sample data có thể không phù hợp với combined strategy
   - Thử với data thực tế

---

## 📝 CÁCH ĐIỀU CHỈNH TRÊN STREAMLIT

### Bước 1: Vào tab "⚙️ CONFIGURE"

### Bước 2: Click vào expander "Configure MACD Crossover"

### Bước 3: Điều chỉnh tham số

**Ví dụ cho MACD:**
- **Fast:** Thay đổi từ 12 → 8 (hoặc 15)
- **Slow:** Thay đổi từ 26 → 21 (hoặc 35)
- **Signal:** Thay đổi từ 9 → 5 (hoặc 12)

**Ví dụ cho RSI:**
- **Period:** Thay đổi từ 14 → 20
- **Oversold:** Thay đổi từ 30 → 25
- **Overbought:** Thay đổi từ 70 → 75

### Bước 4: Chạy lại Backtest

1. Vào tab "🚀 BACKTEST"
2. Click "🚀 RUN BACKTEST"
3. So sánh kết quả với test case

---

## 🧪 TESTING WORKFLOW

### 1. Test từng strategy riêng lẻ

**Test MACD:**
- Chỉ chọn MACD Crossover
- Chạy backtest
- Ghi lại return và Sharpe
- Điều chỉnh tham số nếu cần

**Test RSI:**
- Chỉ chọn RSI Mean-Reversion
- Chạy backtest
- Ghi lại return và Sharpe
- Điều chỉnh tham số nếu cần

### 2. Test Combined Portfolio

- Chọn cả MACD và RSI (và Combined Portfolio)
- Chạy backtest
- So sánh:
  - Combined return có cao hơn individual không?
  - Combined Sharpe có cao hơn không?
  - Combined drawdown có thấp hơn không?

### 3. So sánh với Test Case

| Metric | Test Case | Your Result | Status |
|--------|-----------|-------------|--------|
| MACD Return | 30% | ? | ⬆️/⬇️ |
| MACD Sharpe | 1.05 | ? | ⬆️/⬇️ |
| RSI Return | 28% | ? | ⬆️/⬇️ |
| RSI Sharpe | 1.00 | ? | ⬆️/⬇️ |
| Combined Return | 45% | ? | ⬆️/⬇️ |
| Combined Sharpe | 1.30 | ? | ⬆️/⬇️ |

---

## 💡 TIPS & TRICKS

### 1. Tham số nhỏ = Nhiều signals, nhiều noise
- ✅ Tốt cho trending markets
- ❌ Không tốt cho sideways markets

### 2. Tham số lớn = Ít signals, ít noise
- ✅ Tốt cho sideways markets
- ❌ Bỏ lỡ cơ hội trong trending markets

### 3. Combined Portfolio
- Nên combine strategies **khác loại** (momentum + mean-reversion)
- Không nên combine strategies **cùng loại** (2 momentum strategies)

### 4. Data Quality
- Sample data có thể không realistic
- Nên test với data thực tế (VN-Index, VN30)

### 5. Transaction Costs
- Test case có thể dùng transaction cost thấp hơn (0.10% thay vì 0.15%)
- Thử giảm transaction cost để xem impact

---

## 🔍 DEBUGGING

### Nếu Combined Portfolio vẫn thấp:

1. **Kiểm tra signals:**
   - Vào tab BACKTEST → Debug Info
   - Xem số lượng buy/sell signals của MACD và RSI
   - Xem số lượng signals của Combined

2. **Kiểm tra conflicts:**
   - Nếu MACD và RSI thường conflict → Combined sẽ có ít signals
   - Giải pháp: Dùng weighted voting (MACD weight = 0.6, RSI weight = 0.4)

3. **Kiểm tra transaction costs:**
   - Combined có nhiều trades hơn → Nhiều fees hơn
   - Thử giảm transaction cost xuống 0.10%

4. **Kiểm tra data:**
   - Sample data có thể không phù hợp
   - Thử với data thực tế

---

## ✅ CHECKLIST

Trước khi điều chỉnh:
- [ ] Đã fix Combined Portfolio logic
- [ ] Đã cải thiện MACD strategy
- [ ] Đã hiểu cách strategies hoạt động

Khi điều chỉnh:
- [ ] Test từng strategy riêng lẻ trước
- [ ] Ghi lại tham số và kết quả
- [ ] So sánh với test case
- [ ] Điều chỉnh từng bước (không thay đổi quá nhiều cùng lúc)

Sau khi điều chỉnh:
- [ ] Test lại Combined Portfolio
- [ ] So sánh tổng thể với test case
- [ ] Export CSV và so sánh

---

**Lưu ý:** Kết quả có thể không khớp 100% với test case vì:
- Data khác nhau
- Market conditions khác nhau
- Random seed khác nhau (nếu dùng sample data)

**Mục tiêu:** Đạt được kết quả **tương đương** (trong khoảng ±5-10%) với test case.

---

**Ngày tạo:** 2025-12-27  
**Cập nhật:** Sau khi fix Combined Portfolio và MACD logic

