'''
Program - Accept 1 Number and Display Below Pattern
Input - 5
Output -  1   2   3   4   5
          1   2   3   4   5
          1   2   3   4   5
          1   2   3   4   5
          1   2   3   4   5
''' 
def Display(No):
   
   for i in range(1,No + 1):
      
      print(f"{i}   ",end="")

   print()  
   
def main():

    No = int(input("Enter Number : "))

    for i in range(No):
      
      Display(No)
    
if __name__ == "__main__":
    main()

