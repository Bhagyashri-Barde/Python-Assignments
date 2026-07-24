# Program - Schedule a task that executes every 5 mintutes
# Task should write a current date and time into a file 
# named: Marvellous.txt
# new entries should be appended without removing previous enteries

import schedule
import time
import datetime
import os
import sys

def Display(FileName):
    Border =  "-" * 60      

    fObj = open(FileName,"a")

    if os.path.getsize(FileName) == 0:

        fObj.write(Border + "\n")

        fObj.write("Date And Time Automation Script\n")

        fObj.write(Border + "\n")
            
        
    currentDatetime = datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
       
    fObj.write(f"Task Executed At : {currentDatetime}"+"\n")

    fObj.close()

def main(): 
        
        if(len(sys.argv) == 2):

            schedule.every(5).minutes.do(Display,sys.argv[1])

            while True:
            
                schedule.run_pending()
            
                time.sleep(1)
        else:
              print("Invalid Number of Arguments")

if __name__ =="__main__":
    main()