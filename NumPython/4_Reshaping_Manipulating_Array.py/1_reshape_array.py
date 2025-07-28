"""
The reshape function in NumPy is used to change the shape of an existing array without changing its data.
like 1D -> 2D, 1D -> 3D, also mutidimensional
🔹 The total number of elements must remain the same before and after reshaping.
"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])

reshape_Arr = arr.reshape(2,5)  #2rows, 5columns ==> condtion 2*5=10
print(reshape_Arr)

#* Imp : reshape() does not modify the original array.s
#* Instead, it returns a new view or copy with the specified shape.

