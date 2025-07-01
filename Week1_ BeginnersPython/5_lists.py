########################################################################################
############################* LISTS IN PYTHON *#########################################
########################################################################################

'''
🔹 1. What is a List?
A list is an ordered, changeable (mutable) collection of items.
Lists can hold any type of data: numbers, strings, other lists, etc.
List allow duplicate elements
'''
fruits = ["apple", "mango", "banana"]
print(fruits)


'''🔹 2. Creating a List'''
#List of integers
numbers = [1,2,3,4,5,6,7,7]
print(numbers)


#List of mixed data types
mix_list = [1, "Usama", bool, "Lahore", "World War I"]


#Empty List
empty_list = []
print(empty_list)


'''🔹 3. Accessing Elements (Indexing). Indexing starts at 0. Negative indexing starts from the end.'''
fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes",
    "Pineapple",
    "Strawberry",
    "Papaya",
    "Watermelon",
    "Kiwi"
]
print(fruits[3])
print(fruits[-4])


''' 🔹 4. Modifying List Items '''
cars_list = ['Toyota', 'Mercedes', 'BMW', 'Tesla']
cars_list[3] = 'Ford'
print(cars_list)


'''🔹 5. Slicing Lists (getting some elements of LIST)'''
print(fruits[0:5])   


'''🔹 6. List Methods (Important 🔥)
| Method          | Description                         | Example                    |
| --------------- | ----------------------------------- | -------------------------- |
| `.append(x)`    | Add item at the end                 | `fruits.append("kiwi")`    |
| `.insert(i, x)` | Insert at position `i`              | `fruits.insert(1, "pear")` |
| `.remove(x)`    | Remove first occurrence of `x`      | `fruits.remove("apple")`   |
| `.pop(i)`       | Remove and return item at index `i` | `fruits.pop(2)`            |
| `.index(x)`     | Find index of value                 | `fruits.index("banana")`   |
| `.count(x)`     | Count occurrences                   | `fruits.count("apple")`    |
| `.reverse()`    | Reverse the list                    | `fruits.reverse()`         |
| `.sort()`       | Sort in ascending order             | `numbers.sort()`           |
| `.clear()`      | Remove all elements                 | `fruits.clear()`           |
'''


'''🔹 7. Looping Through a List'''
for x in fruits:
    print(x)
    
    
'''🔹 8. Check if Item Exists'''
if 'Banana' in fruits:
    print("Banana Exist in fruits list")
    
    
'''🔹 9. List Length'''
print(len(fruits))


'''🔹 10. List Comprehension (Advanced but powerful)
A short way to create or modify lists.'''
nums = [x*x for x in range(1,10)]
print(nums)


'''🔹 11. Nested Lists (List inside List)'''
matrix = [
    [1,2],      #* 0 row
    [3,4],      #* 1 row
    [4,5]       #* 2 row
         ]

print(matrix[1][0])  #* 1 row ka 0 index --> 3


'''🔹 12. List Sorting in Python'''
this_list = ['a','b','c','d','g','e','k','l']
this_list.sort()
print(this_list)    #* this will sort the list alphabetically

numbers_list = [10,44,0,94,22,85]
numbers_list.sort()
print(numbers_list)     #* this will sort the list numerically

mixed_letter_list = ['a','c','5','e','9','f','10','h','n']
mixed_letter_list.sort()
print(mixed_letter_list)


'''🔹 12. List Copying in Python'''
#means copy the list into another variable

list_for_copy = ['Usama','Naeem','GenAi','LLM']
copied_list = list_for_copy.copy()
    # OR using list constructor
# copied_list = list(list_for_copy)  
print(copied_list) 


'''🔹 12. Join or concatenate a lists in Python'''
list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11,12,14]

concatenated_list = list1 + list2
print(concatenated_list)
# print(type(concatenated_list))













