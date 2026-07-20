# Program - lamnbda function accepts 1 Number and 
# return square of that number

Square = lambda No : ( No * No )

def main():
    Value = int(input("Enter Your Number : "))

    Ret = Square(Value)

    print("Square of",Value ,"is : ",Ret)

if __name__ == "__main__":
    main()