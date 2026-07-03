# Program - lamnbda function accepts 3 numbers and 
# returns Largest Number

Largest = lambda No1, No2, No3 : No1 if (No1 >= No2 and No1 >= No3) else No2 if(No2 >= No1 and No2 >= No3) else No3

def main():
    Value1 = int(input("Enter First number : "))
    
    Value2 = int(input("Enter Second number : "))

    Value3 = int(input("Enter Third number : "))

    Ret = Largest(Value1, Value2,Value3)

    print("Largest Number is : ",Ret)

if __name__ == "__main__":
    main()
