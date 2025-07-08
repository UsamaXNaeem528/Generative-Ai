'''
What is try-Except:
If the error comes in your code/program (like: divide by zero, invalid input, file not found), then 
use the try-except, it help in a way you can show the program expected error in meaningful way like.
You can show the custom error message for user understanding

try:
    # write the actual code
except:
    # this part runs when the error comes from above try(block)
''' 
# * Example 1: Division Error
try:
    num = int(input('Enter number or divisor : '))
    result = 10 / num
    print(f"Result is : {result}")
except:
    print("Enter a valid input number, don't enter zero!")
    
# * Specific Exception Handling like handling a value error
try:
    val = int('12')
    print(f'Your Entered Value : {val}')
except ValueError:
    print("Value Error: wrong value enter, enter a number")


'''✔ Common Exceptions:'''
'''
| Exception Name      | Cause                         |
| ------------------- | ----------------------------- |
| `ValueError`        | Wrong type (like "abc" → int) |
| `ZeroDivisionError` | Divide by 0                   |
| `FileNotFoundError` | File exists nahi karta        |
| `IndexError`        | List ka index galat ho        |
| `KeyError`          | Dictionary key nahi mila      |
'''


#* Example 2: File Handling with Error
try:
    with open(r'Week1_ BeginnersPython\08_Exception_Handling\file.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found in directory")


#*Example 3: Advanced try-except-else-finally
try:
    num = int(input("Enter a number : "))
    result = 10 / num
except ZeroDivisionError:
    print("Don't enter a zero number!")
except ValueError:
    print("Enter a number or digit!")
else:
    print("Result : ", result)
finally:
    print("Final block will always execute.")


#* Example Calculator
try:
    print("Enter your choice: +, -, *, / (type 'exit' to quit)")
    choice = ''
    while(choice != 'exit'):
        choice = input("Enter Choice of operation you want to perform : ").lower()
        if(choice == '+'):
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            result = num1 + num2
            print(f'Addition : {result}')
            
        elif(choice == '-'):
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            result = num1 - num2
            print(f'Subtraction : {result}')
            
        elif(choice == '*'):
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            result = num1 * num2
            print(f'Multiplication : {result}')
            
        elif(choice == '/'):
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            result = num1 / num2
            print(f'Division : {result}')
            
        elif(choice == 'exit'):
            print("Exiting Calculator")
            
        else:
            print('Choose the correct choice or option!!')
       
except ZeroDivisionError:
    print("dont enter second number as zero if you divide")
except ValueError:
    print("Enter a number or digit!")
finally:
    print('Type exit for exit!')





