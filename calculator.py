print("This is calculator")
op = input("Enter the operrator +,-,%,/,* : ")
if op == "+":
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x+y)
elif op == "-":
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x-y)
elif op == "%":
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x%y)    
elif op == "/":
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x/y)
elif op == "*":
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x*y)    
else:
    print("Invalid");
