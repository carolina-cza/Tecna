import re

name = input("Enter your name: ")
if not re.match(r"[A-Za-z]+$",name): #erlaubt nur buchstaben als input
    print("Only letters are allowed") #error meldung wenn anderes als buchstabe eingegeben wird


id = input("Enter your ID: ")
try:
    id = int(id)
except ValueError:
    print("Invalid input. Only numbers are allowed.") #error meldung wenn was anderes als zahlen eingegebn werden

if name != "Caro" and id != "1234":
    print("Hello unknown")
else:
    print("Welcome Back")
print("Have a nice day!")