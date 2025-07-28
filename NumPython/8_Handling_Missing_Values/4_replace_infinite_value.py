import numpy as np
arr = np.array([2, 4, np.inf, 6, 8, -np.inf])
print(np.isinf(arr))  

fresh_arr = np.nan_to_num(arr, posinf=100, neginf=100)
print(fresh_arr)