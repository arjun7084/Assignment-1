# function to perform addtion
def addition(a,b):
    return a+b

# function to perform subtraction
def subtract(a, b):
    return a-b

# funtion to perform multiplication
def multiply(a ,b ):
    return  a*b

# function to perform division
def divide (a, b) :
    if b == 0:
        return "Cannot Divide by Zero"
    return a/b

# main function to handle user input and caculations
def calculator():
    print("Welcome To Calculator:")
    print("Chose The Operator:")
    print("1. Addition")
    print("2. Substraction ")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter the choice [1,2,3,4]: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print('Result: ',addition(num1, num2))
    elif choice == '2':
        print('Result: ', subtract(num1, num2))
    elif choice == '3':
        print('Result: ', multiply(num1, num2))
    elif choice == '4':
        print('Result: ',divide(num1, num2 ))
    else:
        print ('Invalid Input')

# run the calculator
calculator()