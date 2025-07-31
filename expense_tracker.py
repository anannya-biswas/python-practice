expenses = []

def add_expense():
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    expenses.append((item, amount))
    print("Expense added.")

def show_expenses():
    total = 0
    print("\nExpenses:")
    for item, amount in expenses:
        print(f"{item}: ₹{amount}")
        total += amount
    print(f"\nTotal: ₹{total}")

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
