import os
def main():
    try:
        
        # Not Appicable
        # fObj = open("Demo.txt","r")

        # fObj.remove()

         os.remove("Demo.txt")
        
    except FileNotFoundError as fobj:

        print("File not found...")

if __name__ =="__main__":
    main()
