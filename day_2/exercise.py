# ITP Week 2 Day 2 Exercise

#Write a basic calculator using the input function to complete the following tasks.  
# Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def subtract(num1, num2):
    return num1 - num2

#     - A function that multiplies three integers
def multiply(num1, num2, num3):
    return num1 * num2 * num3

#     - A function that adds four integers
def addition(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    return sum

# Medium: 
#- Create a calculator function using THREE input parameters 
# (two float, one string) to all the user to add, substract, multiply and divide.

float1 = float(input("Enter your first number: "))
string1 = input("Choose from the following(+, -, /, *): ")
float2 = float(input("Enter your second number: "))

def calculator():
    subtract()
    multiply()
    addition()



# Hard: 
# - You're at a restaurant with some friends and the server didn't split up the check.  
# Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  
# BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.