# Reverse a String Without Using Reverse()
# Input: "Python"
# Output: "nohtyP"

text = "Python"
reversed_str = ''
# word = text[-1]    
# print(word)
y = -1
for x in range(len(text)):
    reversed_str += text[y]
    y += 1

print(reversed_str)
    
