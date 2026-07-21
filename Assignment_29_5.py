'''
Frequency of a String in File
Program - Accept a file name and one string from user and 
return the frequency (Count of occurrence) of that string in the file

'''

import sys
                    
def main():

    if(len(sys.argv) == 2):

        try:

            Count = 0

            fObj1 = open(sys.argv[1],"r")

            SearchData = input("Enter String : ")

            FileData = fObj1.read()

            words = FileData.split()

            for data in words:
                if data == SearchData:

                    Count = Count + 1

            # Count = FileData.count(SearchData)

            print(f"Frequency of {SearchData} in {sys.argv[1]} File is :",Count)

            fObj1.close()


        except FileNotFoundError as fobj:

            print("File not found...")

    else:
        
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()