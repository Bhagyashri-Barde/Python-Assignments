# Program - lamnbda function accepts 2 Numbers and 
# return Maximum number

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Value1 = int(input("Enter First Number : "))

    Value2 = int(input("Enter Second Number : "))

    Ret = Maximum(Value1,Value2)

    print("Maximum Number is : ",Ret)

if __name__ == "__main__":
    main()