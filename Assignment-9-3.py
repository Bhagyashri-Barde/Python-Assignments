# Program - Accept one number and prints
# Square of that Number

def Square(No):

    return No * No

def main():

    Value = int(input("Enetr Your Number : "))

    Ret = Square(Value)

    print("Square of", Value," is : ",Ret)

if __name__ == "__main__":
    main()