# Program - Displays the current date and time 
# after every 1 minute
# Expected Output = Current Date and Time 25-07-2026 04:30:00 PM

import schedule
import time
import datetime

def Display():

    print(f"Current Date and Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")

def main(): 
    
    schedule.every(1).minute.do(Display)

    while True:
        
        schedule.run_pending()
        
        time.sleep(1)

if __name__ =="__main__":
    main()