'''
Display File Content
Program - Accepts a file name from user,opens that file and
Displays the entire contents on the console

'''

import sys  
                    
def main():

    if(len(sys.argv) == 2):

        try:

            fObj = open(sys.argv[1],"r")
            
            Data = fObj.read()

            print("File Content :")

            print(Data)

            fObj.close()

        except FileNotFoundError as fobj:

            print("File not found...")

    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()