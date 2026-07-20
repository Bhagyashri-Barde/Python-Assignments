# Count Words in a File
# Program - Accepts a file from the user and 
# count total number of words in that file

import sys
import os

def main():

    if(len(sys.argv) == 2):

        wCount = 0
        fName = sys.argv[1]

        Ret = os.path.exists(fName)
        
        if(Ret == False):

            print("There is no such File with name ",fName)
            
            return
        
        fObj = open(fName,"r")

        with fObj as file:

            # 1.Using readline() function of file

            # wCount = len(file.readline())

            # 2. Using for loop

            for line in file:
                
                words = line.split()
                
                wCount = wCount + len(words)

        print(f"Total number of Words in File : {wCount}")
        
    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()