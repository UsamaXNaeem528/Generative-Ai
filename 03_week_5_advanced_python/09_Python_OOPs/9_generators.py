# ==========================================================
# A generator in Python is a special type of function that 
# uses the yield keyword to produce a sequence of values, 
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
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(5))


# ----------------------------------------------------------
# Factorials of numbers from 1 to n using generator
# ----------------------------------------------------------
def factorial_upto_n(num):
    result = 1
    for i in range(1, num+1):
        result *= i   #result = result * i
        yield result

def print_factorial():
    for i in factorial_upto_n(5):
        print(i)


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
