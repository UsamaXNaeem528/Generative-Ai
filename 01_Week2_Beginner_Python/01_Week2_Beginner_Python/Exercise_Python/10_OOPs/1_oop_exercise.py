class employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(f'ID : {self.id}\nName : {self.name} ')

#Creating a emp instance of Employee class
emp1 = employee(22, 'Usama')
emp1.display()

#deleting the property of object
del emp1.id

try:
    print(f'Employe Id : {emp1.id}')
except NameError:
    print("emp1 is not defined")
except AttributeError:
    print("emp1 does not have an 'id' attribute")


#deleting whole object
del emp1
try:
    emp1.display()
except NameError:
    print(f'emp1 is note defined')
    
