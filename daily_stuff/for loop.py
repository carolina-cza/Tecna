from getpass import getpass
from tkinter import *
password = input("Password: ") #
password = Entry ( show  ="*")
reapet_password = input("Reapet the password: ")

if password == reapet_password:
    print("Correct")
else:
    print("Try again")