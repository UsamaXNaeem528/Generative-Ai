# ==========================================================
# A generator is a special type of iterator
# that yields values one by one instead of returning all values at once.
# returning them one at a time as an iterator, instead of 
# returning them all at once like a normal function.
#
# Each call to next() resumes execution from the last yield.
#
# Generators are memory efficient (O(1) space) because they 
# don’t store the whole sequence, they generate values on demand.
#
# ⚡ In short:
# Generator = Function with yield → returns an iterator → 
# produces values lazily (one at a time).
# ==========================================================


# ----------------------------------------------------------
# Fibonacci series using generator
# ----------------------------------------------------------
def fibonaci(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a+b

for i in fibonaci(10):
    print(i)


# ----------------------------------------------------------
# Table of a number using generator
# ----------------------------------------------------------
def table(n):
    i = 1
    for _ in range(10):
        yield n * i
        i += 1

for i in table(2):
    print(i)


# ----------------------------------------------------------
# Prime numbers less than n using generator
# ----------------------------------------------------------
import math
def prime_num_generator(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

for i in prime_num_generator(20):
    print(i)


# ----------------------------------------------------------
# Even numbers up to n using generator
# ----------------------------------------------------------
def even_number(num):
    for n in range(num+1):
        if n >= 1 and n % 2 == 0:
            yield n

for i in even_number(10):
    print('Even:', i)


# ----------------------------------------------------------
# Odd numbers up to n using generator
# ----------------------------------------------------------
def odd_num(num):
    for n in range(num+1):
        if n >= 1 and n % 2 != 0:
            yield n

for i in odd_num(10):
    print('Odd:', i)


# ----------------------------------------------------------
# Factorial using recursion
# ----------------------------------------------------------
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))


# ----------------------------------------------------------
# Factorial using loop/iteration
# ----------------------------------------------------------
def factorial_loop(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial_loop(5))


# ----------------------------------------------------------
# Factorials of numbers from 1 to n using generator
# ----------------------------------------------------------
def factorial_upto_n(num):
    result = 1
    for i in range(1, num+1):
        result *= i   
        yield result

def print_factorial():
    for i in factorial_upto_n(5):
        print(i)

print_factorial()


# ----------------------------------------------------------
# Check whether a number is prime or not
# ----------------------------------------------------------
def isPrime(num):
    if num <= 1:
        print(f'Number {num} is not a prime number')
        return 
        
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            print(f"Number {num} is not a prime number")
            return
    print(f"Number {num} is a prime number")

isPrime(31)

# # -------------------------------------------------------------------------------
# # Write a generator generate_squares(n) that yields squares of numbers from 1 to n.
# # -------------------------------------------------------------------------------

def generate_squares(num):
    if num<1:
        print("Numbers must be greater than 1")
        return

    for i in range(1, num+1):
        result = i**2
        yield result

for i in generate_squares(2):
    print(i)
    
# # ----------------------------------------------------------------------
# # Create a generator countdown(n) that yields numbers from n down to 1.
# # ----------------------------------------------------------------------

def countdown(num):
    while(num>=1):
        result = num
        num -= 1
        yield result

for i in countdown(10):
    print(i)

# # --------------------------------------------------------------------------------
# # Make a generator infinite_numbers() that yields numbers starting from 1 infinitely.
# # -------------------------------------------------------------------------------

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

for i in infinite_numbers():
    print(i)
    if i == 10:
        break

# # ----------------------------------------------------------------------------
# # Create a generator char_generator(string) that yields one character at a time.
# # ----------------------------------------------------------------------------

def char_generator(string):
    for i in string:
        ch = i
        yield ch

for i in char_generator('usama'):
    print(i)

# # ------------------------------------------------------------------------------------
# # Write a generator read_lines(filename) that reads a text file line by line using yield.
# # # ------------------------------------------------------------------------------------
def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Create a dummy file for the example
with open('index.txt', 'w') as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.write("Line three\n")

for i in read_lines(r'index.txt'):
    print(i)
            
# # ------------------------------
# # Alternate Even–Odd Generator
# # Make one generator even_odd_generator(n) that first yields all even numbers,
# # then all odd numbers up to n.
# # ------------------------------

def even_odd_generator(num):
    if num<=1:
        print("Number must be greater than 1")
        return
    for i in range(1,num+1):
        if i%2 == 0:
            yield i
    
    for i in range(1,num+1):
        if i%2 != 0:
            yield i

for i in even_odd_generator(10):
    print(i)

# # ---------------------------------------------------------------
# # Make a generator running_total(nums) that yields cumulative sums.
# # ---------------------------------------------------------------

# # Example:
# # If nums = [1, 2, 3, 4]
# # then it should yield → 1, 3, 6, 10
            
def running_total(num_lst):
    result = 0
    for i in num_lst:
        result += i
        yield result
    
for i in running_total([1,2,3,4]):
    print(i)

## --------------------------------------------------------
# # Fibonaci series upto n (number) using yield and recursion
## ---------------------------------------------------------
def fibonaci_recursive(num, a=0, b=1):
    if num == 0:
        return
    
    yield a
    yield from fibonaci_recursive(num - 1, a=b, b=a+b)

        
for i in fibonaci_recursive(5):
    print(i)
