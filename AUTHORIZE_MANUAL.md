# 🔐 Authorize Streamlit Cloud Thủ Công (Không Có Popup)

## ❓ Vấn Đề

Khi deploy trên Streamlit Cloud, **KHÔNG thấy popup authorize** từ GitHub.

## 🔍 Nguyên Nhân

- Organization có **OAuth App access restrictions**
- Cần **Organization Owner/Admin approve** trước
- Không thể authorize tự động qua popup

---

## ✅ Giải Pháp: Authorize Thủ Công

### Bước 1: Vào Organization Settings

**Nếu bạn là Organization Owner/Admin:**

1. **Vào GitHub Organization:**
   - https://github.com/organizations/RIVAVIETNAM
   - Hoặc: GitHub → Organizations → `RIVAVIETNAM`

2. **Vào Settings:**
   - Click **"Settings"** tab (trên cùng)
   - Hoặc: https://github.com/organizations/RIVAVIETNAM/settings

3. **Vào Third-party Access:**
   - Trong sidebar bên trái, tìm **"Third-party access"**
   - Hoặc: https://github.com/organizations/RIVAVIETNAM/settings/applications

### Bước 2: Tìm Streamlit Cloud

**Có 2 nơi có thể tìm:**

#### Option A: Third-party Application Access Policy

1. Scroll xuống phần **"Third-party application access policy"**
2. Tìm **"Streamlit Cloud"** hoặc **"Streamlit"** trong list
3. Nếu thấy:
   - Click **"Configure"** hoặc **"Review request"**
   - Chọn repositories (hoặc **"All repositories"**)
   - Click **"Approve"** hoặc **"Grant"**

#### Option B: Authorized OAuth Apps

1. Tìm tab **"Authorized OAuth Apps"**
2. Tìm **"Streamlit Cloud"** trong list
3. Nếu chưa có, sẽ được tạo khi có request

### Bước 3: Approve Streamlit Cloud

**Nếu có request pending:**

1. Click **"Review request"** hoặc **"Configure"**
2. Xem thông tin request:
   - App: Streamlit Cloud
   - Requested access: Organization repositories
3. **Chọn repositories:**
   - ✅ **"All repositories"** (khuyến nghị)
   - Hoặc chọn repositories cụ thể
4. Click **"Approve"** hoặc **"Grant access"**

**Nếu chưa có request:**

1. **Tạo app mới trên Streamlit Cloud:**
   - Repository: `RIVAVIETNAM/multi-stragtegy`
   - Deploy sẽ fail với lỗi authorization
2. **Quay lại Organization Settings:**
   - Request sẽ xuất hiện trong "Third-party application access policy"
   - Approve request đó

### Bước 4: Set Access Policy (Nếu Cần)

**Nếu muốn dễ dàng hơn cho lần sau:**

1. Trong **"Third-party application access policy"**
2. Chọn **"No restrictions"** (cho phép tất cả apps)
3. Hoặc **"Restrict access"** và approve Streamlit Cloud cụ thể

---

## 🔄 Sau Khi Authorize

### Retry Deployment:

1. **Quay lại Streamlit Cloud:** https://share.streamlit.io/
2. **Tạo app mới** (hoặc retry app cũ)
3. **Repository:** `RIVAVIETNAM/multi-stragtegy`
4. **Main file path:** `streamlit/MAIN.py`
5. **Click "Deploy!"**
6. **Lần này sẽ thành công!**

### Kết Quả:

- ✅ Organization `RIVAVIETNAM` sẽ hiện trong Streamlit Cloud
- ✅ Repositories sẽ hiện trong dropdown
- ✅ Có thể deploy app thành công

---

## 📋 Checklist

### Nếu Bạn Là Organization Owner/Admin:

- [ ] Vào Organization Settings
- [ ] Tìm "Third-party application access policy"
- [ ] Tìm "Streamlit Cloud" request
- [ ] Approve và chọn repositories
- [ ] Retry deployment trên Streamlit Cloud
- [ ] Organization sẽ hiện trong dashboard

### Nếu Bạn Không Phải Owner:

- [ ] Liên hệ Organization Owner/Admin
- [ ] Yêu cầu họ approve Streamlit Cloud
- [ ] Gửi link: https://github.com/organizations/RIVAVIETNAM/settings/applications
- [ ] Đợi approve
- [ ] Retry deployment

---

## 🔗 Links Quan Trọng

- **Organization Settings:** https://github.com/organizations/RIVAVIETNAM/settings/applications
- **Third-party Access:** https://github.com/organizations/RIVAVIETNAM/settings/applications
- **Streamlit Cloud:** https://share.streamlit.io/

---

## 💡 Lưu Ý

### OAuth App Access Restrictions

- **Nếu organization có restrictions:**
  - Popup authorize sẽ KHÔNG hiện
  - Phải approve từ Organization Settings
  - Chỉ Owner/Admin mới có quyền approve

### Sau Khi Approve

- **Streamlit Cloud sẽ có quyền truy cập organization**
- **Organization sẽ hiện trong Streamlit Cloud dashboard**
- **Repositories sẽ hiện trong dropdown**
- **Có thể deploy app thành công**

---

## 🎯 Tóm Tắt

**Vì không có popup, cần authorize thủ công:**

1. **Vào Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications

2. **Tìm "Third-party application access policy"**

3. **Approve "Streamlit Cloud"** (nếu có request)

4. **Hoặc set "No restrictions"** (cho phép tất cả)

5. **Retry deployment trên Streamlit Cloud**

**Sau khi approve, deployment sẽ thành công!** 🚀

