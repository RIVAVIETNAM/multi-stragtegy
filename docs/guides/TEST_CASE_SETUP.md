# 📊 HƯỚNG DẪN TẠO TEST CASE KẾT QUẢ

## 🎯 Mục tiêu

Kết quả backtest thực tế từ platform:

| Test Case | Total Return | Annualized Sharpe | Max Drawdown |
|-----------|--------------|-------------------|--------------|
| Strategy A (MACD - Momentum) | 22.77% | 0.56 | -20.93% |
| Strategy B (RSI - Mean-Reversion) | 44.83% | 0.98 | -16.18% |
| Combined Portfolio (A+B) | 10.51% | 0.34 | -19.52% |
| Buy & Hold (VN-Index) | 58.25% | 0.90 | -25.51% |

---

## 📋 CÁC BƯỚC THỰC HIỆN

### Bước 1: Truy cập Platform

**Cloud (Khuyến nghị):**
```
https://multi-stragtegy-vnteam10.streamlit.app/
```

**Local:**
```bash
cd "6 new project"
streamlit run streamlit/MAIN.py
```
→ Mở `http://localhost:8501`

---

### Bước 2: Cấu hình Strategies

1. **Click vào tab "⚙️ CONFIGURE"** ở sidebar

2. **Chọn các strategies sau:**
   - ✅ **MACD Crossover** (Strategy A - Momentum)
   - ✅ **RSI Mean-Reversion** (Strategy B - Mean-Reversion)
   - ✅ **Combined Portfolio (Momentum + Mean-Reversion)** (A+B)
   - ✅ **Buy & Hold** (Benchmark)

3. **Cấu hình tham số:**

   **MACD Crossover (Momentum):**
   - Fast: `12` (mặc định)
   - Slow: `26` (mặc định)
   - Signal: `9` (mặc định)

   **RSI Mean-Reversion:**
   - Period: `14` (mặc định)
   - Oversold: `30` (mặc định)
   - Overbought: `70` (mặc định)

   **Combined Portfolio:**
   - Không có tham số (tự động combine MACD + RSI với equal weight)

   **Buy & Hold:**
   - Không có tham số (mua ở đầu, giữ đến cuối)

4. **Cấu hình Backtest Parameters:**
   - **Initial Capital:** `100,000,000 VND` (100 triệu)
   - **Transaction Cost:** `0.15%` (mặc định)
   - ✅ **Enforce Vietnamese Market Rules:** Bật

---

### Bước 3: Load Market Data

1. **Click vào tab "🚀 BACKTEST"** ở sidebar

2. **Chọn data source:**
   - **Option 1: Sample Data (Demo)**
     - Click nút **"🎲 Generate Sample Data"**
     - Sử dụng dữ liệu mô phỏng (500 ngày)
   
   - **Option 2: Upload CSV**
     - Upload file CSV có cấu trúc:
       ```csv
       date,close,high,low,volume
       2023-01-01,100.0,102.0,98.0,1000000
       2023-01-02,101.0,103.0,99.0,1200000
       ...
       ```
     - Index column phải là `date` (datetime)
     - Phải có các cột: `close`, `high`, `low`, `volume`

   - **Option 3: VNStock API** (Coming soon)

3. **Kiểm tra Data Preview:**
   - Xem số rows, start date, end date
   - Đảm bảo có đủ dữ liệu (ít nhất 200-500 ngày để có signals)

---

### Bước 4: Chạy Backtest

1. **Kiểm tra Execution Plan:**
   - Click vào expander "📋 Execution Plan"
   - Xác nhận:
     - Strategies: MACD Crossover, RSI Mean-Reversion, Combined Portfolio, Buy & Hold
     - Data Points: Số ngày dữ liệu
     - Initial Capital: 100,000,000 VND
     - Transaction Cost: 0.15%
     - VN Rules: Enabled

2. **Click nút "🚀 RUN BACKTEST"**

3. **Đợi kết quả:**
   - Thời gian: 5-30 giây (tùy số lượng strategies và data)
   - Xem Quick Results table hiển thị ngay sau khi chạy xong

---

### Bước 5: Xem Kết Quả Chi Tiết

#### 5.1. Tab "📈 RESULTS"

1. **Multi-Strategy Performance Chart:**
   - Xem equity curves của tất cả strategies trên cùng 1 chart
   - So sánh đường cong tăng trưởng

2. **Individual Strategy Analysis:**
   - Chọn từng strategy từ dropdown
   - Xem metrics:
     - Total Return (%)
     - Sharpe Ratio
     - Max Drawdown (%)
     - Win Rate (%)
     - Profit Factor
     - Number of Trades
     - Final Portfolio Value
   - Xem charts:
     - Drawdown chart
     - Returns distribution
     - Trade log

#### 5.2. Tab "🏆 COMPARE"

1. **Performance Leaderboard:**
   - Bảng so sánh tất cả strategies
   - Sắp xếp theo Sharpe Ratio (mặc định)
   - Color-coded: Green = Better, Red = Worse

2. **Rankings by Metric:**
   - By Total Return
   - By Sharpe Ratio

3. **Strategy Performance Matrix:**
   - RRG-style chart (Relative Strength vs Momentum)
   - Radar chart (normalized metrics)

4. **Best Strategy:**
   - Strategy có Sharpe Ratio cao nhất

---

## 🔧 TINH CHỈNH ĐỂ ĐẠT KẾT QUẢ TƯƠNG TỰ TEST CASE

### ⚠️ Lưu ý quan trọng:

**Kết quả thực tế sẽ KHÁC với test case vì:**
- Test case sử dụng dữ liệu cụ thể (không rõ)
- Test case có thể đã được tối ưu tham số
- Market conditions khác nhau
- Random seed khác nhau (nếu dùng sample data)

### 💡 Cách tinh chỉnh:

#### 1. **Điều chỉnh tham số strategies:**

**MACD Crossover (để tăng return):**
- Thử: Fast=`8`, Slow=`21`, Signal=`5` (nhạy hơn)
- Hoặc: Fast=`15`, Slow=`35`, Signal=`12` (chậm hơn, ít signals hơn)

**RSI Mean-Reversion (để tăng return):**
- Thử: Period=`10`, Oversold=`25`, Overbought=`75` (nhạy hơn)
- Hoặc: Period=`20`, Oversold=`35`, Overbought=`65` (chậm hơn)

#### 2. **Sử dụng dữ liệu thực tế:**

- Upload CSV với dữ liệu VN-Index thực tế
- Hoặc dữ liệu cổ phiếu cụ thể
- Dữ liệu càng dài càng tốt (1-2 năm)

#### 3. **Điều chỉnh transaction cost:**

- Giảm transaction cost xuống `0.10%` hoặc `0.05%` để tăng return
- Tăng lên `0.20%` hoặc `0.25%` để giảm return (realistic hơn)

#### 4. **Tắt VN Rules (nếu cần):**

- Tắt "Enforce Vietnamese Market Rules" để có kết quả khác
- (Không khuyến nghị - không realistic)

#### 5. **Thử nhiều lần với sample data:**

- Sample data sử dụng random seed
- Mỗi lần generate sẽ khác nhau
- Thử generate lại nhiều lần để tìm kết quả tốt

---

## 📊 GIẢI THÍCH KẾT QUẢ

### Metrics quan trọng:

1. **Total Return (%):**
   - Lợi nhuận tổng từ đầu đến cuối
   - Formula: `(Final Equity - Initial Capital) / Initial Capital * 100`

2. **Annualized Sharpe Ratio:**
   - Đo lường risk-adjusted return
   - Formula: `(Mean Return / Std Dev) * sqrt(252)`
   - > 1.0 = Tốt, > 2.0 = Rất tốt

3. **Max Drawdown (%):**
   - Mức giảm tối đa từ peak
   - Càng âm càng tệ (ví dụ: -25% tệ hơn -12%)

4. **Win Rate (%):**
   - Tỷ lệ trades thắng
   - > 50% = Tốt

5. **Profit Factor:**
   - Tỷ lệ tổng lợi nhuận / tổng lỗ
   - > 1.0 = Tốt, > 2.0 = Rất tốt

### Kết quả thực tế:

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|--------------|
| MACD (Strategy A) | 22.77% | 0.56 | -20.93% |
| RSI (Strategy B) | 44.83% | 0.98 | -16.18% |
| Combined Portfolio | 10.51% | 0.34 | -19.52% |
| Buy & Hold | 58.25% | 0.90 | -25.51% |

**Lưu ý:** 
- RSI strategy achieved the best risk-adjusted returns (Sharpe 0.98)
- Combined Portfolio underperformed due to signal conflicts between momentum and mean-reversion
- Buy & Hold significantly outperformed (58.25%), indicating a strong bullish market period

---

## 🐛 TROUBLESHOOTING

### ❌ Backtest ra toàn 0:

**Nguyên nhân:**
- Không có signals (thuật toán không tạo buy/sell)
- Transaction cost quá cao
- Không đủ cash để mua

**Giải pháp:**
1. Kiểm tra Debug Info trong tab BACKTEST
2. Xem số lượng buy/sell signals
3. Giảm transaction cost xuống 0.05%
4. Tăng initial capital
5. Thử strategies khác (SMA Crossover thường có nhiều signals)

### ❌ Không có Combined Portfolio trong list:

**Nguyên nhân:**
- Code chưa được update
- Import lỗi

**Giải pháp:**
1. Pull code mới nhất từ GitHub
2. Restart Streamlit app
3. Kiểm tra `strategies/builtin/__init__.py` có `Combined Portfolio` không

### ❌ Buy & Hold không hoạt động:

**Nguyên nhân:**
- Strategy chỉ mua ở đầu, không bán ở cuối
- Cần đợi đến cuối mới thấy return

**Giải pháp:**
- Đây là đúng behavior của Buy & Hold
- Return sẽ được tính khi backtest kết thúc

---

## 📝 EXPORT KẾT QUẢ

### Export Leaderboard:

1. Vào tab **COMPARE**
2. Scroll xuống phần **"📥 Export Results"**
3. Click **"📊 Download Leaderboard (CSV)"**
4. File sẽ có tên: `vn10_leaderboard_YYYYMMDD.csv`

### Format CSV:

```csv
Strategy,Total Return (%),Sharpe Ratio,Max Drawdown (%),Win Rate (%),Profit Factor,Number of Trades
MACD Crossover,22.77,0.56,-20.93,42.11,1.44,38
RSI Mean-Reversion,44.83,0.98,-16.18,80.00,31.46,11
Combined Portfolio (Momentum + Mean-Reversion),10.51,0.34,-19.52,47.37,1.20,38
Buy & Hold,58.25,0.90,-25.51,0.00,0.00,1
```

---

## ✅ CHECKLIST

Trước khi chạy backtest, đảm bảo:

- [ ] Đã chọn đúng 4 strategies: MACD, RSI, Combined, Buy & Hold
- [ ] Đã load market data (sample hoặc CSV)
- [ ] Initial Capital = 100,000,000 VND
- [ ] Transaction Cost = 0.15%
- [ ] VN Rules = Enabled
- [ ] Data có ít nhất 200-500 ngày
- [ ] Đã kiểm tra Execution Plan

Sau khi chạy:

- [ ] Xem Quick Results table
- [ ] Vào RESULTS tab xem charts
- [ ] Vào COMPARE tab xem leaderboard
- [ ] Export CSV nếu cần
- [ ] So sánh với test case

---

## 🎓 TIPS & TRICKS

1. **Dùng dữ liệu thực tế:**
   - Sample data chỉ để demo
   - Dữ liệu thực tế sẽ cho kết quả chính xác hơn

2. **Test nhiều tham số:**
   - Thử nhiều combination của tham số
   - Ghi lại kết quả tốt nhất

3. **So sánh với benchmark:**
   - Luôn so sánh với Buy & Hold
   - Strategy phải tốt hơn Buy & Hold mới đáng đầu tư

4. **Xem drawdown:**
   - Return cao nhưng drawdown lớn = Rủi ro cao
   - Cân bằng giữa return và risk

5. **Kiểm tra số trades:**
   - Quá ít trades = Không đủ dữ liệu
   - Quá nhiều trades = Transaction cost cao

---

## 📞 HỖ TRỢ

Nếu gặp vấn đề:

1. Kiểm tra **Debug Info** trong tab BACKTEST
2. Xem **Troubleshooting** section ở trên
3. Kiểm tra logs trong console (nếu chạy local)
4. Xem documentation trong `docs/` folder

---

**Chúc bạn backtest thành công! 🚀**

