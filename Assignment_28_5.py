# Search a Word in file
# Program - Accepts a file name and a word from the user and 
# checks whether the word is present in the file or not

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

        Sword = input("Enter Word for search : ")

        wordCount = 0

        with fObj as file:
            
            for lines in file:
                
                lWord = lines.split()
                
                for word in lWord:
                     
                     if Sword == word:

                        wordCount = wordCount + 1

            if wordCount > 0:
                
                print(f"{Sword} is present in File {fObj.name}")
            else:
                print(f"{Sword} is not present in File {fObj.name}")

    else:
        
        print("Invalid Number of Arguments")
if __name__ == "__main__":
    main()