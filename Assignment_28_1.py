# Count Lines in a File
# Program - Accepts a file from the user and 
# count how many lines are present in the file
import sys

def main():

     try:

        lCount = 0
        
        fName = sys.argv[1]

        fObj = open(fName,"w")

        fObj.write("Welcome in File IO.\n This is my First file. \n File name is Demo.txt. \n File IO is very interesting To learn.")

        fObj = open(fName,"r")

        with fObj as file:

            # 1. Using readlines() function of file

            # lCount = len(file.readlines())

            # 2. Using for loop

            for line in file:

                lCount = lCount + 1

        print(f"Total number of lines in File : {lCount}")

     except IndexError as fobj: 
 
            print("list index out of range")
        
     except FileNotFoundError as fobj:

        print("File not found...")

if __name__ == "__main__":
    main()