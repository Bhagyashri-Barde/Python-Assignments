# Program - Accept one number and prints
# Cube of that Number

def Cube(No):

    return No * No * No

def main():

    Value = int(input("Enetr Your Number : "))

    Ret = Cube(Value)

    print("Cube of", Value," is : ",Ret)

if __name__ == "__main__":
    main()