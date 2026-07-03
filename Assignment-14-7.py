# Program - lamnbda function accepts 1 number and 
# returns True if Divisible By 5

DivisibleByFive = lambda No : (No %5 == 0)

def main():
    Value = int(input("enter Your Number : "))

    Ret = DivisibleByFive(Value)

    print(Value,"is divisible By 5 ? : ",Ret)

if __name__ == "__main__":
    main()
