# Program - Contains 1 function named as Add() 
# accepts 2 numbers from user and return
# Addition of that 2 numbers

def Add(No1, No2):
    Sum = 0

    Sum = No1 + No2
    
    return Sum

def main():
   
   No1 = int(input("Enter First Number : "))

   No2 = int(input("Enter Second Number : "))

   Ret = Add(No1,No2)

   print(f"Addition is : {Ret}")

if __name__ == "__main__":
    main()