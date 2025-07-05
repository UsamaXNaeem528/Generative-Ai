'''
🧠 Task:
Sort the employees by:
Department (alphabetically),
Then by salary (descending) within each department.
'''

employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    {'name': 'Bob', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 60000},
    {'name': 'David', 'department': 'Engineering', 'salary': 75000},
    {'name': 'Eve', 'department': 'Marketing', 'salary': 70000}
]

sorted_emp = sorted(employees, key=lambda x: (x['department'], -x['salary']))

for emp in sorted_emp:
    print(emp)