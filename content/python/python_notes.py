import datetime
import calendar
import os
import shutil
import zipfile

# conditional if, elif, else
x = input("what is x ")
y = input("what is y ")

if (str(x) < str(y)):
    print("X<Y")
elif (str(x)==str(y)):
    print("X=Y")
else:
    print("X>Y")


while (x==y):
    print(x)
# when x == y, it will print x

# when x is in range 5-9, if x=7, the function breaks, otherwise print x
for x in range(5,10):
    if (x==7): break # exit the loop
    print(x)

# when x is in range 5-9, if x=7, skip the function at 7, then print x
for x in range(5,10):
    if (x==7): continue # skip 7
    print(x)

# Lists
fruit = ["apple", "orange", "banana", "mango"]
for i, fr in enumerate(fruit): # enumerate add a number to the list
    print(i,fr)

for i in fruit:
    print(i) # iterate through the list

fruit[0] # list subscriptions get item from the list
fruit[0:3] # get items from 0,2,3; return as a list
fruit[-1] # get the last item in the list

# Range
for x in range(5,10): # range 5-9
    print(x) # 5,6,7,8,9
# range is non-inclusive, so 10 is not included but 5 is

# Print Function
print("Hello World")
# print always end with a newline, the end="" can be customized
print("Hello", end=" ") # ends with a space not on a newline
print("World", end='\r') # print everything in the same line

# Basic FileIO
f = open ("readfile.txt", "r", encoding='utf-8') # open the file in read mode, set encoding to ensure best compatibility
f.read() # read content of the file, including the \n newline
f.readline() # read line by line
f.readlines() # read all lines and return as a list
f.close() # close the file

'''Other File IO Modes
r: read
w: write and overwrite
a: append at the end
rb: read binary
wb: write binary and overwrite
ab: append binary
'''

# Write File
n = open ("writefile.txt", "a", encoding='utf-8') # w: write and overwrite; a: append at the end
n.write(str(datetime.datetime.now())+"\n") # write data with newline at the end
n.close()

# Context Manager
with open ("readfile.txt", "r", encoding='utf-8') as f: 
    print(f.read()) # same as above, but automatically close the file
          