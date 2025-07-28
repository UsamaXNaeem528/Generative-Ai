import numpy as np

# using ndim we can check the dimension of array
arr_1d = np.array([10,20,30])
arr_2d = np.array([[40,50,60], [65,70,75]])
arr_3d = np.array([
                   [[1,2,3],[4,5,6]],           
                   [[7,8,9],[10,11,12]],
                ])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)


