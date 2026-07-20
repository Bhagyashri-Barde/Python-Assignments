'''
Create Module Arithmatic contains 4 Functions 
1) Add() - For Addition         2) Sub() - For Subtraction
3) Mult() - For Multiplication  4) Div()- For Division
all functions accepts 2 parameters as number and perform Operations
Program - Call all the functions from Arithmatic Module 
by accepting paramaeters from user

''' 


from Arithmatic import *

def main():

    No1 = int(input("Enter First Number : "))

    No2 = int(input("Enter Second Number : "))

    print(f"Addition is : {Add(No1,No2)}")

    print(f"Subtraction is : {Sub(No1,No2)}")

    print(f"Multiplication is : {Mult(No1,No2)}")

    print(f"Division is : {Div(No1,No2)}")
    
if __name__ == "__main__":
    main()

