import sys
import pandas as pd


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

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
        "SleepHours",
        ]
 
    df["PerformanceIndex"] = (
        (df["StudyHours"] * 2 ) +  df["Attendance"])
    
    # After Adding PerformanceIndex
    feture_cols_1 = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"
        ]

    X = df[feture_cols]
    X1 = df[feture_cols_1]
    Y = df["FinalResult"]

    print("X Shape : ",X.shape)
    print("Y Shape : ",Y.shape)

    return X,X1,Y

###################################################
# Step 4 : Split the dataset for training and testing
###################################################

def SplitDataset(X,X1,Y):

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.3,random_state=42)

    X_Train1,X_Test1,Y_Train1,Y_Test1 = train_test_split(X1,Y,test_size=0.3,random_state=42)

    print("Dataset Spliting Activity Done")

    print("X_Train : ",X_Train.shape)        
    print("X_Test : ",X_Test.shape)           

    print("Y_Train : ",Y_Train.shape)       
    print("Y_Test : ",Y_Test.shape)        

    return X_Train,X_Test,Y_Train,Y_Test,X_Train1,X_Test1,Y_Train1,Y_Test1

###################################################
# Step 5 : Build and Train the model
###################################################

def Train_Model(X_Train,Y_Train,X_Train1,Y_Train1):
    
    print(Border)
    print("Step 5 : Build and Train the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth= 3 ,random_state=42)

    model.fit(X_Train,Y_Train)

    model1 = DecisionTreeClassifier(max_depth= 3 ,random_state=42)

    model1.fit(X_Train1,Y_Train1)

    print("Models Are Trained Successfully")

    return model,model1

################################################################
# Step 6 : Predict and Calculate Accuracy
################################################################
def Evaluate_Test(model,X_Test,Y_Test,model1,X_Test1,Y_Test1):

    print(Border)
    print("Step 7 : Predict and Compare Accuracy of Different Models")
    print(Border)

    Y_test_pred = model.predict(X_Test)

    accuracy = accuracy_score(Y_Test,Y_test_pred) * 100

    Y_test_pred1 = model1.predict(X_Test1)

    accuracy1 = accuracy_score(Y_Test1,Y_test_pred1) * 100

    print("Accuracy is :",accuracy) 

    print("Accuracy1 is :",accuracy1) 

    return accuracy,accuracy1

def FinalResult(accuracy,accuracy1):
    if accuracy1 > accuracy: 
        print("Result: Accuracy improved after adding PerformanceIndex.") 

    elif accuracy1 < accuracy: 
        print("Result: Accuracy decreased after adding PerformanceIndex.") 

    else: 
        print("Result: Accuracy remained the same after adding PerformanceIndex.") 

    print(f"Accuracy difference: {accuracy1 - accuracy:.2f} percentage points")

def Execute_Ml_Pipeline():
    # Step 1 : Load the Dataset
    df =  LoadDataSet(sys.argv[1])
    
    # Step 2 : Data Analysis (EDA)
    DataAnalysis(df)
           
    # Step 3 : Decide Independent & Dependent Variables
    X,X1,Y = SelectFeaturesAndLabels(df)

    # Step 4 : Split the dataset for training and testing
    X_Train,X_Test,Y_Train,Y_Test,X_Train1,X_Test1,Y_Train1,Y_Test1 = SplitDataset(X,X1,Y)
           
    # Step 5 : Build and Train the model
    model,model1 = Train_Model(X_Train,Y_Train,X_Train1,Y_Train1)


    # Step 6 :  Predict and Compare Accuracy of Different Models
    accuracy,accuracy1 = Evaluate_Test(model,X_Test,Y_Test,model1,X_Test1,Y_Test1)

    # Step 7 : Final Result
    FinalResult(accuracy,accuracy1 )
    

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
            print("6 Predict and Compare Accuracy of Different Models")
            print("Final Result")

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

