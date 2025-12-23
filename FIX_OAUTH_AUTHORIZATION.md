# 🔐 Fix OAuth Authorization Error

## ❌ Lỗi

```
You are not authorized to perform the requested action: Although you appear to have the correct authorization credentials, the `RIVAVIETNAM` organization has enabled OAuth App access restrictions
```

## 🔍 Nguyên Nhân

Organization `RIVAVIETNAM` đã bật **OAuth App access restrictions**, nghĩa là cần phải authorize Streamlit Cloud app để truy cập vào organization repositories.

## ✅ Giải Pháp

### Cách 1: Authorize Streamlit Cloud App (Khuyến nghị)

**Nếu bạn là Organization Owner/Admin:**

1. **Vào GitHub Organization Settings:**
   - Vào: https://github.com/organizations/RIVAVIETNAM/settings/applications
   - Hoặc: GitHub → Organization `RIVAVIETNAM` → Settings → Third-party access

2. **Tìm Streamlit Cloud App:**
   - Scroll xuống phần **"Third-party application access policy"**
   - Tìm **"Streamlit Cloud"** hoặc **"Streamlit"** trong list

3. **Authorize App:**
   - Click **"Configure"** hoặc **"Grant access"**
   - Chọn repositories cần access (hoặc **"All repositories"**)
   - Click **"Grant"** hoặc **"Approve"**

4. **Retry Deployment:**
   - Quay lại Streamlit Cloud
   - Thử deploy lại app

### Cách 2: Yêu Cầu Admin Authorize

**Nếu bạn không phải Owner/Admin:**

1. **Liên hệ Organization Owner/Admin:**
   - Yêu cầu họ authorize Streamlit Cloud app
   - Gửi link: https://github.com/organizations/RIVAVIETNAM/settings/applications

2. **Hướng dẫn Admin:**
   - Vào Organization Settings → Third-party access
   - Tìm và authorize "Streamlit Cloud"
   - Grant access cho repository `multi-stragtegy`

### Cách 3: Fork Về Personal Account (Tạm thời)

**Nếu không thể authorize ngay:**

1. **Fork Repository:**
   - Vào: https://github.com/RIVAVIETNAM/multi-stragtegy
   - Click **"Fork"** → Fork về personal account của bạn

2. **Deploy Từ Fork:**
   - Trên Streamlit Cloud, dùng repository của bạn:
   - Repository: `YOUR_USERNAME/multi-stragtegy`
   - Branch: `main`
   - Main file path: `streamlit/MAIN.py`

3. **Sync Với Original (Sau này):**
   - Có thể sync fork với original repo khi cần

---

## 📋 Checklist

### Nếu Bạn Là Admin:

- [ ] Vào GitHub Organization Settings
- [ ] Tìm "Third-party access" section
- [ ] Tìm "Streamlit Cloud" app
- [ ] Click "Configure" hoặc "Grant access"
- [ ] Chọn repositories (hoặc "All repositories")
- [ ] Click "Grant" / "Approve"
- [ ] Retry deployment trên Streamlit Cloud

### Nếu Bạn Không Phải Admin:

- [ ] Liên hệ Organization Owner/Admin
- [ ] Yêu cầu authorize Streamlit Cloud app
- [ ] Hoặc fork repository về personal account
- [ ] Deploy từ personal fork

---

## 🔗 Links Hữu Ích

- **GitHub OAuth Apps:** https://github.com/organizations/RIVAVIETNAM/settings/applications
- **Streamlit Cloud:** https://share.streamlit.io/
- **GitHub Docs:** https://docs.github.com/articles/restricting-access-to-your-organization-s-data/

---

## 💡 Lưu Ý

- **OAuth restrictions** là tính năng bảo mật của GitHub Organizations
- Chỉ Organization Owners/Admins mới có thể authorize apps
- Sau khi authorize, Streamlit Cloud sẽ có quyền truy cập repository
- Có thể revoke access bất cứ lúc nào trong Settings

---

## 🎯 Sau Khi Authorize

1. **Quay lại Streamlit Cloud**
2. **Tạo app mới** (hoặc retry deployment)
3. **Repository:** `RIVAVIETNAM/multi-stragtegy`
4. **Main file path:** `streamlit/MAIN.py`
5. **Deploy!**

---

**Sau khi authorize, deployment sẽ hoạt động bình thường!** 🚀

