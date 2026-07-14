'''
Program - implement a Class named BookStore with following Specification
1) Should Conatin 2 instance variables - Name(Book Name) ,Author (Book Author)
2) Should Conatin 1 class variable - NoOfBooks(initialize to 0)
3) Define a constructor (__init__) - accept Name and Author and initialize instance variable
4)Inside Constructor increment the class veriable NoOfBooks by 1 whenever new Object is Created
5) Implement an instance Method - Display() - Display Book Details in the Format : 
          <BookName> by <Author>. No Of Books : <NoOfBooks>
'''

class BookStore:
    #Class Veriable
    NoOfBooks = 0

    #Constructor
    def __init__(self,BookName,BookAuthor):
        
        #Instance Variable
        self.BookName = BookName

        self.BookAuthor = BookAuthor

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
    
    # Instance Method
    def Display(self):
        
        print()
        print(f"{self.BookName} by {self.BookAuthor}. No Of Books : {BookStore.NoOfBooks}")

# Object Creation  
bsObj1 = BookStore("Linux System Programming", "Robert Love")

# Method Call
bsObj1.Display()

bsObj2 = BookStore("C Programming", "Dennis Ritchie")

bsObj2.Display()

