# Display File Line by line
# Program - Accepts a file from the user and 
# displays the content of the file line by line on the screen

import sys
import os
def main():

     if(len(sys.argv) == 2):

        fName = sys.argv[1]  
        Ret = os.path.exists(fName)

        if(Ret == False):

            print("There is no such File with name ",fName)
            
            return
        
        fObj = open(fName,"r")

        with fObj as file:

            print("File Content : \n")

            for line in file:
                
                print(line,end=""+"\n")

     else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()