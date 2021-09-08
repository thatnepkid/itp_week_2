#Testing Git

# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

# Medium: 
# - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.
tax_rate = 0.0725
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
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) 
#       to allow the user to add, substract, multiply and divide.
def calculator():
    float1 = float(input("Put in your first number. "))
    float2 = float(input("Put in your second number. "))
    str1 = input("Choose from the following (+, -, *, /): ")
    if str1 == "+":
        print(float1 + float2)
    if str1 == "-":
        print(subtract(float1, float2))
    if str1 == "*":
        print(float1 * float2)
    if str1 == "/":
        print(float1 / float2)
while True:
    calculator()
    again = input("Use again? (y/n) ")
    if again != "y":
        break


# Hard: 
#- You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  
# BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  
# CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.

#Write a basic calculator using the input function to complete the following tasks.  
#Be sure to call your functions at the end, using the correct arguments.


tax_rate = 0.0725


def math_stuff_and_inputs():
    num_of_people = float(input("Enter the number of people in your party: "))
    bill_amount = float(input("Enter your bill amount: "))

    tax = bill_amount * tax_rate
    totalwith_tax = bill_amount + tax
    split = totalwith_tax / num_of_people
    print("*************************************************")
    print("This is how much you will be paying in tax $"+ str(round(tax, 3)))
    print("This is your total with tax $"+ str(totalwith_tax))
    print("Each person will have to pay $"+ str(split))
    print("*************************************************")

math_stuff_and_inputs()

