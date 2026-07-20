# Search a Word in file
# Program - Accepts a file name and a word from the user and 
# checks whether the word is present in the file or not

import sys

def main():

     try:

        fName = sys.argv[1]

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

     except IndexError as fobj: 
 
            print("list index out of range")
            
     except FileNotFoundError as fobj:

        print("File not found...")

if __name__ == "__main__":
    main()