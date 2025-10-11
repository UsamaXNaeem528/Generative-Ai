##################################
## Before adding more feature   ##
##################################

file_path = r'03_week_5_advanced_python\Python_Projects_IBHWSS\history.txt'

def save_history(equation):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(equation+'\n')

def show_history(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"File Not found {file_path}")
    except Exception as e:
        print(f"An Error Occured {e}, file is empty")

def clear(file_path):
    with open(file_path,'w',encoding='utf-8') as f:
        f.write('')
    
def calculate(eq):
    # input_list = eq.split(' ')
    # if len(input_list) != 3:
    #     print("For calculation input format must be like this --> 8 + 5")
    #     return 
    # a = int(input_list[0])
    # b = int(input_list[2])
    # oper = input_list[1]
    
    # if oper == '+':
    #     ans = a + b
    #     equation = f'{choice} = {ans}'
    #     save_history(equation)
    #     print(equation)
    # elif oper == '-':
    #     ans = a - b
    #     equation = f'{choice} = {ans}'
    #     save_history(equation)
    #     print(equation)
    # elif oper == '*':
    #     ans = a * b
    #     equation = f'{choice} = {ans}'
    #     save_history(equation)
    #     print(equation)
    # elif oper == '/':
    #     ans = a / b
    #     equation = f'{choice} = {ans}'
    #     save_history(equation)
    #     print(equation)
    # elif oper == '%':
    #     ans = a % b
    #     equation = f'{choice} = {ans}'
    #     save_history(equation)
    #     print(equation)
    # else:
    #     print("Enter Correct Equation")
    
    ##           OR
       if len(eq) < 3:
            print("For calculation input format must be like this --> 8 + 5")
            return 
       try :
            ans = eval(eq)         
       except ZeroDivisionError:
           print("Cant divided by zero")
           return
       
       equation = f'{choice} = {ans}'
       save_history(equation)
       print(equation)     

while True:
    choice = input("Enter the Calculation like (8 + 5) Or Command (exit, clear, history) : ")

    if choice == 'exit':
        break

    elif choice == 'clear':
        clear(file_path)

    elif choice == 'history':
        show_history(file_path)
       
    else:
        calculate(choice)
      
# The eval() function is used to evaluate an expression given as a string 
# and returns the result (which can be of any type, not just int).       

        
           
        
        
        
    
    
    