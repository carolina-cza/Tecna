import tkinter as tk

window = tk.Tk()

#Fenstergröße erhalten
window.geometry("400x300")
frage = tk.LabelFrame(window,text = "Rauchst du?")
frage.pack()
check1 = tk.Checkbutton(frage)
check1["text"] = "JA"
check1.pack()

check2 = tk.Checkbutton(frage)
check2["text"] = "NEIN"
check2.pack()

if check1:
    # Textausgabe erzeugen
    label1 = tk.Label(window, text="Rauchen ist tödlich",
                    fg = 'white', #Vordergrundfarbe
                    bg ='red', #Hintergrundfarbe
                    font = ('arial',25,'bold','italic'),#Schriefart und Schrieftgröße setzen
                    height=20,
                    width=30,
                    anchor= 'center') #ausrichtung

    #print(dir(tk.Grid))
    # in GUI Elemente einbetten
    label1.pack()
else:
    lable2 =tk.Label(window, text ="sehr gut")
window.mainloop()