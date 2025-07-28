"""
slicing means extract sub array from parent array

parameters logic / syntax
||
\/
arr[startindex, stop/endIndex, step]  

arr[start:end] --> start to end-1

->In stop index always put 1 step forward value of index(because it works like [stopindex - 1])
->step value always default is 1.

=> parameter can be pass into negative -1,-2,... in reverse order
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[2:5])  #index 2-4
print(arr[:4:])  #index 0-3
print(arr[::3])  #print after 10 every third value
print(arr[1:-1:])   #print from 20 to 50
