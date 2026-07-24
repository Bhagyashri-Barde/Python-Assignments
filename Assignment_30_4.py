# Program - Create Task that executes 
# every day at 9:00 AM and Prints Namaskar...

import schedule
import time

def Display():

    print("Namaskar...")

def main(): 
    
    schedule.every().day.at("09:00").do(Display)

    while True:
        
        schedule.run_pending()
        
        time.sleep(1)

if __name__ =="__main__":
    main()