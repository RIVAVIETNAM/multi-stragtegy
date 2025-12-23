# 🔍 Tại Sao Không Thấy Organization Repositories?

## ❓ Vấn Đề

Khi tạo app trên Streamlit Cloud, không thấy repositories từ organization `RIVAVIETNAM` trong dropdown list.

## 🔍 Nguyên Nhân

1. **Streamlit Cloud chưa được authorize** để truy cập organization repositories
2. **Organization có OAuth restrictions** - cần approve app
3. **Bạn không có quyền** truy cập organization repositories
4. **Streamlit Cloud chưa sync** organization repositories

---

## ✅ Giải Pháp

### Cách 1: Nhập Repository URL Thủ Công

**Thay vì chọn từ dropdown, nhập trực tiếp:**

1. **Vào Streamlit Cloud:** https://share.streamlit.io/
2. **Click "New app"**
3. **Trong form, thay vì chọn từ dropdown:**
   - **Nhập trực tiếp vào field "Repository URL":**
   ```
   RIVAVIETNAM/multi-stragtegy
   ```
4. **Điền các thông tin khác:**
   - Branch: `main`
   - Main file path: `streamlit/MAIN.py`
5. **Click "Deploy!"**
6. **GitHub sẽ hiện popup authorize** - Click "Authorize"

### Cách 2: Authorize Organization Trước

1. **Vào GitHub Settings:**
   - Vào: https://github.com/settings/applications
   - Hoặc: GitHub → Your Profile → Settings → Applications

2. **Tìm "Authorized OAuth Apps":**
   - Click vào "Authorized OAuth Apps"
   - Tìm "Streamlit Cloud"
   - Nếu chưa có, sẽ được tạo khi deploy lần đầu

3. **Vào Organization Settings:**
   - Vào: https://github.com/organizations/RIVAVIETNAM/settings/applications
   - Tìm "Third-party application access policy"
   - Approve "Streamlit Cloud" nếu có request

### Cách 3: Kiểm Tra Quyền Truy Cập

1. **Kiểm tra bạn có quyền:**
   - Vào: https://github.com/RIVAVIETNAM/multi-stragtegy
   - Xem bạn có thể access repository không
   - Kiểm tra bạn có role gì trong organization

2. **Nếu không có quyền:**
   - Liên hệ organization admin
   - Yêu cầu thêm bạn vào organization
   - Hoặc grant access cho repository

---

## 🎯 Cách Đơn Giản Nhất

### Nhập Repository URL Thủ Công:

1. **Vào Streamlit Cloud:** https://share.streamlit.io/
2. **Click "New app"**
3. **Trong field "Repository URL", nhập:**
   ```
   RIVAVIETNAM/multi-stragtegy
   ```
   (KHÔNG có `.git`, KHÔNG có `https://github.com/`)

4. **Điền form:**
   ```
   Repository URL: RIVAVIETNAM/multi-stragtegy
   Branch: main
   Main file path: streamlit/MAIN.py
   App URL: multi-stragtegy-vnteam
   ```

5. **Click "Deploy!"**
6. **Khi GitHub hỏi authorize:**
   - Click "Authorize Streamlit Cloud"
   - Chọn repositories (hoặc "All repositories")
   - Click "Authorize"

---

## 🔐 Nếu Vẫn Không Được

### Kiểm Tra Organization Settings:

1. **Vào Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications

2. **Kiểm tra "Third-party application access policy":**
   - Nếu là "No restrictions" → OK
   - Nếu là "Restrict access" → Cần approve Streamlit Cloud

3. **Approve Streamlit Cloud:**
   - Tìm "Streamlit Cloud" trong pending requests
   - Click "Review request"
   - Chọn repositories
   - Click "Approve"

---

## 📋 Checklist

- [ ] Đã thử nhập repository URL thủ công
- [ ] Đã authorize Streamlit Cloud khi GitHub hỏi
- [ ] Đã kiểm tra quyền truy cập organization
- [ ] Đã kiểm tra organization OAuth settings
- [ ] Đã liên hệ admin nếu cần

---

## 💡 Lưu Ý

- **Organization repositories** có thể không hiện trong dropdown nếu chưa authorize
- **Nhập URL thủ công** thường hoạt động tốt hơn
- **Sau khi authorize lần đầu**, repositories sẽ hiện trong dropdown lần sau

---

## 🎯 Tóm Tắt

**Cách nhanh nhất:**
1. Vào Streamlit Cloud
2. Click "New app"
3. **Nhập trực tiếp:** `RIVAVIETNAM/multi-stragtegy` (không chọn từ dropdown)
4. Điền form
5. Deploy và authorize khi GitHub hỏi

**Đơn giản và hiệu quả!** 🚀

