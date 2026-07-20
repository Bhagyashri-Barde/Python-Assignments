# Count Lines in a File
# Program - Accepts a file from the user and 
# count how many lines are present in the file
 
import sys
import os

def main():

     if(len(sys.argv) == 2):

        lCount = 0
        
        fName = sys.argv[1]

        Ret = os.path.exists(fName)

        if(Ret == False):

            print("There is no such File with name ",fName)
            
            return
        
        fObj = open(fName,"r")

        with fObj as file:

            # 1. Using readlines() function of file

            # lCount = len(file.readlines())

            # 2. Using for loop

            for line in file:

                lCount = lCount + 1

        print(f"Total number of lines in File : {lCount}")

     else:

        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()