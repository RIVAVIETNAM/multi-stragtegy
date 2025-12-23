# 🚀 Tạo App Mới Trên Streamlit Cloud

## 📋 Thông Tin Cần Thiết

### Repository Info
- **Repository:** `RIVAVIETNAM/multi-stragtegy`
- **Branch:** `main`
- **Main file path:** `streamlit/MAIN.py` ⚠️ QUAN TRỌNG
- **App URL:** `multi-stragtegy-vnteam` (hoặc tên bạn muốn)

---

## 🔧 Các Bước Tạo App

### Bước 1: Đăng Nhập Streamlit Cloud

1. Vào: **https://share.streamlit.io/**
2. Click **"Sign in"**
3. Chọn **"Continue with GitHub"**
4. Authorize Streamlit Cloud

### Bước 2: Tạo App Mới

1. Click **"New app"** (nút lớn ở giữa hoặc góc trên)
2. Điền form:

```
┌─────────────────────────────────────────┐
│ Repository URL                          │
│ RIVAVIETNAM/multi-stragtegy            │
│                                         │
│ Branch                                  │
│ main                                    │
│                                         │
│ Main file path                          │
│ streamlit/MAIN.py  ⚠️ QUAN TRỌNG      │
│                                         │
│ App URL (optional)                      │
│ multi-stragtegy-vnteam                  │
└─────────────────────────────────────────┘
```

3. Click **"Deploy!"**

### Bước 3: Đợi Deployment

- Streamlit Cloud sẽ:
  1. Clone repository
  2. Install dependencies từ `requirements.txt`
  3. Start app
  4. Cung cấp public URL

**Thời gian:** 2-5 phút

### Bước 4: Kiểm Tra

Sau khi deploy xong, bạn sẽ có:
- **Public URL:** `https://multi-stragtegy-vnteam.streamlit.app/`
- **Dashboard:** Quản lý app tại https://share.streamlit.io/

---

## ⚠️ Lưu Ý Quan Trọng

### Main File Path

**✅ ĐÚNG:**
```
streamlit/MAIN.py
```

**❌ SAI:**
```
app/MAIN.py
MAIN.py
streamlit/app/MAIN.py
```

### Repository Format

**✅ ĐÚNG:**
```
RIVAVIETNAM/multi-stragtegy
```

**❌ SAI:**
```
https://github.com/RIVAVIETNAM/multi-stragtegy.git
RIVAVIETNAM/multi-stragtegy.git
```

---

## 🔍 Troubleshooting

### Nếu Không Thấy Repository

1. **Kiểm tra GitHub:**
   - Repository có public không?
   - Bạn có quyền truy cập không?
   - Repository name đúng chưa?

2. **Refresh:**
   - Logout và login lại Streamlit Cloud
   - Refresh browser

### Nếu Deploy Fail

1. **Check Logs:**
   - Vào app settings
   - Xem "Logs" tab
   - Tìm error message

2. **Common Errors:**

   **"Main file not found":**
   - Kiểm tra Main file path = `streamlit/MAIN.py`
   - File có tồn tại trong repo không?

   **"Dependencies error":**
   - Kiểm tra `requirements.txt` có đúng format không
   - Tất cả packages có available không?

   **"Import error":**
   - Kiểm tra imports trong code
   - Đảm bảo tất cả dependencies đã install

---

## 📸 Screenshot Guide

### Form Tạo App:

```
┌─────────────────────────────────────────────┐
│  Deploy a new app                            │
├─────────────────────────────────────────────┤
│                                             │
│  Repository URL *                           │
│  ┌─────────────────────────────────────┐   │
│  │ RIVAVIETNAM/multi-stragtegy        │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  Branch *                                   │
│  ┌─────────────────────────────────────┐   │
│  │ main                                │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  Main file path *                           │
│  ┌─────────────────────────────────────┐   │
│  │ streamlit/MAIN.py                    │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  App URL (optional)                         │
│  ┌─────────────────────────────────────┐   │
│  │ multi-stragtegy-vnteam              │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  [Cancel]  [Deploy!]                        │
└─────────────────────────────────────────────┘
```

---

## ✅ Checklist

Trước khi deploy, đảm bảo:

- [ ] Repository là public hoặc bạn có quyền truy cập
- [ ] Branch `main` tồn tại và có code
- [ ] File `streamlit/MAIN.py` tồn tại trong repo
- [ ] File `requirements.txt` có trong root
- [ ] Đã test local: `streamlit run streamlit/MAIN.py` chạy được

---

## 🎯 Sau Khi Deploy Thành Công

1. **Share URL:** https://multi-stragtegy-vnteam.streamlit.app/
2. **Monitor:** Xem logs và usage trên dashboard
3. **Update:** Mỗi khi push code, app tự động redeploy

---

**Chúc bạn deploy thành công! 🚀**

