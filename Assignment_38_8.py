import matplotlib.pyplot as plt
import pandas as pd

def DrawBoxPlot(df):

    attendance = df['Attendance']

    plt.boxplot(
        attendance,
        widths = 0.9,
        showfliers = True,
        showbox = True,
        showmeans = True,
        vert = True,
        patch_artist = True

    )

    plt.title("Student's Box Plot")
    plt.ylabel("Attendance")
    plt.xticks([1], ['Attendance'])

    plt.show()

def main():

    df = pd.read_csv('student_performance_ml.csv')

    DrawBoxPlot(df)

if __name__ == "__main__":
    main()