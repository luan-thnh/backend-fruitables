<div align="center">
  <h1 style="color: #d1af75; text-transform: uppercase;">
    <b>Hướng dẫn cài đặt module và run server</b>
  </h1>
</div>

### **1. Cài đặt `virtualenv`:**

```bash
pip install virtualenv
```

Nếu bạn không thể chạy lệnh trên, thử chạy:

```bash
pip install -r requirements.txt
```

Điều này sẽ cài đặt các gói module cần thiết global trong máy thay vì cài đặt chúng vào môi trường ảo.

Nếu chưa có file `requirements.txt` thì hãy tạo và thêm vào file:

```python
django
djangorestframework
djangorestframework_simplejwt
django-cors-headers
djoser
requests
cloudinary
python-decouple
psycopg2-binary
dj-database-url
drf-yasg
gunicorn
whitenoise
```

Sau đó chạy lại lệnh

### **2. Tạo môi trường ảo:**

```bash
virtualenv env
```

<div style="page-break-after: always;"></div>

### **3. Kích hoạt môi trường ảo:**

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### **4. Cài đặt các package cần thiết:**

```bash
pip install -r requirements.txt
```

### **5. Khởi tạo cơ sở dữ liệu:**

```bash
python manage.py makemigrations user
python manage.py makemigrations upload
python manage.py makemigrations products
python manage.py migrate
python manage.py makemigrations
```

### **6. Chạy server:**

```bash
python manage.py runserver
```

Nếu bạn gặp **lỗi**, làm theo các bước sau:

- Xóa thư mục `migrations` (nếu có)
- Xóa file `db.sqlite3`

Sau đó, lặp lại các bước 5 và 6.
