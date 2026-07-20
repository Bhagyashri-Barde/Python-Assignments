# Program - lamnbda function accepts 2 numbers and 
# returns Multiplication

Multiplication = lambda No1, No2 : (No1 * No2)

def main():
    Value1 = int(input("Enter First number : "))
    
    Value2 = int(input("Enter Second number : "))

    Ret = Multiplication(Value1, Value2)

    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()
