from getpass import getpass


richtiges_password = "1234" #richtige password wird definiert(könnte theoertisch sich auf eine liste beziehen evtl?)

for eigabe_password in range(3): # if schleife wird drei mal ausgeführt und wenn die nicht erfüllt wird wird das letzte else ausgeführt
    eingabe_password = getpass("Bitte gib dein Password ein: ") #eingabe ist nicht sichtbar
    if richtiges_password == eingabe_password:
        print("Richtiges Passwort")
        break #wenn es erfüllt wird wird die if schleife beendet
    else:
        print("Versuch es nochmal")
else:
    print("Versuche es später noachmal")
    