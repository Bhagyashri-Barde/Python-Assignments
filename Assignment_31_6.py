# Program - That schedules the following messages
# 1) Monday at 9:00 AM : Start your weekly goals
# 2) wednesday at 5:00 PM : Review your weekly progress
# 3) Friday at 6:00 PM : Weekly work completed

import time
import schedule
import os
import sys
import datetime

def MondayMessage():
    
    print("Start your weekly goals")

def WednesdayMessage():
     
     print("Review your weekly progress")

def FridayMessage():
     
     print("Weekly work completed")

def main():

   schedule.every().monday.at("09:00").do(MondayMessage)

   schedule.every().wednesday.at("17:00").do(WednesdayMessage)
   
   schedule.every().friday.at("18:05").do(FridayMessage)
            
   while True:
      schedule.run_pending()
      time.sleep(1)

if __name__ == "__main__":
    main()
