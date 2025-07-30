def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose (+ or -): ")

if operation == '+':
    print("Result:", add(num1, num2))
elif operation == '-':
    print("Result:", subtract(num1, num2))
else:
    print("Invalid operation")
