# 📚 BOOKLY

BOOKLY یک پروژه مدیریت و کشف کتاب با استفاده از Django است.

---

## 🚀 نصب و اجرای پروژه

### 1. Clone کردن پروژه

```bash
git clone https://github.com/ALIasgharBalochi/library_management.git
```

### 2. ساخت Virtual Environment

```bash
python -m venv venv
```

فعال‌سازی محیط مجازی:

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 3. نصب Dependencies

```bash
pip install -r requirements.txt
```

### 4. ساخت Migration ها

```bash
python manage.py makemigrations
```

### 5. اعمال Migration ها

```bash
python manage.py migrate
```

### 6. اجرای پروژه

```bash
python manage.py runserver
```

سپس وارد آدرس زیر شوید:

http://127.0.0.1:8000/

---

## 🛠️ تکنولوژی‌های استفاده شده

- Python
- Django
- Django ORM
- SQLite
- HTML
- Tailwind CSS
- Django Templates

---

## ✨ امکانات

- 📚 مدیریت کتاب‌ها
- ➕ اضافه کردن کتاب
- ✏️ ویرایش کتاب
- 🗑️ حذف کتاب
- 🔎 جستجوی کتاب
- 🔍 فیلتر کتاب‌ها
- 👤 ثبت‌نام و ورود کاربران
- ❤️ افزودن کتاب به علاقه‌مندی‌ها
- 📖 مشاهده کتاب‌های موردعلاقه
- 👤 صفحه پروفایل کاربر
- 🏷️ مدیریت دسته‌بندی کتاب‌ها
- 🎨 رابط کاربری مدرن با Tailwind CSS

---

## 📁 ساختار پروژه

```text
lib_manager/
│
├── book/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── lib_manager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Developer

Built with ❤️ and Django.

**BOOKLY — Curated Library**
