"""
Broadcasting ek technique hai jo NumPy ko allow karti hai ke arrays of different shapes ke darmiyan
mathematical operations perform kare bina shape match kiye. 

💡 Simple words: Jab chhoti shape wala array automatically bada array ke sath adjust ho jata hai operation
ke liye — isay broadcasting kehte hain.

🎓 Real-life analogy:
Jese agar aap ek class ke sare students ko ek hi 5 bonus marks dena chah rahe ho — to aap broadcast kar rahe ho
ek single number to all.

No looping in it.
"""

#mathematically broadcasting
import numpy as np

prices = np.array([100,200, 300])
discount = 10  #discount to all customers.
new_prices = prices - (prices * discount/100)    
print(new_prices)

