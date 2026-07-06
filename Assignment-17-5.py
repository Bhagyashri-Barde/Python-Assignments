# Program - Accept 1 Number from User and check whether
# Number is prime or not
def ChkPrime(No):

    Count = 0
    
    for i in range(1,No + 1):

        if (No % i == 0):
            
            Count = Count + 1

    if (Count == 2):
        return True
    else: 
        return False 

def main():

    No = int(input("Enter Number : "))

    Ret = ChkPrime(No)

    if (Ret == True):
         print(f"{No} is Prime Number")
    else:
         print(f"{No} is not Prime Number")

if __name__ == "__main__":
    main()

