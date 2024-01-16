myList = [20, 30, 40, 50, 40, 44, 32, 123,-1, 2]

#mit einer for Schleife
resultanList = []

for element in myList:
    if element not in resultanList:
        resultanList.append(element)
print(resultanList)


#mit funktion set()
original_list = [60,50,40,50,40,2,2,44,32,23,1,1,0,0,278]
print("Originale Liste: ", original_list)

convert_to_set = set(original_list)
print("Set: ", convert_to_set)

new_list = list(convert_to_set)
print("Duplikate aus der originallen Liste entfernt: ", new_list)


#OrderDict verwenden
from collections import OrderedDict

List = [2,1,2,3,2,4,55,35,63,76,0,8,1]

final_list = list(OrderedDict.fromkeys(List))

print(final_list)