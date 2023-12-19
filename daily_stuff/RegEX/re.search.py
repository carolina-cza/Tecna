import re

satz = "Informatik ist toll"

match = re.search('matik', satz)

if match:
    print("Silbe im Satz gefunden")
else:
    print("Silbe nicht gefunden")
print(match)