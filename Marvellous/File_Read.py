def main():
    try:

        fObj = open("Demo.txt","r")

        print("Fille gets opend...")

        
        Data = fObj.read(10)

        print("Data From File : ",Data)

        fObj.close()
        
    except FileNotFoundError as fobj:

        print("File not found...")

if __name__ =="__main__":
    main()
