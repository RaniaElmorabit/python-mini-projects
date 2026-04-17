def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed."
    return a/b
while True:
    print("""Welcome to the Simple Calculator!
        Please select an operation:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide""")
    choice=input("Enter your choice (1/2/3/4): ")
    
    if choice=='1':
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        print(f"The result of {num1} + {num2} is: {Add(num1,num2)}")
    elif choice=='2':
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))          
        print(f"The result of {num1} - {num2} is: {Subtract(num1,num2)}")
    elif choice=='3':
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        print(f"The result of {num1} * {num2} is: {Multiply(num1,num2)}")
    elif choice=='4':
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        print(f"The result of {num1} / {num2} is: {Divide(num1,num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")
