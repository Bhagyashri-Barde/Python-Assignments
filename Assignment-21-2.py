'''
Program - Design Python Application 
Create 2 Threads
1) Thread1 - Should display Maximum element from an list

2) Thread2 - Should display Minimum element from the same list
the list should be accepted from the user

'''
import threading 

def Maximum(Data):
    Max = Data[0]

    for no in Data:

        if Max < no:

            Max = no

    print("Maximum Number is : ",Max)

def Minimum(Data):
      Min = Data[0]

      for no in Data:

        if Min > no:

            Min = no

      print("Maximum Number is : ",Min)

def main():
    numList = list()

    eleCount = int(input("How many numbers you want to add in List : "))
    
    print("Enter Numbers : ",end="")

    for i in range(eleCount):
        
        numList.append(int(input()))
    
    print("List is :",numList)

    t1 = threading.Thread(target=Maximum,args=(numList,))

    t2 = threading.Thread(target=Minimum,args=(numList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()