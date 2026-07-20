# Program - lamnbda function accepts 1 number and 
# return True if number is Odd otherwise False

ChekOdd = lambda No : No % 2 != 0

def main():
    Value = int(input("Enter Your Number : "))

    Ret = ChekOdd(Value)

    print(Value,"is Odd ?: ",Ret)

if __name__ == "__main__":
    main()

