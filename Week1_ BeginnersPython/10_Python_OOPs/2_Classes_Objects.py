class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no 
    
    def debit(self, amount):
        self.balance -= amount
        print(f'Rs.{amount} was debited')
        print(f'Remaining Balance : {self.balance}')
        
    def credit(self, amount):
        self.balance += amount
        print(f'Rs.{amount} was credited')
        print(f'Remaining Balance : {self.balance}')
        

acc1 = Account(50000, 12435)
acc1.debit(10000)
acc1.credit(10000)
acc1.debit(15000)



