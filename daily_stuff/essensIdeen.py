import random

#define lists with meals
healthy = ["appel cinamon oats", "Banana pancakes","Chilaquiles Rojos"]

unhealthy = ["pommes fires with nuggets", "Hamburger","Kochkässchnitzel"]

snack = ["banana snicker bites","cookies", "fruits", "granola bar","chocolate"]

frage = input("What do you want to eat today?: healthy/unhealthy/snack ")

#define output
if frage == "healthy":
   select_healthy = random.choice(healthy)
   print(select_healthy)

if frage == "unhealthy":
   selcet_unhealthy = random.choice(unhealthy)
   print(selcet_unhealthy)

if frage == "snack":
   select_snack = random.choice(snack)  
   print(select_snack)

else:
   print("Try again")
