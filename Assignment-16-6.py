# Program - Accept Number from user and check whether 
# that number is Positive or Negative or Zero

def main():
    No = int(input("Enter Number : "))

    if No > 0:

        print(f"{No} is Positive Number") 

    elif No < 0:

        print(f"{No} is Negative Number")

    else : 
        
        print(f"{No} is Zero")

if __name__ == "__main__":
    main()