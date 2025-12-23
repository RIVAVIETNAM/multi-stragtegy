# 🏢 Làm Cho Organization Hiện Trong Streamlit Cloud

## 🎯 Mục Tiêu

Làm cho organization `RIVAVIETNAM` và các repositories của nó hiện lên trong Streamlit Cloud dashboard.

## ✅ Giải Pháp

### Cách 1: Authorize Organization Khi Deploy (Tự Động)

**Khi tạo app mới, Streamlit Cloud sẽ tự động hỏi authorize organization:**

1. **Vào Streamlit Cloud:** https://share.streamlit.io/
2. **Click "New app"**
3. **Trong form "Repository URL":**
   - **Nhập trực tiếp:** `RIVAVIETNAM/multi-stragtegy`
   - (Không cần chọn từ dropdown)
4. **Điền form:**
   ```
   Repository URL: RIVAVIETNAM/multi-stragtegy
   Branch: main
   Main file path: streamlit/MAIN.py
   ```
5. **Click "Deploy!"**
6. **GitHub sẽ hiện popup:**
   - "Authorize Streamlit Cloud"
   - **Quan trọng:** Chọn **"Grant access to RIVAVIETNAM"** hoặc **"Authorize organization"**
   - Chọn repositories (hoặc "All repositories")
   - Click **"Authorize"**

7. **Sau khi authorize:**
   - Organization sẽ hiện trong Streamlit Cloud
   - Repositories sẽ hiện trong dropdown lần sau

### Cách 2: Authorize Organization Trước (Thủ Công)

**Nếu bạn là Organization Owner/Admin:**

1. **Vào GitHub Organization Settings:**
   - Vào: https://github.com/organizations/RIVAVIETNAM/settings/applications
   - Hoặc: GitHub → Organization `RIVAVIETNAM` → Settings → Third-party access

2. **Tìm "Third-party application access policy":**
   - Scroll xuống phần này
   - Tìm **"Streamlit Cloud"** trong list

3. **Authorize Streamlit Cloud:**
   - Nếu có request pending: Click **"Review request"** → **"Approve"**
   - Nếu chưa có: Sẽ được tạo khi deploy lần đầu

4. **Cấu hình Access:**
   - Chọn **"No restrictions"** (cho phép tất cả apps)
   - Hoặc **"Restrict access"** và approve Streamlit Cloud cụ thể

### Cách 3: Authorize Qua Personal GitHub Settings

**Nếu bạn không phải Organization Owner:**

1. **Vào Personal GitHub Settings:**
   - Vào: https://github.com/settings/applications
   - Hoặc: GitHub → Your Profile → Settings → Applications

2. **Tìm "Authorized OAuth Apps":**
   - Click vào tab này
   - Tìm **"Streamlit Cloud"**

3. **Configure Organization Access:**
   - Click vào **"Streamlit Cloud"**
   - Tìm phần **"Organization access"**
   - Tìm organization `RIVAVIETNAM`
   - Click **"Grant"** hoặc **"Request"** access

4. **Nếu cần Organization Owner approve:**
   - Owner sẽ nhận notification
   - Owner cần approve trong Organization Settings

---

## 🔍 Kiểm Tra Organization Đã Được Authorize

### Trên Streamlit Cloud:

1. **Vào Dashboard:** https://share.streamlit.io/
2. **Khi tạo app mới:**
   - Dropdown "Repository URL" sẽ hiện organization `RIVAVIETNAM`
   - Có thể chọn repositories từ organization

### Trên GitHub:

1. **Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications
   - Xem "Third-party application access policy"
   - Streamlit Cloud phải được approve

2. **Personal Settings:**
   - https://github.com/settings/applications
   - Xem "Authorized OAuth Apps" → "Streamlit Cloud"
   - Organization access phải được grant

---

## 📋 Checklist

### Nếu Bạn Là Organization Owner/Admin:

- [ ] Vào Organization Settings
- [ ] Tìm "Third-party application access policy"
- [ ] Approve "Streamlit Cloud" (nếu có request)
- [ ] Hoặc set "No restrictions" (cho phép tất cả)
- [ ] Test: Tạo app mới trên Streamlit Cloud
- [ ] Organization sẽ hiện trong dropdown

### Nếu Bạn Không Phải Owner:

- [ ] Vào Personal GitHub Settings
- [ ] Authorize Streamlit Cloud cho organization
- [ ] Request access từ Organization Owner
- [ ] Đợi Owner approve
- [ ] Test: Tạo app mới trên Streamlit Cloud

---

## 🎯 Cách Nhanh Nhất

### Authorize Khi Deploy:

1. **Vào Streamlit Cloud:** https://share.streamlit.io/
2. **Click "New app"**
3. **Nhập repository URL:** `RIVAVIETNAM/multi-stragtegy`
4. **Click "Deploy!"**
5. **Khi GitHub hỏi authorize:**
   - ✅ **Chọn "Grant access to RIVAVIETNAM"**
   - ✅ Chọn repositories
   - ✅ Click "Authorize"
6. **Sau khi authorize:**
   - Organization sẽ hiện trong Streamlit Cloud
   - Repositories sẽ hiện trong dropdown

---

## ⚠️ Lưu Ý

### OAuth App Access Restrictions

- **Nếu organization có restrictions:**
  - Cần Organization Owner approve
  - Không thể authorize từ personal account
  - Phải liên hệ Owner

### Sau Khi Authorize

- **Organization sẽ hiện trong Streamlit Cloud**
- **Repositories sẽ hiện trong dropdown**
- **Có thể chọn từ dropdown thay vì nhập thủ công**

---

## 🔗 Links

- **Organization Settings:** https://github.com/organizations/RIVAVIETNAM/settings/applications
- **Personal Settings:** https://github.com/settings/applications
- **Streamlit Cloud:** https://share.streamlit.io/

---

## 🎯 Tóm Tắt

**Cách đơn giản nhất:**
1. Tạo app mới trên Streamlit Cloud
2. Nhập repository URL: `RIVAVIETNAM/multi-stragtegy`
3. Khi GitHub hỏi, **chọn "Grant access to RIVAVIETNAM"**
4. Authorize
5. Organization sẽ hiện trong Streamlit Cloud sau đó

**Sau khi authorize lần đầu, organization và repositories sẽ tự động hiện trong dropdown!** 🚀

