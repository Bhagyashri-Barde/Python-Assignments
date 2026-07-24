# Program - That performs File Backup every Hour
# Program Should -
# 1) Accept the source file path
# 2) Accept the destination directory path
# 3) Copy Source file to destination directory
# 4) Add the current date and time to the backup filename (Data_25_07_2026_16_30_00.txt)
# 5) Write Backup operation details into Backup_log.(Backup Log - Backup Completed Successfully at 25-07-2026 04:30:00 PM)
# Log file : backup_log.txt

import datetime
import schedule
import time
import os
import sys
import shutil

def FileBackup(fileName,directoryPath):
    Border = "-" * 60
    
    backupFileExtention = os.path.splitext(fileName)[1]

    logFileName = "backup_log.txt"

    backUpFileName = f"Data_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}{backupFileExtention}"


    destinationDirectoryPath = os.path.join(directoryPath,backUpFileName)
    
    if not os.path.exists(directoryPath):

        print("File Backup Automation Error : There is no such Directory with name ",directoryPath)
        
        return
    
    if not os.path.isdir(directoryPath):
        
         print("File Backup Automation Error : It is not a Directory with name ",directoryPath)
         
         return
    
    if not os.path.isfile(fileName):

        print("File Backup Automation Error : Source file does not exist.")
        
        return
    
    shutil.copy(fileName,destinationDirectoryPath)

    fObj = open(logFileName,"a")

    if os.path.getsize(logFileName) == 0:
        
        print("Log File gets created with name : ",logFileName,"\n")
        
        fObj.write(Border+"\n")
        fObj.write("File Backup Automation Script \n")
        fObj.write(Border+"\n\n")

    fObj.write(f"Backup Completed Successfully at {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
    
    print("Backup file gets created with name : ",backUpFileName,"\n")
    
    fObj.close()

def main():

    if (len(sys.argv) == 3):

        schedule.every(1).hours.do(FileBackup,sys.argv[1],sys.argv[2])
    
        while True:

            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("Invalid Number of Arguments")
        
if __name__ =="__main__":
    main()