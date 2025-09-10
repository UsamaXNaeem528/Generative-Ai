import json
import time

#===================File handling Part=====================#
tasks = []
#loading a json file
file_path = r'2_ToDo_App\tasks.json'
try:
    with open(file_path, 'r', encoding='utf-8') as j_file:
        tasks = json.load(j_file)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    tasks = []

#===================Time Part===============================#

local_time_struct = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",local_time_struct)

#===================Main Functions==========================#
#add a task
def add_task(task):
    task_no = len(tasks) + 1
    new_task = {"task_number" : task_no, "title":task, "done":False, "time": formatted_time}
    tasks.append(new_task)
    save_tasks()
    print(f'Your Task  {task_no}  is saved ✅')

#update task
def update_task(task_num, title):
    for task in tasks:
        if task['task_number'] == task_num:
            if task['title'] == title or title == "":
                task['title'] = task['title']
                task['done'] =  task['done']
                task['time'] = task['time']
                print(f'Nothing to update in task {task_num} ')
                break
            else:
                task['title'] = title
                task['done'] = False
                task['time'] = formatted_time
                save_tasks()
                print(f'Task {task_num} is Updated')
                break
    else:
            print("Invalid Task Number")

#delete a task
def delete_task(task_num):
    task_num -= 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        task_num +=1
        print(f"Task no {task_num} is deleted")
        save_tasks()
    else:
        print("Invalid Task Number ❌")

#display a task
def show_tasks():
    if len(tasks) == 0:
        print("Tasks List Is Empty")
    else:
        print('-' * 40)
        print("\t\tTasks List\t")
        print('-' * 40)
        for i,task in enumerate(tasks):
            i += 1
            if(task['done'] == False):
                print(f'Task {task['task_number']}')
                print(f'Details : {task['title']}')
                print(f'Time : {task['time']}')
                print('Status : Not complete ❌')
                print('-' * 20)
            else:
                print(f'Task {task['task_number']}')
                print(f'Details : {task['title']}')
                print(f'Status : Completed ✅ at {task['time']}')
                print('-' * 20)

#mark done as task
def mark_asdone(task_num):
    found = False
    for task in tasks:
        if task['task_number'] == task_num:
            found = True
            if(task['done'] == True):
                print("You already Complete this Task")
                break
            else:
                task['done'] = True
                task['time'] = formatted_time
                save_tasks()
            print(f"Task no {task_num} is marked as Done ✅")
    if not found:
        print("Invalid Task Number ❌")

def search_task_by_task_no(task_num):
    found = False
    for task in tasks:
        if task['task_number'] == task_num:
            found = True
            print(f'Task {task['task_number']}')
            print(f'Details : {task['title']}')
            print(f'Time : {task['time']}')
            print('Status : Not complete ❌')
    if not found:
        print("No task Exist ⚠️")
            
#save a task
def save_tasks():
    with open(file_path, 'w',encoding='utf-8') as j_file:
        json.dump(tasks, j_file, indent=4)


print("Welcome to To-Do List CLI App")
print("1. Add Task")
print("2. Show All Tasks")
print("3. Update Task")
print("4. Delete Task")
print("5. Mark Task as Done")
print("6. Search Task By Task No.")
print("7. Exit")

choice = ''
while choice != '6':
    choice = input("Enter your choice: ")

    if choice == '1':
        task_title = input("Enter task description: ")
        if task_title.strip() != "":
            add_task(task_title)
        else:
            print("❌ Task cannot be empty.")

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        try:
            task_num = int(input("Enter task number to update: "))
            new_title = input("Enter new task description (leave blank to keep same): ")
            update_task(task_num, new_title)
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == '4':
        try:
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == '5':
        try:
            task_num = int(input("Enter task number to mark as done: "))
            mark_asdone(task_num)
        except ValueError:
            print("❌ Please enter a valid number.")
    
    elif choice == '6':
        try:
            task_num = int(input("Enter task number you want to search: "))
            search_task_by_task_no(task_num)
        except ValueError:
            print("❌ Please enter a valid number.")
            
    elif choice == '7':
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please enter 1-6.")

