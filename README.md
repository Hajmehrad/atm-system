# ATM System

یک سیستم خودپرداز (ATM) ساده و کارآمد که برای مدیریت حساب‌های بانکی طراحی شده است.

## ویژگی‌ها ✨

- ✅ **مشاهده موجودی** - نمایش موجودی حساب با احراز هویت رمز
- 💰 **واریز پول** - افزودن مبلغ به حساب
- 🏦 **برداشت پول** - کسر مبلغ از حساب (با بررسی کافی بودن موجودی)
- 🔐 **تغییر رمز عبور** - امکان تغییر رمز برای امنیت بیشتر
- 🔑 **احراز هویت** - بررسی رمز عبور برای عملیات حساس

## نصب 📦

```bash
pip install -r requirements.txt
```

یا

```bash
pip install git+https://github.com/Hajmehrad/atm-system.git
```

## استفاده 🚀

### اجرای مستقیم

```python
from atm_system.atm import atm_system

# با رمز عبور و موجودی پیش‌فرض
atm_system()

# یا با مقادیر سفارشی
atm_system(password="5678", balance=5000000)
```

### استفاده توابع جداگانه

```python
from atm_system.atm import check_balance, deposit, withdraw, change_password

# مشاهده موجودی
balance = check_balance(balance=1000000, password="1234")

# واریز
balance = deposit(balance=1000000)

# برداشت
balance = withdraw(balance=1000000, password="1234")

# تغییر رمز
password = change_password(password="1234")
```

## تنظیمات پیش‌فرض ⚙️

- **رمز عبور پیش‌فرض**: `1234`
- **موجودی اولیه**: `1,000,000` ریال

## ساختار پروژه 📁

```
atm-system/
├── README.md
├── requirements.txt
├── setup.py
└── atm_system/
    ├── __init__.py
    └── atm.py
```

## لایسنس 📄

MIT License

## نویسنده 👤

Hajmehrad

---

برای گزارش مشکل یا پیشنهاد بهبود، لطفاً یک Issue باز کنید.
