'''
Copy File Content into New File (Command Line)
Program - Accepts a existing name from command Line argument,
Create a new File named Demo.txt and copies all contents from
the given file into Demo.txt

'''

import sys
                    
def main():

    if(len(sys.argv) == 2):

        try:

            fObj1 = open(sys.argv[1],"r")

            fObj2 = open("Demo.txt","w")


            Data = fObj1.read()

            fObj2.write(Data)

            print("File Copied Successfully")

            fObj1.close()

            fObj2.close()

        except FileNotFoundError as fobj:

            print("File not found...")

    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()