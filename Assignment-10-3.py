# Program - Accept 1 number and
# Prints Factorial of that number


print("-------------------------------------")
print("-------- Factorial Of Number --------")
print("-------------------------------------")

def Factorial(No):

    FactNo = 1

    if No == 0 or No == 1 :
        return 1
    else:
        for i in range(1,No+1):
            FactNo = FactNo * i

        return FactNo
    
def main():
    Value = int(input("Enter your number : "))

    Ret = Factorial(Value)

    print("Factorial of " ,Value ,"is : ",Ret)

if __name__ == "__main__":
    main()
