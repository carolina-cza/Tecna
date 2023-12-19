import re

zahl = '39801 356, 2102 1111'
pattern = '(\d{3}) (\d{2})'

match = re.search(pattern,zahl)

if match:
    print(match.group())
else:
    print("pattern not found")