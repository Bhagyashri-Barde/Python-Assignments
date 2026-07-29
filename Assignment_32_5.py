# Program - That deletes all empty files from a specified directory every hour
# The Program Should : 
# 1) Scan the directory recursively
# 2) Detect files whoes size is zero bytes
# 3) Delete all empty files
# 4) Store deleted files path in a log file
# 5) Handle permissions Error


import time
import schedule
import os
import sys
import shutil

def DeleteFiles(directoryPath):
    Border = "-"*60

    if not os.path.exists(directoryPath):

        print("File Automation Error : There is no such Directory with name ",directoryPath )
        return
    
    if not os.path.isdir(directoryPath):
       
        print("File Automation Error : It is not a Directory with name ",directoryPath)
        return
   
    totalDeletdfiles = 0
    deltedFiles = []
    totalFiles = 0

    for FolderName,subFolder,FileName in os.walk(directoryPath):
        
        for filename in FileName:

            totalFiles = totalFiles + 1

            deletedfilepath = os.path.join(FolderName,filename)
            
            if(os.path.getsize(deletedfilepath) == 0):
               
                try:
                   
                    deltedFiles.append(deletedfilepath)
                    os.remove(deletedfilepath)
                    totalDeletdfiles = totalDeletdfiles + 1

                except PermissionError as e:

                    print(f"Permission denied : {filename}")
                    print(e)

                except OSError as e:

                    print(f"Unable to Delete file : {filename}")
                    print(e)

    fObj = open("File_Delete_Log.txt","a")
    print("Log File gets Created Successfully")

    if os.path.getsize("File_Delete_Log.txt") == 0:

        fObj.write(Border+"\n")
        fObj.write("File Automation Script \n")
        fObj.write(Border+"\n\n")
   
    fObj.write(f"Total Files:{totalFiles}\n")
    fObj.write(f"Total Files Deleted :{totalDeletdfiles}\n")
    fObj.write("Deleted Files Name : \n")
    for file in deltedFiles:

        fObj.write(file + "\n")

    fObj.write(Border+"\n")      
    fObj.write(f"Date and Time : {time.strftime("%Y-%m-%d %H:%M:%S")}\n")
    fObj.write(Border+"\n")
    
    fObj.close()

def main():

    if(len(sys.argv) == 2):

        schedule.every(1).hour.do(DeleteFiles,sys.argv[1])

        while True:

            schedule.run_pending()

            time.sleep(1)
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()
