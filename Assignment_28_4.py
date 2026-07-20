# Copy file content into another file
# Program - Accepts a 2 file names from the user 
# 1. First file is Existing file
# 2. Second file in new file
# copy all content from the first file into second file
import sys

def main():

     try:
        
        fName1 = sys.argv[1]

        fName2 = sys.argv[2]

        fObj1 = open(fName1,"r")

        fObj2 = open(fName2,"w")

        file1_Data = fObj1.read()

        fObj2.write(file1_Data)

        print("File Copied Successfully...")

        fObj1.close()
        fObj2.close()

     except IndexError as fobj: 
 
            print("list index out of range")

     except FileNotFoundError as fobj:

        print("File not found...")

if __name__ == "__main__":
    main()