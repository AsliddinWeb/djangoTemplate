# **Django Template**

Ushbu loyiha **Django** asosida yaratilgan.

---

## **O'rnatish**

Loyihani **GitHub**'dan yuklab olish:
```bash
git clone https://github.com/AsliddinWeb/djangoTemplate.git
cd djangoTemplate
```

**1. `.env` faylini yaratish va unga quyidagi ma'lumotni kiritish:**
```env
SECRET_KEY=secret_key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_ENV=dev

```

**2. Virtual muhitni yaratish va faollashtirish:**

✅ **MacOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Kerakli kutubxonalarni o'rnatish:**
```bash
pip install -r requirements.txt
```

---

## **Ma'lumotlar bazasini yangilash**

🖥 **MacOS/Linux:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

🖥 **Windows:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Loyihani ishga tushirish**

🚀 **MacOS/Linux:**
```bash
python3 manage.py runserver
```

🚀 **Windows:**
```bash
python manage.py runserver
```

**Server ishga tushgandan so'ng, brauzerda quyidagi manzilga o'ting:**
```
http://127.0.0.1:8000/
```

✅ **Loyiha muvaffaqiyatli ishga tushdi!** 🎉
