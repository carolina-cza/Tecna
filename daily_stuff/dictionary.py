#https://www.dataquest.io/blog/python-dictionaries/

# Create a Harry Potter dictionary

harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}
# Characters to add to the Harry Potter dictionary
add_characters_1 = {
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw"
}

# Merge dictionaries
harry_potter_dict.update(add_characters_1)

add_characters_2 = [
    ["Draco Malfoy", "Slytherin"],
    ["Cedric Diggory", "Hufflepuff"]
]
harry_potter_dict.update(add_characters_2)

del harry_potter_dict["Draco Malfoy"]

# Display the dictionary
#print(harry_potter_dict)

print()
print("Dictionary without Voldemort:")
print(harry_potter_dict)
print()

print("Return the default value of Voldemort:")
#If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None
print(harry_potter_dict.setdefault("Voldemort", "Slytherin"))
print()

print("Voldemort is now in the dictionary!")
#print(harry_potter_dict)

#Loop through key and value
for key, value in harry_potter_dict.items():
    print((key, value))

# Loop only through the keys
for key in harry_potter_dict.keys():
    print(key)