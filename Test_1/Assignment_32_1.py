# Program - That creates a new text file every minute 
# File should contain current timestamp - File_25_07_2026_16_30.txt
# write following information into it
# 1) FileName
# 2) Creattion date
# 3) Creation time

import time
import schedule
import datetime

def CreateFile():
    Border = "-" * 60
    fileName = f"File_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"
    fObj = open(fileName,"w")
    print("File Created Successfully...")
    fObj.write(Border+"\n")
    fObj.write("File Automation Script \n")
    fObj.write(Border+"\n\n")

    fObj.write(f"File Name : {fileName}\n")
    fObj.write(f"Creation Date : {datetime.datetime.now().strftime('%d-%m-%Y')}\n")
    fObj.write(f"Creation Time : {datetime.datetime.now().strftime('%I:%M:%S %p')}\n")
    
    fObj.write(Border+"\n")

    fObj.close()


def main():
    schedule.every(1).minute.do(CreateFile)

    while True:

        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()
