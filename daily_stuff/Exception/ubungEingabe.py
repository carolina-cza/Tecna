import re

name = input("Enter your name: ")
if not re.match(r"[A-Za-z]+$",name): #erlaubt nur buchstaben als input
    print("Only letters are allowed") #error meldung wenn anderes als buchstabe eingegeben wird
if  len(name)>8:
    # try:
    #     name = str(name)
    # except ValueError as e:
    print("Error only 8 charackters are allowed.")

id = input("Enter your ID: ")

if len(id) < 4:
    try:
        id = int(id)
    except ValueError:
        print("Invalid input. Only numbers are allowed.") #error meldung wenn was anderes als zahlen eingegebn werden

    print("Mininum lenght is four. ")    

if name != "Caro" and id != "20032005":
    print("Hello unknown")
else:
    print("Welcome Back")
print("Have a nice day!")