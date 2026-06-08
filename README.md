# ATM System 🏦

یک سیستم خودپرداز (ATM) ساده و کارآمد که برای مدیریت حساب‌های بانکی طراحی شده است.

## 🚀 نصب و اجرا (یک دستور!)

```bash
pip install atm-system && atm-system
```

**تمام!** برنامه شروع میشه! ✨

---

## 📖 نصب مرحله به مرحله

### مرحله 1: نصب
```bash
pip install atm-system
```

### مرحله 2: اجرا
```bash
atm-system
```

**برنامه شروع میشه!** 🎉

---

## ✨ ویژگی‌ها

- ✅ **مشاهده موجودی** - نمایش موجودی حساب با احراز هویت رمز
- 💰 **واریز پول** - افزودن مبلغ به حساب
- 🏦 **برداشت پول** - کسر مبلغ از حساب (با بررسی کافی بودن موجودی)
- 🔐 **تغییر رمز عبور** - امکان تغییر رمز برای امنیت بیشتر
- 🔑 **احراز هویت** - بررسی رمز عبور برای عملیات حساس

---

## 💻 استفاده در کد Python

```python
from atm_system import atm_system

# اجرای ساده
atm_system()
```

با مقادیر سفارشی:

```python
from atm_system import atm_system

# رمز: 5678، موجودی: 5 میلیون
atm_system(password="5678", balance=5000000)
```

---

## ⚙️ تنظیمات پیش‌فرض

- **رمز عبور**: `1234`
- **موجودی اولیه**: `1,000,000` ریال

---

## 📚 توابع جداگانه

```python
from atm_system import check_balance, deposit, withdraw, change_password

balance = check_balance(balance=1000000, password="1234")
balance = deposit(balance=1000000)
balance = withdraw(balance=1000000, password="1234")
password = change_password(password="1234")
```

---

## 🖥️ سیستم‌های پشتیبانی

- ✅ Windows
- ✅ macOS  
- ✅ Linux

**نیاز:** Python 3.6 یا بالاتر

---

## 🆘 مشکل‌های رایج

### `atm-system` کار نمی‌کند؟

```bash
pip install --upgrade pip
pip install --upgrade atm-system
atm-system
```

### `pip not found`؟

```bash
python -m pip install atm-system
python -m atm_system
```

### هنوز مشکل دارید؟

```bash
pip uninstall atm-system -y
pip install atm-system
```

**راهنمای کامل:** [INSTALL.md](INSTALL.md)

---

## 📄 لایسنس

MIT License - آزادانه استفاده کنید ✨

---

## 👤 نویسنده

**Hajmehrad**

**مشکلات یا پیشنهادات:** https://github.com/Hajmehrad/atm-system/issues
