# Program - Accept Marks and Dispaly grade 
# 1) >= 75 -> Distinction 
# 2) >= 60 -> First Class 
# 3) >= 50 -> Second Class
# 4) < 50 -> Fail

def DisplayGrade(marks):

    if(marks >= 75):

        return "Distiction"
    
    elif(marks >=60 and marks < 75):

        return "First Class"
    
    elif(marks >= 50 and marks < 60):

        return "Second Class"
    
    else:

        return "Fail"
    
def main():
    Marks = int(input("Enter Marks : "))

    Grade = DisplayGrade(Marks)

    print("Grade : ",Grade)

if __name__ == "__main__":
    main()