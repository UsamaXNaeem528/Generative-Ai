"""
np.delete(arr, index, axis=None)
axis=None --> delete element from flattern or 1D array
"""

# delete element from 1D array
import numpy as np
arr = np.array([10,20,30,40,50])
new_arr = np.delete(arr, 2, axis=None)
print(new_arr)      # [10 20 40 50]

# delete element from 2D array
arr_2d = np.array([[2,4,6,8],
                  [1,3,5,7]])

arr_edit = np.delete(arr_2d, 1, axis=0)   # 1 means first row
print(arr_edit)  # [[2 4 6 8]]
