'''🔸 1. Conditional Statements'''
# if, elif, else help to program to take decision.
#✅ Syntax:
'''
if condition:
    # code runs if condition is True
elif another_condition:
    # runs if first is False and this is True
else:
    # runs if no condition is True from above
'''
#*===========================
'''🔹 Conditions Use:
==, !=, >, <, >=, <=

and, or, not'''

name = input(f'Enter you name : ')
age = int(input(f'Enter Your age : '))

#lets make a decision about the which person are eligible for the driving licesne
if(age == 18):
    print(f'{name} is elgibile for driving license')
elif(age > 18):
    print(f'{name} is eligible for driving license')
else:
    print(f'{name} is not eligible for driving license')
    


