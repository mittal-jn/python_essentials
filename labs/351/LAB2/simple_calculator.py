num1= input("Enter your first number: ")
num2= input("Enter your second number: ")

print("Choose an operation to perform: + , - , * , /")
operation= input("Enter your choice: ")
if num1.isdigit() and num2.isdigit():
    if(operation == "+"):
        print(f"{num1} + {num2} = {int(num1) + int(num2)}")
    elif (operation == "-"):
        print(f"{num1} - {num2} = {int(num1) - int(num2)}")
    elif (operation == "*"):
        print(f"{num1} * {num2} = {int(num1) * int(num2)}")
    elif (operation == "/"):
        print(f"{num1} / {num2} = {int(num1) / int(num2)}")
else:
    print("Invalid input")
    