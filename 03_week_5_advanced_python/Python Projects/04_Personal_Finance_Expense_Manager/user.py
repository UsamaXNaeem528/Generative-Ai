import json
import os
from datetime import datetime

class User:
    '''Represent a single entity'''
    def __init__(self, username, password, created_at=None):
        self.username = username
        self.password = password
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    def return_to_dict(self):
        '''Function for store the user signIn/SignUp info in form of dictionary'''    
        return{
            "username" : self.username,
            "password" : self.password,
            "created_at" : self.created_at
        }

class UserManager:
    '''This class handle user creation, login and save it into the file'''
    # file_path = r'03_week_5_advanced_python\Python_Projects_IBHWSS\04_Personal_Finance_Expense_Manager\datastore.json'
    def __init__(self, file_path=r'C:\Users\Admin\OneDrive\Desktop\Python Projects\04_Personal_Finance_Expense_Manager\user.json'):
        self.file_path = file_path
        self.users = self.load_all_users()     #its a dictionary in json file
     
    def load_all_users(self):
        if not os.path.exists(self.file_path):
            return []
        else:
            try: 
                with open(self.file_path, 'r', encoding='utf-8') as json_file:
                    return json.load(json_file)
            except json.JSONDecodeError:
                return []
    
    def save_all_users(self):
        '''Save all users into file'''
        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.users, json_file, indent=4)

    def create_user(self, username, password):
        for user in self.users:     # first check user alread exist or not
            if user['username'] == username:
                print("This UserName already exist, Try another one")
                return
            
        #if not create a new user
        new_user = User(username, password)
        self.users.append(new_user.return_to_dict())
        self.save_all_users()
        print(f"✅ Account created successfully for {username}!")
        return new_user

    def login_user(self, username, password):
        found = False
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                found = True
                # print(f'Welcome Back user "{user['username']}"')
                return True
        
        if not found:
            print("Invalid Username and password")
            return None
        
if __name__ == '__main__':
    user = UserManager()
    user.create_user('Harry','harry123')
    print(user.load_all_users())


            
                    
        
        
        
    
