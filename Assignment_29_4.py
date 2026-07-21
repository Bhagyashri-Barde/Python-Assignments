'''
Compare 2 Files (Command Line)
Program - Accepts 2 files name from command Line argument,and 
Comare the content of both files
1) If Both files contain the Same Content Display Success
2) Otherwise Diaply Failure

'''

import sys
                    
def main():

    if(len(sys.argv) == 3):

        try:

            fObj1 = open(sys.argv[1],"r")

            fObj2 = open(sys.argv[2],"r")


            FData1 = fObj1.read()

            FData2 = fObj2.read()

            if FData1 == FData2:
                print("Success")
            else:
                print("Failure")

            fObj1.close()

            fObj2.close()

        except FileNotFoundError as fobj:

            print("File not found...")

    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()