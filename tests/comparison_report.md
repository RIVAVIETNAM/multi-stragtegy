# 📊 BÁO CÁO SO SÁNH: CSV EXPORT vs WORD DOCUMENT

## 📋 TÓM TẮT

**File CSV:** `tests/2025-12-27T09-34_export.csv`  
**File Word:** `5 TÀI LIỆU CHÍNH/CHECK VN10.docx`  
**Ngày so sánh:** 2025-12-27

---

## 📈 KẾT QUẢ CSV EXPORT (Thực tế từ Backtest)

| Strategy | Total Return (%) | Sharpe Ratio | Max Drawdown (%) | Win Rate (%) | Profit Factor | Number of Trades |
|----------|-----------------|--------------|------------------|-------------|---------------|------------------|
| **RSI Mean-Reversion** | 44.83 | 0.98 | -16.18 | 80.00 | 31.46 | 11 |
| **Buy & Hold** | 58.25 | 0.90 | -25.51 | 0.00 | 0.00 | 1 |
| **MACD Crossover** | 22.77 | 0.56 | -20.93 | 42.11 | 1.44 | 38 |
| **Combined Portfolio** | 10.51 | 0.34 | -19.52 | 47.37 | 1.20 | 38 |

---

## 🎯 TEST CASE TRONG WORD DOCUMENT (Mục tiêu)

| Test Case | Total Return (%) | Annualized Sharpe | Max Drawdown (%) |
|-----------|------------------|-------------------|------------------|
| **Strategy A (Momentum)** | 30% | 1.05 | -15% |
| **Strategy B (Mean-Reversion)** | 28% | 1.00 | -18% |
| **Combined Portfolio (A+B)** | 45% | 1.30 | -12% |
| **Buy & Hold (VN-Index)** | 22% | 0.85 | -25% |

---

## 🔍 SO SÁNH CHI TIẾT

### 1. Strategy A (Momentum) = MACD Crossover

| Metric | Test Case | CSV Export | Chênh lệch |
|--------|-----------|-----------|------------|
| **Total Return** | 30% | 22.77% | **-7.23%** ❌ |
| **Sharpe Ratio** | 1.05 | 0.56 | **-0.49** ❌ |
| **Max Drawdown** | -15% | -20.93% | **-5.93%** ❌ |

**Kết luận:** MACD Crossover trong CSV có performance **THẤP HƠN** test case đáng kể.

---

### 2. Strategy B (Mean-Reversion) = RSI Mean-Reversion

| Metric | Test Case | CSV Export | Chênh lệch |
|--------|-----------|-----------|------------|
| **Total Return** | 28% | 44.83% | **+16.83%** ✅ |
| **Sharpe Ratio** | 1.00 | 0.98 | **-0.02** ⚠️ |
| **Max Drawdown** | -18% | -16.18% | **+1.82%** ✅ |

**Kết luận:** RSI Mean-Reversion trong CSV có return **CAO HƠN** test case, nhưng Sharpe tương đương.

---

### 3. Combined Portfolio (A+B)

| Metric | Test Case | CSV Export | Chênh lệch |
|--------|-----------|-----------|------------|
| **Total Return** | 45% | 10.51% | **-34.49%** ❌❌ |
| **Sharpe Ratio** | 1.30 | 0.34 | **-0.96** ❌❌ |
| **Max Drawdown** | -12% | -19.52% | **-7.52%** ❌ |

**Kết luận:** Combined Portfolio trong CSV có performance **THẤP HƠN NHIỀU** so với test case. Đây là vấn đề lớn nhất!

---

### 4. Buy & Hold (Benchmark)

| Metric | Test Case | CSV Export | Chênh lệch |
|--------|-----------|-----------|------------|
| **Total Return** | 22% | 58.25% | **+36.25%** ✅✅ |
| **Sharpe Ratio** | 0.85 | 0.90 | **+0.05** ✅ |
| **Max Drawdown** | -25% | -25.51% | **-0.51%** ⚠️ |

**Kết luận:** Buy & Hold trong CSV có return **CAO HƠN NHIỀU** test case, có thể do data khác nhau.

---

## ⚠️ PHÂN TÍCH VẤN ĐỀ

### 🔴 Vấn đề nghiêm trọng: Combined Portfolio

**Test Case:** 45% return, 1.30 Sharpe  
**CSV Export:** 10.51% return, 0.34 Sharpe

**Nguyên nhân có thể:**
1. **Logic combine sai:** Có thể cách combine strategies không đúng
2. **Tham số strategies:** MACD và RSI có thể không tối ưu
3. **Data khác nhau:** Test case dùng data khác với CSV export
4. **Transaction costs:** Có thể transaction costs quá cao khi combine
5. **Signal conflicts:** Khi combine, signals có thể conflict nhau

### 🟡 Vấn đề: MACD Crossover (Strategy A)

**Test Case:** 30% return, 1.05 Sharpe  
**CSV Export:** 22.77% return, 0.56 Sharpe

**Nguyên nhân có thể:**
1. **Tham số chưa tối ưu:** Fast=12, Slow=26, Signal=9 có thể không phù hợp với data
2. **Data period khác:** Test case có thể dùng data period khác
3. **Market conditions:** Market conditions trong CSV khác với test case

### 🟢 Điểm tốt: RSI Mean-Reversion

**CSV Export có return cao hơn test case (44.83% vs 28%)**, nhưng Sharpe tương đương. Điều này cho thấy RSI strategy hoạt động tốt với data hiện tại.

### 🟢 Điểm tốt: Buy & Hold

**CSV Export có return cao hơn nhiều (58.25% vs 22%)**, cho thấy data trong CSV có xu hướng tăng mạnh hơn test case.

---

## 💡 KHUYẾN NGHỊ

### 1. Kiểm tra Logic Combined Portfolio

Cần review lại file `strategies/builtin/portfolio_combined.py`:
- Cách combine signals có đúng không?
- Có conflict giữa signals không?
- Weight allocation có đúng không?

### 2. Tối ưu tham số Strategies

Thử các tham số khác cho MACD:
- Fast=8, Slow=21, Signal=5 (nhạy hơn)
- Fast=15, Slow=35, Signal=12 (chậm hơn)

### 3. Sử dụng dữ liệu giống Test Case

Nếu có thể, sử dụng chính xác data mà test case đã dùng để so sánh công bằng.

### 4. Kiểm tra Transaction Costs

Test case có thể dùng transaction cost khác (0.10% thay vì 0.15%).

### 5. Debug Combined Portfolio

Thêm logging để xem:
- Số lượng signals từ mỗi strategy
- Cách combine signals
- Tại sao return thấp

---

## ✅ KẾT LUẬN

**CSV Export KHÔNG KHỚP hoàn toàn với Test Case trong Word Document.**

**Điểm khớp:**
- ✅ RSI Mean-Reversion: Sharpe tương đương (0.98 vs 1.00)
- ✅ Buy & Hold: Sharpe tương đương (0.90 vs 0.85)

**Điểm không khớp:**
- ❌ Combined Portfolio: Return và Sharpe thấp hơn nhiều
- ❌ MACD Crossover: Return và Sharpe thấp hơn
- ⚠️ Có thể do data khác nhau, tham số chưa tối ưu, hoặc logic combine chưa đúng

**Cần hành động:**
1. Review và fix logic Combined Portfolio
2. Tối ưu tham số MACD
3. Sử dụng data giống test case nếu có thể
4. Debug chi tiết Combined Portfolio

---

**Ngày tạo:** 2025-12-27  
**Người tạo:** Auto-generated comparison script

