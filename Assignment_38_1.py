import pandas as pd
import sys
def DisplayDatasetInfo(DataPath):
    Border = "-" * 70

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully.")

    print(Border)
    print("First 5 Records")
    print(Border)

    print(df.head(5))

    print(Border)
    print("Last 5 Records")
    print(Border)

    print(df.tail(5))

    print(Border)
    print("Total number of Rows and columns")
    print(Border)

    print("Rows : ",df.shape[0])
    print("Columns : ",df.shape[1])
    

    print(Border)
    print("List of Column Names")
    print(Border)

    columnsList = list(df.columns)

    for col in columnsList:
        print(col)
   
    print(Border)
    print("Datatype of each column")
    print(Border)

    print(df.dtypes)

def main():
    Border = "-" * 70

    print(Border)
    print("Student Performance Case Study")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 First 5 records")
            print("3 Last 5 records")
            print("4 Total number of rows and columns")
            print("5 List of column names")
            print("6 Datatype of each column")
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