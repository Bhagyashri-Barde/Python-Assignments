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

    random_state_0_model = DecisionTreeClassifier(max_depth= 3,random_state=0)

    random_state_0_model.fit(X_Train,Y_Train)

    random_state_10_model = DecisionTreeClassifier(max_depth= 3,random_state=10)

    random_state_10_model.fit(X_Train,Y_Train)

    random_state_42_model = DecisionTreeClassifier(max_depth= 3 ,random_state=42)

    random_state_42_model.fit(X_Train,Y_Train)

    print("Models Are Trained Successfully")

    return random_state_0_model, random_state_10_model, random_state_42_model

################################################################
# Step 6 : Predict and Compare Accuracy of Different Models
################################################################
def Compare_Accuracy(random_state_0_model,random_state_10_model,random_state_42_model,X_Test,Y_Test):

    print(Border)
    print("Step 7 : Predict and Compare Accuracy of Different Models")
    print(Border)

    Y_test_pred_0 = random_state_0_model.predict(X_Test)
    Y_test_pred_10 = random_state_10_model.predict(X_Test)
    Y_test_pred_42 = random_state_42_model.predict(X_Test)

    Testing_accuracy_0 = accuracy_score(Y_Test,Y_test_pred_0) * 100
    Testing_accuracy_10 = accuracy_score(Y_Test,Y_test_pred_10) * 100
    Testing_accuracy_42 = accuracy_score(Y_Test,Y_test_pred_42) * 100

    print(f"Testing Accuracy for Random State = 0:{Testing_accuracy_0 : .4f} % \n")
    print(f"Testing Accuracy for Random State = 10:{Testing_accuracy_10 : .4f} % \n")
    print(f"Testing Accuracy for Random State = 42:{Testing_accuracy_42 : .4f} % \n")

    if Testing_accuracy_0 == Testing_accuracy_10 == Testing_accuracy_42: 
       
        print("Result: Testing accuracy is the same for all random states.") 

    else: 
        
        print("Result: Testing accuracy changes for different random states.")


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
    random_state_0_model,random_state_10_model,random_state_42_model = Train_Model(X_Train,Y_Train)


    # Step 6 :  Predict and Compare Accuracy of Different Models
    Compare_Accuracy(random_state_0_model,random_state_10_model,random_state_42_model,X_Test,Y_Test)

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

