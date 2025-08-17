num1=int(input("enter a number: "))
operator=input("enter an operator +,-,/,%,*: ")
num2=int(input("enter a number: "))
if operator=='+':
    print(num1+num2,"sum")
elif operator=="-":
    print(num1-num2,"difference")
elif operator=="/":
    print(num1/num2,"division")
elif operator=="%":
    print(num1%num2,"remainder")
elif operator=="*":
    print(num1*num2,"multiplication")
else :
    print("invalid command")
    
