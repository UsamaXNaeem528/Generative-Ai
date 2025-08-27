'''
Features:
Add expenses (amount, category, date, description)
View all expenses
Filter by category/date range
Show total spending, highest spending category
Store data in a .json or .csv file
'''

expenses = []
from datetime import date

import json
file_path = r'5_expense_tracker_cli\expense_logs.json'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        expenses = json.load(file)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    expenses = []
    
def addExpenses(category, amount, description):
    id = len(expenses) + 1
    today = date.today()
    today = str(today)   # convert the date into string because json dont supports date
    new_expense = {'id': id, 'category':category, 'date':today, 'amount':amount, 'description':description}
    expenses.append(new_expense)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, indent=4)
        print("Expense is saved")
        return

def viewAllExpenses():
    for expense in expenses:
        print(f'Date : {expense["date"]}')
        print(f'Category : {expense["category"]}')
        print(f'Amount : {expense["amount"]}')
        print(f'Description : {expense["description"]}')
        print('-' * 20)

def filterExpenseByDate(date):
    filtered_expenses = []
    for expense in expenses:
        if(expense['date'] == date):
            filtered_expenses.append(expense)
    
    if len(filtered_expenses) == 0:
        print("No expense available within this date")
    
    for expense in filtered_expenses:
        print(f'Date : {expense['date']}')
        print(f'Category : {expense['category']}')
        print(f'Amount : {expense['amount']}')
        print(f'Description : {expense['description']}')
        print('-' * 20)

def filterExpenseByCategory(category):
    filtered_expenses = []
    for expense in expenses:
        if(expense['category'] == category):
            filtered_expenses.append(expense)
    
    if len(filtered_expenses) == 0:
        print("No expense available with this category")
    
    for expense in filtered_expenses:
        print(f'Date : {expense["date"]}')
        print(f'Category : {expense["category"]}')
        print(f'Amount : {expense["amount"]}')
        print(f'Description : {expense["description"]}')
        print('-' * 20)

def filterExpenseByDateRange(first_date, last_date):
    filtered_expenses = []
    for expense in expenses:
        if(first_date <= expense['date'] <= last_date):
            filtered_expenses.append(expense)
    if not filtered_expenses:
        print('No Expenses available between these dates')
    for expense in filtered_expenses:
        print(f'Date : {expense["date"]}')
        print(f'Category : {expense["category"]}')
        print(f'Amount : {expense["amount"]}')
        print(f'Description : {expense["description"]}')
        print('-' * 20)
        
def total_spendings():
    total_amount = 0
    combined_expenses = []
    
    for expense in expenses:
        total_amount += expense['amount']
        
    # add a amount with same category in combined_expenses list[]
    for expense in expenses:
        found = False
        for category in combined_expenses:
            if category['category'] == expense['category']:
                category['amount'] += expense['amount']
                found = True
                break
        if not found:
            combined_expenses.append({'category':expense['category'], 'amount': expense['amount']})

#   print(combined_expenses)
    highest_category = max(combined_expenses, key=lambda x: x['amount'])
    print('Total Spendings :',total_amount)
    print('-----Highest Spending-----')
    print('Category :',highest_category['category'])
    print('Amount :',highest_category['amount'])
        
while True:
    print("\n📌 Expense Tracker")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses By Date")
    print("4. Filter Expenses By Category")
    print("5. Filter Expenses By Date Range")
    print("6. Show Total Amount You Spend")
    print("7. Exit")
    print('-' * 20)
    
    choice = input("Enter your choice (1-7): ").strip()
    
    if choice == '1':
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))
        description = input("Enter description: ").strip()
        addExpenses(category, amount, description)
        
    elif choice == '2':
        viewAllExpenses()
        
    elif choice == '3':
        date_inp = input("Enter date (YYYY-MM-DD): ").strip()
        filterExpenseByDate(date_inp)
        
    elif choice == '4':
        category_inp = input("Enter category: ").strip()
        filterExpenseByCategory(category_inp)
        
    elif choice == '5':
        first_date = input("Enter start date (YYYY-MM-DD): ").strip()
        last_date = input("Enter end date (YYYY-MM-DD): ").strip()
        filterExpenseByDateRange(first_date, last_date)
        
    elif choice == '6':
        total_spendings()
        
    elif choice == '7':
        print("Goodbye! 👋")
        break
        
    else:
        print("❌ Invalid choice. Please select between 1 and 7.")

    
    


    
    