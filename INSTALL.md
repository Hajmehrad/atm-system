# 📖 راهنمای کامل نصب و اجرا

---

## مرحله 1️⃣: نصب ماژول

### روش 1: نصب از PyPI (توصیه شده)

```bash
pip install atm-system
```

### روش 2: نصب از GitHub (نیاز به Git)

```bash
pip install git+https://github.com/Hajmehrad/atm-system.git
```

### روش 3: نصب محلی (برای توسعه‌دهندگان)

```bash
git clone https://github.com/Hajmehrad/atm-system.git
cd atm-system
pip install -e .
```

---

## مرحله 2️⃣: اجرا از ترمینال

### روش ساده

```bash
atm-system
```

برنامه شروع میشه! 🎉

---

## مرحله 3️⃣: اجرا از Python

### ایجاد فایل `my_atm.py`

```python
from atm_system import atm_system

if __name__ == "__main__":
    atm_system()
```

### اجرا

```bash
python my_atm.py
```

---

## ✅ چک کردن نصب موفق

```bash
python -c "from atm_system import atm_system; print('✅ نصب موفق!')"
```

---

## 🆘 حل مشکل‌ها

### مشکل: `pip not found`

**حل:**
```bash
python -m pip install atm-system
```

### مشکل: `ModuleNotFoundError`

**حل:**
```bash
pip install --upgrade atm-system
```

### مشکل: `Permission denied`

**حل (Windows و macOS):**
```bash
pip install --user atm-system
```

**حل (Linux):**
```bash
sudo pip install atm-system
```

### مشکل: `atm-system` کار نمی‌کند

**حل 1:**
```bash
python -m atm_system
```

**حل 2: حذف و نصب دوباره**
```bash
pip uninstall atm-system -y
pip install atm-system
```

---

## 📋 نسخه‌های Python پشتیبانی شده

- Python 3.6+
- Python 3.7+
- Python 3.8+
- Python 3.9+
- Python 3.10+
- Python 3.11+
- Python 3.12+
- Python 3.13+

---

## 🔄 بروزرسانی ماژول

```bash
pip install --upgrade atm-system
```

---

## ❌ حذف ماژول

```bash
pip uninstall atm-system
```

---

## 📌 اطلاعات بیشتر

- **GitHub**: https://github.com/Hajmehrad/atm-system
- **PyPI**: https://pypi.org/project/atm-system/
- **Issues**: https://github.com/Hajmehrad/atm-system/issues
