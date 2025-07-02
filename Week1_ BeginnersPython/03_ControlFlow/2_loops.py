'''🔸 2. Loops (Repeat Tasks)'''
''' ✅ for loop used when you know how many times to loop.'''

for i in range(5):
    print(i)

print("=============================")
#! OR define range --> range(staring index, stopping index)

for i in range(12,24):
    print(i)
    
print("=============================")

#* Print a List using for loop
loop_list = ["forloop", "whileLoop", "DoWhileLoop", "ForeachLoop"]

for y in loop_list:
    print(y)    
    
print("=============================")

'''✅ while loop - used when the end condition is unknown.'''
#* using while loop i have to print the counting from 50 to 100 and ignore to print the 75 

count = 50
while(count<=100):
    if(count == 75):
        count += 1
    print(count)
    count += 1
    
'''🔸 3. Loop Control Keywords'''
'''
| Keyword    | Use                        |
| ---------- | -------------------------- |
| `break`    | Exit the loop immediately  |
| `continue` | Skip to the next iteration |
| `pass`     | Do nothing (placeholder)   |
'''

'''Task is that take 10 students marks from user and print such students marks having marks is greater than
or equal to 80 marks in list form '''
students_grades = []
for x in range(1,11):
    marks = int(input(f' Enter {x} student marks : '))
    students_grades.append(marks)

new_std_grades = []
for y in students_grades:
    if(y>=80):
        new_std_grades.append(y)     

print(new_std_grades)

    





