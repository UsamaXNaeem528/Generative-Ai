"""
Filtering (or boolean masking) is a powerful technique in NumPy that allows you to select elements of an 
array based on a condition. Instead of looping through the array manually, you use boolean expressions to
create a mask (True/False values) and apply it to the array directly.
"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])

#print even elements from array
print(arr[arr % 2 == 0])

#behind the working it return true fasle based on condition