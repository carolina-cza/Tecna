import re

satz = "Informatik ist toll"

#the re.search() method takes two arguments: a pattern and a string. The method looks for the first laocation where the Regex pattern produces a match with the string.
match = re.search('matik', satz)

if match:
    print("Silbe im Satz gefunden")
else:
    print("Silbe nicht gefunden")
print(match)