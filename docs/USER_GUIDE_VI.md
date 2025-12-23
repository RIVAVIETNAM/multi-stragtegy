# 📖 HƯỚNG DẪN SỬ DỤNG VN10 PLATFORM

## Nền tảng Backtesting Đa Chiến Lược

---

## 🚀 KHỞI ĐỘNG

### Chạy ứng dụng

```bash
cd "D:\OneDrive\2026\IPITEX\10 Multi-Strategy Backtesting Platform\6 new project"
streamlit run app/main.py
```

Ứng dụng sẽ mở tại: **http://localhost:8501**

---

## 📱 GIAO DIỆN CHÍNH

VN10 có **4 trang chính**, navigate bằng sidebar bên trái:

1. **⚙️ Configure** - Cấu hình chiến lược
2. **🚀 Backtest** - Chạy kiểm thử
3. **📈 Results** - Xem kết quả chi tiết
4. **🏆 Compare** - So sánh chiến lược

---

## BƯỚC 1: CONFIGURE (Cấu hình) ⚙️

### Chọn chiến lược

**Location:** Sidebar → Configure

1. Tick vào checkbox các chiến lược muốn test:

   - ✅ **MACD Crossover** (Động lượng)
   - ✅ **RSI Mean-Reversion** (Phản hồi)
   - ✅ **Bollinger Bands** (Biến động)
   - ✅ **SMA Crossover** (Xu hướng)
2. Mở rộng mỗi chiến lược để **tùy chỉnh tham số**:

   - MACD: Fast, Slow, Signal
   - RSI: Period, Oversold, Overbought
   - Bollinger: Window, Num Std
   - SMA: Short Window, Long Window

### Cài đặt Backtest

**Vốn ban đầu (Initial Capital):**

- Mặc định: 100,000,000 VND
- Có thể điều chỉnh từ 1M - 1B VND

**Phí giao dịch (Transaction Cost):**

- Mặc định: 0.15% mỗi giao dịch
- Slider: 0% - 1%

**Quy tắc VN (Vietnamese Market Rules):**

- ✅ **Bật (Recommended):** Áp dụng ±7% giới hạn, T+2 thanh toán
- ❌ **Tắt:** Kết quả không thực tế, chỉ để so sánh

### Kiểm tra tóm tắt

Ở cuối trang Configure, xem:

- Số chiến lược đã chọn
- Vốn ban đầu
- Phí giao dịch

✅ Khi đã sẵn sàng → **Chuyển sang trang Backtest**

---

## BƯỚC 2: BACKTEST (Chạy kiểm thử) 🚀

### Tải dữ liệu thị trường

**3 cách tải dữ liệu:**

#### Cách 1: Sample Data (Demo) - Khuyến nghị cho lần đầu

1. Chọn **"Sample Data (Demo)"**
2. Bấm nút **"🎲 Generate Sample Data"**
3. Chờ vài giây → Dữ liệu 500 ngày được tạo
4. Xem preview: Start Date, End Date, số dòng

#### Cách 2: Upload CSV

1. Chọn **"Upload CSV"**
2. Click **"Browse files"**
3. Chọn file CSV có cột: `close`, `high`, `low`, `volume`
4. Index phải là datetime

#### Cách 3: VNStock API (Đang phát triển)

- Tích hợp với API thật sẽ có trong phiên bản sau

### Chạy Backtest

1. **Xem Execution Plan** (mở rộng):

   - Chiến lược sẽ chạy
   - Số điểm dữ liệu
   - Vốn, phí, quy tắc VN
2. Bấm nút **"🚀 RUN BACKTEST"** (màu xanh, to)
3. Chờ xử lý:

   - Thanh spinner hiện "Running parallel backtests..."
   - Mất ~5-10 giây cho 4 chiến lược
4. Kết quả xuất hiện:

   - ✅ "Backtest completed!"
   - 🎈 Hiệu ứng balloons
   - 📊 Quick Results table (preview)

### Đọc Quick Results

Bảng hiện ngay sau khi chạy xong:

| Strategy | Total Return | Sharpe | Max DD | Win Rate |
| -------- | ------------ | ------ | ------ | -------- |
| ...      | %            | số    | %      | %        |

- **Màu xanh:** Hiệu suất tốt
- **Màu đỏ:** Hiệu suất kém
- **Sắp xếp:** Theo Sharpe Ratio (tốt → kém)

✅ Bấm **"👉 Go to Results"** để xem chi tiết!

---

## BƯỚC 3: RESULTS (Kết quả) 📈

### Biểu đồ Tổng hợp

**Multi-Strategy Performance (Đầu trang):**

- Biểu đồ đường (line chart) tất cả chiến lược
- Mỗi chiến lược = 1 màu
- Trục X: Thời gian
- Trục Y: Giá trị danh mục (VND)
- Hover chuột để xem giá trị chính xác

**Cách đọc:**

- Đường đi lên → Chiến lược sinh lời
- Đường đi xuống → Chiến lược thua lỗ
- Đường mượt → Ít rủi ro
- Đường gập ghềnh → Nhiều biến động

### Phân tích từng chiến lược

**Chọn chiến lược** (dropdown):

- Chọn 1 trong các chiến lược đã test

**4 chỉ số chính (Metrics Row):**

1. **Total Return** (Lợi nhuận tổng)

   - Đơn vị: %
   - Màu xanh nếu > 0
   - Ví dụ: +25.3% = Lãi 25.3%
2. **Sharpe Ratio** (Hiệu suất điều chỉnh rủi ro)

   - Không đơn vị
   - > 1.0 = Tốt ✅
     >
   - > 2.0 = Rất tốt 🌟
     >
   - < 0 = Kém ❌
3. **Max Drawdown** (Sụt giảm tối đa)

   - Đơn vị: %
   - Luôn âm
   - -10% = Giảm tối đa 10% từ đỉnh
   - Càng gần 0 càng tốt
4. **Win Rate** (Tỷ lệ thắng)

   - Đơn vị: %
   - > 50% = Tốt
     >
   - 100% = Hoàn hảo (hiếm)

**3 chỉ số phụ:**

- **Profit Factor:** Tổng lãi / Tổng lỗ (> 1.0 là sinh lời)
- **Number of Trades:** Số lệnh giao dịch
- **Final Portfolio:** Giá trị cuối cùng (VND)

### 3 Tabs chi tiết

#### Tab 1: Drawdown (Sụt giảm)

- Biểu đồ vùng màu đỏ
- Hiện các giai đoạn tài khoản giảm
- Vùng càng sâu = Rủi ro càng cao

#### Tab 2: Returns Distribution (Phân bố lợi nhuận)

- Biểu đồ cột (histogram)
- Hiện tần suất lợi nhuận hàng ngày
- Hình chuông = Ổn định
- Đuôi dài = Biến động lớn

#### Tab 3: Trade Log (Nhật ký giao dịch)

- Bảng chi tiết từng lệnh
- Cột: Date, Type (BUY/SELL), Price, Shares, Cost/Proceeds
- Dùng để kiểm tra logic chiến lược

### Best Performers (Cuối trang)

3 hộp màu xanh hiện:

- **Best Return:** Chiến lược lãi cao nhất
- **Best Risk-Adjusted:** Sharpe Ratio cao nhất
- **Lowest Drawdown:** Rủi ro thấp nhất

💡 **Lưu ý:** Chiến lược tốt cần cân bằng cả 3 yếu tố!

---

## BƯỚC 4: COMPARE (So sánh) 🏆

### Bảng Leaderboard chính

**Performance Leaderboard:**

- Tất cả chiến lược trong 1 bảng
- Sắp xếp theo Sharpe Ratio (cao → thấp)
- Màu sắc:
  - 🟩 Xanh = Tốt
  - 🟥 Đỏ = Kém
  - Áp dụng cho: Return, Sharpe, Win Rate
  - Ngược lại cho: Max Drawdown (càng âm càng đỏ)

### Rankings (Xếp hạng)

**2 cột:**

**By Total Return (Theo lợi nhuận):**

- 🥇 Hạng 1 (medal vàng)
- 🥈 Hạng 2 (medal bạc)
- 🥉 Hạng 3 (medal đồng)
- #4, #5... (các hạng còn lại)

**By Sharpe Ratio (Theo hiệu suất):**

- Cùng format
- Thường khác với ranking theo Return
- Sharpe quan trọng hơn vì tính rủi ro

### Radar Chart (Biểu đồ radar)

**Multi-Metric Comparison:**

- Mỗi chiến lược = 1 màu
- 4 trục: Return, Sharpe, Win Rate, Profit Factor
- Vùng càng rộng = Hiệu suất càng tốt
- Dùng để so sánh trực quan

### Winner Announcement (Công bố chiến lược tốt nhất)

**Hộp xanh lớn giữa trang:**

- 🏆 Tên chiến lược thắng
- 4 chỉ số chính
- Dựa trên Sharpe Ratio (không phải Return)

**Tại sao Sharpe?**
→ Vì Sharpe tính cả rủi ro, không chỉ lợi nhuận

### Export Results (Xuất kết quả)

**Download Leaderboard (CSV):**

- Bấm nút "📊 Download Leaderboard"
- File CSV tải về máy
- Tên file: `vn10_leaderboard_YYYYMMDD.csv`
- Mở bằng Excel để phân tích thêm

---

## 💡 MẸO SỬ DỤNG

### Mẹo 1: Bắt đầu với Sample Data

- Lần đầu dùng, test với dữ liệu mẫu
- Làm quen giao diện trước
- Sau đó mới dùng dữ liệu thật

### Mẹo 2: Chọn nhiều chiến lược

- Luôn test ít nhất 2-3 chiến lược
- Để so sánh và tìm tốt nhất
- Đừng chỉ dùng 1 chiến lược

### Mẹo 3: Bật VN Rules

- Luôn bật "Enforce Vietnamese Market Rules"
- Kết quả mới thực tế với thị trường VN
- Chỉ tắt khi muốn so sánh lý thuyết

### Mẹo 4: Đọc cả 3 chỉ số

- Đừng chỉ xem Total Return
- Sharpe Ratio quan trọng (tính rủi ro)
- Max Drawdown để biết rủi ro tối đa

### Mẹo 5: Kiểm tra Trade Log

- Nếu kết quả lạ, xem Tab "Trade Log"
- Đảm bảo chiến lược giao dịch đúng logic
- Số lệnh quá ít/nhiều = Có vấn đề

### Mẹo 6: So sánh công bằng

- Tất cả chiến lược dùng cùng:
  - 1 bộ dữ liệu
  - 1 mức phí
  - 1 vốn ban đầu
  - Cùng quy tắc VN
- → So sánh mới công bằng ✅

---

## ❓ FAQ (Câu hỏi thường gặp)

### Q1: Sharpe Ratio là gì?

**A:** Chỉ số đo lợi nhuận có tính rủi ro. Cao hơn = Tốt hơn.

- < 1.0: Kém
- 1.0-2.0: Tốt
- \> 2.0: Rất tốt

### Q2: Tại sao Max Drawdown quan trọng?

**A:** Cho biết mức giảm tối đa bạn sẽ gặp.

- -10% = Chịu nổi
- -30% = Áp lực tâm lý lớn
- -50%+ = Rủi ro quá cao

### Q3: Win Rate cao = Chiến lược tốt?

**A:** KHÔNG! Win rate chỉ là 1 yếu tố.

- 80% win nhưng lỗ nhiều khi thua = Vẫn lỗ
- 40% win nhưng lãi lớn khi thắng = Có thể lời

### Q4: Nên chọn chiến lược nào?

**A:** Chiến lược có Sharpe cao + Drawdown thấp.

- Không chỉ xem Return
- Cân bằng giữa lãi và rủi ro

### Q5: Dữ liệu thật từ đâu?

**A:** Hiện tại dùng:

- Sample data (demo)
- Upload CSV
- VNStock API (sắp có)

### Q6: Backtest mất bao lâu?

**A:**

- 4 chiến lược: ~5-10 giây
- 500 ngày dữ liệu
- Chạy song song nên nhanh

### Q7: Có thể tùy chỉnh chiến lược?

**A:** Có! Ở trang Configure:

- Mở expander mỗi chiến lược
- Điều chỉnh các tham số
- Ví dụ: RSI period từ 14 → 20

### Q8: Kết quả có chính xác không?

**A:** Backtest chỉ mô phỏng quá khứ.

- Không đảm bảo tương lai
- Nhưng hữu ích để lọc chiến lược kém
- Luôn test với dữ liệu mới

---

## 🎯 WORKFLOW HOÀN CHỈNH

### Lần đầu tiên (30 phút)

1. **Configure** (5 phút)

   - Chọn tất cả 4 chiến lược
   - Giữ tham số mặc định
   - Vốn 100M, phí 0.15%, VN Rules ON
2. **Backtest** (10 phút)

   - Generate Sample Data
   - Xem preview
   - Run Backtest
   - Đọc Quick Results
3. **Results** (10 phút)

   - Xem biểu đồ tổng hợp
   - Chọn từng chiến lược
   - Xem 4 metrics chính
   - Browse 3 tabs
4. **Compare** (5 phút)

   - Xem leaderboard
   - Đọc rankings
   - Tìm chiến lược tốt nhất
   - Download CSV

### Lần sau (15 phút)

1. Upload dữ liệu thật (CSV)
2. Thử điều chỉnh tham số
3. Chạy lại backtest
4. So sánh với lần trước

---

## 🚨 XỬ LÝ LỖI

### Lỗi 1: "No module named..."

**Nguyên nhân:** Thiếu thư viện
**Giải pháp:**

```bash
pip install -r requirements.txt
```

### Lỗi 2: "No strategies selected"

**Nguyên nhân:** Chưa chọn chiến lược ở Configure
**Giải pháp:** Quay lại trang Configure, tick chiến lược

### Lỗi 3: "No market data loaded"

**Nguyên nhân:** Chưa tải dữ liệu
**Giải pháp:** Bấm "Generate Sample Data" hoặc upload CSV

### Lỗi 4: Biểu đồ không hiện

**Nguyên nhân:** Plotly chưa cài
**Giải pháp:**

```bash
pip install plotly
```

### Lỗi 5: Streamlit không mở

**Nguyên nhân:** Port 8501 bị chiếm
**Giải pháp:**

```bash
streamlit run app/main.py --server.port 8502
```

---

## 📞 HỖ TRỢ

**Tài liệu:**

- `README.md` - Tổng quan dự án
- `QUICKSTART.md` - Hướng dẫn nhanh
- `implementation_plan.md` - Chi tiết kỹ thuật

---

**Chúc bạn backtesting thành công! 🇻🇳📈**

*VN10 Platform v1.0 - Built for Vietnamese Stock Market*
