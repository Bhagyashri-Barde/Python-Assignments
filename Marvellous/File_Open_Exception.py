def main():
    try:

        open("Demo.txt","r")

        print("Fille gets opend...")
        
    except FileNotFoundError as fobj:

        print("File not found...")

if __name__ =="__main__":
    main()
