import re

zahl = '39801 356, 2102 1111'
#three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# the group() method returns the part of the string where there is a match
match = re.search(pattern,zahl)

if match:
    print(match.group())
else:
    print("pattern not found")