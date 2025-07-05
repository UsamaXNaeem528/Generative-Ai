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

def print_pattern(rows):    
    rows += 1
    for i in range(rows):    # Outer loop for rows
        for j in range(i):   # Inner loop for columns
            print('*',end='')   # Print star without newline
        print()                 # Move to next line after inner loop
        
print_pattern(4)

# def print_pattern(rows):
#     for i in range(rows):
#         print((i+1) * '*')
        
# print_pattern(4)
    
        

