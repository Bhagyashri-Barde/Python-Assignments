# Program - lamnbda function accepts 1 number and 
# return True if number is even otherwise False

ChekEven = lambda No :  No % 2 == 0 

def main():
    Value = int(input("Enter Your Number : "))

    Ret = ChekEven(Value)

    print(Value,"is Even ? : ",Ret)

if __name__ == "__main__":
    main()

