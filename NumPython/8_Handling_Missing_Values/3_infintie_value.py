# check infinite value in data 
#* np.inf
#* np.isinf(arr)
# means the value to much length like 10^10000 OR value/0 leads to undefined

#checking the infinte value in data

import numpy as np
arr = np.array([2, 4, np.inf, 6, 8, -np.inf])

print(np.isinf(arr))  

#output
#[False False  True False False  True]