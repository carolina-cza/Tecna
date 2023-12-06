import datetime
currentDay = datetime.datetime.now() #gibt das aktuelle datum aus sowie die genau Zeit der Abfrage
print(currentDay)

#überprüft ob heute Nikolaus ist
if currentDay.month == 12 and currentDay.day == 6:
    print ("Heute ist Nikolaus")
#überprüft ob schon Weihnachten ist
print( "Is today Christmas?")
if currentDay.month == 12 and currentDay.day == 24:
    print("Merry Chrsitmas!")
else:
    print("not yet:(")