# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

a = 8 # int
b = 3.2 # float
c = 2 + 3j # complex class
d = "Hello" # str
e = [1, 2, 3] # list
f = (1, 2, 3) # tuple
g = {1, 2, 3} # set
h = {1: "one", 2: "two"} # dict
i = True # bool
j = None # NoneType
k = b"Hello" # bytes
l = bytearray(5) # bytearray
m = memoryview(bytes(5)) # memoryview
n = frozenset([1, 2, 3]) # frozenset

print(type(c))