print("Welcome to my calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input ("Enter operation(+ , -, *, /): ")

if operation == "+":
    result = num1 + num2
    print (f"the answer is {result}")
elif operation == "-":
    result = num1 - num2
    print (f"the answer is {result}")
elif operation == "*":
    result = num1 * num2
    print (f"the answer is {result}")
elif operation == "/":
    result = num1 / num2
    print (f"the answer is {result}")