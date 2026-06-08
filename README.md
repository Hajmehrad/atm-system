# ATM System 🏦

یک سیستم خودپرداز (ATM) ساده و کارآمد برای مدیریت حساب‌های بانکی.

---

## 🚀 نصب سریع (یک دستور)

```bash
pip install atm-system
```

**تمام!** ✅

---

## ▶️ اجرا (یک دستور)

```bash
atm-system
```

**برنامه شروع میشه!** 🎉

---

## ✨ ویژگی‌ها

- ✅ **مشاهده موجودی** - نمایش موجودی با رمز
- 💰 **واریز پول** - افزودن مبلغ
- 🏦 **برداشت پول** - کسر مبلغ
- 🔐 **تغییر رمز** - امنیت بیشتر
- 🔑 **احراز هویت** - محافظت عملیات

---

## 💻 استفاده در Python

### ساده‌ترین روش

```python
from atm_system import atm_system

atm_system()
```

### با مقادیر سفارشی

```python
from atm_system import atm_system

atm_system(password="5678", balance=5000000)
```

### توابع جداگانه

```python
from atm_system import check_balance, deposit, withdraw, change_password

# مشاهده موجودی
balance = check_balance(balance=1000000, password="1234")

# واریز
balance = deposit(balance=1000000)

# برداشت
balance = withdraw(balance=1000000, password="1234")

# تغییر رمز
password = change_password(password="1234")
```

---

## ⚙️ تنظیمات پیش‌فرض

- **رمز عبور**: `1234`
- **موجودی**: `1,000,000` ریال

---

## 🖥️ سیستم‌های پشتیبانی

- ✅ Windows
- ✅ macOS
- ✅ Linux

**نیاز**: Python 3.6+

---

## 🆘 مشکل‌های رایج

### `atm-system: command not found`

```bash
pip install --upgrade pip
pip install --upgrade atm-system
atm-system
```

### `pip: command not found`

```bash
python -m pip install atm-system
python -m atm_system
```

### حذف و نصب دوباره

```bash
pip uninstall atm-system -y
pip install atm-system
```

---

## 📄 لایسنس

MIT License ✨

---

## 👤 نویسنده

Hajmehrad

**مشکلات یا پیشنهادات**: https://github.com/Hajmehrad/atm-system/issues
