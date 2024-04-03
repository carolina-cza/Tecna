#function: print random recipe from a website for every run

import requests

response = requests.get ('https://www.themealdb.com/api/json/v1/1/random.php')
#checking what we response to
#print(response) 

#print the hole list
#print(response.json())

meals = response.json()['meals'] [0]
#print('meals')

name = meals['strMeal']
category = meals['strCategory']
instructions = meals['strInstructions']

print(f"Name: {name}")
print(f"Category: {category}")

question = input('Do you want the instruction? yes/no ')
if question == 'yes':
    print(f"Instructions: {instructions}")
else:
    print("Enjoy")

print("Good cooking^^")