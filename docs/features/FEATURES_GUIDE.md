# 🚀 Hướng Dẫn Sử Dụng Các Tính Năng Mới

## 📋 Tóm Tắt

Dự án đã được nâng cấp với các tính năng lấy cảm hứng từ FC-Terminal:

1. ✅ **Custom UI/UX** - Giao diện hiện đại với CSS tùy chỉnh
2. ✅ **AI Strategy Generator** - Tạo chiến lược từ mô tả ngôn ngữ tự nhiên (Optional)
3. ✅ **Enhanced Visualizations** - Charts đẹp hơn với Plotly
4. ✅ **Strategy Performance Matrix** - RRG-style visualization

**Tất cả tính năng đã sẵn sàng sử dụng!** 🎉

---

## 1. 🎨 Custom UI/UX

### Cách Sử Dụng

Custom CSS đã được tự động load khi chạy ứng dụng. Không cần cấu hình thêm!

**Tính năng:**
- Gradient headers và buttons
- Modern card designs
- Smooth animations
- Professional color scheme
- Responsive design

**File liên quan:**
- `app/assets/custom.css` - CSS styles
- `app/utils/ui_helpers.py` - Helper functions

---

## 2. 🤖 AI Strategy Generator

### ⚠️ TÍNH NĂNG TÙY CHỌN (OPTIONAL)

**Lưu ý quan trọng:** Tính năng này là **KHÔNG BẮT BUỘC**. 
- ✅ App vẫn chạy bình thường nếu không cài `google-generativeai`
- ✅ Tất cả tính năng khác hoạt động đầy đủ
- ✅ Chỉ cần cài nếu muốn dùng AI Generator

### Yêu Cầu (Chỉ nếu muốn dùng AI Generator)

1. **Cài package:**
   ```bash
   pip install google-generativeai
   ```
   
   **Hoặc uncomment trong requirements.txt:**
   - Mở `requirements.txt`
   - Tìm dòng `# google-generativeai>=0.3.0`
   - Uncomment (xóa dấu `#`)
   - Chạy: `pip install -r requirements.txt`

2. **Google Gemini API Key**
   - Đăng ký tại: https://makersuite.google.com/app/apikey
   - Lưu API key vào:
     - Environment variable: `GEMINI_API_KEY`
     - Hoặc nhập trực tiếp trong trang AI Strategy Generator

### Cách Sử Dụng

1. **Truy cập trang:** Sidebar → **AI Strategy Generator**

2. **Cấu hình API Key:**
   - Chọn "Environment Variable" nếu đã set
   - Hoặc chọn "Enter Manually" và nhập key

3. **Mô tả chiến lược:**
   ```
   Ví dụ: "Buy when RSI is below 30 and sell when RSI is above 70. Use period 14 for RSI calculation."
   ```

4. **Generate:**
   - Click "🚀 Generate Strategy"
   - AI sẽ tạo code Python hoàn chỉnh

5. **Sử dụng chiến lược:**
   - Download code
   - Lưu vào `strategies/custom/` folder
   - Import và sử dụng trong trang Configure

### Ví Dụ Mô Tả Chiến Lược

**Tốt:**
- ✅ "Buy when MACD line crosses above signal line. Use fast period 12, slow period 26, signal period 9."
- ✅ "Buy at lower Bollinger Band (2 standard deviations) and sell at upper band. Use window 20."
- ✅ "Buy when price crosses above 10-day SMA and sell when price crosses below 30-day SMA." *Note: Default SMA windows are 10/30 (changed from 50/200 for better sample data compatibility)*

**Không tốt:**
- ❌ "Make money" (quá mơ hồ)
- ❌ "Buy low sell high" (không cụ thể)

### Tips

- **Be Specific:** Nêu rõ indicator, period, threshold
- **Use Standard Indicators:** RSI, MACD, Bollinger Bands, SMA, EMA
- **Describe Entry/Exit:** Rõ ràng khi nào buy/sell

**Xem thêm:** [Why Google Generative AI?](../features/WHY_GOOGLE_GENERATIVEAI.md)

---

## 3. 📊 Enhanced Visualizations

### Cải Tiến

**Equity Curves:**
- Gradient colors
- Better hover tooltips
- Professional styling
- Improved legends

**Drawdown Charts:**
- Gradient fills
- Max drawdown annotations
- Enhanced readability

**File:** `analytics/visualize.py`

### Sử Dụng

Tự động áp dụng khi xem charts trong:
- **Results** page
- **Compare** page

---

## 4. 🎯 Strategy Performance Matrix

### Mô Tả

Relative Rotation Graph (RRG) style visualization cho strategies, tương tự FC-Terminal's Sector Matrix.

### 4 Quadrants

1. **🟢 Leading** (Góc trên phải)
   - High Relative Strength
   - Positive Momentum
   - **Best performers**

2. **🟠 Weakening** (Góc trên trái)
   - High Relative Strength
   - Negative Momentum
   - **Losing strength**

3. **🔴 Lagging** (Góc dưới trái)
   - Low Relative Strength
   - Negative Momentum
   - **Underperformers**

4. **🔵 Improving** (Góc dưới phải)
   - Low Relative Strength
   - Positive Momentum
   - **Recovering**

### Cách Xem

1. Chạy backtest với nhiều strategies
2. Vào trang **Compare**
3. Tab **"🎯 Performance Matrix (RRG)"**
4. Xem strategies được phân loại vào quadrants

### Ý Nghĩa

- **Leading:** Strategies đang perform tốt nhất
- **Weakening:** Strategies đang mất momentum
- **Lagging:** Strategies cần cải thiện
- **Improving:** Strategies đang phục hồi

**File:** `analytics/strategy_matrix.py`

---

## 📦 Cài Đặt Dependencies

### Dependencies Bắt Buộc

```bash
pip install -r requirements.txt
```

**Lưu ý:** `google-generativeai` đã được **loại bỏ** khỏi requirements.txt vì là optional.

### Dependencies Tùy Chọn (Chỉ nếu cần)

**AI Strategy Generator:**
```bash
pip install google-generativeai
```

Hoặc:
```bash
pip install -r requirements-optional.txt
```

---

## 🚀 Chạy Ứng Dụng

```bash
cd "6 new project"
streamlit run streamlit/MAIN.py
```

Truy cập: http://localhost:8501

---

## 📝 Cấu Trúc Files Mới

```
6 new project/
├── app/
│   ├── assets/
│   │   └── custom.css          # Custom CSS styles
│   ├── utils/
│   │   └── ui_helpers.py       # UI helper functions
│   └── pages/
│       └── 5_AI_STRATEGY_GENERATOR.py  # AI Generator page
├── analytics/
│   └── strategy_matrix.py      # RRG-style matrix
├── strategies/
│   └── ai_generator.py         # AI strategy generator
└── requirements-optional.txt  # Optional dependencies
```

---

## 🐛 Troubleshooting

### AI Generator không hoạt động

1. **Kiểm tra API Key:**
   ```python
   import os
   print(os.getenv("GEMINI_API_KEY"))  # Should print your key
   ```

2. **Kiểm tra Internet:** Cần kết nối để gọi Gemini API

3. **Kiểm tra Quota:** API có thể có giới hạn requests

### CSS không load

1. Kiểm tra file `app/assets/custom.css` tồn tại
2. Kiểm tra `app/utils/ui_helpers.py` được import đúng
3. Restart Streamlit app

### Strategy Matrix không hiển thị

1. Cần ít nhất 2 strategies để so sánh
2. Kiểm tra backtest results có trong session state
3. Xem console logs để debug

---

## 💡 Best Practices

1. **AI Strategy Generator:**
   - Test generated code trước khi dùng
   - Review logic cẩn thận
   - Adjust parameters nếu cần

2. **Performance Matrix:**
   - So sánh ít nhất 3-4 strategies
   - Xem cả matrix và radar chart
   - Focus vào Leading quadrant

3. **Visualizations:**
   - Export charts nếu cần
   - Zoom in để xem chi tiết
   - Compare multiple timeframes

---

## 📚 Tài Liệu Tham Khảo

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Streamlit Custom Components](https://docs.streamlit.io/library/components)
- [FC-Terminal Compatibility Analysis](../analysis/FC_TERMINAL_COMPATIBILITY.md)

---

## ✅ Checklist Sử Dụng

- [ ] Cài đặt `google-generativeai` (nếu cần AI Generator)
- [ ] Lấy Gemini API key (nếu cần AI Generator)
- [ ] Test AI Strategy Generator
- [ ] Xem Strategy Performance Matrix
- [ ] Review enhanced visualizations
- [ ] Tùy chỉnh CSS nếu cần

---

**Chúc bạn sử dụng thành công! 🎉**

