# ATM System 🏦

A simple and efficient Automated Teller Machine (ATM) system designed for banking account management.

---

## 🚀 Quick Installation (One Command)

```bash
pip install atm-system
```

**Done!** ✅

---

## ▶️ Run (One Command)

```bash
atm-system
```

**Program starts!** 🎉

---

## ✨ Features

- ✅ **Check Balance** - View account balance with password authentication
- 💰 **Deposit Money** - Add amount to account
- 🏦 **Withdraw Money** - Deduct amount from account
- 🔐 **Change Password** - Update password for more security
- 🔑 **Authentication** - Protect sensitive operations

---

## 💻 Usage in Python

### Simple Way

```python
from atm_system import atm_system

atm_system()
```

### With Custom Values

```python
from atm_system import atm_system

atm_system(password="5678", balance=5000000)
```

### Individual Functions

```python
from atm_system import check_balance, deposit, withdraw, change_password

# Check balance
balance = check_balance(balance=1000000, password="1234")

# Deposit
balance = deposit(balance=1000000)

# Withdraw
balance = withdraw(balance=1000000, password="1234")

# Change password
password = change_password(password="1234")
```

---

## ⚙️ Default Settings

- **Password**: `1234`
- **Initial Balance**: `1,000,000`

---

## 🖥️ Supported Systems

- ✅ Windows
- ✅ macOS
- ✅ Linux

**Requirement**: Python 3.6+

---

## 🆘 Common Issues

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

### Remove and Reinstall

```bash
pip uninstall atm-system -y
pip install atm-system
```

---

## 📄 License

MIT License ✨

---

## 👤 Author

Hajmehrad

**Issues or Suggestions**: https://github.com/Hajmehrad/atm-system/issues

---

## 📖 Documentation

- **فارسی (Persian)**: [README.md](README.md)
- **Installation Guide**: [INSTALL.en.md](INSTALL.en.md)
- **Quick Start**: [QUICKSTART.en.md](QUICKSTART.en.md)
