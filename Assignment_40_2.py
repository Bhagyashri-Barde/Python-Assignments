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

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(X_Train,Y_Train)


    print("Model Trained Successfully")

    return model
###################################################
# Step 6 : Prediction and Accuracy Check
###################################################


def Evaluate_Test(model,X_Test,X_Train,Y_Test,Y_Train):

    print(Border)
    print("Step 6 : Prediction and Accuracy Check")
    print(Border)

     # predict Testing model
    Y_test_pred = model.predict(X_Test)

    # predict Training model
    Y_train_pred = model.predict(X_Train)

    print("Model Testing Done \n")

    print("Testing Model Prediction: ")

    print(Y_test_pred,"\n")

    print("Training Model Prediction: ")
    print(Y_train_pred)

    Testing_accuracy = accuracy_score(Y_Test,Y_test_pred) * 100

    Training_accuracy = accuracy_score(Y_Train,Y_train_pred) * 100

    return  Testing_accuracy, Training_accuracy

###################################################
# Step 7 : Remove SleepHours and Retrain the Model
###################################################

def Remove_SleepHours_Train_AccuracyCheck(df):
    
    print(Border)
    print("Step 6 : Remove SleepHours and Retrain the Model")
    print(Border)
     
    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"
    ]

    X_new = df[feature_cols]
    Y_new = df["FinalResult"]

    print("X Shape : ",X_new.shape)
    print("Y Shape : ",Y_new.shape)

    X_Train_New, X_Test_New, Y_Train_New, Y_Test_New = train_test_split(
        X_new,
        Y_new,
        test_size=0.3,
        random_state=42
    )

    model_new = DecisionTreeClassifier(max_depth=3 ,random_state=42)

    model_new.fit(X_Train_New, Y_Train_New)


    Y_test_Pred_New = model_new.predict(X_Test_New)

    Y_train_pred_New = model_new.predict(X_Train_New)

    print("Model Testing Done \n")

    print("Testing Model Prediction: ")
    print(Y_test_Pred_New,"\n")

    print("Training Model Prediction: ")
    print(Y_train_pred_New,"\n")

    Testing_accuracy_New = accuracy_score(Y_Test_New,Y_test_Pred_New) * 100

    Training_accuracy_New = accuracy_score(Y_Train_New,Y_train_pred_New) * 100

    return  Testing_accuracy_New, Training_accuracy_New

###################################################
# Step 8 : Display Final Result
###################################################

def DisplayResult(Testing_accuracy, Training_accuracy,Testing_accuracy_New, Training_accuracy_New):

    print(Border)
    print("Step 7 : Display Final Result")
    print(Border)

    print("Original Testing Accuracy :",Testing_accuracy)
    print("Original Treaning Accuracy :",Training_accuracy)

    print("Testing Accuracy for new Model:",Testing_accuracy_New)
    print("Treaning Accuracy for new Model:",Training_accuracy_New)

    if Testing_accuracy > Testing_accuracy_New:
        print("\nRemoving SleepHours decreased the performance.")

    elif Testing_accuracy < Testing_accuracy_New:
        print("\nRemoving SleepHours improved the performance.")

    else:
        print("\nRemoving SleepHours did not clearly affect the performance.")


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

    # Step 6 : Prediction and Accuracy Check
    Testing_accuracy, Training_accuracy = Evaluate_Test(model,X_Test,X_Train,Y_Test,Y_Train)

    # Step 7 :  Remove SleepHours and Retrain the Model
    Testing_accuracy_New, Training_accuracy_New = Remove_SleepHours_Train_AccuracyCheck(df)

    # Step 8 : Display Final Result
    DisplayResult(Testing_accuracy, Training_accuracy,Testing_accuracy_New, Training_accuracy_New)

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
            print("6 Prediction and Accuracy Check")
            print("7 Remove SleepHours and Retrain the Model")
            print("8 Display Final Result")

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