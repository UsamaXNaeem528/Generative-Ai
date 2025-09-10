########################################################################################
############################* DICTIONARIES IN PYTHON *##################################
########################################################################################
'''
Dictionaries are used to store data values in key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Dictionaries cannot have two items with the same key, key must be unique
'''
std_dict = {
    'name' : 'Usama',
    'grades' : 'A+',
    'phone_no' : '03481499528',
    'education' : 'BS ComputerScience'
}

'''🔹 1. Access Items Use the key to get the value.'''
print(std_dict['name'], std_dict['grades'])

#also same with using get() function
print(std_dict.get('phone_no'), std_dict.get('education'))


'''🔹 2. Change Items Update the value for a key.'''
std_dict['grades'] = 'B+'
print(std_dict)


'''🔹 3. Add Items Just assign a new key and value.'''
std_dict['profession'] = 'Gen Ai engineer'
print(std_dict)


'''🔹 4. Remove Items  it is possible in three ways using .pop() , del key word, 
clear-> delete all items in dictionary '''
# std_dict.pop("profession")
# del std_dict['profession'] 
# print(std_dict.clear())
# print(std_dict)

'''🔹 5. Loop Dictionaries Loop through keys, values and both keys, values'''
#* loop through keys
for key in std_dict:
    print(key)
    
#* loop through values of dictionary
for value in std_dict.values():
    print(value)

print("=== loop print key values ===")
#* loop through the both key values
for key, value in std_dict.items():
    print(f'{key} : {value}')
    
'''🔹 6. Copy Dictionaries'''
#! Don't use = (it links both) like dict2 = dict1 it target the same memory location(fake copy)
#* so use the .copy() function OR dict() constructor for real copying
car_dict = {
    'company' : 'Toyota',
    'model' : 'Supra',
    'color' : 'sport-green',
    'number' : 'LEQ-8230'
}
#coping
# new_car_dict = car_dict.copy()
            #OR
new_car_dict = dict(car_dict)
print(new_car_dict)


'''🔹 7. Nested Dictionaries A dictionary inside another dictionary.'''
students_records = {
    'std_1' : {'name':'usama_naeem',
               'roll_no':'fa21-164-bscs'},
    
    'std_2' : {'name':'ghaffir_ahmed',
               'roll_no':'fa21-165-bscs'}
}
print(students_records)


'''🔹 8. Dictionary Methods
| Method      | Description                       |
| ----------- | --------------------------------- |
| `.get(key)` | Returns value of specified key    |
| `.keys()`   | Returns a list of keys            |
| `.values()` | Returns a list of values          |
| `.items()`  | Returns key-value pairs as tuples |
| `.pop(key)` | Removes specified key             |
| `.update()` | Updates or adds multiple items    |
| `.clear()`  | Removes all items                 |
'''
students_records.pop('std_2')
print(students_records)
