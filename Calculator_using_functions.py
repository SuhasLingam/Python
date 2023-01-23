x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
op = (input("Enter the operator + , * , / , % , - : "))


def calculator(x, y):
    if op == "+":
        print(f"Value for {x} + {y} is {x + y}")
    elif op == "-":
        print(f"Value for {x} - {y} is {x - y}")
    elif op == "%":
        print(f"Value for {x} % {y} is {x % y}")
    elif op == "/":
        print(f"Value for {x} / {y} is {x / y}")
    elif op == "*":
        print(f"Value for {x} * {y} is {x * y}")
    else:
        print("invalid option")

calculator(x, y)

