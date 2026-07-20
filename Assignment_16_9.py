# Program - Display first 10 Even Numbers on Screen

def main():
   
   print("First 10 Even Numbers : ")

   for no in range(2,(10 * 2 + 1),2):
       
       print(no,end=" ")

   print()

if __name__ == "__main__":
    main()