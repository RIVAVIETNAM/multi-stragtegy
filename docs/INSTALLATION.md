# 📦 Installation Guide

Hướng dẫn cài đặt Multi-Strategy Backtesting Platform.

> 🌐 **Không muốn cài đặt?** Sử dụng trực tiếp tại: [https://multi-stragtegy-vnteam.streamlit.app/](https://multi-stragtegy-vnteam.streamlit.app/)

---

## 🚀 Quick Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd "6 new project"
```

### 2. Install Core Dependencies

```bash
pip install -r requirements.txt
```

**Hoặc cài từng package:**

```bash
pip install pandas numpy scipy vnstock requests ta scikit-learn optuna streamlit plotly matplotlib sqlalchemy python-dotenv
```

### 3. Verify Installation

```bash
python -c "import streamlit; import pandas; import plotly; print('✅ All core packages installed!')"
```

---

## ⚙️ Optional Dependencies

### AI Strategy Generator

**Chỉ cài nếu muốn dùng tính năng AI Strategy Generator:**

1. **Mở file `requirements.txt`**
2. **Uncomment dòng:** `# google-generativeai>=0.3.0`
3. **Cài đặt:**
   ```bash
   pip install google-generativeai
   ```

**Hoặc cài trực tiếp:**

```bash
pip install google-generativeai
```

**Yêu cầu thêm:**
- Google Gemini API key (xem [Features Guide](features/FEATURES_GUIDE.md))

**Lưu ý:** App vẫn chạy bình thường nếu không cài package này!

---

## 🔧 Environment Setup

### Python Version

- **Minimum:** Python 3.8
- **Recommended:** Python 3.10+

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables (Optional)

Tạo file `.env` trong root directory:

```bash
# .env file
GEMINI_API_KEY=your_api_key_here
```

---

## ✅ Installation Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created (optional)
- [ ] Core dependencies installed (`requirements.txt`)
- [ ] Optional dependencies installed (if needed)
- [ ] Environment variables set (if using AI Generator)
- [ ] Installation verified

---

## 🐛 Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError`

**Solution:**
```bash
# Reinstall all packages
pip install --upgrade -r requirements.txt
```

### Streamlit Not Found

**Problem:** `streamlit: command not found`

**Solution:**
```bash
# Install streamlit
pip install streamlit

# Or reinstall all
pip install -r requirements.txt
```

### VNStock Issues

**Problem:** Cannot import vnstock

**Solution:**
```bash
# Update vnstock
pip install --upgrade vnstock
```

### Version Conflicts

**Problem:** Package version conflicts

**Solution:**
```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 📚 Next Steps

Sau khi cài đặt xong:

1. **Chạy ứng dụng:**
   ```bash
   streamlit run streamlit/MAIN.py
   ```

2. **Xem hướng dẫn:**
   - [Streamlit Guide](guides/STREAMLIT_GUIDE.md)
   - [Features Guide](features/FEATURES_GUIDE.md)

3. **Bắt đầu sử dụng:**
   - Truy cập: http://localhost:8501
   - Xem [Quick Start](../README.md#-quick-start)

---

## 📝 Requirements File

- **`requirements.txt`** - Tất cả dependencies (core + optional)
  - Core dependencies: Bắt buộc
  - Optional dependencies: Được comment, uncomment nếu cần

---

**Cần hỗ trợ?** Xem [README.md](../README.md) hoặc tạo issue trên GitHub.

