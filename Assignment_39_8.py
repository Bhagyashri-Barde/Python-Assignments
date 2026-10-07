import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)

Border = "-" * 60
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

    print("Missing values per columns : ")
    print(df.isnull().sum())

    print("Class distribution (Final Result count) : ")
    print(df["FinalResult"].value_counts())

    print("Statistical report of dataset : ")
    print(df.describe())

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
# # Step 4 : Visualisation of Dataset
###################################################
def DataVisualization(df):

    print(Border)
    print("Step 4 : Visualisation of Dataset")
    print(Border)

    # Scatter plot
    plt.figure(figsize=(7,7))

    for sp in df["FinalResult"].unique():

        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["StudyHours"],temp["SleepHours"],label = sp)

    plt.title("Student Performance Case Study")

    plt.xlabel("Study Hours")
    plt.ylabel("Sleep Hours")

    plt.legend()
    plt.grid()
    plt.show()

###################################################
# Step 5 : Split the dataset for training and testing
###################################################

def SplitDataset(Features,Labels):

    print(Border)
    print("Step 5 : Split the dataset for training and testing")
    print(Border)

    X = Features
    Y = Labels

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Dataset Spliting Activity Done")

    print("X : ",X.shape)                    #(30,5)
    print("Y : ",Y.shape)                    #(30,)

    print("X_Train : ",X_Train.shape)        #(15,5)     
    print("X_Test : ",X_Test.shape)          #(15,5) 

    print("Y_Train : ",Y_Train.shape)        #(15,) 
    print("Y_Test : ",Y_Test.shape)          #(15,) 

    return X_Train,X_Test,Y_Train,Y_Test,X,Y

###################################################
# Step 6 : Build and Train the model
###################################################

def Train_Model(X_Train,Y_Train):

    print(Border)
    print("Step 6 :Build and Train the model")
    print(Border)

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(X_Train,Y_Train)

    print("Model Trained Successfully")

    return model

###################################################
# Step 7 : Prediction
###################################################

def Evaluate_Test(model,X_Test,Y_Test,X):

    print(Border)
    print("Step 7 : Prediction")
    print(Border)

    Y_pred = model.predict(X_Test)

    print("Model Testing Done")
    print("Expected Values : ")
    print(Y_Test)

    print("Predicted Values : ")
    print(Y_pred)

    plt.figure(figsize=[12,8])
    
    plot_tree(model,filled=True,feature_names= X.columns,class_names=['Fail','Pass'])
    
    plt.title("Student Performsnce Decision Tree Classifier")
    
    plt.show()

    return Y_pred
###################################################
# Step 8 : Accuracy Calculation
###################################################

def Calculate_Accuracy(Y_Test,Y_pred):

    print(Border)
    print("Step 8 : Accuracy Calculation")
    print(Border)

    accuracy = accuracy_score(Y_Test,Y_pred)
   
    print(f"Accuracy of model is :{accuracy * 100 : .2f} %")

###################################################
# Step 9 : Generate Confusion Matrix
###################################################

def Generate_ConfusionMatrix(Y_Test,Y_pred):

    print(Border)
    print("Step 9 : Generate Confusion Matrix")
    print(Border)

    print("Confussion matrix :")
    cm = confusion_matrix(Y_Test,Y_pred)
    print(cm)

###################################################
# Step 10 : Final Conclusion
###################################################
def Final_Result(Y_Test,Y_pred):

    print(Border)
    print("Step 10 : Final Conclusion")
    print(Border)

    print("Clasification report")
    print(classification_report(Y_Test,Y_pred))

def Execute_Ml_Pipeline():
    # Step 1 : Load the Dataset
    df =  LoadDataSet(sys.argv[1])
    
    # Step 2 : Data Analysis (EDA)
    DataAnalysis(df)


           
    # Step 3 : Decide Independent & Dependent Variables
    X,Y = SelectFeaturesAndLabels(df)

    # Step 4 : Visualisation of Dataset
    DataVisualization(df)

    # Step 5 : Split the dataset for training and testing
    X_Train,X_Test,Y_Train,Y_Test,X,Y = SplitDataset(X,Y)
           
    # Step 6 : Build and Train the model
    model = Train_Model(X_Train,Y_Train)

    # Step 7 : Prediction    
    Y_pred = Evaluate_Test(model,X_Test,Y_Test,X)
           
    # Step 8 : Accuracy Calculation
    Calculate_Accuracy(Y_Test,Y_pred)
           
    # Step 9 : Generate Confusion Matrix
    Generate_ConfusionMatrix(Y_Test,Y_pred)
    
    # Step 10 : Final Conclusion
    Final_Result(Y_Test,Y_pred)


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
            print("4 Visualize the Dataset")
            print("5 Split the dataset for training and testing")
            print("6 Build and Train the model")
            print("7 Prediction")
            print("8 Accuracy Calculation")
            print("8 Generate Confusion Matrix")
            print("8 Final Result")
            print("For better usage please check --u flag")
        
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