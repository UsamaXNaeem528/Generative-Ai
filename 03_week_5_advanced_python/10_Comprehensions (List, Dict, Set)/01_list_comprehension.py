# List Comprehensions Practice Questions

#1. Squares of Numbers:
# Generate a list of squares for numbers from 1 to 10 using a list comprehension.
# num = [num**2 for num in range(1,11)]
# print(num)


#2. Filter Even Numbers:
# From a list of integers [1, 4, 7, 10, 13, 16],
# create a new list containing only the even numbers using list comprehension.
# num_list = [1,4,7,10,13,16]
# even_list = [num for num in num_list if num%2==0]
# print(even_list)


# Flatten a List of Lists:
# Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# use a list comprehension to flatten it into a single list [1, 2, 3, 4, 5, 6, 7, 8, 9].
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# flat_list = []
# flat_list = [num for row in matrix for num in row]
# print(flat_list)


# Extract First Letters:
# Given a list of words ['apple', 'banana', 'cherry'],
# create a list of their first letters using a list comprehension.
# fruits = ['apple','banana', 'cherry']
# first_letter = [f[0] for f in fruits]
# print(first_letter)


## Conditional Transformation:
# Given a list of numbers [1, 2, 3, 4, 5],
# create a new list where numbers divisible by 2 are doubled and others remain the same.

nums_list = [1,2,3,4,5]
filter_list = [num*2 if num%2==0 else num for num in nums_list]
print(filter_list)