# 7/3/2024 - Python Activity 1.5 Enhanced Calculator


# funtions for math operations
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return x ** y

# Ask user operation
print("Select operation. Type 1, 2, 3, 4. ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")

# Inputs
userInput = input() 
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter exponent: "))

# Where the actual operation occurs
if userInput == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", add(num1, num2))
elif userInput == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", subtract(num1, num2))
elif userInput == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", multiply(num1, num2))
elif userInput == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", divide(num1, num2))
elif userInput == '5':
    num1 = float(input("Enter first number: "))
    num3 = float(input("Enter exponent: "))
    print("Result:", exponent(num1, num3))
else:
    print("Please enter a valid number. ")