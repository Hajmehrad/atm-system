# 🚀 شروع سریع

---

## 📦 نصب

```bash
pip install atm-system
```

---

## ▶️ اجرا

```bash
atm-system
```

---

## 🎮 نحوه استفاده

بعد از اجرا، این منو نمایش داده می‌شود:

```
------ ATM ------
1-Balance        (مشاهده موجودی)
2-Deposit        (واریز پول)
3-Withdraw       (برداشت پول)
4-Change password (تغییر رمز)
5-Exit           (خروج)
```

### مثال‌ها

**مشاهده موجودی:**
```
Choice: 1
Password: 1234
Your balance is: 1000000
```

**واریز پول:**
```
Choice: 2
Deposit amount: 100000
Deposit successful.
Your balance is: 1100000
```

**برداشت پول:**
```
Choice: 3
Password: 1234
Withdrawal amount: 50000
Withdrawal successful.
Your balance is: 950000
```

**تغییر رمز:**
```
Choice: 4
Current password: 1234
New password: 5678
Password changed successfully.
```

**خروج:**
```
Choice: 5
Exiting the program.
```

---

## 💻 استفاده در کد Python

### ساده‌ترین روش

```python
from atm_system import atm_system

atm_system()
```

### با مقادیر سفارشی

```python
from atm_system import atm_system

# رمز: 5678، موجودی: 5 میلیون
atm_system(password="5678", balance=5000000)
```

### استفاده توابع جداگانه

```python
from atm_system import check_balance, deposit, withdraw, change_password

balance = 1000000
password = "1234"

# مشاهده موجودی
balance = check_balance(balance, password)

# واریز
balance = deposit(balance)

# برداشت
balance = withdraw(balance, password)

# تغییر رمز
password = change_password(password)
```

---

## ⚙️ تنظیمات پیش‌فرض

- **رمز عبور**: `1234`
- **موجودی**: `1,000,000` ریال

---

## ❓ سوالات رایج

**S: چطور متوقف کنم؟**

A: انتخاب `5` (خروج) یا `Ctrl+C`

**S: رمز پیش‌فرض چیست؟**

A: `1234`

**S: موجودی اولیه چقدره؟**

A: `1,000,000` ریال

**S: می‌تونم رمز تغییر بدم؟**

A: بله! انتخاب `4` از منو

---

## 📚 مستندات کامل

- **فارسی**: [README.md](README.md) - مستندات کامل
- **English**: [README.en.md](README.en.md) - Full documentation
- **نصب فارسی**: [INSTALL.md](INSTALL.md)
- **Installation English**: [INSTALL.en.md](INSTALL.en.md)
