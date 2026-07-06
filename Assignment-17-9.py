# Program - Accept Number from User and return Number of digits in that number

def main():
    Count = 0

    No = abs(int(input("Enter Number : ")))

    if(No == 0):

        Count = Count +1

    while(No != 0):

        No = No // 10

        Count = Count + 1

    print("count:",Count)

if __name__ == "__main__":
    main()

