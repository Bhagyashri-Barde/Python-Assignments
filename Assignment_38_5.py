import pandas as pd
import sys
def AnalyzeDatasetInfo(DataPath):
    Border = "-" * 70

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully.")

    # 1 -> Pass student
    # 0 -> Fail student

    print(Border)

    avgStudyHours = df.groupby('FinalResult')['StudyHours'].mean()

    passHours = avgStudyHours.get(1,0)
    failHours = avgStudyHours.get(0,0)

    print("Pass Study Hours:", passHours)
    print("Fail Study Hours:", failHours)


    if passHours > failHours:
        print("Higher study hours are associated with a higher chance of passing.")
    else:
        print("Higher study hours are not associated with a higher chance of passing.")

    print(Border)
    
    avgAttendance = df.groupby('FinalResult')['Attendance'].mean()

    passAttendance = avgAttendance.get(1,0)
    failAttendance = avgAttendance.get(0,0)

    print("Pass Attendance:", passAttendance)
    print("Fail Attendance:", failAttendance)

    if passAttendance > failAttendance:
        print("Students with higher attendance have a higher chance of passing.")
    else:
        print("Higher attendance does not appear to be associated with a higher chance of passing.")


def main():
    Border = "-" * 70

    print(Border)
    print("Student Performance Case Study")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Analyze the dataset")
            print("3 Check whether Higher study hours increase the chance of passing or not")
            print("4 Check whether Higher attendance improve final result or not")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

             print("Please execute the scipt as")

             print("Pyhton fileName.py CSV_File_Path")
            
        else:

            AnalyzeDatasetInfo(sys.argv[1])

    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for More information")
        
    print(Border)
    print("Thank you for using Student Performance Study")
    print(Border)
    
if __name__ == "__main__":
    main()