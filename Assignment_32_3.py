# Program - That reads and displays a content of specified text file every minute
# Handle the following conditions
# 1) File does not exist
# 2) File is empty
# 3) permision is denied
# 4) File can not be opened

import time
import schedule
import os
import sys

def ReadFile(fileName):
    try :
        if not os.path.exists(fileName):
            raise FileNotFoundError

        if os.path.getsize(fileName) == 0:
            print("File is Empty")
            return

        fObj = open(fileName,"r")
        Data = fObj.read()
        print(Data)
        fObj.close()
 
    except FileNotFoundError as fnfobj:
      
      print("Error : File not found...",fnfobj)

    except PermissionError as peobj:

        print("Error : Permission denied.",peobj)

    except OSError as oseobj:

        print("Error : File cannot be opened.",oseobj)
        

def main():
    if(len(sys.argv) == 2):

        schedule.every(1).minute.do(ReadFile,sys.argv[1])

        while True:

            schedule.run_pending()

            time.sleep(1)
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()
