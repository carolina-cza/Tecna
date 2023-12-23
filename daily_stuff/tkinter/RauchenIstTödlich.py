import tkinter as tk

window = tk.Tk()

#Fenstergröße erhalten
window.geometry("400x300")

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

window.mainloop()