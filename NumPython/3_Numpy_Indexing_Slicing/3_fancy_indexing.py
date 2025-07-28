"""
Fancy Indexing
select multiple elements from array at once.
->mostly helpful in non-squential data.

*Imp: it must to pass list for indexing in fancing indexing,
*original array cannot change after indexing.
"""
import numpy as np
arr = np.array([10,12,14,16,18,20])
print(arr[[0, 2, 4]])