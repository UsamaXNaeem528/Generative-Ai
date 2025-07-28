"""
The np.concatenate() function is used to join two or more arrays along an existing axis (not a new one).

np.concatenate((array1, array2, ...), axis=0)

arrays: A sequence (e.g., tuple or list) of arrays to be joined.
All arrays must have the same shape except in the dimension corresponding to axis.

axis: The axis along which the arrays will be joined.

axis=0: join vertically (rows)

axis=1: join horizontally (columns)

Default is axis=0
"""

# 1. 1D Example – Join two arrays
import numpy as np
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
new_arr = np.concatenate((arr_1,arr_2))
print(new_arr)


# 2D Example – Axis 0 (stack rows)
import numpy as np

arr_one = np.array([[1,2],[3,4]])
arr_two = np.array([[5,7],[6,8]])         
new_arr1 = np.concatenate((arr_one,arr_two), axis=0)   
print(new_arr1)

# 2D Example – Axis 1 (stack colums)
arr_one = np.array([[1,2],[3,4]])
arr_two = np.array([[5,7],[6,8]])         
new_arr1 = np.concatenate((arr_one,arr_two), axis=1)   
print(new_arr1)












