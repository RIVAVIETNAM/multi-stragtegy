# 🔧 Fix Streamlit Cloud Path Error

## ❌ Lỗi Hiện Tại

```
❗️ Error: failed to update the application source because the directory '/mount/src/multi-stragtegy/app' does not exist
```

## 🔍 Nguyên Nhân

Streamlit Cloud đang tìm file ở **`app/MAIN.py`** nhưng file đã được di chuyển sang **`streamlit/MAIN.py`**

## ✅ Giải Pháp

### Cách 1: Cập Nhật Trên Streamlit Cloud Dashboard (Khuyến nghị)

1. **Đăng nhập Streamlit Cloud:**
   - Vào: https://share.streamlit.io/
   - Đăng nhập với GitHub account

2. **Vào App Settings:**
   - Click vào app: `multi-stragtegy-vnteam`
   - Click **"Settings"** (⚙️ icon)

3. **Cập Nhật Main File Path:**
   - Tìm field **"Main file path"**
   - **Thay đổi từ:** `app/MAIN.py`
   - **Thành:** `streamlit/MAIN.py`
   - Click **"Save"**

4. **Redeploy:**
   - App sẽ tự động redeploy
   - Hoặc click **"Reboot app"** nếu cần

### Cách 2: Tạo App Mới (Nếu không tìm thấy settings)

1. **Delete app cũ** (nếu cần)
2. **Tạo app mới:**
   - Repository: `RIVAVIETNAM/multi-stragtegy`
   - Branch: `main`
   - **Main file path:** `streamlit/MAIN.py` ⚠️ QUAN TRỌNG
   - App URL: `multi-stragtegy-vnteam` (hoặc tên khác)

## 📋 Checklist

- [ ] Main file path = `streamlit/MAIN.py` (KHÔNG phải `app/MAIN.py`)
- [ ] Branch = `main`
- [ ] Repository = `RIVAVIETNAM/multi-stragtegy`
- [ ] Đã click "Save"
- [ ] Đợi redeploy (2-5 phút)

## 🔍 Verify

Sau khi redeploy, kiểm tra:
- ✅ App load được không
- ✅ Không còn error về missing directory
- ✅ URL: https://multi-stragtegy-vnteam.streamlit.app/ hoạt động

## 📸 Screenshot Hướng Dẫn

**Trong Streamlit Cloud Settings, bạn sẽ thấy:**

```
Main file path: [streamlit/MAIN.py]  ← Phải là path này
```

**KHÔNG phải:**
```
Main file path: [app/MAIN.py]  ← SAI
```

---

**Sau khi fix, app sẽ tự động redeploy và hoạt động bình thường!** 🚀

