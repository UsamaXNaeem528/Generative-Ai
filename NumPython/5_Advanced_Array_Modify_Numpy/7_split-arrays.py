"""
Array splitting in NumPy means dividing a single array into multiple sub-arrays, along a specified axis.
np.split(arr, value to be split equally) -> equally divided

np.vplit()
np.hsplit()
"""

import numpy as np
arr = np.array([10,20,30,40,50,60])

print(np.split(arr, 3))

#=======================
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(np.hsplit(arr, 2))  # Split into 2 by columns
print(np.vsplit(arr, 3))  # Split into 2 by rows



