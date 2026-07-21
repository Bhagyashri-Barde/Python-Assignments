'''
 Check File exists in current directory
 Program - Accepts a file name from user and checks whether 
 this file exists in current directory or not

'''

import sys
import os

def checkfile(FName):
    Flag = False
    for FolderName, SubFolder,FileName in os.walk("Marvellous"):
            
            for name in FileName:
                 
                 print("File:",name)

                 if(FName == name):

                    Flag = True
    return Flag
                
def main():

    if(len(sys.argv) == 2):

        Ret = checkfile(sys.argv[1])

        if Ret:
             
             print(f"{sys.argv[1]} is Exists") 

        else:

            print(f"{sys.argv[1]} is not Exists")    

    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()