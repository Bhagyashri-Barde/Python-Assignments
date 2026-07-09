'''
Program - Design Python Application 
Create 2 Threads
1) Prime - Should display all Prime numbers from the list

2) NonPrime - Should display all Non Prime numbers from the list

Both threadsshould accept list of integers

'''
import threading 

def Prime(Data):
    primeList = list()
   
    for no in Data:
         
         Count = 0

         for i in range(1,no + 1):
             
             if no % i == 0:
                 
                 Count = Count + 1

         if Count == 2:
             
             primeList.append(no)
        
    print("List of Prime Numbers : ",primeList)

def NonPrime(Data):
    NonprimeList = list()

    for no in Data:
         
         Count = 0

         for i in range(1,no + 1):
             
             if no % i == 0:
                 
                 Count = Count + 1

         if Count != 2:
             
             NonprimeList.append(no)

    print("List of Non Prime Numbers : ",NonprimeList)
    
def main():
    numList = [4,5,9,11,21,17,63,27,29,2]

    print("List of Numbers : ",numList)

    t1 = threading.Thread(target=Prime,args=(numList,))

    t2 = threading.Thread(target=NonPrime,args=(numList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()