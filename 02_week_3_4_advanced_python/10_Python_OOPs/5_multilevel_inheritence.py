# MultiLevel Inhertitance
# One Parent Class can derived many child classes and these child classes inherit the properties of previous parent classes
# Person → Employee → Developer

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        print(f'Person name : {self.name}\nPerson Age : {self.age}')
        
class Employee(Person):
    def __init__(self, emp_id):
        self.emp_id = emp_id
    
    def display_emp_info(self):
        self.display_person_info()
        print(f'Employee ID : {self.emp_id}')
        
class Developer(Employee):
    def __init__(self, programming_language):
        self.programming_language = programming_language
        
    def display_develpor_info(self):
        self.display_emp_info()
        print(f'Programming Language : {self.programming_language}')

obj1 = Developer('Python')      
obj1.name = 'Usama'
obj1.age = 23
obj1.emp_id = '001'
obj1.display_develpor_info()
    
        
        
        
