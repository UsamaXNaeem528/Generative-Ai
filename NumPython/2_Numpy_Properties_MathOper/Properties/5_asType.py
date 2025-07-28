# using astpye() we can convert the datatype of array like int to str, str to int, int<->float

import numpy as np

arr = np.array([1.5, 3.5, 5.5])
print(arr)
print(arr.dtype)

arr_int = arr.astype(int)
print(arr_int)
print(arr_int.dtype)

