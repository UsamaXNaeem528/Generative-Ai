# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet.
#    is its length. If tiles cost 500 rs per square feet, how much will be the total.
#    cost to replace all tiles. Calculate and print the cost using python.
#    Hint: Use power operator (**) to find area of a square.

area_square = 5.5**2
per_sqft_cost = 500
cost_replace_all = area_square * 500
print(f'Cost to replace the tiles : {cost_replace_all}')


# Example Calculator with Try Except

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
            try:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))
                result = num1 / num2
                print(f'Division : {result}')
            except ZeroDivisionError:
                print("dont enter second number as zero if you divide")
                
        elif(choice == 'exit'):
            print("Exiting Calculator")
            
        else:
            print('Choose the correct choice or option!!')
            
except ValueError:
    print("Enter a number or digit!")


