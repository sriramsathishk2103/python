import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chaitu@2003",  
    database="bank_system"
)

cursor = db.cursor()

def create_account():
    acc = int(input("Enter Account Number: "))
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Amount: "))

    cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)", (acc, name, balance))
    db.commit()
    print("Account created successfully!")

def deposit():
    acc = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Deposit: "))

    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no=%s", (amount, acc))
    db.commit()
    print("Amount Deposited!")

def withdraw():
    acc = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Withdraw: "))

    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc,))
    result = cursor.fetchone()

    if result is None:
        print("Account not found")
        return

    balance = result[0]

    if balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no=%s", (amount, acc))
        db.commit()
        print("Withdrawal Successful!")
    else:
        print("Insufficient Balance")

def check_balance():
    acc = int(input("Enter Account Number: "))
    cursor.execute("SELECT * FROM accounts WHERE account_no=%s", (acc,))
    data = cursor.fetchone()

    if data:
        print("\nAccount Number:", data[0])
        print("Name:", data[1])
        print("Balance:", data[2])
    else:
        print("Account Not Found")


while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid Option, Try Again.")
