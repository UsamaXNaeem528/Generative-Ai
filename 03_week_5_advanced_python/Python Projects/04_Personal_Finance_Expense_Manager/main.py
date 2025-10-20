from user import UserManager
from transaction import TransactionManager 
from budget import BudgetManager

print(f"{50 * '-'}")
print("Welcome to the Personal Finance & Expense Manager 💰")
print(f"{50 * '-'}")

user = UserManager()
trans = TransactionManager()
budget = BudgetManager()

while True:
    print("\n1) Login\n2) Create Account\n3) Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if user.login_user(username, password):  # Must return True if login successful
            print(f"\n✅ Welcome, {username}!\n")

            while True:
                print("\n1) Add Income\n2) Add Expense\n3) Set Budget\n4) Search / Filter Transactions\n5) Logout")
                option = input("Enter your option: ")

                match option:
                    case '1':
                        # Add Income
                        category = input("Enter Income Category (e.g., Salary, Bonus): ")
                        amount = float(input("Enter Income Amount: "))
                        desc = input("Enter Description: ")
                        trans.add_new_transaction(username=username, category=category, trans_type="income", amount=amount, description=desc)
                        print("✅ Income Added Successfully!\n")

                    case '2':
                        # Add Expense
                        category = input("Enter Expense Category (e.g., Food, Travel): ")
                        amount = float(input("Enter Expense Amount: "))
                        desc = input("Enter Description: ")
                        trans.add_new_transaction(username=username, category=category, trans_type="expense", amount=amount, description=desc)
                        print("✅ Expense Added Successfully!")

                        # Check Budget
                        budget.check_budget(username=username, category=category)

                    case '3':
                        # Set Budget
                        category = input("Enter Category Name: ")
                        amount = float(input("Enter Budget Amount: "))
                        period = input("Enter Period (monthly/yearly): ").lower()
                        budget.set_budget(username, category, amount, period)

                    case '4':
                        # Filter / Search Transactions
                        keyword = input("Enter category or keyword to search: ")
                        trans.search_transactions(username, keyword)

                    case '5':
                        print(f"👋 Logged out, {username}!\n")
                        break

                    case _:
                        print("❌ Invalid option, please try again.")

        else:
            print("❌ Invalid username or password. Try again.")

    elif user_choice == '2':
        username = input("Create Username: ")
        password = input("Create Password: ")
        user.create_user(username, password)

    elif user_choice == '3':
        print("👋 Exiting program... Goodbye!")
        break

    else:
        print("❌ Invalid choice, please try again.")
