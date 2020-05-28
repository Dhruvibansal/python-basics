print("hello")
## Importing Libraries
# from package import module
# import module as nickname
# import package.module as nickname
from math import *

## To take input in the shell
name = input("Enter your name : ")


## To take output in the shell
print("Hello World")
print("Hello", name)  # Simplest method
print("Hi %s" %name) # traditional method
print("Bye {}" .format(name))

## %d - int
## %s - str
## %f - float

## Program 1
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
print("Addition of the numbers is", (a+b))


## Program 2
cash=int(input("How much do you have? "))
amt = floor(cash/100)
print("You can buy",amt,"apples")


## Rounding off
round(1.5)  # This method rounds off to the closest integer
ceil(1.5)   # This method rounds off to next integer (math lib req)
floor(1.5)  # This method rounds off to prev integer (math lib req)


## A block of code example (IF ELSE)
a = 10
b = 7
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")