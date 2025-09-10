'''
🧺 Python Sets
Written using curly braces {}

Duplicates are not allowed

Unordered (no indexing)

Can contain different data types
'''
'''✅ Creating a Set:'''
my_set = {1, 2, 3, 4}

# You can also use the set() constructor:
prime_no_set = set([1, 3, 5, 7, 9, 13])
print(prime_no_set)

'''🔸 Properties of Sets'''
# | Property      | Set Behavior                 |
# | ------------- | ---------------------------- |
# | No duplicates | `{1, 2, 2, 3}` → `{1, 2, 3}` |
# | No indexing   | You **can't** do `my_set[0]` |
# | Mutable       | You can add/remove elements  |
# | Iterable      | You can loop through it      |

'''🔹 1. Add Items to a Set'''
my_set.add(5)
print(my_set)

'''🔹 2. Update Set (Add multiple items)'''
my_set.update([6, 7, 8, 9, 10])
print(my_set)

'''🔹 3. Remove Items
| Method      | Behavior                            |
| ----------- | ----------------------------------- |
| `remove()`  | Removes item, error if not found    |
| `discard()` | Removes item, no error if not found |
| `pop()`     | Removes a random item               |
| `clear()`   | Removes all items                   |
'''

my_set.remove(5)   #* remove one item from set.
# print(my_set)


'''🔹 4. Looping Through a Set'''
for item in my_set:
    print(item)
    
    
#! set are immutable though the index, can access it using index but it poosible using list                                                                                                                                                                   
fruits_set = {'apple', 'banana', 'orange', 'kiwi'}
temp = list(fruits_set)
temp[2] = 'grapes'
fruits_set = set(temp)
print(fruits_set)







