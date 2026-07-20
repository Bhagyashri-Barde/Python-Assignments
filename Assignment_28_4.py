# Copy file content into another file
# Program - Accepts a 2 file names from the user 
# 1. First file is Existing file
# 2. Second file in new file
# copy all content from the first file into second file

import sys
import os

def main():

     if(len(sys.argv) == 3):
        
        fName1 = sys.argv[1]

        fName2 = sys.argv[2]

        Ret = os.path.exists(fName1)

        if(Ret == False):
            
            print("There is no such File with name ",fName1)
            
            return

        fObj1 = open(fName1,"r")

        fObj2 = open(fName2,"w")

        file1_Data = fObj1.read()

        fObj2.write(file1_Data)

        print("File copied successfully")

        fObj1.close()
        fObj2.close()

     else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()