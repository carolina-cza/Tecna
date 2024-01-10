# -*_coding: utf-8-*-
import random

zufallsantworten = ["Oh, wirklich", "Interessant ...", "Das kann man so sehen","Ich verstehe ..."]

reaktionsantworten = {"hallo": "aber Hallo",
                      "geht": "Was verstehst du darunter?",
                      "essen": "Ich habe leider keinen Geschmacksinn :("
                      }
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne Heute sprechen?")
print("Zumbeenden einfach 'bye' eintippen")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntwort = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntwort = True
        if intelligenteAntwort == False:
            print(random.choice(zufallsantworten))

        print("")

print("Eine schönen Tag wünsche ich Dir.Bis zum nächsten Mal")