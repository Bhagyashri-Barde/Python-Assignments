# Program - Contains 1 function that accept 1 number from user and
# returns True if Number is divisible By 5
# Otherwise return False

def ChkDivisibility(No):

    if No % 5 == 0:

        return True
    
    else:

        return False

def main():
   
   No = int(input("Enter Number : "))

   Ret = ChkDivisibility(No)

   print(f"{No} is Divisible By 5 ? : ",Ret)

if __name__ == "__main__":
    main()