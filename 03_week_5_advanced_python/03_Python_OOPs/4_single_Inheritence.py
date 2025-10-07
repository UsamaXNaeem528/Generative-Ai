# Single Level Inheritence "Parent Class has one only one derived class"
class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
    
    def display_info(self):
        print(f'Employee Name : {self.emp_name}\nEmployee ID : {self.emp_id}')

class Manager(Employee):
    def __init__(self, mang_name, mang_id, mang_dept):
        self.mang_name = mang_name
        self.mang_id = mang_id
        self.mang_dept = mang_dept
    
    def display_manager_info(self):
        print(f'Manager Name : {self.mang_name}\nManager ID : {self.mang_id}\nManger Department : {self.mang_dept}')
        
obj1 = Manager("Naeem",30,'Human Resource')
obj1.emp_id = 12
obj1.emp_name = "Usama"
obj1.display_info()
obj1.display_manager_info()





        
        
    
        