# 🔄 Cập Nhật App Hiện Có (Giữ Nguyên URL)

## 🎯 Mục Tiêu

Bạn muốn **giữ nguyên URL cũ** `https://multi-stragtegy-vnteam.streamlit.app/` thay vì tạo app mới.

## ✅ Giải Pháp

### Cách 1: Update App Hiện Có (Nếu App Đã Tồn Tại)

1. **Vào Streamlit Cloud Dashboard:**
   - https://share.streamlit.io/
   - Đăng nhập

2. **Tìm App Cũ:**
   - Tìm app có URL: `multi-stragtegy-vnteam`
   - Click vào app đó

3. **Vào Settings:**
   - Click **"Settings"** (⚙️ icon)
   - Hoặc click **"Manage app"** → **"Settings"**

4. **Cập Nhật Main File Path:**
   - Tìm field **"Main file path"**
   - **Thay đổi từ:** `app/MAIN.py` (hoặc path cũ)
   - **Thành:** `streamlit/MAIN.py`
   - Click **"Save"**

5. **Redeploy:**
   - App sẽ tự động redeploy
   - Hoặc click **"Reboot app"** nếu cần
   - URL vẫn giữ nguyên: `https://multi-stragtegy-vnteam.streamlit.app/`

### Cách 2: Xóa App Cũ Và Tạo Lại Với Cùng URL

**Nếu app cũ không hoạt động hoặc không tìm thấy:**

1. **Xóa App Cũ (Nếu Có):**
   - Vào Streamlit Cloud Dashboard
   - Tìm app cũ
   - Click **"Settings"** → **"Delete app"**
   - Xác nhận xóa

2. **Tạo App Mới Với Cùng URL:**
   - Click **"New app"**
   - Điền form:
     ```
     Repository URL: RIVAVIETNAM/multi-stragtegy
     Branch: main
     Main file path: streamlit/MAIN.py
     App URL: multi-stragtegy-vnteam  ← CÙNG URL CŨ
     ```
   - Click **"Deploy!"**

3. **Kết Quả:**
   - App mới với URL cũ: `https://multi-stragtegy-vnteam.streamlit.app/`
   - Code mới từ repository
   - Không có nhiều phiên bản

---

## 🔍 Tìm App Hiện Có

### Nếu Không Thấy App Trong Dashboard:

1. **Kiểm tra Account:**
   - Đảm bảo đăng nhập đúng GitHub account
   - Account có quyền truy cập organization `RIVAVIETNAM`

2. **Kiểm tra URL Trực Tiếp:**
   - Thử truy cập: https://multi-stragtegy-vnteam.streamlit.app/
   - Nếu app tồn tại, sẽ hiện app
   - Nếu không, sẽ báo "App not found"

3. **Kiểm tra Organization:**
   - App có thể thuộc organization account
   - Thử đăng nhập với organization account

---

## 📋 Checklist

### Nếu App Đã Tồn Tại:

- [ ] Tìm app trong Streamlit Cloud Dashboard
- [ ] Vào Settings của app
- [ ] Cập nhật Main file path: `streamlit/MAIN.py`
- [ ] Save và đợi redeploy
- [ ] Kiểm tra URL cũ vẫn hoạt động

### Nếu App Không Tồn Tại:

- [ ] Xóa app cũ (nếu có)
- [ ] Tạo app mới với cùng App URL
- [ ] Repository: `RIVAVIETNAM/multi-stragtegy`
- [ ] Main file path: `streamlit/MAIN.py`
- [ ] App URL: `multi-stragtegy-vnteam` (giữ nguyên)

---

## ⚠️ Lưu Ý

### App URL (Subdomain)

- **App URL** là subdomain của Streamlit Cloud
- Format: `your-app-name.streamlit.app`
- **Mỗi URL chỉ dùng được cho 1 app**
- Nếu app cũ đã dùng `multi-stragtegy-vnteam`, bạn có thể:
  - Update app cũ (giữ URL)
  - Hoặc xóa app cũ rồi tạo mới với cùng URL

### Không Tạo Nhiều Phiên Bản

- **KHÔNG** tạo app mới với URL khác
- **CHỈ** update app hiện có hoặc tạo lại với cùng URL
- Điều này giữ nguyên link và không tạo nhiều phiên bản

---

## 🎯 Tóm Tắt

**Cách tốt nhất:**
1. Tìm app cũ trong dashboard
2. Update Main file path: `streamlit/MAIN.py`
3. Giữ nguyên URL: `multi-stragtegy-vnteam`

**Nếu không tìm thấy:**
1. Xóa app cũ (nếu có)
2. Tạo app mới với cùng App URL
3. Đảm bảo Main file path: `streamlit/MAIN.py`

---

**Làm theo cách này sẽ giữ nguyên URL và không tạo nhiều phiên bản!** 🚀

