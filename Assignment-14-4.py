# Program - lamnbda function accepts 2 Numbers and 
# return Minimum number

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter First Number : "))

    Value2 = int(input("Enter Second Number : "))

    Ret = Minimum(Value1,Value2)

    print("Minimum Number is : ",Ret)

if __name__ == "__main__":
    main()