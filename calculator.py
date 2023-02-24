print("This is calculator")

 x = int(input("Enter 1st number : "))
 y = int(input("Enter 2nd number : "))

op = input("Enter the operrator +,-,%,/,* : ")
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "%":
    print(x%y)    
elif op == "/":
    print(x/y)
elif op == "*":
    print(x*y)    
else:
    print("Invalid");
