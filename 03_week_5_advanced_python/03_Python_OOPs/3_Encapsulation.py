## Enapsulation: Hiding internal details of an object (private variables)
# | Modifier  | How it works                                         | Example         |
# | --------- | ---------------------------------------------------- | --------------- |
# | Public    | Accessible anywhere                                  | `self.brand`    |
# | Protected | Accessible in class & subclasses (single underscore) | `self._speed`   |
# | Private   | Accessible only inside class (double underscore)     | `self.__engine` |

#=============== Deleting an class object or instance ======================#
class Vehicle:
    def __init__(self, name, color):
      self.name = name
      self.color = color
      

obj1 = Vehicle('BMW', 'black')
print(obj1.name, obj1.color)

del obj1
print(obj1.name, obj1.color)  #this will give an error becasue object is deleted

#============Private atrrbiutes and methods of class=======================#
# we can use the private attributes inside the class like in another function inside the but not the inside
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance      #private member
        
    def deposit(self, amount):
        print(f'Rs. {amount} is deposit')
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance == 0:
            print("Current Account balacne is 0")
        elif self.__balance<amount:
            print(f'Insufficient amount to withdrawl current balance is  Rs.{self.__balance}')
        else:
            print(f'Rs. {amount} is withdrwal')
            self.__balance -= amount
            
    def get_balance(self):
        print(f'Current Account Balance : {self.__balance}')
    
    def display_info(self):
        print("Account Holder Name : ",self.owner)
        print("Current Account Balanace : ",self.__balance)
    
acc1 = BankAccount('usama',100)
#acc1.__balance    #getting error because __balance is private attribute.
acc1.display_info()
# acc1.deposit(50)
# acc1.get_balance()
# acc1.withdraw(100)
# acc1.get_balance()





    




