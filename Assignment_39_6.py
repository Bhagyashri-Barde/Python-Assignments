import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

    model_1 = DecisionTreeClassifier(max_depth = 1)
    model_1.fit(X_Train,Y_Train)

    model_3 = DecisionTreeClassifier(max_depth = 3)
    model_3.fit(X_Train,Y_Train)

    model_None = DecisionTreeClassifier(max_depth = None)
    model_None.fit(X_Train,Y_Train)

    print("Models Trained Successfully")

    return model_1,model_3,model_None

###################################################
# Step 6 : Prediction
###################################################

def Evaluate_Test(model_1,model_3,model_None,X_Test,X_Train):

    print(Border)
    print("Step 6 : Prediction")
    print(Border)

     # predict Testing model
    Y_test_pred_1 = model_1.predict(X_Test)
    Y_test_pred_3 = model_3.predict(X_Test)
    Y_test_pred_None = model_None.predict(X_Test)

    # predict Training model
    Y_train_pred_1 = model_1.predict(X_Train)
    Y_train_pred_3 = model_3.predict(X_Train)
    Y_train_pred_None = model_None.predict(X_Train)

    print("Model Testing Done \n")

    print("Testing Model Prediction: ")

    print(Y_test_pred_1,"\n")
    print(Y_test_pred_3,"\n")
    print(Y_test_pred_None,"\n")

    print("Training Model Prediction: ")
    print(Y_train_pred_1)
    print(Y_train_pred_3)
    print(Y_train_pred_None)

    return  Y_test_pred_1, Y_test_pred_3,Y_test_pred_None, Y_train_pred_1,Y_train_pred_3,Y_train_pred_None

###################################################
# Step 7 : Accuracy Calculation
###################################################

def Calculate_Accuracy(Y_Test,Y_Train,Y_test_pred_1,Y_test_pred_3,Y_test_pred_None, Y_train_pred_1,Y_train_pred_3,Y_train_pred_None):

    print(Border)
    print("Step 7 : Accuracy Calculation")
    print(Border)

    Testing_accuracy_1 = accuracy_score(Y_Test,Y_test_pred_1) * 100
    Testing_accuracy_3 = accuracy_score(Y_Test,Y_test_pred_3) * 100
    Testing_accuracy_None = accuracy_score(Y_Test,Y_test_pred_None) * 100

    Training_accuracy_1 = accuracy_score(Y_Train,Y_train_pred_1) * 100
    Training_accuracy_3 = accuracy_score(Y_Train,Y_train_pred_3) * 100
    Training_accuracy_None = accuracy_score(Y_Train,Y_train_pred_None) * 100

    print(f"Testing Accuracy for max Depth = 1:{Testing_accuracy_1 : .4f} % \n")
    print(f"Testing Accuracy for max Depth = 3:{Testing_accuracy_3 : .4f} % \n")
    print(f"Testing Accuracy for max Depth = None:{Testing_accuracy_None : .4f} % \n")

    print(f"Training Accuracy for max Depth = 1 :{Training_accuracy_1 : .4f} % \n")
    print(f"Training Accuracy for max Depth = 3 :{Training_accuracy_3 : .4f} % \n")
    print(f"Training Accuracy for max Depth = None :{Training_accuracy_None : .4f} % \n")

    underfit_threshold = 70
    overfit_threshold = 10

    accuracy_difference_1 = Training_accuracy_1 - Testing_accuracy_1
    accuracy_difference_3 = Training_accuracy_3 - Testing_accuracy_3
    accuracy_difference_None = Training_accuracy_None - Testing_accuracy_None
    
    print(Border)

    if (Training_accuracy_1 < underfit_threshold and Testing_accuracy_1 < underfit_threshold):
          print("The model with max_depth = 1 is UNDERFITTING.")
    elif (accuracy_difference_1 > overfit_threshold ):
         print("The model with max_depth = 1 is OVERFITTING.")
    else:
        print("The model with max_depth = 1 is WELL-FITTED.")
    
    print(Border)

    if (Training_accuracy_3 < underfit_threshold and Testing_accuracy_3 < underfit_threshold) :
         print("The model with max_depth = 3 is UNDERFITTING.")
    elif(accuracy_difference_3 > overfit_threshold):
        print("The model with max_depth = 3 is OVERFITTING.")
    else :
        print("The model with max_depth = 3 is WELL-FITTED.")
    
    print(Border)
    
    if (Training_accuracy_None < underfit_threshold and Testing_accuracy_None < underfit_threshold):
         print("The model with max_depth = None is UNDERFITTING.")
    elif (accuracy_difference_None > overfit_threshold):
        print("The model with max_depth = None is OVERFITTING.")
    else:
        print("The model with max_depth = None is WELL-FITTED.")

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
    model_1,model_3,model_None = Train_Model(X_Train,Y_Train)

    # Step 6 : Prediction    
    Y_test_pred_1,Y_test_pred_3,Y_test_pred_None, Y_train_pred_1,Y_train_pred_3,Y_train_pred_None =Evaluate_Test(model_1,model_3,model_None,X_Test,X_Train)

    # Step 7 : Accuracy Calculation
    Calculate_Accuracy(Y_Test,Y_Train,Y_test_pred_1,Y_test_pred_3,Y_test_pred_None, Y_train_pred_1,Y_train_pred_3,Y_train_pred_None)

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
            print("6 Prediction")
            print("7 Accuracy Calculation")

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