"""
np.insert(array, index, value, axis=None)

array - jis array ma value insert karni ha.
index - postion
value - 
axis = 0 --> value inserted as row-wise
axis = 1 --> value inserte as column wise
(default)axis = None --> insert value in flatten way means in 1D row. [1,2,3,inserted value]
#! original array remains unchange, new arr will be created
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)

new_arr = np.insert(arr, 3, 100)
print(new_arr)