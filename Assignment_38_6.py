import matplotlib.pyplot as plt
import pandas as pd

def PlotHisTogram(df):

    studyHours = df['StudyHours']

    plt.hist(
        studyHours,               # Continuos data
        bins = 6,                 # number of groups
        edgecolor = "Black",      # Border color
        alpha = 0.8,              # Transparancy
        rwidth = 0.9,             # Relative width of Bars
    )

    plt.title("Study Hours Histogram")
    plt.xlabel("Study Hours")
    plt.ylabel("Frequncy")

    plt.show()

def main():

    df = pd.read_csv('student_performance_ml.csv')
    
    PlotHisTogram(df)

if __name__ == "__main__":
    main()