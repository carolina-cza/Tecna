liste1 = "Deutschland, Frankreich, Polen, Österreich"
print("Orginale Liste: ")
print(liste1)

liste2 = liste1.replace(",", ";")
print("Transformierte Liste: ")
print(liste2)

print("##Zweite Methode##")
#zweite Methode
import re
list12 = "Deutschland, Frankreich, Polen, Österreich"
print("Orginale Liste: ")
print(list12)
list13 = re.sub(","," ",list12)
print("Transformierte list: ")
print(list13)