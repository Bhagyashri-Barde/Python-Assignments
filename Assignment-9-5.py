# Program - Accept one number and Checks
# wheter it is divisible by 3 and 5

def ChkDivisible(No):
     
     if(No % 3 == 0 and No % 5 == 0):
        return True
     else:
        return False

def main():
     Value = int(input("Enter Your Number : "))

     Ret = ChkDivisible(Value)

     if(Ret == True):
          print(Value," is divisible by 3 and 5")
     else:
          print(Value," is not divisible by 3 and 5")

if __name__ == "__main__":
     main()

    

     
