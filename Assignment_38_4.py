import pandas as pd
import sys
def DisplayDatasetInfo(DataPath):
    Border = "-" * 70

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully.")

    # 1 -> Pass student
    # 0 -> Fail student

    print(Border)

    print("Distribution of Final Result :",df['FinalResult'].value_counts())

    PassStudents = (df['FinalResult'].value_counts(normalize=True).get(1,0)) * 100

    FailStudents = (df['FinalResult'].value_counts(normalize=True).get(0,0)) * 100

    print("Pass Students Percentage: ",PassStudents)

    print("Fail Students Percentage : ",FailStudents)

    difference =  abs(PassStudents - FailStudents)

    print("difference :",difference)

    if difference <= 20:

        print("The dataset is reasonably balanced.")
    else:
        print("The dataset is imbalanced.")


def main():
    Border = "-" * 70

    print(Border)
    print("Student Performance Case Study")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Distribution of Final Result")
            print("3 Percentage of Pass Students")
            print("4 Percentage of Fail Students")
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