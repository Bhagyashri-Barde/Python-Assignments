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

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.3,random_state=42)

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

    model = DecisionTreeClassifier(max_depth= 3 ,random_state=None)

    model.fit(X_Train,Y_Train)

    print("Models Are Trained Successfully")

    return model

################################################################
# Step 6 : Predict and Calculate Accuracy
################################################################
def Evaluate_Test(model,X_Test,Y_Test,X_Train,Y_Train):

    print(Border)
    print("Step 7 : Predict and Compare Accuracy of Different Models")
    print(Border)

    Y_test_pred = model.predict(X_Test)

    testing_accuracy = accuracy_score(Y_Test,Y_test_pred) * 100

    Y_train_pred = model.predict(X_Train)

    training_accuracy = accuracy_score(Y_Train,Y_train_pred) * 100

    accuracy_difference = training_accuracy - testing_accuracy

    print("Testing Accuracy is :",testing_accuracy) 

    print("Trainig Accuracy is :",training_accuracy) 

    print(f"Accuracy Difference is : {accuracy_difference:.2f}\n") 

    return training_accuracy,testing_accuracy

def FinalResult(training_accuracy,testing_accuracy):

    if training_accuracy > testing_accuracy: 
        print("Result: Training accuracy is higher than testing accuracy.") 
        print("Reason:")
        print("1) The model may be overfitting the training data.") 
        print("2) It learns the training data well but makes some")
        print("incorrect predictions on unseen testing data.")

    elif training_accuracy < testing_accuracy: 
        print("Result: Testing accuracy is higher than training accuracy.") 
        print("Reason: The testing dataset may be easier to predict.")
    else: 
        print("Result: Training and testing accuracy are equal.\n") 
        print("The model shows no accuracy gap on these datasets.")

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


    # Step 6 :  Predict and Compare Accuracy of Different Models
    training_accuracy,testing_accuracy = Evaluate_Test(model,X_Test,Y_Test,X_Train,Y_Train)

    # Step 7 : Final Result
    FinalResult(training_accuracy,testing_accuracy  )
    

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

