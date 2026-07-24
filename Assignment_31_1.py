# Program - That accepts 
# 1) Message from the user
# 2) Time interval in seconds
# schedule the program that display the message repitedly after the specified interval
# validate that the interval grater than zero

import time
import schedule

def DisplayMessage(message):

    print(message)

def main():

    message = input("Enter Message : ")

    try:
        interval = float(input("Enter interval in seconds : "))
    
        if interval <= 0:

            print("Time interval Should be grater than Zero")            

            return
        
        schedule.every(interval).seconds.do(DisplayMessage,message)
        
        while True:

            schedule.run_pending()
            time.sleep(1)

    except ValueError as eOej:

        print("Please enter valid interval value : ",eOej)

if __name__ == "__main__":
    main()
