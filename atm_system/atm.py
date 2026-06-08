def check_balance(balance, password):
    """نمایش موجودی"""
    p = input("Password: ")
    if p == password:
        print("Your balance is:", balance)
    else:
        print("Wrong password !!")
    return balance


def deposit(balance):
    """واریز پول"""
    amount = int(input("Deposit amount: "))
    balance = balance + amount
    print("Deposit successful.")
    print("Your balance is:", balance)
    return balance


def withdraw(balance, password):
    """برداشت پول"""
    p = input("Password: ")
    if p == password:
        amount = int(input("Withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Your balance is:", balance)
        else:
            print("Insufficient balance.")
    else:
        print("Wrong password !!")
    return balance


def change_password(password):
    """تغییر رمز عبور"""
    p = input("Current password: ")
    if p == password:
        new_password = input("New password: ")
        password = new_password
        print("Password changed successfully.")
    else:
        print("Wrong password !!")
    return password


def display_menu():
    """نمایش منو"""
    print("\n------ ATM ------")
    print("1-Balance")
    print("2-Deposit")
    print("3-Withdraw")
    print("4-Change password")
    print("5-Exit")


def atm_system(password="1234", balance=1000000):
    """تابع اصلی سیستم خودپرداز"""
    while True:
        display_menu()
        choice = input("Choice: ")

        if choice == "1":
            balance = check_balance(balance, password)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance, password)

        elif choice == "4":
            password = change_password(password)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm_system()