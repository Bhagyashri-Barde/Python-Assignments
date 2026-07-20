# Program - Accepts 1 Number and Prints
# Binary Equivalent

def DisplayBinary(No):
    BianryNum = ""

    while(No > 0):

        reminder = No % 2

        BianryNum = str(reminder) + BianryNum

        No = No // 2

    return BianryNum



def main():
    Value = int(input("Enter your Number : "))

    Ret = DisplayBinary(Value)

    print("Binary Equivalent of" , Value,"is : ",Ret)
    
if __name__ == "__main__":
    main()