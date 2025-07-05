'''
🔧 Python Functions 
🔹 What is a Function
'''
'''A function is a block of reusable code that performs a specific task.
It helps organize, reuse, and reduce repetition in your code.'''

'''✅1. Defining a Function'''
def greet():
    name = "Usama"
    print(f'Hello {name}')

# calling function
greet()



'''✅ 2. Function with Parameters'''
def greet_user(name):
    print(name)
    
greet_user("function with paramters ==> Usama")



'''✅ 3. Function with Return Value
(function return something like value, expression etc. at return statement function stop execution)'''
# def add_fun(x,y):
#     sum = x + y
#     return sum

# first_num = int(input('Enter first number : '))
# second_num = int(input('Enter second number : '))
# sum = add_fun(first_num, second_num)
# print(sum)



'''✅ 4. Default Parameters
In this we set the default parameter in function declarartion, in case when user dont pass any arguement'''
def greet_guest(name='guests'):
    print(f'Hello, welcome {name} in my home')
    
greet_guest()  #===> output : Hello, welcome guests in my home
greet_guest('Harry')     #===> output : Hello, welcome Harry in my home



'''✅ 5. Arbitrary Arguments (*args)
Use *args when you don't know how many arguments you'll get.'''
def print_all(*all):
    return all
print(print_all('Usama', 'is', 'learning', 'python'))

def sum_all(*nums):
    sums = sum(nums)
    return sums
print(sum_all(1,2,3,4,5,6,7,8,9,10))
    


'''✅ 6. Keyword Arguments (**kwargs)
Use **kwargs to accept key-value pairs means pass (dictionary) key = values in arguements in function calling.
'''

def print_user_info(**info):
    for key, value in info.items():
        return(f'{key} ==> {value}')
        
print("User Information")
print(print_user_info(name='Usama Naeem', age='23', interst='Artificial Intelligence'))

'''✅ 7. Scope: Local vs Global Variables
Global variable ==> variable outside the function.
Local variable ==> variable inside the function.
'''
x = 'I am global variable'

def sample_fun():
    y = 'I am local variable'
    return y

print(x)
print(sample_fun())



 
        














