import pandas as pd
import sys
def DisplayDatasetInfo(DataPath):
    Border = "-" * 70

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully.")

    print(Border)

    totalStudents = df.shape[0]

    totalStudyHours = df['StudyHours'].sum()
    
    avgStudyHours = (totalStudyHours / totalStudents)

    print("Average Study Hours:",avgStudyHours)

    totalAttendance = df['Attendance'].sum()

    avgAttendance = totalAttendance / totalStudents

    print("Average Attendance :",avgAttendance)

    maxPreviousScores = df['PreviousScore'].max()

    print("Maximum Precious Score :",maxPreviousScores)

    minSleepHours = df['SleepHours'].min()

    print("Minimum Sleep Hours :",minSleepHours)

def main():
    Border = "-" * 70

    print(Border)
    print("Student Performance Case Study")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Average Study Hours")
            print("3 Average Attendance")
            print("4 Maximum Previous Score")
            print("5 Minimum sleep hours")
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