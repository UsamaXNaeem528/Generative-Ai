#np.nan_to_num(array, nan=value)  default value->0

#array with Nan and then replace Nan with '1'

import numpy as np
arr = np.array([2, 4, np.nan, 6, 8, np.nan])

print(np.nan_to_num(arr ,1))  

#output
# [2. 4. 0. 6. 8. 0.]
