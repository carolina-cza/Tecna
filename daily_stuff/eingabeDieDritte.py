errorcount = 0
while True:
    nameInput = input("Name eingabe: ")

    name = "Caro"

    if not nameInput == name:
        print("wrong")
        errorcount += 1
    else:
        print("correct")
        break

    if errorcount == 3:
        exit()    