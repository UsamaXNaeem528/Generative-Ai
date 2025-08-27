'''
📦 What is a Tuple in Python?
A tuple is like a list, but:
✅ Ordered
🚫 Immutable (cannot be changed after creation)
✅ Can contain mixed data types
✅ Allows duplicates
Syntax
variable = (element1, element2, element3)
'''
fruitsTuple = ('apple','cherry','banana')
print(fruitsTuple)

'''🔹 1. Access Tuples (Indexing & Slicing)'''
studentsTuple = ('Harry','John', 'Dal', 'Michal', 'William', 'Lilly')
print(studentsTuple[3])
print(studentsTuple[0:5])
print(studentsTuple[-4:])

'''🔹 2. Update Tuples ❌ (Not directly allowed)'''
#Tuples are immutable.
#but it can be change using list constructor and tuple constructor 
x = ("This", "is", "the", "tuple")
tupleList = list(x)
tupleList.insert(3,'python')  
x = tuple(tupleList)
print(x)

'''🔹 3. Unpack Tuples'''
#Split tuple items into variables:
computerScince = ['Artificial Intelligence', 'Machine Learning', 'WebDevelopment']
a, b, c = computerScince
print(a)
print(b)
print(c)

'''🔹 4. Loop Tuples'''
loop_tuple = ['for_loop', 'while_loop', 'do_while_loop']
for x in loop_tuple:
    print(x)

'''🔹 5. Join Tuples'''
tuple_1st = ("Pakistan", "Zindabad")
tuple_2nd = ("Zindadilane", "Lahore")
tuples_joined = tuple_1st + tuple_2nd
print(f'Joined Tuples {tuples_joined}')

'''🔹 6. Tuple Methods'''
'''
| Method      | Description                       |
| ----------- | --------------------------------- |
| `.count(x)` | Count how many times `x` appears  |
| `.index(x)` | Return the index of the first `x` |
'''

numbers = (0,3,4,8,1,4,9,9,5,2,8)
print(numbers.count(4))
print(numbers.index(9))

'''🧠 Tuple Challenge'''
data = ("Usama", 23, "Python", "Python", 6.2, True)
'''
✅ Your Tasks:
Print your name from the tuple.
Count how many times "Python" appears.
Get the index of the float value.
Loop through the tuple and print each item.
Try to update "Usama" to "Ali" (using the correct method).
Join it with this tuple: extra = ("AI", "Developer")
🧪 Bonus:
Unpack this new tuple after joining into 4 variables (first, second, *middle, last)
'''
print(data[0])

print(data.count('Python'))

print(data.index(6.2))

for x in data:
    print(x)
    
updateTuple = list(data)
updateTuple[0] = "Ali"
data = tuple(updateTuple)
print(data)

extra = ("AI", "Developer")
new_tuple = data + extra
print(new_tuple)

#unpacking new Tuple
print("UnPacking Tuple")
first,second, *middle, last = new_tuple           #*middle --> is a list 
for x in first, second, middle, last:
    print(x)











 


