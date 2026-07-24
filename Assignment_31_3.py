# Program - That scan a specified directory every minute
# The Task should display
# 1) Directory Name
# 2) Number of Files
# 3) Number of subdirectories
# 4) Date and time of Scanning
# use the os module

import time
import schedule
import os
import sys
import datetime

def DirectoryScanner(directoryPath):
   Border =  "-"*60
   totalFiles = 0
   totalSubFolders = 0

   if not os.path.exists(directoryPath):
        print("There is no such Directory with name ",directoryPath)
        
        return

   if not os.path.isdir(directoryPath):
        
         print("It is not a Directory with name ",directoryPath)
         
         return
   
   print(f"Scanning Directory...\n")

   for FolderName,SubFolder,FileName in os.walk(directoryPath):
      
      for subDir in SubFolder:
         
          totalSubFolders = totalSubFolders + 1
      
      for fName in FileName:
         
          totalFiles = totalFiles + 1
  
   print("Directory Name : ",directoryPath)
   print("Total Files : ",totalFiles)
   print("Total Subdirectories : ",totalSubFolders)
   print("Scan Time : ",datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p'))
   print(Border,"\n")

def main():
   Border =  "-"*60
    
   print(Border,"\n")
   print("Directory Traversal Automation Script")
   print(Border,"\n")

   if(len(sys.argv) == 2):
      if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):

        print("This automation script is used to traverse the directory")
        print("For better usage please check --u flag")
    
      elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
        
        print("Please execute the scipt as")
        print("Python fileName.py DirectoryName")
        print("Directory name should be absolute path")

      else:

        schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
        while True:
            schedule.run_pending()
            time.sleep(1)
   else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for More information")

if __name__ == "__main__":
    main()
