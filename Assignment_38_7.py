import matplotlib.pyplot as plt
import pandas as pd

def DrawScatterPlot(df):

    studyHours = df['StudyHours']

    previousScore = df['PreviousScore']

    plt.scatter(
        studyHours,
        previousScore,
        s = 100,
        marker = "o",
        alpha = 0.8,
        edgecolors = "black",
        linewidths = 1,
        label = "Students"
    )

    plt.title("Student's Scatter Plot")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)

    plt.legend()
    plt.show()

def main():

    df = pd.read_csv('student_performance_ml.csv')

    DrawScatterPlot(df)

if __name__ == "__main__":
    main()