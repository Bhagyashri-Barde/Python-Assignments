# seek(Where,From) seek(Kuthe,Kuthun)
# From - 0/1/2
# 0 - Starting
# 1 - Current
# 2 - End

def main():
    try:

        fObj = open("Demo.txt","r")

        print("Fille gets opend...")

        Data = fObj.read()

        print("File Data:",Data)

        fObj.seek(10,0)

        Data1 = fObj.read()

        print("File Data : ",Data1)

        fObj.close()
        
    except FileNotFoundError as fobj:

        print("File not found...")

if __name__ =="__main__":
    main()
