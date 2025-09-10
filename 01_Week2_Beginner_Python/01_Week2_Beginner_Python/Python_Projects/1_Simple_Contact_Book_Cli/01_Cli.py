#✅ Step 1: Project Structure aur Target Sochna
#Let’s break it into small ABC-type steps:
#🎯 Target:
#Contact ka naam aur number store karna
#Contact list dikhana
#Contact delete karna

import json
file_path = r'1_Simple_Contact_Book_Cli\contacts.json'

contacts = []
# loading a contacts from a json file in contacts list
with open(file_path, 'r', encoding='utf-8') as json_file:
    contacts = json.load(json_file)

def add_contact(name, number):
    new_contact = {"name": name, "number":number}
    for contact in contacts:
        if number == contact['number']:         #check contact already exist with number
            print(f"Contact with this name {contact['name']} already exist\nNumber must be unique")
            break
    else:
        contacts.append(new_contact)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(contacts, json_file, indent=4)
        print("Contact is added ✅")

def show_contact():
    print(f'Total Contacts {len(contacts)}')
    if(len(contacts) == 0):
        print("Contact Book is empty No Such Contact to display")
    else:
        for contact in contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone no : {contact['number']}")
            print('-'* 20)
        
def delete_contact(number):
    for contact in contacts:
        if number == contact['number']:
           contacts.remove(contact)
           print(f'Contact with number {number} is deleted 🗑️.')
           with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(contacts, json_file, indent=4)
           break
    else:
        print("No such contact exist with this number")

def search_contact_byName(name):
    retrieved_contacts = []
    for contact in contacts:
        if name.lower() == contact['name'].lower():
            retrieved_contacts.append({'name' : contact['name'], 'number' : contact['number']})
    if(len(retrieved_contacts) == 0):
        print("No such contacts exist with this number")
    else:
        for contact in retrieved_contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone no : {contact['number']}")
            print('-'* 20)

def update_contact(old_name, new_name, old_number, updated_number):
    for contact in contacts:
        if old_name == contact['name'] and old_number == contact['number']:
            contact['name'] = new_name
            contact['number'] = updated_number
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(contacts, json_file, indent=4)
            print("✅ Contact Updated")

choice = ''
while(choice != '6'):
    print("\nWelcome to Contact Book")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Delete Contact")
    print("4. Search Contacts By Name")
    print("5. Update Contact")
    print("6. Exit")
    choice = str(input("Enter Your Choice for Contact Book : "))
    if choice == '1':
        name = str(input("Enter the name : "))
        number = str(input("Enter the phone number : "))
        if(number.isdigit() and len(number) == 11):
            add_contact(name, number)
        else:
            print("Number must be in digit and 11 in lenght")
    
    elif choice == '2':
        show_contact()
    
    elif choice == '3':
        number = str(input("Enter contact number you want to delete : "))
        delete_contact(number)
    
    elif choice == '4':
        name = str(input("Enter name of Contact : "))
        search_contact_byName(name)
    
    elif choice == '5':
        # Get input for old contact details
        old_name = input("Enter the OLD name of the contact you want to update: ")
        old_number = input("Enter the OLD number of the contact you want to update: ")
        # Get input for new contact details (can be left blank if no change)
        new_name = input("Enter the NEW name for the contact : ")
        updated_number = input("Enter the UPDATED number for the contact : ")
        update_contact(old_name, new_name, old_number, updated_number)
    
    elif choice == '6':
        print("Goodbye! 👋 Your contacts have been saved.")
    else:
        print("Choose and enter the correct options")   

     



