import datetime
currentDay = datetime.datetime.now() #gibt das aktuelle datum aus sowie die genau Zeit der Abfrage
print(currentDay)

#daycounter till an special date based on the current date
dc =  datetime.datetime (currentDay.year,12, 24) - datetime.datetime.now()

#überprüft ob heute Nikolaus ist
if currentDay.month == 12 and currentDay.day == 6:
    print ("Heute ist Nikolaus")

#überprüft ob schon Weihnachten ist
print( "Is today Christmas?")
if currentDay.month == 12 and currentDay.day == 24:
    print("Merry Chrsitmas!")

else:
    print("not yet:( is still " + str(dc) + " till christmas")

if currentDay.month == 1 and currentDay.day == 6:
    print("Heute ist heilige drei Könige.")

if currentDay.month == 3 and currentDay.day == 20:
    print("Happy Birthday!")