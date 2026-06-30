# Program - Accept 1 number and Prints
# Count of digits in that number

def CountDigits(No):
     Count = 0
    
     if No == 0:
         Count = 1
     else:
         while(No>0):
             Count = Count + 1
             No = int(No / 10)            
             # No = No // 10            # // - returns the value without the decimal part

     return Count

def main():
    Value = abs(int(input("Enter Your Number : ")))       # abs()- removes the negative sign from a number.

    Ret = CountDigits(Value)

    print("Number of Digits in",Value,"is : ",Ret)
   
if __name__ == "__main__":
    main()