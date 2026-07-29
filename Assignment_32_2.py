# Program - That Monitorize the size of specified file every 30 seconds
# write following details into FileSizeLog.txt
# 1) File Path
# 2) File size in bytes
# 3) Date and time
# handle the situation where the file does not exist

import time
import schedule
import datetime
import os
import sys

def ChkFileSize(fileName):
    Border = "-" * 60

    if not os.path.exists(fileName):

        print("File is not exist...")

        return

    fObj = open("FileSizeLog.txt","a")

    if os.path.getsize("FileSizeLog.txt") == 0:
      
      fObj.write(Border+"\n")
      fObj.write("File Automation Script \n")
      fObj.write(Border+"\n\n")

    print("Log File gets Created Successfully")


    fObj.write(f"File Name : {os.path.abspath(fileName)}\n")
    fObj.write(f"File Size in bytes : {os.path.getsize(fileName)} bytes\n")
    fObj.write(f"Date and Time : {datetime.datetime.now().strftime('%d-%M-%Y %I:%M:%S %p')}\n")
        
    fObj.write(Border+"\n")

    fObj.close()

def main():
    if(len(sys.argv) == 2):
        
        schedule.every(30).seconds.do(ChkFileSize,sys.argv[1])

        while True:

            schedule.run_pending()

            time.sleep(1)
    else:

        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()
