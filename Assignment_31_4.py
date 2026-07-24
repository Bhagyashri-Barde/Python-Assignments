# Program - That creates a new log File every 10 mintutes
# The File name should contain current date and time : MarvellousLog_25_07_2026_16_30_00.txt
# The File Should contain : 
# Log file created successfully
# creation Time : 25-7-2026 04:30:00 PM

import time
import schedule
import os
import sys
import datetime

def LogFileCreation():
   Border = "-" * 60
   logFileName = f"MarvellousLog_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"
   fObj = open(logFileName,"w")

   print("Log File gets created with name : ",logFileName)
   
   if os.path.getsize(logFileName) == 0:
      fObj.write(Border+"\n")
      fObj.write("Marvellous Automation Script \n")
      fObj.write(Border+"\n\n")

   fObj.write("Log file created successfully. \n")
   fObj.write(f"Creation Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")
   fObj.close()

def main():

        schedule.every(10).minutes.do(LogFileCreation)
            
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
