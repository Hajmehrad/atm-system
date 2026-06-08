# 📖 Complete Installation and Usage Guide

---

## Step 1️⃣: Install Module

### Method 1: From PyPI (Recommended)

```bash
pip install atm-system
```

### Method 2: From GitHub (Requires Git)

```bash
pip install git+https://github.com/Hajmehrad/atm-system.git
```

### Method 3: Local Installation (For Developers)

```bash
git clone https://github.com/Hajmehrad/atm-system.git
cd atm-system
pip install -e .
```

---

## Step 2️⃣: Run from Terminal

### Simple Way

```bash
atm-system
```

Program starts! 🎉

---

## Step 3️⃣: Run from Python

### Create File `my_atm.py`

```python
from atm_system import atm_system

if __name__ == "__main__":
    atm_system()
```

### Run

```bash
python my_atm.py
```

---

## ✅ Verify Installation

```bash
python -c "from atm_system import atm_system; print('✅ Installation successful!')"
```

---

## 🆘 Troubleshooting

### Problem: `pip not found`

**Solution:**
```bash
python -m pip install atm-system
```

### Problem: `ModuleNotFoundError`

**Solution:**
```bash
pip install --upgrade atm-system
```

### Problem: `Permission denied`

**Solution (Windows & macOS):**
```bash
pip install --user atm-system
```

**Solution (Linux):**
```bash
sudo pip install atm-system
```

### Problem: `atm-system` doesn't work

**Solution 1:**
```bash
python -m atm_system
```

**Solution 2: Remove and reinstall**
```bash
pip uninstall atm-system -y
pip install atm-system
```

---

## 📋 Supported Python Versions

- Python 3.6+
- Python 3.7+
- Python 3.8+
- Python 3.9+
- Python 3.10+
- Python 3.11+
- Python 3.12+
- Python 3.13+

---

## 🔄 Update Module

```bash
pip install --upgrade atm-system
```

---

## ❌ Uninstall Module

```bash
pip uninstall atm-system
```

---

## 📚 More Information

- **GitHub**: https://github.com/Hajmehrad/atm-system
- **PyPI**: https://pypi.org/project/atm-system/
- **Issues**: https://github.com/Hajmehrad/atm-system/issues
