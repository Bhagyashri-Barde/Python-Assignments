# Program - Contain lambda function 
# Accepts 2 parameters and return its multiplication

Multiply = lambda No1, No2 : No1 * No2

def main():
    N1 = int(input("Enter First Number : "))

    N2 = int(input("Enter Second  Number : "))

    Ret = Multiply(N1,N2)

    print(f"Result ({N1} X {N2}) : {Ret}")

if __name__ == "__main__":
    main()