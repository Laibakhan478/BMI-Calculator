import addition
import subtraction
import multiplication
import division
def calculator():
    while true:
        num1 =float(input("enter first number"))
        operator =input("enter operator (+,-,*,/")
        num2 =float(input("enter second number"))
        if operator=="+":
            result =addition.add(num1,num2)
        elif operator=="-":
            result =subtraction.subtract(num1,num2)
        elif operator=="*":
            result =multiplication.multiply(num1,num2)
        elif operator=="/":
            result =division.divide(num1,num2)
        else:
            print("invalid operator")
            continue
            print(f"result{result}")
calculator()

