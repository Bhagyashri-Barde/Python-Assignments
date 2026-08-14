import matplotlib.pyplot as plt
import pandas as pd

def DrawScatterPlot(df):

    AssignmentsCompleted = df['AssignmentsCompleted']

    FinalResult = df['FinalResult']

    plt.scatter(
        AssignmentsCompleted,
        FinalResult,
        s = 100,
        marker = "o",
        alpha = 0.8,
        edgecolors = "black",
        linewidths = 1,
    )

    plt.title("Student's Scatter Plot")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")
    plt.grid(True)

    plt.show()

def main():

    df = pd.read_csv('student_performance_ml.csv')

    DrawScatterPlot(df)

if __name__ == "__main__":
    main()