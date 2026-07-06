'''
Program - Accept 1 Number and Display Below Pattern
Input - 5
Output -  *   *   *   *   *
          *   *   *   *   *
          *   *   *   *   *
          *   *   *   *   *
          *   *   *   *   *
''' 

def main():

    No = int(input("Enter Number : "))

    for i in range(No):
        print("*   " * No,)

if __name__ == "__main__":
    main()

