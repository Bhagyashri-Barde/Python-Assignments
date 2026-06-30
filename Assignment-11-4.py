# Program - Accept 1 number and Print
# Reverse of that number

def Reverse(No):
     Rev = 0

     if No == 0:

         Rev = 0
     
     else:
         while(No>0):
            No1 = No % 10

            No2 = Rev * 10

            Rev = No2 + No1   

            No = int(No / 10) 

     return Rev

def main():
    Value = abs(int(input("Enter Your Number : ")))       # abs() - remove negative sign from anumber

    Ret = Reverse(Value)

    print("Reverse number of",Value,"is : ",Ret)
   
if __name__ == "__main__":
    main()