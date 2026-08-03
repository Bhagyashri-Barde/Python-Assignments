######################################################
#
# Import Required Libraries
#
#####################################################

import sys
import psutil
import time

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
            info = proc.as_dict(attrs=["pid","name","username"])
    
            listProcess.append(info)

        except psutil.AccessDenied as ad:

            print("Access Denied")

        except psutil.NoSuchProcess as np:
            
            print("Not Such Process")

    ProcessServillence(listProcess)

######################################################################
#
#  Function Name  : RunningProcessScan
#  Input          : ProcessName
#  Description    : Fetches and returns information about the specified process if it is running.
#  Date           : 01/08/2026
#  Author        : Bhagyashri Manoj Barde
#
#######################################################################

def RunningProcessScan(processName):
    
    listProcess = []
    
    for proc in psutil.process_iter():

        try:
            if processName.casefold() == proc.name().casefold():

                if proc.status() == psutil.STATUS_RUNNING:
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
                    ProcessServillence(listProcess)
                else:
                    print("Process is not running")

                return

        except psutil.AccessDenied as ad:

            print("Access Denied")

        except psutil.NoSuchProcess as np:

            print("Not Such Process")

    print("Process not found")

######################################################################
#
#  Function Name  : ProcessServillence
#  Input          : Data
#  Description    : Generates a log file containing running process information         
#  Date           : 01/08/2026
#  Author         : Bhagyashri Manoj Barde
#
#######################################################################
    
def ProcessServillence(Data):
    Border = "-" * 60

    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    fileName = f"Marvellous_{timeStamp}.log"

    fObj = open(fileName,"w")

    print(f"Log file gets succssfully created with name {fileName}")

    fObj.write(Border+"\n")
    fObj.write("----- Platform Servillence System -----\n")
    fObj.write("Log file gets created at : "+timeStamp+"\n")
    fObj.write(Border+"\n\n")

    fObj.write("--------------- Process Report ---------------\n")

    for info in Data:

        fObj.write(f"PID : {info.get("pid")}\n")
        fObj.write(f"Name : {info.get("name")}\n")
        fObj.write(f"User Name : {info.get("username")}\n")

        if(info.get("status") == psutil.STATUS_RUNNING):

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
    fObj.write("--------------- End of Log file ---------------\n")
    fObj.write(Border+"\n")

    fObj.close()

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

    if(len(sys.argv) == 1):

        ProcessScan()

    elif(len(sys.argv) == 2):
         # --h and --u handling
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
           
            print("This automation script is used to Show Process Information")
            print("1 : It fetch information of all running processes if no process name is provided.")
            print("1 :  It fetch information of the specified process if the process name is provided and it is running.")
            print("6 : It maintains all records into log file")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} : Fetch information of all running processes.")
            print()
            print(f"python {sys.argv[0]} Process_Name : Fetch information of the specified process if it is running.")
        else:

            RunningProcessScan(sys.argv[1])

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