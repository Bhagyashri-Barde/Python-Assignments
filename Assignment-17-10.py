# Program - Accept Number from User and return addition of digits in that number

def main():
    Sum = 0

    No = abs(int(input("Enter Number : ")))

    while(No != 0):
        
        rem = No % 10 
        
        No = No // 10

        Sum = Sum + rem

    print("Addition of Digits in Number is :",Sum)

if __name__ == "__main__":
    main()

