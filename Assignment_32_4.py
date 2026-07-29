# Program - That copies all .txt files from one directory to another every 10 minutes
# The Program Should :
# 1) Accept source and destination directory
# 2) validate both directories
# 3) copy only .txt files
# 4) Maintain log of copied files
# 5) Avoid terminating one file cannot be copied


import time
import schedule
import os
import sys
import shutil

def CopyFiles(sourceDir,destinationDir):
    Border = "-"*60

    if not os.path.exists(sourceDir):

        print("File Automation Error : There is no such Directory with name ",sourceDir )
        return
    
    if not os.path.exists(destinationDir):
       
        print("File Automation Error : There is no such Directory with name ",destinationDir )
        return
    
    if not os.path.isdir(sourceDir):
        
        print("File Automation Error : It is not a Directory with name ",sourceDir)
        return
    
    if not os.path.isdir(destinationDir):
        
        print("File Automation Error : It is not a Directory with name ",destinationDir)
        return
    
    copiedFileCount = 0
    CopiedFileNames = []
    totalFiles = 0

    for FolderName,subFolder,FileName in os.walk(sourceDir):
        
        for filename in FileName:

            totalFiles = totalFiles + 1

            if filename.endswith(".txt"):

                sourceFile = os.path.join(FolderName,filename)
                destinationFile = os.path.join(destinationDir,filename)
                
                try:

                    shutil.copy(sourceFile,destinationFile)
                    CopiedFileNames.append(filename)
                    copiedFileCount = copiedFileCount + 1

                except Exception as e:

                    print(f"Unable to copy file : {filename}")
                    print(e)

    fObj = open("File_Copy_Log.txt","a")
    print("Log File gets Created Successfully")

    if os.path.getsize("File_Copy_Log.txt") == 0:

        fObj.write(Border+"\n")
        fObj.write("File Automation Script \n")
        fObj.write(Border+"\n\n")
   
    fObj.write(f"Total Files:{totalFiles}\n")
    fObj.write(f"Total Text Files Copied :{copiedFileCount}\n")
    fObj.write("Copied Files Name : \n")
    for file in CopiedFileNames:

        fObj.write(file + "\n")

    fObj.write(Border+"\n")      
    fObj.write(f"Date and Time : {time.strftime("%Y-%m-%d %H:%M:%S")}\n")
    fObj.write(Border+"\n")
    
    fObj.close()

def main():

    if(len(sys.argv) == 3):

        schedule.every(10).minutes.do(CopyFiles,sys.argv[1],sys.argv[2])

        while True:

            schedule.run_pending()

            time.sleep(1)
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()
