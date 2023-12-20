import re

for name in range(3):
    name = input("Enter your name: ")
    if not re.match(r"[A-Za-z]+$",name): #erlaubt nur buchstaben als input
        print("Only letters are allowed") #error meldung wenn anderes als buchstabe eingegeben wird
#wenn re.match erfüllt ist soll der range abbrechen, aber no clue how 
   
        
for id in range(3):
    id = input("Enter your ID: ")
    if not re.match(r"^[0-9]*$",id):
        try:
            id = int(id)
        except ValueError:
            print("Invalid input. Only numbers are allowed.") #error meldung wenn was anderes als zahlen eingegebn werden
        # except ValueError:
        #     print("Mininum lenght is four. ")
        
        

# if name != "Caro" and id != "20032005":
#     print("Hello unknown")
# else:
#     print("Welcome Back")
# print("Have a nice day!")