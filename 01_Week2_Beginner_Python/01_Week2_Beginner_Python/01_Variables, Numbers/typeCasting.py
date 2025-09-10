# 🔁 What is Type Conversion in Python?
# Type conversion means changing a value from one data type to another. 
# like int to float, string to num, num to string

# 1. Implicit Conversion
# 2. Explicit Conversion using built in functions.

#Implicit automatically
a = 10
b = 7.5
c = a + b 
print(f'sum of a and b {c}') 
print(type(c))
# In the answer of this we can see that a = 10 integer automatically converts into float

#Explicit Conversion using built in functions int(), float(), str(), bool()
# !str to int conversion will not work if the string is not a number
int_num = 10
string = str(int_num)
print(type(str))

str_num = "10"
int_num1 = int(str_num)
print(type(int_num1))

#=========================================================

# 🧠 Challenge:
# You’re given these variables:
a1 = "20"
b2 = "5.5"
c3 = 10

# ✅ Your Task:
# Convert a to an integer.
# Convert b to a float.
# Add all three numbers together.
# Print the final result.

a1 = int(a1)
b2 = float(b2)
print(f'sum of a1 + b2 + c3 = {a1 + b2 + c3}')








