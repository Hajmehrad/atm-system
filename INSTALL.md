# مراحل نصب و استفاده 📖

## گام 1: نصب ماژول

ترمینال رو باز کن و این دستور رو بزن:

```bash
pip install atm-system
```

**منتظر بمان تا نصب کامل شود** ✅

---

## گام 2: اجرا

بعد از نصب، این دستور رو بزن:

```bash
atm-system
```

برنامه شروع میشه! 🎉

---

## اگر مشکل داشتی

### مشکل: `command not found` یا `'atm-system' is not recognized`

**حل:**
```bash
pip install --upgrade pip
pip install --upgrade atm-system
```

سپس دوباره:
```bash
atm-system
```

---

### مشکل: `pip not found`

**حل:**
```bash
python -m pip install atm-system
```

سپس:
```bash
python -m atm_system
```

---

### مشکل: هنوز کار نمی‌کند؟

```bash
# حذف و نصب دوباره
pip uninstall atm-system
pip install atm-system
```

---

## استفاده در Python Code

فایل جدید بساز: `my_atm.py`

```python
from atm_system import atm_system

if __name__ == "__main__":
    atm_system()
```

سپس:
```bash
python my_atm.py
```

---

**مشکل دیگری دارید؟ Issue باز کنید:** https://github.com/Hajmehrad/atm-system/issues
