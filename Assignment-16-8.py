# Program - Accept number from user and 
# print that number of "*" on screen 

def main():
   
   No = int(input("Enter Number : "))

   for i in range(No):
      
      print(" * ",end=" ")

   print()


if __name__ == "__main__":
    main()