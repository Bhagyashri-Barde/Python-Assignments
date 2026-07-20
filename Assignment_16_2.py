# Program - Contains 1 function named as ChkNum() 
# accept 1 parameter as number 
# if number is even it should display "Even number"
# otherwise display "Odd number" on console

def ChkNum(No):

    if No % 2 == 0 :

        print("Result : Even Number")

    else:
        
        print("Result : Odd Number")

def main():
   
   No = int(input("Enter Number : "))

   ChkNum(No)

if __name__ == "__main__":
    main()