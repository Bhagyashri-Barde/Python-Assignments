import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-" *60
###################################################
# Step 1 : Load the Dataset
###################################################

def LoadDataSet(dataSetPath):
    df = pd.read_csv(dataSetPath)
    print("Step 1 : Load the dataset")
    print(Border)
    print("Dataset Load Successfully..")

    return df

###################################################
# Step 2 : Data Analysis (EDA)
###################################################

def DataAnalysis(df):
    print(Border)
    print("Step 2 : Data Analysis (EDA)")
    print(Border)

    print("Shape of dataset : ",df.shape)

    print("Columns Names : ",list(df.columns))

    print("Class distribution (Final Result count) : ")
    print(df["FinalResult"].value_counts())

###################################################
# Step 3 : Decide Independent & Dependent Variables
###################################################

def SelectFeaturesAndLabels(df):

    print(Border)
    print("Step 3 : Decide Independent & Dependent Variables")
    print(Border)

    # X : Independent Variable / Fetures
    # Y : Dependent Variable / Labels

    feture_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
        ]

    X = df[feture_cols]
    Y = df["FinalResult"]

    print("X Shape : ",X.shape)
    print("Y Shape : ",Y.shape)

    return X,Y

###################################################
# Step 4 : Split the dataset for training and testing
###################################################

def SplitDataset(X,Y):

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Dataset Spliting Activity Done")

    print("X_Train : ",X_Train.shape)        #(15,5)     
    print("X_Test : ",X_Test.shape)          #(15,5) 

    print("Y_Train : ",Y_Train.shape)        #(15,) 
    print("Y_Test : ",Y_Test.shape)          #(15,) 

    return X_Train,X_Test,Y_Train,Y_Test

###################################################
# Step 5 : Build and Train the model
###################################################

def Train_Model(X_Train,Y_Train):

    print(Border)
    print("Step 5 : Build and Train the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(X_Train,Y_Train)

    print("Model Trained Successfully")

    return model

###################################################
# Step 6 : Prediction for New Student Record
###################################################

def Evaluate_Test(model,new_student_record):

    print(Border)
    print("Step 6 : Prediction")
    print(Border)

     # predict for model
    prediction = model.predict(new_student_record)

    print("Model Prediction: ")
    # 0 = Fail
    # 1 = Pass

    if prediction[0] == 1:
        print("The student will PASS.")
    elif prediction[0] == 0:
        print("The student will FAIL.")
    else:
        print("Predicted Result :", prediction)


def Execute_Ml_Pipeline():
    # Step 1 : Load the Dataset
    df =  LoadDataSet(sys.argv[1])
    
    # Step 2 : Data Analysis (EDA)
    DataAnalysis(df)
           
    # Step 3 : Visualisation of Dataset
    X,Y = SelectFeaturesAndLabels(df)

    # Step 4 : Split the dataset for training and testing
    X_Train,X_Test,Y_Train,Y_Test = SplitDataset(X,Y)
           
    # Step 5 : Build and Train the model
    model = Train_Model(X_Train,Y_Train)

    # Step 6 : Prediction    

    StudyHours = 6
    Attendance = 85
    PreviousScore = 66
    AssignmentsCompleted = 7
    SleepHours = 7

    new_student_record = pd.DataFrame([{
        "StudyHours": StudyHours,
        "Attendance": Attendance,
        "PreviousScore": PreviousScore,
        "AssignmentsCompleted": AssignmentsCompleted,
        "SleepHours": SleepHours
    }])

    Evaluate_Test(model,new_student_record)

def main():
    print(Border)
    print("Student Performance Case Study")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Analys the data")
            print("3 Decide Independent & Dependent Variables")
            print("4 Split the dataset for training and testing")
            print("5 Build and Train the model")
            print("6 Prediction")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

             print("Please execute the scipt as")

             print("Pyhton fileName.py CSV_File_Path")
            
        else:

            Execute_Ml_Pipeline()
           
    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for More information")
        
    print(Border)
    print("Thank you for using Student Performance Case Study")
    print(Border)
if __name__ == "__main__":
    main()