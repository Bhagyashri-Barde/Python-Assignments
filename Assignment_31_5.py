# Program - That accepts a directory name from user and
# Count the number of files inside it every 5 minutes
# Write the result into : DirectoryCountLog.txt
# Each entery should contain:
# 1) Directory Path
# 2) Number of Files
# 3) Date and time

import time
import schedule
import os
import sys
import datetime

def DirectoryScanner(directoryPath):
   Border =  "-"*60
   totalFiles = 0

   if not os.path.exists(directoryPath):
        
        print("There is no such Directory with name ",directoryPath)
        
        return

   if not os.path.isdir(directoryPath):
        
         print("It is not a Directory with name ",directoryPath)
         
         return

   for FolderName,SubFolder,FileName in os.walk(directoryPath):
     
      for fName in FileName:
         
          totalFiles = totalFiles + 1
   
   
   fObj = open("DirectoryCountLog.txt","a")

   if os.path.getsize("DirectoryCountLog.txt") == 0:
      
      print("Log File gets created with name : DirectoryCountLog.txt")
      fObj.write(Border+"\n")
      fObj.write("Directory Scan Automation Script \n")
      fObj.write(Border+"\n\n")
   
   print("DirectoryCountLog.txt gets updated")
   
   fObj.write(f"Directory Name : {os.path.abspath(directoryPath)} \n")
   fObj.write(f"Total Files : {totalFiles} \n")
   fObj.write(f"Date and Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} \n")
   fObj.write(Border+"\n\n")
   fObj.close()

def main():
   Border =  "-"*60
    
   print(Border,"\n")
   print("Directory Scan Automation Script")
   print(Border,"\n")

   if(len(sys.argv) == 2):
      if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):

        print("This automation script is used to traverse the directory")
        print("For better usage please check --u flag")
    
      elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
        
        print("Please execute the script as")
        print("Python fileName.py DirectoryName")
        print("Directory name should be absolute path")

      else:

        schedule.every(5).minutes.do(DirectoryScanner,sys.argv[1])
            
        while True:
            schedule.run_pending()
            time.sleep(1)
   else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for More information")

if __name__ == "__main__":
    main()
