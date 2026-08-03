######################################################
#
# Import Required Libraries
#
#####################################################

from email.message import EmailMessage
from logging import config
import sys
import psutil
import os
import time
import smtplib
import config

######################################################################
#
#  Function Name  : ProcessScan
#  Input          : None
#  Description    : Fetch information about all running processes using
#                   the psutil.process_iter() method and returns
#                   the collected process details.
#  Date           : 01/08/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################

def ProcessScan():
    listProcess = []

    for proc in psutil.process_iter():
        
        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])
            
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["exe"] = proc.exe()
            info["memory_info"] = proc.memory_info()
            info["ppid"] = proc.ppid()
            info["create_time"] = proc.create_time()
            info["num_threads"] = proc.num_threads()
            info["cwd"] = proc.cwd()
            info["open_files"] = proc.open_files()
            info["net_connections"] = proc.net_connections()
            info["nice"] = proc.nice()
            info["environ"] = proc.environ()

            listProcess.append(info)

        except psutil.AccessDenied as ad:

            print("Access Denied")

        except psutil.NoSuchProcess as np:

            print("Not Such Process")

    return listProcess

######################################################################
#
#  Function Name  : ProcessServillence
#  Input          : FolderName,Email(default: None)
#  Description    : Checks the specified directory, creates it if it does not exist
#                   generates a log file containing running process information
#                   and emails the log file if an email address is provided.
#  Date           : 01/08/2026
#  Author         : Bhagyashri Manoj Barde
#
#######################################################################

def ProcessServillence(FolderName,Email = None):
    Border = "-" * 50
    
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
         Ret = os.path.isdir(FolderName)

         if(Ret == False):
             print("Unable to proceed as directory name is existing but its not a directory")
             return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully")

    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    fileName = os.path.join(FolderName,"Marvellous_%s.log" %timeStamp)

    fObj = open(fileName,"w")

    print(f"Log file gets succssfully created with name {fileName}")

    fObj.write(Border+"\n")
    fObj.write("----- Process Servillence System -----\n")
    fObj.write("Log file gets created at : "+timeStamp+"\n")
    fObj.write(Border+"\n\n")

    fObj.write("--------------- Process Report ---------------\n")

    Data = ProcessScan()

    for info in Data:

        fObj.write(f"PID : {info.get("pid")}\n")
        fObj.write(f"Name : {info.get("name")}\n")
        fObj.write(f"User Name : {info.get("username")}\n")
        fObj.write(f"Status : {info.get("status")}\n")
        fObj.write(f"CPU Usage : {info.get("cpu_percent")}\n")
        fObj.write(f"RAM Usage : {info.get("memory_percent")}\n")
        fObj.write(f"Creation Time : {info.get("create_time")}\n")
        fObj.write(f"Memory Details : {info.get("memory_info")}\n")
        fObj.write(f"Execution path : {info.get("exe")}\n")
        fObj.write(f"Parent PID : {info.get("ppid")}\n")
        fObj.write(f"Number of Threads : {info.get("num_threads")}\n")
        fObj.write(f"Current Working Directory :{info.get("cwd")}\n")
        fObj.write(f"Network Connections : {info.get("net_connections")}\n")
        fObj.write(f"Process Priority :{info.get("nice")}\n")
        fObj.write(f"Environment Variables : {info.get("environ")}\n")
        
        
        if(len(info.get("open_files")) == 0):

            fObj.write("Open Files : None \n")

        else:

            fObj.write(Border+"\n")
            fObj.write("Open Files : \n")
            fObj.write(Border+"\n")

            for data in info.get("open_files"):

                fObj.write(f"{data.path}\n")
        
        fObj.write(Border+"\n")

    fObj.write(Border+"\n")
    fObj.write("--------------- End of Log file ---------------\n")
    fObj.write(Border+"\n")

    fObj.close()

    Send_Mail(fileName,Email)

######################################################################
#
#  Function Name  : Send_Email
#  Input          : logFile, EmailID
#  Description    : Creates an SMTP connection, composes the email with
#                   the subject, message body, and log file attachment,
#                   and sends the email to the specified recipient.
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
####################################################################### 

def Send_Mail(logFile,emailid):
    
     # Sender Gmail address
    sender_email = config.sender_email

    # Google App Password (16 characters)
    app_password = config.app_password

    # Receiver Gmail address
    receiver_email = emailid

    subject = "Platform Servillence System Report with Log File"

    body = """Jay Ganesh,

    The Process Surveillance System report was generated successfully..


    """

    body += """Please find the detailed log file attached to this email containing the details of the running processes.

    Regards,
    Marvellous Automation System
    """

    msg = EmailMessage()

    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.set_content(body)
    emailStatus = ""
    try:

        fObj = open(logFile, "rb") 

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

########################################################
#
#  Function Name  : main
#  Input          : Command Line Arguments
#  Description    : It controls the script
#  Date           : 29/07/2026
#  Author        : Bhagyashri Manoj Barde
#
########################################################
def main():
    Border = "-" * 50

    print(Border)
    print("----- Platform Servillence System -----")
    print(Border)

    if(len(sys.argv) == 2):
         # --h and --u handling
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
           
            print("This automation script is used to Show Process Information")
            print("1 : It fetchs the information of running processes")
            print("2 : It maintains all process information in the log file.")
            print("3 : It creates the directory if the specified directory does not exist")
            print("4 : It stores log file in the specified directory")
            print("5 : It sends the log file to the specified email address (if provided)")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Folder_Name :")
            print("Creates a log file and stores it in the specified folder.")
            print()
            print(f"python {sys.argv[0]} Folder_Name EmailID: ")
            print("Creates a log file, stores it in the specified folder")
            print("and sends the log file to the specified email address.")
            
        else:

            ProcessServillence(sys.argv[1])

    elif(len(sys.argv) == 3):
            
            ProcessServillence(sys.argv[1],sys.argv[2])
    else:

        print("Invalid number of arguments")
        print("Unable to procced as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("Thank You For Using Our Automation System")
    print(Border)

########################################################
#
# Starter of the automation Script
#
########################################################

if __name__ =="__main__":
    main()