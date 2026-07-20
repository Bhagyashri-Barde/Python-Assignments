# Program - lamnbda function accepts 1 Number and 
# return cube of that number

Cube = lambda No : (No * No * No)

def main():
    Value = int(input("Enter Your number : "))

    Ret = Cube(Value)

    print("Cube of",Value,"is: ",Ret)

if __name__ == "__main__":
    main()
