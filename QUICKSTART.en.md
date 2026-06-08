# 🚀 How to Run

---

## 📦 Installation

```bash
pip install atm-system
```

---

## ▶️ Run

```bash
atm-system
```

---

## 🎮 How to Use

After running, you'll see this menu:

```
------ ATM ------
1-Balance        (Check balance)
2-Deposit        (Deposit money)
3-Withdraw       (Withdraw money)
4-Change password (Change password)
5-Exit           (Exit)
```

### Examples

**Check Balance:**
```
Choice: 1
Password: 1234
Your balance is: 1000000
```

**Deposit Money:**
```
Choice: 2
Deposit amount: 100000
Deposit successful.
Your balance is: 1100000
```

**Withdraw Money:**
```
Choice: 3
Password: 1234
Withdrawal amount: 50000
Withdrawal successful.
Your balance is: 950000
```

**Change Password:**
```
Choice: 4
Current password: 1234
New password: 5678
Password changed successfully.
```

**Exit:**
```
Choice: 5
Exiting the program.
```

---

## 💻 Use in Python Code

### Simplest Way

```python
from atm_system import atm_system

atm_system()
```

### With Custom Values

```python
from atm_system import atm_system

# Password: 5678, Balance: 5 million
atm_system(password="5678", balance=5000000)
```

### Use Individual Functions

```python
from atm_system import check_balance, deposit, withdraw, change_password

balance = 1000000
password = "1234"

# Check balance
balance = check_balance(balance, password)

# Deposit
balance = deposit(balance)

# Withdraw
balance = withdraw(balance, password)

# Change password
password = change_password(password)
```

---

## ⚙️ Default Settings

- **Password**: `1234`
- **Initial Balance**: `1,000,000`

---

## ❓ Frequently Asked Questions

**Q: How to stop?**

A: Choose `5` (Exit) or press `Ctrl+C`

**Q: What's the default password?**

A: `1234`

**Q: What's the initial balance?**

A: `1,000,000`

**Q: Can I change the password?**

A: Yes! Choose `4` from menu

---

## 📚 Full Documentation

- **Persian**: [README.md](README.md) - مستندات کامل
- **English**: [README.en.md](README.en.md) - Full documentation
- **Installation Persian**: [INSTALL.md](INSTALL.md)
- **Installation English**: [INSTALL.en.md](INSTALL.en.md)
