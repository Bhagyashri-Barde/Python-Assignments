'''
Program - Design Python Application 
Create 2 Threads
1) EvenList Thread - i) Should Extaect all Even numbers from the list
                    ii) Calculate and disply their sum
2) OddList Thread - i) Should Extaect all Odd numbers from the list
                    ii) Calculate and disply their sum

Both threads should accept list of integers as input
Threads should call concurrently

'''
import threading

def EvenList(Data):
    Sum = 0

    print("Even Numbers : ")

    for i in range(len(Data)):
        
        if Data[i] % 2 == 0:

            print(Data[i])

            Sum = Sum + Data[i]

    print("Summetion of Even Numbers :",Sum)  

def OddList(Data):
    Sum = 0

    print("Odd Numbers : ")

    for i in range(len(Data)):
        
        if Data[i] % 2 != 0:

            print(Data[i])

            Sum = Sum + Data[i]
            
    print("Summetion of Odd Numbers :",Sum)

def main():
    numList = [10,3,76,68,9,21,55,17,32,33]

    print("List is : ",numList)

    t1 = threading.Thread(target=EvenList,args=(numList,))

    t2 = threading.Thread(target=OddList,args=(numList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
