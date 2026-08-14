import pandas as pd
import sys
def DisplayDatasetInfo(DataPath):
    Border = "-" * 70

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully.")

    print(Border)

    print("Total number of students in the dataset : ",df.shape[0])

    # Passed Students -> FinalResult = 1
    # Failed Students -> FinalResult = 0

    totalPass = (df['FinalResult'] == 1).sum()
    totalFail = (df['FinalResult'] == 0).sum()

    # totalPass = 0
    # totalFail = 0

    #for data in df['FinalResult']:

        # if(data == 1):                          # Passed Students -> FinalResult = 1

        #     totalPass = totalPass +1

        # if(data == 0):                           # Failed Students -> FinalResult = 0

        #     totalFail = totalFail +1

    print("Total passed students :",totalPass)

    print("Total failed students :",totalFail)

def main():
    Border = "-" * 70

    print(Border)
    print("Student Performance Case Study")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Total number of students in the dataset")
            print("3 Total passed students")
            print("4 Total failed students")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

             print("Please execute the scipt as")

             print("Pyhton fileName.py CSV_File_Path")
            
        else:

            DisplayDatasetInfo(sys.argv[1])

    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for More information")
        
    print(Border)
    print("Thank you for using Student Performance Study")
    print(Border)
    
if __name__ == "__main__":
    main()