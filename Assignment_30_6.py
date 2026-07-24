# Program - Script that schedules the following task
# 1) Print Lunch Time! every day at 1:00 PM
# 2) Print Wrap up work every day at 6:00 PM
# Both functions handled by seprate functions

import schedule
import time

def LuchBreakMessage():
   
   print("Lunch Time!")

def WrapUpInMessage():
     
     print("Wrap up work")

def main(): 
    
    schedule.every().day.at("13:00").do(LuchBreakMessage)

    schedule.every().day.at("18:00").do(WrapUpInMessage)
    
    while True:

        schedule.run_pending()
            
        time.sleep(1)
        
if __name__ =="__main__":
    main()