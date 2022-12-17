text = "Hello"

print(f"{text:_>20}") 
#O/P -->   _______________Hello

print(f"{text:$<20}") 
#O/P -->  Hello$$$$$$$$$$$$$$$$

print(f"{text:.^20}")
#O/P --> .......Hello........


#-----------------------------------------------


#printing Emojis in python

#UNICODE CODEPOINT
print("\U0001f995")
#GETTING THE CODE
codePoint = "🦕".encode("unicode_escape") 

#UNICODE NAME
print("\N{SAUROPOD}")
#GETTING THE CODE
import unicodedata
codeName = unicodedata.name("🦕") 


#-----------------------------------------------


#formatting upto 2 digits 
x = 3.14159265
print(f"{x:.2f}")


#-----------------------------------------------

#Hiding user input in the terminal

from getpass import getpass

user = input("Username: ")
password = getpass("Password: ")

#-----------------------------------------------

#dataclass Boiler-plate

from dataclass import dataclass

@dataclass
class Person:
    name:str
    age:int


#------------------------------------------------

#injecting a value in a list inbetween automatically

import bisect

a = [3, 5, 9, 11, 20]

value = 7
idx = bisect.bisect(a, value)
print(idx) 
#O/P --> 2

a.insert(idx, value)
print(a)
#O/P --> [3, 5, 7, 9, 10, 11, 20]

#------------------------------------------------

#No Private methods

class User:
    def __foo(self):
        print("Hi!")

user = User()

user.__foo() 
#O/P --> raises an AttributeError

user._User__foo()
#O/P --> Name mangling, and it works 

#------------------------------------------------


