'''This module contains some useful functions and variables'''
# just like a def functions, this string is a documentation that describes the module

def factorial_3(x):
    '''This function calculates factorial of a number'''
    if x == 0:
        return 1
    else:
        return x * factorial_3(x - 1)
    
def fibonacci(n):
    '''This function  calculates n number of Fibonacci series'''
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    return fib_series

def sq_root(x):
    '''This function calculates square root of a number'''
    return x ** 0.5

def power(x, y):
    '''This function calculates power of a number'''
    return x ** y

# variable
pi = 3.14
e = 2.7