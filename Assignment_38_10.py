import matplotlib.pyplot as plt
import pandas as pd

def DrawScatterPlot(df):

    SleepHours = df['SleepHours']

    FinalResult = df['FinalResult'] 

    plt.scatter(
        SleepHours,
        FinalResult,
        s = 100,
        marker = "o",
        alpha = 0.8,
        edgecolors = "black",
        linewidths = 1,
    )

    plt.title("Student's Scatter Plot")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")

    plt.yticks([0,1],['Fail','Pass'])

    plt.grid(True)
    
    plt.show()

def main():

    df = pd.read_csv('student_performance_ml.csv')

    DrawScatterPlot(df)

if __name__ == "__main__":
    main()