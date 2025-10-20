import json
import os
from datetime import datetime
from transaction import TransactionManager

class BudgetManager:
    def __init__(self, file_path=r"C:\Users\Admin\OneDrive\Desktop\Python Projects\04_Personal_Finance_Expense_Manager\budget.json"):
        self.file_path = file_path
        self.budgets = self.load_budgets()

    def load_budgets(self):
        """Load all budgets from file."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_budgets(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.budgets, file, indent=4)

    def set_budget(self, username, category, amount, period="monthly"):
        for b in self.budgets:           # check if budget already exist then update
           if b['username'] == username and b['category'] == category and b['period'] == period:
               b['amount'] = amount
               b['created_at'] = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
               self.save_budgets()
               print("Budget already exist! Amount Updated successfully")
               return
           
        # if budget not exist then create a new budget in form of dict
        new_buget = {
            "username": username,
            "category" : category,
            "amount" : amount,
            "period" : period,
            "created_at" : datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }

        self.budgets.append(new_buget)
        self.save_budgets()
        print(f'Budget {category} = {amount} is added!')
        
    def check_budget(self, username, category, period='monthly'):
        budget_amount = 0
        for b in self.budgets:
            if b['username'] == username and b['category'] == category and b['period'] == period:  #if budget exist then get budget amount
                budget_amount = b['amount']
                break
        
        if not budget_amount:           # in not then stop function
            return

        total_expense = 0
        current_month = datetime.now().month
        all_trans = TransactionManager()
        transactions = all_trans.load_all_transaction()
        
        for t in transactions:          # check the all amount spend for specific category expense and add them.
            t_date = datetime.strptime(t["date"], '%Y-%m-%d %H-%M-%S')
            if t['username'] == username and t['category'] == category and t['trans_type'] == 'expense' and t_date.month == current_month:
                total_expense += t['amount']
        
        if budget_amount < total_expense:
            print(f"⚠️ Budget exceeded for {category}! Spent: {total_expense} / Budget: {budget_amount}")
        else:
            print(f"✅ {category} expenses within budget. Spent: {total_expense} / Budget: {budget_amount}")

        
if __name__ == '__main__':
    # Initialize BudgetManager
    budget_manager = BudgetManager()

    # Set a new budget
    # budget_manager.set_budget('usamanaeem', 'petrol', 3000)

    # transactions = [
    #     {"username": "usamanaeem", "amount": 1000, "category": "petrol", "type": "expense", "date": "2025-10-9 12:00:00"},
    #     {"username": "usamanaeem", "amount": 500, "category": "petrol", "type": "expense", "date": "2025-10-15 12:00:00"},
    # ]

    # Check budget
    budget_manager.check_budget('usamanaeem', 'petrol')
