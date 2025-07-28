"""
💡 Vectorization in NumPy kya hota hai?
Vectorization ka matlab hai:
"For loops" ko avoid karna aur directly array par fast operations lagana.

📌 Simple Words:
Aap loops ke bajaye NumPy functions aur operators use karein jo C language ke level par optimized hotay hain — 
isay hi vectorized operations kehte hain.
Kisi bhi NumPy array par aap custom expressions laga sakte ho binna loop ke.
"""

#vecorized multipication
#multiple with those elements of array which is grater than the 20 and return same array

import numpy as np

num_arr = np.array([10, 20, 30, 40])
multiple = 2
num_arr[num_arr > 20] *= multiple   #output [20 40 60 80]
print(num_arr)










