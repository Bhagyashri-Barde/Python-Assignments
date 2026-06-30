# Program - Accept 1 number and checks whether
# it is Palindrom or not

def Palindrom(No):
     Rev = 0
     tmpNo = No

     if tmpNo == 0:

         Rev = 0
     
     else:
         while(tmpNo>0):

            No1 = tmpNo % 10

            No2 = Rev * 10

            Rev = No2 + No1   

            tmpNo = int(tmpNo / 10) 

     if No == Rev:
         return True
     else:
         return False

def main():
    Value = abs(int(input("Enter Your Number : ")))       # abs() - remove negative sign from anumber

    Ret = Palindrom(Value)

    if Ret == True:
        print(Value,"is Palindrom")
    else:
        print(Value,"is not Palindrom")
   
if __name__ == "__main__":
    main()