mylist= [1,1,2,3,4,5,6,4,8,7,9,100,34,12,34]

print("Kleinster Wert: "+ str(min(mylist)))
print("Größter Wert: " + str(max(mylist)))

for mylists in mylist:
    #chek if the coutn of items is > 1 (repeating item)
    while (mylist.count(mylists) > 1):
        #remove the first occurrence of sweet until one occurrence remains.
        mylist.remove(mylists)
print(mylist)

def remove_duplcates(mylist):
    return(mylist(set(mylist)))

