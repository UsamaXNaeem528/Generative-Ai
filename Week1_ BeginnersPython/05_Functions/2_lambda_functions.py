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


'''✅ Use in map(), filter(), and sorted()'''
'''🔸 Using with map()'''

nums = [1,3,5,7,9]
square = list(map(lambda x : x**2, nums)) #*maps the nums list to expression to find square.
print(square)


'''🔸 Using with filter()  ==> filter list, tuple, dictionaries elemens on specific condition'''
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


