# calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Choose your operator (+, -, /, *): ")

if c == "+":
    print(a + b)

elif c == "-":
    print(a - b)

elif c == "/":
    print(a / b)

elif c == "*":
    print(a * b)

else:
    print("NOT A OPERATOR")
