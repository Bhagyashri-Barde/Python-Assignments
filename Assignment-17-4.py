# Program - Accept 1 Number from User and return addition of its Factors 

def Factor(No):
    Sum = 0
    
    for i in range(1,No):

        if (No % i == 0):
            
            Sum = Sum + i
 
    return Sum

def main():

    No = int(input("Enter Number : "))

    Ret = Factor(No)

    print(f"Addition of Factors of {No} is : ",Ret)

if __name__ == "__main__":
    main()

