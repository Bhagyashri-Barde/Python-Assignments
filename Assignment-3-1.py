# Program To Display
# 1) Data Type
# 2) Memoey Address
# 3) Size in bytes of a veriable enterd by the user

from sys import getsizeof

value = eval(input("Enter Your Variable : "))
print("\n ----- Output -----\n")
print("Data Type : ",type(value))                   # Data Type
print("Memory Address : ", id(value))               # Memory Address
print("Size in bytes :",getsizeof(value))           # Size in  bytes
