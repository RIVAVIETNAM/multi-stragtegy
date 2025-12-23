# 🚀 HƯỚNG DẪN SỬ DỤNG STREAMLIT
## Multi-Strategy Backtesting Platform

---

## 🌐 TRUY CẬP PLATFORM

### ✅ Đã Deploy lên Cloud (Khuyến nghị)

**Không cần localhost!** Truy cập trực tiếp qua URL:

```
🔗https://multi-stragtegy-vnteam10.streamlit.app/
```

**Ưu điểm:**
- ✅ Truy cập từ bất kỳ đâu (máy tính, điện thoại, tablet)
- ✅ Không cần chạy code local
- ✅ Không cần cài Python
- ✅ Chia sẻ dễ dàng qua link

**Nhược điểm:**
- ❌ Phụ thuộc internet
- ❌ Giới hạn resources (1GB RAM)

---

### 🏠 Chạy Local (Cho developers)

**Chỉ dành cho lập trình viên cần test/modify code**

```bash
cd "6 new project"
streamlit run streamlit/MAIN.py
```
→ Mở browser: **http://localhost:8501**

**Khi nào cần local:**
- Khi đang phát triển/sửa code
- Khi test trước khi deploy
- Khi không có internet

---

## ⚡ QUICK START (5 PHÚT)

> **Lưu ý:** Hướng dẫn dưới đây áp dụng cho CẢ deployed version VÀ local version. 
> Chỉ khác nhau URL truy cập.

### Bước 1: Mở Platform
- **Cloud:** Mở`https://multi-stragtegy-vnteam10.streamlit.app/`
- **Local:** Chạy `streamlit run streamlit/MAIN.py` → `http://localhost:8501`

### Bước 2: Cấu hình (1 phút)
1. Click **CONFIGURE** ở sidebar
2. ✅ Tick vào **tất cả 4 strategies**
3. Giữ nguyên tham số mặc định

### Bước 3: Chạy Backtest (2 phút)
1. Click **BACKTEST** ở sidebar
2. Click nút **"🎲 Generate Sample Data"**
3. Click nút **"🚀 RUN BACKTEST"**
4. Đợi 5-10 giây

### Bước 4: Xem Kết quả (2 phút)
1. Click **RESULTS** → Xem charts
2. Click **COMPARE** → Xem leaderboard
3. ✅ Hoàn tất!

---

## 📱 GIAO DIỆN TỔNG QUAN

### 🎨 Theme & Design

**Light Theme (Mặc định):**
- ✅ Nền sáng, dễ nhìn
- ✅ Sidebar màu xám nhạt
- ✅ Text màu đen trên nền trắng
- ✅ Contrast tốt, dễ đọc
- ✅ Modern, professional design

**Tùy chỉnh:**
- Theme được cấu hình trong `.streamlit/config.toml`
- CSS tùy chỉnh trong `streamlit/app/assets/custom.css`

### Sidebar (Menu bên trái)

```
┌─────────────────────┐
│  📊 Navigation      │
│                     │
│  • MAIN             │ ← Trang chủ
│  • CONFIGURE        │ ← Cấu hình chiến lược
│  • BACKTEST         │ ← Chạy kiểm thử
│  • RESULTS          │ ← Xem kết quả
│  • COMPARE          │ ← So sánh
└─────────────────────┘
```

**Cách sử dụng:**
- Click vào tên page để chuyển trang
- Sidebar luôn hiện, không cần toggle

---

## 📖 HƯỚNG DẪN CHI TIẾT TỪNG TRANG

---

## 1️⃣ TRANG MAIN (Trang chủ)

### Giao diện
[Main Page]

### Nội dung hiển thị:
- **Title:** "🇻🇳 Multi-Strategy Backtesting Platform"
- **Subtitle:** "For Vietnamese Stock Market"
- **Section 1:** WELCOME
  - Key Features (5 bullets)
  - Quick Start box (bên phải)
  
- **Section 2:** Why This Platform?
  - Speed, Fairness, Specialized boxes
  
- **Section 3:** Built-in Strategies
  - 4 expandable cards: MACD, RSI, Bollinger, SMA
  
- **Section 4:** Vietnamese Market Rules
  - Price Limits (HOSE ±7%)
  - Settlement (T+2, T+3)

### Thao tác:
1. **Đọc giới thiệu** để hiểu platform
2. **Mở rộng strategy cards** để xem chi tiết
3. Click **sidebar → CONFIGURE** để bắt đầu

---

## 2️⃣ TRANG CONFIGURE (Cấu hình)

### Giao diện
[Configure Page]

### Phần 1: Select Strategies

```
┌─────────────────────────────────────┐
│ 📊 Select Strategies                │
├─────────────────────────────────────┤
│                                     │
│ ☑ MACD Crossover (Momentum)        │
│   └─ Configure MACD Crossover ▼    │
│                                     │
│ ☑ RSI Mean-Reversion (Mean-Rev)    │
│   └─ Configure RSI Mean-Rev ▼      │
│                                     │
│ ☑ Bollinger Bands (Volatility)     │
│   └─ Configure Bollinger Bands ▼   │
│                                     │
│ ☑ SMA Crossover (Trend)            │
│   └─ Configure SMA Crossover ▼     │
└─────────────────────────────────────┘
```

**Thao tác:**

**A. Chọn chiến lược:**
1. ✅ **Tick vào checkbox** để chọn chiến lược
2. Có thể chọn 1, 2, 3 hoặc tất cả 4
3. **Khuyến nghị:** Chọn tất cả 4 để so sánh đầy đủ

**B. Tùy chỉnh tham số (optional):**
1. Click **"Configure [Tên Strategy]"** để mở rộng
2. Thấy mô tả và tham số hiện tại
3. Dùng **number input** để thay đổi:
   - MACD: Fast (12), Slow (26), Signal (9)
   - RSI: Period (14), Oversold (30), Overbought (70)
   - Bollinger: Window (20), Num Std (2.0)
   - SMA: Short Window (50), Long Window (200)

### Phần 2: Backtest Parameters

```
┌─────────────────────────────────────┐
│ 🎯 Backtest Parameters              │
├─────────────────────────────────────┤
│ Initial Capital (VND)               │
│ [100,000,000         ] ← Input box  │
│                                     │
│ ☑ Enforce Vietnamese Market Rules   │
│   ✅ VN rules active: ±7% limit...  │
│                                     │
│ Transaction Cost (%)                │
│ [━━●━━━━━━━] 0.15%   ← Slider      │
└─────────────────────────────────────┘
```

**Thao tác:**

1. **Initial Capital (Vốn ban đầu):**
   - Click vào ô số
   - Nhập số tiền (VD: 100000000 = 100 triệu VND)
   - Phím ↑↓ để tăng/giảm

2. **VN Market Rules:**
   - ✅ **Bật (Recommended):** Realistic results
   - ❌ **Tắt:** Unrealistic, for comparison only

3. **Transaction Cost:**
   - Kéo slider: 0% → 1%
   - Mặc định: 0.15% (phí thực tế VN)

### Phần 3: Configuration Summary

```
┌─────────────────────────────────────┐
│ 📋 Configuration Summary            │
├─────────────────────────────────────┤
│  Strategies Selected    4           │
│  Initial Capital        100M VND    │
│  Transaction Cost       0.15%       │
└─────────────────────────────────────┘
```

**Kiểm tra:**
- Đảm bảo ≥ 1 strategy được chọn
- Vốn hợp lý (10M - 1B VND)
- Phí 0.1-0.3% là chuẩn

### ✅ Khi đã xong:
→ Click **BACKTEST** ở sidebar để tiếp tục

---

## 3️⃣ TRANG BACKTEST (Chạy kiểm thử)

### Giao diện
[Backtest Page]

> *Screenshot placeholder - Chụp trang Backtest với Sample Data button*

### Phần 1: Market Data

```
┌─────────────────────────────────────┐
│ 📊 Market Data                      │
├─────────────────────────────────────┤
│ ⚪ Sample Data (Demo)               │
│ ⚪ Upload CSV                        │
│ ⚪ VNStock API                       │
└─────────────────────────────────────┘
```

**OPTION 1: Sample Data (Khuyến nghị cho lần đầu)**

**Bước 1:** Click radio **"Sample Data (Demo)"**

**Bước 2:** Click nút **"🎲 Generate Sample Data"**
```
┌─────────────────────────────────────┐
│  🎲 Generate Sample Data            │ ← CLICK HERE
└─────────────────────────────────────┘
```

**Bước 3:** Đợi vài giây, thấy:
```
✅ Generated 500 days of sample data!

📈 Data Preview
┌──────────┬──────────┬──────────┐
│ Rows     │ 500      │          │
│ Start    │ 2023-... │          │
│ End      │ 2024-... │          │
└──────────┴──────────┴──────────┘

▼ View Data (expandable)
```

**OPTION 2: Upload CSV**

1. Click radio **"Upload CSV"**
2. Click **"Browse files"**
3. Chọn file CSV có cột: `close`, `high`, `low`, `volume`
4. Index phải là datetime

**OPTION 3: VNStock API** (Đang phát triển)
- Coming soon...

### Phần 2: Execute Backtest

```
┌─────────────────────────────────────┐
│ ⚡ Execute Backtest                  │
├─────────────────────────────────────┤
│ 📋 Execution Plan (expandable)      │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │  🚀 RUN BACKTEST                │ │ ← HUGE BLUE BUTTON
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**Thao tác:**

**Bước 1:** Click **"📋 Execution Plan"** để xem (optional):
```
Strategies: MACD Crossover, RSI Mean-Rev, Bollinger...
Data Points: 500
Initial Capital: 100,000,000 VND
Transaction Cost: 0.15%
VN Rules: Enabled
```

**Bước 2:** Click nút lớn **"🚀 RUN BACKTEST"**

**Bước 3:** Đợi xử lý:
```
⏳ Running parallel backtests...
[━━━━━━━━━━] Processing...
```

**Bước 4:** Sau 5-10 giây, thấy:
```
✅ Backtest completed for 4 strategies!
🎈 (Balloons animation)

🎯 Quick Results
┌────────────┬────────┬────────┬─────┐
│ Strategy   │ Return │ Sharpe │ DD  │
├────────────┼────────┼────────┼─────┤
│ MACD       │ 25.3%  │ 1.2    │-12% │
│ RSI        │ 18.5%  │ 0.9    │-15% │
│ Bollinger  │ 22.1%  │ 1.1    │-10% │
│ SMA        │ 20.8%  │ 1.0    │-14% │
└────────────┴────────┴────────┴─────┘
```

### ✅ Khi hoàn tất:
→ Click **RESULTS** hoặc **COMPARE** để xem chi tiết

---

## 4️⃣ TRANG RESULTS (Kết quả chi tiết)

### Giao diện
[Results Page - Charts]

### Phần 1: Multi-Strategy Performance

**Biểu đồ đường tổng hợp:**
```
        Portfolio Value (VND)
        ↑
120M    │         ╱╲  ___
        │    ╱──╲╱  ╲╱   ╲──── MACD
100M    │───╱              ╲─── RSI
        │  ╱                  ── Bollinger
 80M    │ ╱                   ── SMA
        │╱
        └────────────────────────→ Time
```

**Cách đọc:**
- **Trục X:** Thời gian (dates)
- **Trục Y:** Giá trị danh mục (VND)
- **Mỗi màu:** 1 chiến lược
- **Hover chuột:** Xem giá trị chính xác

**Ý nghĩa:**
- Đường đi lên 📈 = Chiến lược lời
- Đường đi xuống 📉 = Chiến lược lỗ
- Đường mượt = Ổn định
- Đường gập ghềnh = Biến động cao

### Phần 2: Individual Strategy Analysis

```
┌─────────────────────────────────────┐
│ 🔍 Individual Strategy Analysis     │
├─────────────────────────────────────┤
│ Select Strategy: [MACD Crossover ▼] │ ← Dropdown
└─────────────────────────────────────┘
```

**A. Metrics Row (4 chỉ số chính):**

```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Total Return │ Sharpe Ratio │ Max Drawdown │   Win Rate   │
│   +25.3%     │     1.20     │    -12.1%    │    62.5%     │
│   ↗ +25.3%   │   ✓ Good     │   ↘ -12.1%   │   ↗ 62.5%   │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

**Cách đọc:**
1. **Total Return (Lợi nhuận):**
   - +25.3% = Lãi 25.3%
   - Màu xanh nếu > 0
   - Số càng cao càng tốt

2. **Sharpe Ratio (Hiệu suất/Rủi ro):**
   - 1.20 = "Good" ✓
   - > 1.0 = Tốt
   - > 2.0 = Rất tốt
   - < 0 = Kém

3. **Max Drawdown (Sụt giảm tối đa):**
   - -12.1% = Mất tối đa 12.1%
   - Luôn âm
   - Càng gần 0 càng tốt
   - -10% OK, -30% High risk

4. **Win Rate (Tỷ lệ thắng):**
   - 62.5% = Thắng 62.5% số lệnh
   - > 50% = Tốt
   - 100% = Hiếm có

**B. Additional Metrics:**
```
┌────────────────┬─────────────────┬──────────────────┐
│ Profit Factor  │ Number of Trades│ Final Portfolio  │
│     2.15       │       45        │  125,300,000 VND │
└────────────────┴─────────────────┴──────────────────┘
```

**C. Tabs (3 tabs chi tiết):**

**Tab 1: 📉 Drawdown**
```
         Drawdown %
         ↑
    0%  │────╲
        │     ╲___
  -5%   │         ╲____╱────
        │              
 -10%   │                 ╲__
        │                    ╲
 -15%   │                     ╲
        └────────────────────────→ Time
```
- Vùng đỏ phía dưới 0
- Càng sâu = Rủi ro càng lớn

**Tab 2: 📊 Returns Distribution**
```
    Frequency
    ↑
40  │     ██
    │   ████
30  │  ██████
    │ ████████
20  │██████████
    │████████████
10  │██████████████
    └────────────────→ Daily Return %
      -5  0  +5
```
- Hình chuông = Ổn định
- Lệch trái/phải = Có bias

**Tab 3: 📋 Trade Log**
```
┌────────────┬──────┬────────┬────────┬───────────┐
│ Date       │ Type │ Price  │ Shares │ Cost      │
├────────────┼──────┼────────┼────────┼───────────┤
│ 2024-01-15 │ BUY  │ 85,000 │ 1,000  │ 85,127... │
│ 2024-02-20 │ SELL │ 92,500 │ 1,000  │ 92,361... │
│ 2024-03-10 │ BUY  │ 88,200 │ 1,100  │ 97,152... │
│ ...        │ ...  │ ...    │ ...    │ ...       │
└────────────┴──────┴────────┴────────┴───────────┘
```

### Phần 3: Best Performers

```
┌─────────────────┬─────────────────┬─────────────────┐
│  Best Return    │ Best Risk-Adj   │ Lowest Drawdown │
├─────────────────┼─────────────────┼─────────────────┤
│  MACD Crossover │ Bollinger Bands │ Bollinger Bands │
│     25.3%       │  Sharpe: 1.25   │    -10.2%       │
└─────────────────┴─────────────────┴─────────────────┘
```

### ✅ Tip:
Chiến lược tốt = Return cao + Sharpe > 1 + Drawdown thấp

---

## 5️⃣ TRANG COMPARE (So sánh)

### Giao diện
[Compare Page - Leaderboard]

### Phần 1: Summary Statistics

```
┌─────────────────────────────────────────────────────┐
│  Best Return │ Best Sharpe │ Lowest DD │ Total     │
│    25.3%     │    1.25     │  -10.2%   │ Strategies│
│              │             │           │     4     │
└─────────────────────────────────────────────────────┘
```

### Phần 2: Performance Leaderboard (Bảng chính)

```
┌─────────────────┬────────┬────────┬─────────┬──────────┬──────────┬────────┐
│ Index │ Strategy│ Return │ Sharpe │ Max DD  │ Win Rate │ Profit F │ Trades │
├───────┼─────────┼────────┼────────┼─────────┼──────────┼──────────┼────────┤
│   1   │Bollinger│ 22.1%  │  1.25  │ -10.2%  │  65.2%   │   2.3    │   42   │ 🟩
│   2   │MACD     │ 25.3%  │  1.20  │ -12.1%  │  62.5%   │   2.1    │   45   │ 🟩
│   3   │SMA      │ 20.8%  │  1.00  │ -14.3%  │  58.9%   │   1.8    │   38   │ 🟨
│   4   │RSI      │ 18.5%  │  0.90  │ -15.8%  │  55.1%   │   1.5    │   51   │ 🟥
└───────┴─────────┴────────┴────────┴─────────┴──────────┴──────────┴────────┘

📌 Sorted by Sharpe Ratio (risk-adjusted returns)
🟩 Green = Better | 🟥 Red = Worse
```

**Cách đọc màu sắc:**
- **Return, Sharpe, Win Rate:** 🟩 Xanh = Cao (tốt), 🟥 Đỏ = Thấp (kém)
- **Max Drawdown:** 🟩 Xanh = Gần 0 (tốt), 🟥 Đỏ = Rất âm (kém)

### Phần 3: Rankings by Metric

```
┌─────────────────────┬──────────────────────┐
│  By Total Return    │  By Sharpe Ratio     │
├─────────────────────┼──────────────────────┤
│ 🥇 MACD: 25.3%      │ 🥇 Bollinger: 1.25   │
│ 🥈 Bollinger: 22.1% │ 🥈 MACD: 1.20        │
│ 🥉 SMA: 20.8%       │ 🥉 SMA: 1.00         │
│ #4 RSI: 18.5%       │ #4 RSI: 0.90         │
└─────────────────────┴──────────────────────┘
```

**Lưu ý:** Ranking theo Sharpe ≠ Ranking theo Return!

### Phần 4: Radar Chart

[Radar Chart]

> *Screenshot: Biểu đồ radar 4 trục*

```
        Return
          ↑
          │
  PF ←────┼────→ Sharpe
          │
          ↓
      Win Rate
```
- Mỗi chiến lược = 1 màu
- Vùng càng rộng = Càng tốt overall

### Phần 5: Winner Announcement

```
┌─────────────────────────────────────┐
│          🏆 BOLLINGER BANDS         │
│                                     │
│  Sharpe Ratio:    1.25              │
│  Total Return:    22.1%             │
│  Max Drawdown:    -10.2%            │
│  Win Rate:        65.2%             │
│                                     │
│  *Based on risk-adjusted returns*   │
└─────────────────────────────────────┘
```

**Tại sao Bollinger thắng?**
→ Vì Sharpe cao nhất (tính cả rủi ro), không chỉ Return

### Phần 6: Export Results

```
┌─────────────────────────────────────┐
│  📊 Download Leaderboard (CSV)      │ ← Click to download
├─────────────────────────────────────┤
│  📄 PDF export coming soon...       │
└─────────────────────────────────────┘
```

**File CSV tải về:**
- Tên: `vn10_leaderboard_20241223.csv`
- Mở bằng Excel để phân tích thêm

---

## 🎯 WORKFLOW HOÀN CHỈNH (Checklist)

### Lần đầu tiên (30 phút)

- [ ] **1. Start** 
  - Chạy `streamlit run streamlit/MAIN.py`
  - Mở http://localhost:8501

- [ ] **2. CONFIGURE (5 phút)**
  - Tick 4 strategies
  - Vốn: 100M VND
  - VN Rules: ON
  - Phí: 0.15%

- [ ] **3. BACKTEST (10 phút)**
  - Generate Sample Data
  - Click RUN BACKTEST
  - Đợi kết quả

- [ ] **4. RESULTS (10 phút)**
  - Xem equity curves
  - Chọn từng strategy
  - Đọc 4 metrics
  - Browse 3 tabs

- [ ] **5. COMPARE (5 phút)**
  - Xem leaderboard
  - So sánh rankings
  - Tìm winner
  - Download CSV

### Lần sau (15 phút)

- [ ] Upload dữ liệu thật (CSV)
- [ ] Thử điều chỉnh tham số
- [ ] Chạ lại backtest
- [ ] So sánh với lần trước

---

## 💡 TIPS & TRICKS

### Tip 1: Đọc Sharpe, không chỉ Return
❌ **Sai:** "MACD có Return 25.3% cao nhất → Tốt nhất"
✅ **Đúng:** "Bollinger có Sharpe 1.25 cao nhất → Tốt nhất (tính rủi ro)"

### Tip 2: Luôn bật VN Rules
✅ Realistic results cho thị trường Việt Nam
❌ Tắt = Kết quả không thực tế

### Tip 3: Test nhiều strategies
- Ít nhất 2-3 strategies để so sánh
- Tốt nhất là test cả 4

### Tip 4: Kiểm tra Trade Log nếu lạ
- Tab "Trade Log" trong RESULTS
- Đảm bảo số lệnh hợp lý (không quá ít/nhiều)

### Tip 5: Win Rate cao ≠ Lời nhiều
- Win 80% nhưng lỗ lớn khi thua = Vẫn lỗ
- Win 40% nhưng lãi lớn khi thắng = Có thể lời

### Tip 6: Download CSV để phân tích offline
- COMPARE page → Download Leaderboard
- Mở Excel → Làm thêm charts/pivot tables

---

## 🚨 XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi 1: "No strategies selected"
**Nguyên nhân:** Chưa tick strategy ở CONFIGURE
**Giải pháp:** Quay lại CONFIGURE, tick ít nhất 1 strategy

### Lỗi 2: "No market data loaded"
**Nguyên nhân:** Chưa generate data ở BACKTEST
**Giải pháp:** Click "Generate Sample Data" hoặc upload CSV

### Lỗi 3: Charts không hiện
**Nguyên nhân:** Chưa chạy backtest
**Giải pháp:** 
1. CONFIGURE → Chọn strategies
2. BACKTEST → Generate data → RUN
3. Sau đó mới vào RESULTS/COMPARE

### Lỗi 4: Sidebar menu không thay đổi
**Nguyên nhân:** Cache browser
**Giải pháp:** Nhấn **Ctrl + Shift + R** để hard reload

### Lỗi 5: Streamlit không mở
**Nguyên nhân:** Port 8501 bị chiếm
**Giải pháp:**
```bash
streamlit run streamlit/MAIN.py --server.port 8502
```

---

## ❓ FAQ

**Q: Backtesting có chính xác không?**
A: Backtest chỉ mô phỏng quá khứ, không đảm bảo tương lai. Nhưng hữu ích để lọc strategies kém.

**Q: Tại sao cần nhiều strategies?**
A: Để so sánh và tìm chiến lược tốt nhất cho portfolio của bạn.

**Q: VN Rules có cần thiết?**
A: CÓ! Không có VN rules = kết quả không thực tế cho thị trường Việt.

**Q: Sharpe Ratio tốt là bao nhiêu?**
A: > 1.0 = Tốt, > 2.0 = Rất tốt, < 0 = Kém

**Q: Có thể tùy chỉnh strategies không?**
A: Có! Mở expander trong CONFIGURE để điều chỉnh tham số.

---

**Chúc bạn backtesting thành công! 🇻🇳📈**

*Multi-Strategy Backtesting Platform v1.0*
