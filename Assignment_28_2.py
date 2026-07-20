# Count Words in a File
# Program - Accepts a file from the user and 
# count total number of words in that file
import sys

def main():

     try:

        wCount = 0

        fName = sys.argv[1]

        fObj = open(fName,"r")

        with fObj as file:

            # 1.Using readline() function of file

            # wCount = len(file.readline())

            # 2. Using for loop

            for line in file:
                
                words = line.split()
                
                wCount = wCount + len(words)

        print(f"Total number of Words in File : {wCount}")
        
     except IndexError as fobj: 
 
            print("list index out of range")

     except FileNotFoundError as fobj:

        print("File not found...")

if __name__ == "__main__":
    main()