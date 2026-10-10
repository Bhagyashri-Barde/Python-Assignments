import sys
import pandas as pd


from sklearn.metrics import accuracy_score
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

    print("X_Train : ",X_Train.shape)        
    print("X_Test : ",X_Test.shape)           

    print("Y_Train : ",Y_Train.shape)       
    print("Y_Test : ",Y_Test.shape)        

    return X_Train,X_Test,Y_Train,Y_Test

###################################################
# Step 5 : Build and Train the model
###################################################

def Train_Model(X_Train,Y_Train):
    
    print(Border)
    print("Step 5 : Build and Train the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth= 3,random_state=42)

    model.fit(X_Train,Y_Train)

    print("Model Trained Successfully")

    return model

################################################################
# Step 6 : Analyze Misclassified Students
################################################################

def Analyze_Misclassified_Students(model,X_Test,X_Train,Y_Test,Y_Train):
    
    print(Border)
    print("Step 6 : Analyze Misclassified Students")
    print(Border)

    # predict Testing model
    Y_test_pred = model.predict(X_Test)

    misclassified_Students = Y_Test != Y_test_pred

    print("Total Misclassified Students : ",misclassified_Students.sum(),"\n")

    print("Misclassified Students Record :")
    
    if misclassified_Students.any():
        print(X_Test[misclassified_Students].T)

        print("\nCommon Pattern Analysis:")

        print("Average features of misclassified students:")
        print(X_Test[misclassified_Students].mean().round(2))

        print("\nAverage features of correctly classified students:")
        print(X_Test[~misclassified_Students].mean().round(2))
    else:
        print("No students were misclassified.")


    # if misclassified_Students.sum() > 0:
    #     print("\nAverage Features of Misclassified Students:")
    #     print(X_Test[misclassified_Students].mean(numeric_only=True).round(2))

    # print("\nActual Result Distribution:")
    # print(Y_Test.loc[misclassified_Students].value_counts())


def Execute_Ml_Pipeline():
    # Step 1 : Load the Dataset
    df =  LoadDataSet(sys.argv[1])
    
    # Step 2 : Data Analysis (EDA)
    DataAnalysis(df)
           
    # Step 3 : Decide Independent & Dependent Variables
    X,Y = SelectFeaturesAndLabels(df)

    # Step 4 : Split the dataset for training and testing
    X_Train,X_Test,Y_Train,Y_Test = SplitDataset(X,Y)
           
    # Step 5 : Build and Train the model
    model = Train_Model(X_Train,Y_Train)


    # Step 6 :  Analyze Misclassified Students
    Analyze_Misclassified_Students(model,X_Test,X_Train,Y_Test,Y_Train)

def main():
    print(Border)
    print("Student Performance Case Study")
    print(Border)
    
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This autonmation script is used for Student Performance Case Study")
            print("1 Load the data from CSV file")
            print("2 Analys the data")
            print("3 Decide Independent & Dependent Variables")
            print("4 Split the dataset for training and testing")
            print("5 Build and Train the model")
            print("6 Analyze Misclassified Students")

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

