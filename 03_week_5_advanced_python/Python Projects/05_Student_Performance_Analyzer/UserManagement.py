#UserManagement.py
from DataManager import Data
from datetime import datetime

class UserManager:
    def __init__(self, file_path=r'03_week_5_advanced_python\Python Projects\05_Student_Performance_Analyzer\teacher_users.json'):
        self.file_path = file_path
        self.data_obj = Data(self.file_path)
        self.users = self.data_obj.load_all_data()

    def login_teacher(self, teacherUsername, password):
        # print(teacherUsername, password)
        for u in self.users:
            if u['teacher_username'] == teacherUsername and u['password'] == password:
                print("User Successfully Login!")
                return True
        print("❌ Invalid Username And Password !")
        return False
    
    def create_teacher_acc(self, teacherUsername, password, phoneNo):
        for u in self.users:
            if u['teacher_username'] == teacherUsername:
                print("User with this name already exist! , Try Unique name.")
                return
            
        new_user = {
            "teacher_username" : teacherUsername,
            "password" : password,
            "phone_no" : phoneNo,
            "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }
        
        self.users.append(new_user)
        self.data_obj.save_all_data(self.users)
        
if __name__ == '__main__':
    u1 = UserManager()
    u1.login_teacher('adil_a','pass_adil')
    # u1.create_teacher_acc('John','john123', '0341323')
    # u1.create_teacher_acc('jb','john123', '0341323')