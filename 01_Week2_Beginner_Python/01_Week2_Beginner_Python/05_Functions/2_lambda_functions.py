'''
⚡ Lambda Functions
🔹 What is a Lambda Function?
A lambda function is a small anonymous function with no name, written in one line.
Syntax:
lambda arguments: expression
'''

'''✅ Example:'''
cube = lambda x : x**3
print(cube(5))


'''✅ Lambda with Multiple Arguments'''
mul = lambda a, b : a * b 
print(mul(2,3))


#⚡ Map Function
#🔹 map() in Python is used to apply a function to every item of an iterable (like a list, tuple, set, etc.).
# It transforms data item-by-item. 
# map functions used the built in functions, or can be use user defined functions

'''✅ Use in map(), filter(), and sorted()'''
'''🔸 Using with map()'''

nums = [1,3,5,7,9]
square = list(map(lambda x : x**2, nums)) #*maps the nums list to expression to find square. 
print(square)

'''🔸 Using with filter()  ==> filter list, tuple, dictionaries elements on specific condition'''
'''like filtering a odd number from a tuples of natural numbers'''

natural_nums = (1,2,3,4,5,6,7,8,10,11,12,13,14,15)
odd_nums = tuple(filter(lambda x : x % 2 != 0, natural_nums))
print(odd_nums)   #* (1, 3, 5, 7, 11, 13, 15)




'''
🆚 Regular Function vs Lambda
| Feature        | Regular Function | Lambda Function        |
| -------------- | ---------------- | ---------------------- |
| Syntax         | `def my_func():` | `lambda x: x + 1`      |
| Name required? | Yes              | No (can be anonymous)  |
| Multi-line?    | Yes              | ❌ No (only one line)  |
| Return keyword | Required         | Implicit (no `return`) |
'''

'''Sorted Function
sorted(iterable, key=None, reverse=False)
'''

students = [
    {'name': 'John', 'age': 20, 'grade': 85},
    {'name': 'Alice', 'age': 22, 'grade': 90},
    {'name': 'Bob', 'age': 20, 'grade': 85},
    {'name': 'Charlie', 'age': 21, 'grade': 90},
    {'name': 'David', 'age': 19,'grade':80}
]

sorted_std = sorted(students, key=lambda x:(-x['grade'], x['age'], x['name']))
for x in sorted_std:
    print(x)

       
'''working
🔹 lambda x: (-x['grade'], x['age'], x['name'])

This tells Python how to prioritize sorting:
-x['grade']: Sort by grade descending (higher grades come first).
x['age']: If grades are the same, sort by age ascending (younger students first).
x['name']: If grade and age are same, sort alphabetically by name.
'''
