# Program - Accept 1 number and Print
# Sum of Digits

def SumOfDigits(No):
     Sum = 0

     if No == 0:
         
         Sum = 0

     else:
         while(No>0):
            Sum = Sum + No % 10
            No = int(No / 10)          

     return Sum

def main():
    Value = abs(int(input("Enter Your Number : ")))       # abs() - remove negative sign from anumber

    Ret = SumOfDigits(Value)

    print("Sum of Digits in -",Value,"is : ",Ret)
   
if __name__ == "__main__":
    main()