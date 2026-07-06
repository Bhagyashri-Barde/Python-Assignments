# Program - Accept 1 Number from User and return its Factorial 

def Factorial(No):
    result = 1

    for i in range(1,No+1):

        result = result * i
        
    return result

def main():

    No = int(input("Enter Number : "))

    Ret = Factorial(No)

    print(f"Factorial of {No} is : {Ret}")

if __name__ == "__main__":
    main()

