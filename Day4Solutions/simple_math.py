"""
Simple_math module - a collection of simple math operations

Functions:
    simple_add(a,b) - sum of two numbers
    
    simple_sub(a,b) - Subtratction of two numbers, b from a
    
    simple_mult(a,b) - the multiplication of two numbers
    
    simple_div(a,b) - the division of a/b
    
    poly_first(x, a0, a1) - first degree polynomial
    
    poly_second(x, a0, a1, a2) - second degree polynomial

"""

def simple_add(a,b):
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
