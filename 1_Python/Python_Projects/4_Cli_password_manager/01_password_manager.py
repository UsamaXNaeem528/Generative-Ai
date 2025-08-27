"""
🎯 Goals:
Save website login credentials (website, username, password)
View saved credentials
Search credentials by website name
Delete credentials
Secure with a master password
Store everything in a JSON file
"""

#Master Password

master_pass = '@admin123'
entered_pass = str(input("Enter Master Password Key : "))
if(master_pass != entered_pass):
    print("Access Denied ❌")
    exit()    
    
credentials = []
import json
import re

file_path = r'4_Cli_password_manager\credentials.json'

try:
    with open(file_path, 'r', encoding='utf-8') as j_file:
        credentials = json.load(j_file)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    credentials = []


def save_credentials(website, username, password):
    new_credentials = {'website': website, 'username': username, 'password': password}
    
    # validation checks
    if not website.strip():
        print("❌ Website name cannot be empty")
        return
    elif '.' not in website:
        print("❌ Website name must contain a dot (e.g., google.com)")
        return
        
    if not username.strip():
        print("❌ Username cannot be empty")
        return
    
    if len(password) < 8:
        print("❌ Password length must be at least 8 characters")
        return
    elif not re.search(r"[A-Z]", password):
        print("❌ Password must contain at least one uppercase letter")
        return
    elif not re.search(r"[a-z]", password):
        print("❌ Password must contain at least one lowercase letter")
        return
    elif not re.search(r"[0-9]", password):
        print("❌ Password must contain at least one number")
        return
    elif not re.search(r"[\W_]", password):
        print("❌ Password must contain at least one special character")
        return
    
    # duplicate entry check
    for cred in credentials:
        if cred['username'] == username and cred['website'] == website:
            print("⚠️ Credential already exists for this website and username!")
            return
    
    credentials.append(new_credentials)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(credentials, file, indent=4)
        print("✅ Credentials Saved Successfully")

def viewSavedCredentials():
    for cred in credentials:
        print(cred['website'])
        print(cred['username'])
        print(cred['password'])
        print('-' * 20)

def searchCredByWeb(website):
    for cred in credentials:
        if(cred['website'] == website):
            print(cred['website'])
            print(cred['username'])
            print(cred['password'])
            break
    else:
        print("No Such website exist with this name")

def deleteCredentialsbyUsername(username):
    for cred in credentials:
        if username == cred['username']:
            credentials.remove(cred)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(credentials, file, indent=4)
                print("Credentials deleted")
                return
    else:
        print("No such credentials exist with this username")
            
while True:
    print("\n📌 Password Manager Menu")
    print("1. Save New Credentials")
    print("2. View All Credentials")
    print("3. Search Credentials by Website")
    print("4. Delete Credentials by Username")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        website = input("Enter Website: ").strip()
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        save_credentials(website, username, password)

    elif choice == '2':
        viewSavedCredentials()

    elif choice == '3':
        website = input("Enter Website to Search: ").strip()
        searchCredByWeb(website)

    elif choice == '4':
        username = input("Enter Username to Delete: ").strip()
        deleteCredentialsbyUsername(username)

    elif choice == '5':
        print("Exiting Password Manager. Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please select from 1 to 5.")

            
        
    
        
    



