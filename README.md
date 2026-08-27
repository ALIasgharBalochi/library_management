# BOOKLY — Local Tailwind Edition

این نسخه هیچ CDN، فونت خارجی، آیکون‌پک آنلاین، تصویر خارجی یا سرویس خارجی ندارد.
در زمان اجرای Django، تمام CSS و JavaScript از فایل‌های local پروژه لود می‌شوند.

## نصب Tailwind به‌صورت Local

در ریشه این پوشه:

```bash
npm install
npm run dev
```

برای production:

```bash
npm run build
```

بعد از build فایل زیر ساخته می‌شود:

book/static/book/css/output.css

## Django

در `settings.py` مطمئن شو:

```python
INSTALLED_APPS = [
    # ...
    "django.contrib.staticfiles",
]
```

و در development:

```python
STATIC_URL = "static/"
```

## نکته

این قالب از `{% load static %}` و فایل‌های local استفاده می‌کند. بنابراین برای نمایش سایت به هیچ CDN یا سرویس خارجی وابسته نیست.
