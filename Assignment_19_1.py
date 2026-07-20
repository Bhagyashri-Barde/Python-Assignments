# Program - Contain lambda function 
# Accept 1 parameter and return power of 2

Power = lambda No : 2 ** No

def main():
    No = int(input("Enter Number : "))

    Ret = Power(No)

    print(f"Power Of {No} is : {Ret}")

if __name__ == "__main__":
    main()