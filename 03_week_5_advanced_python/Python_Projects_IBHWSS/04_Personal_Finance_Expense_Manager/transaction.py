from datetime import datetime
import json
class Transaction:
    def __init__(self, username, amount, category, trans_type, description=None, date=None):
        self.username = username
        self.amount = amount
        self.category = category   #food, travel etc.
        self.trans_type = trans_type             #income or expense.
        self.description = description
        self.date_time = date if date else datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    def return_to_dict(self):
        return{
            "username": self.username,
            "amount" : self.amount,
            "category" : self.category,    
            "trans_type" : self.trans_type,
            "description" : self.description,
            "date" : self.date_time
        }
    
class TransactionManager:
    def __init__(self, file_path=r'03_week_5_advanced_python\Python_Projects_IBHWSS\04_Personal_Finance_Expense_Manager\transaction.json'):
        self.file_path = file_path
        self.transactions = self.load_all_transaction()
        
    def load_all_transaction(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []
    
    def save_all_transactions(self):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.transactions, file, indent=4)
        except:
            return []
    
    def add_new_transaction(self, username, amount, category, trans_type, description=None):
        new_transaction = Transaction(username, amount, category, trans_type, description)
        self.transactions.append(new_transaction.return_to_dict())
        self.save_all_transactions()
        print("New Transaction is added")
        return
    
    def load_user_transaction(self, username):
        user_trans = [t for t in self.transactions if t['username'] == username]
        if not user_trans:
            print("Not transaction found for user",username)
        
        print(f"\n📜 Transaction History for {username}:")
        print("-" * 50)
        for t in user_trans:
            print(f"{t['date']} | {t['trans_type'].upper()} | {t['category']} | ${t['amount']} | {t['description']}")
        print("-" * 50)
    
    def calculate_balance(self, username):
        '''balance = income - expenses'''
        income = sum([t['amount'] for t in self.transactions if t['username'] == username and t['trans_type'] == 'income'])
        expense = sum([t['amount'] for t in self.transactions if t['username'] == username and t['trans_type'] == 'expense'])
        print(income)
        print(expense)
        balance = income -  expense
        print(f"Remainig Balance for {username} | {balance}")

        if income == 0 and expense > 0:
            print("⚠️ No income recorded yet. All transactions are expenses.")
        elif balance < 0:
            print(f"⚠️ You are overspending! Current Balance: {balance}")
        else:
            print(f"💰 Current Balance: {balance}")
    
    def search_transactions(self, username, keyword):
        """Filter user transactions by category or description"""
        keyword = keyword.lower()
        found = [
            t for t in self.transactions
            if t["username"] == username and
               (keyword in t["category"].lower() or keyword in t["description"].lower())
        ]

        if not found:
            print(f"❌ No transactions found for keyword: {keyword}")
        else:
            print(f"\n🔍 Transactions matching '{keyword}':\n")
            print(f"{'-'*60}")
            for t in found:
                print(f"Category: {t['category']}")
                print(f"Type: {t['trans_type'].capitalize()}")
                print(f"Amount: {t['amount']}")
                print(f"Description: {t['description']}")
                print(f"Date: {t['date']}")
                print(f"{'-'*60}")

if __name__ == '__main__':
    trans = TransactionManager()
    # print(trans.load_all_transaction())
    # # trans.add_new_transaction('usama', '1500', 'food', 'expense','buying a new food')
    # # trans.load_user_transaction('usama')
    # trans.calculate_balance('usama')
    trans.add_new_transaction('john', '400', 'expense', 'petrol in bike')
    
    



    
    

        
        
    

        
        