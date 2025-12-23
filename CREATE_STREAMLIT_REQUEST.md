# 🔄 Tạo Request Cho Streamlit Cloud

## ❓ Vấn Đề

Trong Organization Settings → Third-party Access, **KHÔNG có Streamlit Cloud** trong list.

## 🔍 Nguyên Nhân

- Streamlit Cloud chưa request access
- Hoặc request chưa được tạo
- Cần trigger request bằng cách deploy app

---

## ✅ Giải Pháp

### Cách 1: Tạo Request Bằng Cách Deploy App

**Deploy app sẽ tự động tạo request:**

1. **Vào Streamlit Cloud:** https://share.streamlit.io/
2. **Click "New app"**
3. **Điền form:**
   ```
   Repository URL: RIVAVIETNAM/multi-stragtegy
   Branch: main
   Main file path: streamlit/MAIN.py
   App URL: multi-stragtegy-vnteam
   ```
4. **Click "Deploy!"**
5. **Deploy sẽ FAIL** với lỗi authorization
6. **NHƯNG** request sẽ được tạo trên GitHub

7. **Quay lại Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications
   - Vào "Third-party application access policy"
   - **Streamlit Cloud sẽ xuất hiện** với status "Pending" hoặc "Request"
   - Click **"Review request"** → **"Approve"**

### Cách 2: Set "No Restrictions" (Cho Phép Tất Cả)

**Nếu bạn là Organization Owner và muốn dễ dàng:**

1. **Vào Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications

2. **Tìm "Third-party application access policy"**

3. **Chọn "No restrictions":**
   - Cho phép tất cả OAuth apps truy cập
   - Không cần approve từng app
   - Streamlit Cloud sẽ tự động được authorize

4. **Save settings**

5. **Retry deployment trên Streamlit Cloud**

### Cách 3: Approve Từ Personal GitHub Settings

**Nếu bạn không phải Organization Owner:**

1. **Vào Personal GitHub Settings:**
   - https://github.com/settings/applications
   - Hoặc: GitHub → Your Profile → Settings → Applications

2. **Tìm "Authorized OAuth Apps":**
   - Click vào tab này
   - Tìm **"Streamlit Cloud"**

3. **Nếu chưa có Streamlit Cloud:**
   - Deploy app trên Streamlit Cloud (sẽ tạo request)
   - Streamlit Cloud sẽ xuất hiện trong list

4. **Configure Organization Access:**
   - Click vào **"Streamlit Cloud"**
   - Tìm phần **"Organization access"**
   - Tìm organization `RIVAVIETNAM`
   - Click **"Grant"** hoặc **"Request"**

5. **Nếu cần Organization Owner approve:**
   - Owner sẽ nhận notification
   - Owner cần approve trong Organization Settings

---

## 📋 Checklist

### Nếu Bạn Là Organization Owner:

- [ ] Deploy app trên Streamlit Cloud (sẽ fail nhưng tạo request)
- [ ] Vào Organization Settings → Third-party Access
- [ ] Tìm "Streamlit Cloud" request (sẽ xuất hiện sau khi deploy)
- [ ] Click "Review request" → "Approve"
- [ ] Hoặc set "No restrictions" (cho phép tất cả)
- [ ] Retry deployment trên Streamlit Cloud

### Nếu Bạn Không Phải Owner:

- [ ] Deploy app trên Streamlit Cloud
- [ ] Vào Personal GitHub Settings → Authorized OAuth Apps
- [ ] Grant organization access cho Streamlit Cloud
- [ ] Request sẽ được gửi đến Organization Owner
- [ ] Đợi Owner approve
- [ ] Retry deployment

---

## 🎯 Cách Nhanh Nhất

### Cho Organization Owner:

1. **Vào Organization Settings:**
   - https://github.com/organizations/RIVAVIETNAM/settings/applications

2. **Tìm "Third-party application access policy"**

3. **Chọn "No restrictions"** (cho phép tất cả apps)

4. **Save**

5. **Deploy app trên Streamlit Cloud:**
   - Repository: `RIVAVIETNAM/multi-stragtegy`
   - Main file: `streamlit/MAIN.py`
   - Deploy sẽ thành công ngay!

---

## ⚠️ Lưu Ý

### "No Restrictions" vs "Restrict Access"

**No Restrictions:**
- ✅ Dễ dàng, không cần approve từng app
- ✅ Streamlit Cloud tự động được authorize
- ⚠️ Ít bảo mật hơn (cho phép tất cả apps)

**Restrict Access:**
- ✅ Bảo mật hơn (chỉ approve apps cụ thể)
- ⚠️ Cần approve từng app
- ⚠️ Cần approve Streamlit Cloud cụ thể

### Sau Khi Approve

- ✅ Streamlit Cloud sẽ có quyền truy cập organization
- ✅ Organization sẽ hiện trong Streamlit Cloud dashboard
- ✅ Repositories sẽ hiện trong dropdown
- ✅ Deploy sẽ thành công

---

## 🔗 Links

- **Organization Settings:** https://github.com/organizations/RIVAVIETNAM/settings/applications
- **Personal Settings:** https://github.com/settings/applications
- **Streamlit Cloud:** https://share.streamlit.io/

---

## 🎯 Tóm Tắt

**Vì không có Streamlit Cloud trong list:**

1. **Deploy app trên Streamlit Cloud** (sẽ fail nhưng tạo request)
2. **Quay lại Organization Settings** → Streamlit Cloud sẽ xuất hiện
3. **Approve request**
4. **Hoặc set "No restrictions"** (cho phép tất cả)
5. **Retry deployment**

**Sau khi approve, deployment sẽ thành công!** 🚀

