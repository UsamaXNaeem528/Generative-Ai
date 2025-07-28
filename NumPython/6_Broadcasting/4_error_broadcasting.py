# error in broadcasting occurs when 
# 📌 Rule:
# 1D array ke elements ki count = 2D array ke columns (i.e., row ke elements) hone chahiye.

#! this code generate error
import numpy as np 

arr_1d = np.array([5,8])     #(2 elements only)
arr_2d = np.array([[1,2,3],[4,5,6]])  #(2,3)

new_arr = arr_1d + arr_2d
print(new_arr)

#! ValueError: operands could not be broadcast together with shapes (2,3) (2,) 