# insert value in 2D array
#! original array remains unchange, new arr will be created

import numpy as np

arr_2d = np.array([[1,2,3],
                  [4,5,6]])
print(arr_2d)

new_arr = np.insert(arr_2d, 1, [10, 20, 30],0)
print(new_arr)