#https://www.youtube.com/watch?v=3k4X9K5BjDg
#function: print random cocktails from a website for every run

import requests

response = requests.get ('https://www.thecocktaildb.com/api/json/v1/1/random.php')
#checking what we response to
#print(response) 

#print the hole list
#print(response.json())

cocktails = response.json()['drinks'] [0]
#print(cocktails)

#define what sould be selected from the list
name = cocktails['strDrink']
glass = cocktails['strGlass']
alcohol = cocktails['strAlcoholic']
instructions = cocktails['strInstructions']

#output
print(f"Name: {name}")
print(f"Type of Glass: {glass}")
if alcohol == "Alcoholic":
    print(f"Alcoholic: Yes ")
else:
    print(f"Alcoholic: No ")
print(f"Instructions: {instructions}")