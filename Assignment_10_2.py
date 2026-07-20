# Program - Accept 1 number and
# Prints Sum of first N Natural Numbers

def Sum(No):

    Sum = 0

    for i in range(No+1):
        Sum = Sum + i

    return Sum

def main():

    Value = int(input("Enter Your Number : "))

    Ret = Sum(Value)

    print("Sum of Your Numbers Are : ",Ret)

if __name__ == "__main__":
    main()
