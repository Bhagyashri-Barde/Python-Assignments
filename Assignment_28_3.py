# Display File Line by line
# Program - Accepts a file from the user and 
# displays the content of the file line by line on the screen
import sys

def main():

     try:
        fName = sys.argv[1]
        
        fObj = open(fName,"r")

        with fObj as file:

            print("File Content : ")

            for line in file:
                
                print(line,end="")

     except IndexError as fobj: 
 
            print("list index out of range")

     except FileNotFoundError as fobj:

        print("File not found...")

if __name__ == "__main__":
    main()