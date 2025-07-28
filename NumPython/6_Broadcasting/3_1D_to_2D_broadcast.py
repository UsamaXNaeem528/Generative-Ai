""" 1D array --> 2D array Broadcasting
📌 Rule:
1D array ke elements ki count = 2D array ke columns (i.e., row ke elements) hone chahiye.
"""
import numpy as np
arr_1d = np.array([2,3,4])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])


result = arr_1d + arr_2d
print(result)

