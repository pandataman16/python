def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divisible(a,b):
    return a/b

def prime(n):
    k=n//2
    flag=False
    for i in range(2,k):
        if 1%2==0:
            flag=True
    if(flag):
        return False
    else:
        return True

import math as m
def fact(n):
    return m.factorial(n)