import random

#define lists with meals
healthy = ["appel cinnamon oats", "Banana pancakes","Chilaquiles Rojos"]

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

# else:
#    print("Try again")

#ask for the recipe
ask = input("Do you want the recipe? yes/no ")

if ask == "yes":
   if select_healthy == "appel cinnamon oats":
      print("""Ingredients:
                1 cup water or milk
                ½ Tablespoon maple syrup, brown sugar or coconut sugar (optional)
                ¼-½ teaspoon ground cinnamon
                ½ teaspoon vanilla extract
                pinch of sea salt
                2 Tablespoons chopped pecans, for topping
               CINNAMON APPLES
                ½ cup diced apples
                2 teaspoons maple syrup
                ¼ teaspoon cinnamon""")
   if select_healthy == "Banana pancakes":
      print("Recipe: 1 bannana mash, 1 cup oats, 1 egg, 1tsp milk, 1tsp baking powder")
   if select_healthy == "Chilaquiles Rojos":
      print("Ask google pls")
      
if ask == "no":
   print("ok")