'''
Write a function called print_pattern that takes integer number as an argument and
prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
'''

def print_pattern(n):
    for i in range(n):
        i += 1
        s=''
        for j in range(i):
            s = s + '*'
        print(s)
        
print_pattern(4)

# def print_pattern(rows):
#     for i in range(rows):
#         print((i+1) * '*')
        
# print_pattern(4)
    
        

