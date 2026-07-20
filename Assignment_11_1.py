# Program - Accept 1 number and checks whether
# it is Prime or not

def isPrime(No):
     Count = 0
    
     if No<=1:
         Count = 0
     else:
         for i in range(1,No+1):
             if(No % i == 0):
                 Count = Count + 1
    
     return Count

def main():
    Value = int(input("Enter Your Number : "))

    Ret = isPrime(Value)

    print(Ret)

    if(Ret == 2):
        print(Value, "is prime Number")
    else:
        print(Value, "is Not prime Number")

if __name__ == "__main__":
    main()