# 🚀 DEPLOY LÊN STREAMLIT CLOUD

Hướng dẫn deploy Multi-Strategy Backtesting Platform lên Streamlit Cloud để truy cập từ bất kỳ đâu.

---

## ✅ YÊU CẦU TRƯỚC KHI DEPLOY

- [x] Code đã push lên GitHub: https://github.com/RIVAVIETNAM/multi-stragtegy
- [x] File `requirements.txt` đã có
- [x] File `app/MAIN.py` là entry point
- [x] Tất cả dependencies đã list trong requirements.txt

---

## 📝 BƯỚC 1: CHUẨN BỊ REPOSITORY

### 1.1 Kiểm tra file requirements.txt

Đảm bảo file có đầy đủ dependencies:

```txt
# Core Data Science
pandas>=2.2.0
numpy>=1.26.0
scipy>=1.14.0

# Vietnamese Market Data
vnstock>=3.0.0
requests>=2.32.0

# Technical Analysis
ta>=0.11.0
scikit-learn>=1.5.0

# Optimization
optuna>=4.0.0

# Web Interface
streamlit>=1.40.0

# Visualization
plotly>=5.24.0
matplotlib>=3.9.0

# Database
sqlalchemy>=2.0.0

# Utils
python-dotenv>=1.0.0
```

### 1.2 Tạo file .streamlit/config.toml (Optional)

Tạo folder `.streamlit` và file `config.toml`:

```bash
mkdir .streamlit
```

**File: `.streamlit/config.toml`**
```toml
[theme]
primaryColor = "#3498db"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

### 1.3 Push lên GitHub (nếu chưa)

```bash
git add .streamlit/config.toml
git commit -m "Add Streamlit config for deployment"
git push
```

---

## 🌐 BƯỚC 2: DEPLOY LÊN STREAMLIT CLOUD

### 2.1 Đăng ký/Đăng nhập Streamlit Cloud

1. Vào: https://streamlit.io/cloud
2. Click **"Sign up"** hoặc **"Sign in"**
3. Chọn **"Continue with GitHub"**
4. Authorize Streamlit để truy cập GitHub

### 2.2 Tạo App mới

**Cách 1: Qua Dashboard**

1. Sau khi đăng nhập, click **"New app"**
2. Điền thông tin:

```
Repository: RIVAVIETNAM/multi-stragtegy
Branch: main
Main file path: app/MAIN.py
App URL (optional): multi-strategy-backtest (hoặc tên khác)
```

3. Click **"Deploy!"**

**Cách 2: Qua URL trực tiếp**

Vào link này và điền form:
```
https://share.streamlit.io/deploy
```

### 2.3 Cấu hình Advanced Settings (Optional)

Click **"Advanced settings"** để cấu hình:

**Python version:**
```
3.11
```

**Secrets:** (Nếu cần API keys)
```toml
# Chưa cần thiết cho dự án này
```

---

## ⏳ BƯỚC 3: ĐỢI DEPLOYMENT

### 3.1 Quá trình deploy

Streamlit Cloud sẽ:
1. ✅ Clone repository từ GitHub
2. ✅ Cài đặt dependencies từ `requirements.txt`
3. ✅ Khởi động app
4. ✅ Cung cấp public URL

**Thời gian:** 2-5 phút

### 3.2 Theo dõi logs

Trong quá trình deploy, xem logs để debug:

```
Building... 🔨
Installing dependencies...
✓ pandas>=2.2.0
✓ streamlit>=1.40.0
✓ vnstock>=3.0.0
...
Starting server... 🚀
Your app is live at: https://multi-strategy-backtest.streamlit.app
```

---

## 🎉 BƯỚC 4: TRUY CẬP APP

### 4.1 URL công khai

App sẽ có URL dạng:
```
https://multi-strategy-backtest.streamlit.app
```

Hoặc:
```
https://RIVAVIETNAM-multi-stragtegy-app-MAIN-[hash].streamlit.app
```

### 4.2 Chia sẻ

Giờ bạn có thể chia sẻ URL này với:
- Đồng nghiệp
- Khách hàng
- Bất kỳ ai có internet

---

## 🔧 BƯỚC 5: CẬP NHẬT APP

### Khi cần update code:

1. **Sửa code local:**
```bash
# Edit files...
git add .
git commit -m "Update feature X"
git push
```

2. **Streamlit tự động deploy lại:**
   - Streamlit Cloud tự động detect push
   - Rebuild và deploy trong 2-3 phút
   - URL giữ nguyên

### Hoặc deploy thủ công:

1. Vào Streamlit Cloud Dashboard
2. Chọn app
3. Click **"Reboot app"** hoặc **"Rerun"**

---

## ⚠️ LƯU Ý QUAN TRỌNG

### 1. Giới hạn Streamlit Cloud (Free tier)

```
✅ Unlimited public apps
✅ 1 GB RAM per app
✅ 1 CPU core per app
✅ Community support
❌ No custom domain (paid)
❌ Password protection (paid)
```

### 2. Performance

**Dự án này cần:**
- RAM: ~500MB (OK với 1GB limit)
- CPU: Vừa phải (OK với 1 core)

**Lưu ý:**
- Sample data generation: OK
- Lớn hơn 1000 ngày data: Có thể chậm
- Nhiều strategies (>4): Memory cao hơn

### 3. Data Persistence

⚠️ **Streamlit Cloud KHÔNG lưu dữ liệu giữa sessions**

**Giải pháp:**
- Sample data: Generate mỗi lần (OK)
- Upload CSV: User tự upload
- VNStock API: Fetch real-time (Coming soon)

---

## 🐛 XỬ LÝ LỖI DEPLOYMENT

### Lỗi 1: "ModuleNotFoundError"

**Nguyên nhân:** Thiếu package trong `requirements.txt`

**Giải pháp:**
```bash
# Thêm vào requirements.txt
echo "package_name>=version" >> requirements.txt
git add requirements.txt
git commit -m "Add missing package"
git push
```

### Lỗi 2: "App is taking too long to load"

**Nguyên nhân:** Dependencies lớn hoặc nhiều

**Giải pháp:**
- Xóa packages không dùng
- Pin versions cụ thể thay vì `>=`
- Dùng lightweight alternatives

### Lỗi 3: "Maximum execution time exceeded"

**Nguyên nhân:** Code chạy quá lâu

**Giải pháp:**
- Giảm sample data size
- Optimize backtest engine
- Add caching với `@st.cache_data`

### Lỗi 4: "GitHub repository not found"

**Nguyên nhân:** Streamlit không có quyền truy cập

**Giải pháp:**
1. Vào GitHub Settings → Applications
2. Authorize Streamlit Cloud
3. Grant access to organization RIVAVIETNAM

### Lỗi 5: "App crashed"

**Nguyên nhân:** Runtime error

**Giải pháp:**
1. Xem logs trong Streamlit Cloud
2. Test local trước: `streamlit run app/MAIN.py`
3. Fix bugs và push lại

---

## 📊 MONITORING

### Xem app usage:

1. Vào Streamlit Cloud Dashboard
2. Click vào app
3. Xem **Analytics:**
   - Number of viewers
   - CPU usage
   - Memory usage
   - Errors

### Logs:

Click **"Manage app"** → **"Logs"** để xem real-time logs

---

## 🔒 BẢO MẬT (Optional)

### Nếu muốn private app:

**Free tier:** App luôn public

**Paid tier ($20/month):**
- Password protection
- Custom domain
- More resources

**Workaround cho free:**
- Dùng obscure URL (không share rộng rãi)
- Add simple password check trong code:

```python
import streamlit as st

password = st.text_input("Enter password:", type="password")
if password != "your_secret_password":
    st.error("Incorrect password")
    st.stop()

# Rest of your app...
```

---

## 🎯 CHECKLIST DEPLOY

- [ ] Code đã push lên GitHub
- [ ] `requirements.txt` đầy đủ
- [ ] Test local thành công
- [ ] Đăng ký Streamlit Cloud
- [ ] Authorize GitHub
- [ ] Tạo new app
- [ ] Chọn repo: RIVAVIETNAM/multi-stragtegy
- [ ] Branch: main
- [ ] Main file: app/MAIN.py
- [ ] Click Deploy
- [ ] Đợi 2-5 phút
- [ ] Test app trên URL public
- [ ] Chia sẻ URL

---

## 🔗 LINKS QUAN TRỌNG

- **Streamlit Cloud:** https://streamlit.io/cloud
- **Documentation:** https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Repo:** https://github.com/RIVAVIETNAM/multi-stragtegy
- **App URL:** (Sẽ có sau khi deploy)

---

## 💡 TIPS

### Tip 1: Test local trước
Luôn chạy `streamlit run app/MAIN.py` local trước khi deploy

### Tip 2: Pin versions
Thay `package>=1.0.0` bằng `package==1.2.3` để tránh breaking changes

### Tip 3: Use caching
Add `@st.cache_data` cho functions tốn thời gian

### Tip 4: Lightweight dependencies
Tránh install packages nặng không cần thiết

### Tip 5: Monitor usage
Check Analytics thường xuyên để biết ai đang dùng

---

## 📞 HỖ TRỢ

**Streamlit Community:**
- Forum: https://discuss.streamlit.io/
- Discord: https://discord.gg/streamlit

**GitHub Issues:**
- https://github.com/RIVAVIETNAM/multi-stragtegy/issues

---

**Chúc bạn deploy thành công! 🚀📈**

*Deploy một lần, truy cập mọi nơi!*
