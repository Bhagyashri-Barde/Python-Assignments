# Duplicate File Removal Automation Using Python

######################################################
#
# Import Required Libraries
#
#####################################################
import sys
import os
import re
import hashlib
import time
import smtplib
import datetime
from email.message import EmailMessage
import config
import schedule
######################################################################
#
#  Function Name  : CalculateCheckSum
#  Input          : FileName
#  Description    : Calculates the checksum of the specified file
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################

def CalculateCheckSum(fileName):
    try:
        fObj = open(fileName,"rb")
        # print("File open in binary mode")
        hObj = hashlib.md5()

        Buffer = fObj.read(1024)

        while(len(Buffer)>0):

            hObj.update(Buffer)

            Buffer = fObj.read(1024)

        fObj.close()

        return hObj.hexdigest() 
    except FileNotFoundError as e:
        print(f"Error: File '{fileName}' not found.")
        return None
    except Exception as e:
        print(f"Error while calculating checksum: {e}")
        return None

######################################################################
#
#  Function Name  : FindDuplicate
#  Input          : DirectoryPath
#  Description    : Returns a dictionary containing duplicate files grouped by their checksum
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################


def FindDuplicate(directoryPath,details):

    Duplicate = {}
    details['Directory Scanned'] = os.path.abspath(directoryPath)

    Start_time = datetime.datetime.now()
    details['Starting Time of Scanning'] = Start_time.strftime("%d %B %Y, %I:%M:%S %p")
    totalFiles = 0
    
    for FolderName,SubFolder,FileName in os.walk(directoryPath):
        for filename in FileName:
                totalFiles = totalFiles + 1
                filename = os.path.join(FolderName,filename)
                
                checksum =  CalculateCheckSum(filename)
                if checksum is not None:
                    if checksum in Duplicate:
                        
                        Duplicate[checksum].append(filename)

                    else:
                        
                        Duplicate[checksum] = [filename]

    End_time = datetime.datetime.now()
    details['Completion Time of Scanning'] = End_time.strftime("%d %B %Y, %I:%M:%S %p")
    details['Total Number of Files Scanned'] = totalFiles

    return Duplicate  
 
######################################################################
#
#  Function Name  : updateLogFile
#  Input          : logFile, emailStatus
#  Description    : Updates the existing log file with the email
#                   delivery status after the email is sent.
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
####################################################################### 

def updateLogFile(logFile,emailStatus):
    Border = "-" * 60
    logFile =os.path.abspath(logFile)
    fObj = open(logFile,"a")
    fObj.write("Email Delivery status : "+ emailStatus+"\n")
    fObj.write(Border+"\n")
    fObj.close() 


######################################################################
#
#  Function Name  : Send_Email
#  Input          : logFile, Details dictionary containing file operation details
#  Description    : Creates an SMTP connection, composes the email with
#                   the subject, message body, and log file attachment,
#                   and sends the email to the specified recipient.
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
####################################################################### 
def Send_Mail(logFile,details):
     # Sender Gmail address
    sender_email = config.sender_email
    # Google App Password (16 characters)
    app_password = config.app_password

    # Receiver Gmail address
    receiver_email = sys.argv[3]

    subject = "Duplicate File Removal Automation Report with Log File"

    body = """Jay Ganesh,

    The Duplicate File Removal operation has been completed successfully.

    Operation Statistics:

    """
    body = body + f"Starting time of Scanning : {details['Starting Time of Scanning']}\n"  
    body = body + f"  Completion time of Scanning : {details['Completion Time of Scanning']}\n"       
    body = body + f"  Directory Scanned : {details['Directory Scanned']}\n" 
    body = body + f"  Total Number of Files Scanned : {details['Total Number of Files Scanned']}\n" 
    body = body + f"  Total Number of Duplicate files found : {details['Total Duplicate Files Found']}\n" 
    body = body + f"  Total Number of duplicate files deleted : {details['Total Duplicate Files Deleted']}\n" 
    body += """Please find the detailed log file attached to this email.

    Regards,
    Marvellous Automation System
    """

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.set_content(body)
    try:

        with open(logFile, "rb") as fObj:
            print(fObj)
            msg.add_attachment(
                fObj.read(),
                maintype="text",
                subtype="plain",
                filename=os.path.basename(fObj.name)
            )   
        
        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login(sender_email,app_password)

        smtp.send_message(msg)
        smtp.quit()
        emailStatus = "Success"
        print("Mail Sent Successfully")
    except smtplib.SMTPAuthenticationError:
        emailStatus = "Failed - Authentication Error"
        print("Error :",emailStatus)
    except smtplib.SMTPConnectError:
        emailStatus = "Failed - Unable to Connect to SMTP Server"
        print("Error :",emailStatus)
    except Exception as e:
        emailStatus = f"Failed - {e}"
        print("Error :",emailStatus)
    
    updateLogFile(logFile,emailStatus)
    
######################################################################
#
#  Function Name  : maintainLogFiles
#  Input          : ErrorList, Details dictionary containing file operation details
#  Description    : Creates a folder for log files if it does not exist,
#                   creates a log file containing the file operation details,
#                   and stores the log file in that folder. 
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################    
def maintainLogFiles(errorList,details):
    Border = "-" * 60
    Ret = False
    Ret = os.path.exists("Marvellous")

    if(Ret == True):
         Ret = os.path.isdir("Marvellous")

         if(Ret == False):
            # print("Unable to proceed as directory name is existing but its not a directory")
             return
    else:
        os.mkdir("Marvellous")
       # print("Directory for the log file gets created successfully")
    
    timeStamp = time.strftime("%d_-%m_%Y_%H_%M_%S")

    fileName = os.path.join("Marvellous","DuplicateRemovalLog_%s.log" %timeStamp)

    fObj = open(fileName,"w")

    print(f"Log file gets succssfully created with name {fileName}")

    fObj.write(Border+"\n")
    fObj.write("--------------- Duplicate File Removal Script --------------\n")

    fObj.write(Border+"\n\n")
    fObj.write(f"Name of scanned Directory : {details['Directory Scanned']}\n")
    fObj.write(f"Starting Time of Directory scanning : {details['Starting Time of Scanning']}\n")
    fObj.write(f"Completion of Directory scanning : {details['Completion Time of Scanning']}\n")
    fObj.write(f"Total number of files scanned : {details['Total Number of Files Scanned']}\n")
    fObj.write(f"Total number of duplicate files: {details['Total Duplicate Files Found']}\n")
    fObj.write(f"Total number of duplicate files deleted : {details['Total Duplicate Files Deleted']}\n")
    if details.get("Total Duplicate Files Deleted"):
       if len(details.get("Deleted Files")):
            fObj.write(Border+"\n")
            fObj.write("Deleted Duplicate Files:\n")
            fObj.write("\n")
            for file in details.get("Deleted Files"):
                fObj.write(file+"\n")

    fObj.write(Border+"\n")
    if len(details.get("Checksum")) > 0:
        fObj.write("CheckSum values of Duplicate Files:\n")
        fObj.write("\n")
        for data in details.get("Checksum"):
            fObj.write(data+"\n")
        fObj.write(Border+"\n")

    if(len(errorList)==0):
        fObj.write("Errors Encountered During Execution : No errors encountered.\n")
    else:
        fObj.write("Errors Encountered During Execution :\n")
        fObj.write(Border+"\n")
        for error in errorList:
            fObj.write(error+"\n")
        fObj.write(Border+"\n")
    fObj.close()
    Send_Mail(fileName,details)

######################################################################
#
#  Function Name  : DeleteDuplicate
#  Input          : DirectoryPath
#  Description    : Deletes duplicate files from the duplicate file dictionary
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################

def DeleteDuplicate(directoryPath):
    errorList = []
    details = {}
    duplicateFilesCheckSum = []
    FileDict = FindDuplicate(directoryPath,details)
    print("FileDict :",FileDict)
    Result = list(filter(lambda x : len(x) > 1,FileDict.values() ))
    for key, value in FileDict.items():
        if len(value) > 1:
            duplicateFilesCheckSum.append(key)
    Count = 0
    TotalDeleted = 0
    TotalDuplicateFiles = 0
    deletedFiles = []
    for value in Result:
        TotalDuplicateFiles = TotalDuplicateFiles + len(value) - 1
        for subValue in value:
             Count = Count + 1
            
             if Count > 1:
                # print("Duplicate Found : ",subValue)
                try:
                    deletedFiles.append(subValue)
                    TotalDeleted = TotalDeleted + 1
                    os.remove(subValue)
                except PermissionError:
                     errorList.append(f"Permission denied: {subValue}")
                except OSError as e:
                    errorList.append(f"Unable to delete {subValue}: {e}")
                 
                
        
        Count = 0
    
    details['Total Duplicate Files Deleted'] = TotalDeleted
    details['Deleted Files'] = deletedFiles
    details['Checksum'] = duplicateFilesCheckSum
    details['Total Duplicate Files Found'] = TotalDuplicateFiles

    maintainLogFiles(errorList,details)


########################################################
#
#  Function Name  : main
#  Input          : Command Line Arguments
#  Description    : It controls the script,Check number of arguments,Validate directory path
#                   Validate time interval, Validate email address
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
########################################################
def main():
    Border = "-" * 70
    
    if(len(sys.argv) == 4):
        print(Border)
        print("Duplicate File Removal Automation")
        print(Border,"\n")

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" or sys.argv[1] == '--help'):
           
            print("This script scan a directory,identify a duplicate files using checksum,")
            print("delete duplicate files,creates a log file, and sends the log file through email\n")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U" or sys.argv[1] == '--usage'):
           
            print("Please execute the scipt as \n")
            print("python3 DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMintutes> <ReceiverEmailAddress>")
        else:  
            pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

            if  not os.path.exists(sys.argv[1]):
                print("Duplicate File Removal Automation Error : There is no such Directory with name :  ",sys.argv[1])
                return
            if not os.path.isdir(sys.argv[1]):
                print("Duplicate File Removal Automation Error : It is not a Directory with name :  ",sys.argv[1])
                return
            if not os.path.isabs(sys.argv[1]):
                print("Duplicate File Removal Automation Error : Please provide an absolute path.")
                return
            if not os.access(sys.argv[1],os.W_OK | os.X_OK):
                print("Duplicate File Removal Automation Error : Permission denied.")
                return
            if (not sys.argv[2].isdigit()) or (int(sys.argv[2]) <= 0):
                print("Duplicate File Removal Automation Error : Time interval must be a numeric value and grater than Zero.")
                return
            if not re.fullmatch(pattern, sys.argv[3]):
                print("Invalid Email Address")
                return 
            schedule.every(1).minutes.do(DeleteDuplicate,sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
            
    else:
        print("Invalid Number of Arguments\n")
        print("Please use --h or --u for More information")
        
    print(Border)
    print("Thank you for using Duplicate File Removal Automation Script")
    print(Border)
    
    

########################################################
#
# Starter of the automation Script
#
########################################################
if __name__ == "__main__":
    main()