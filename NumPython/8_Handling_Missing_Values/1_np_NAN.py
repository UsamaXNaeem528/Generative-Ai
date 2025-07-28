"""
np.nan stands for:
"Not a Number"
used to find missing, undefined, or invalid numerical values in data or arrays.
"""

import numpy as np
arr = np.array([1, 2, np.nan, 4, 5, np.nan])
print(np.isnan(arr))  # isnan function return true(if value is nan) or false(if value is not nan).

#interview Question
print(np.nan == np.nan)  #Output : False
'''nan is not equal to anything — not even itself.
It's meant to represent undefined or missing values.
So np.nan == np.nan is always False, even though both sides are nan.'''

print(np.isnan(np.nan))   # Output: True

