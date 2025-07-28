"""
ravel() and flaten() both used to convert the multi-dimensional(3D->1D) arrays into 1D array.
but the difference in both->
ravel -> return the view of means change the original array
flaten -> return the copy of array
"""
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_2d.ravel())
print(arr_2d.flatten())


