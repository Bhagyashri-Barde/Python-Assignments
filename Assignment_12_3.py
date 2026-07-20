# Program - Accept 2 numbers and Prints
# 1) Addition          2) Subtarction 
# 3) Multiplication    4) Division

from ArithmaticOperations import Addition
from ArithmaticOperations import Subtraction
from ArithmaticOperations import Multiplication,Division

print("-----------------------------------")
print("------ Arithmatic Operations ------")
print("-----------------------------------")

def main():
    Value1 = int(input("Enter First Number : "))

    Value2 = int(input("Enter Second Number : "))

    print("Addition is : ",Addition(Value1,Value2))

    print("Division is : ",Subtraction(Value1,Value2))

    print("Multilication is : ",Multiplication(Value1,Value2))

    print("Division is : ",Division(Value1,Value2))

if __name__ == "__main__":
    main()

