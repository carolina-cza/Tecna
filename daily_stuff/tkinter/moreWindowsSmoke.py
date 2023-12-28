import tkinter as tk

def Smoker():
    
    window = tk.Toplevel(mainWindow)
    window.geometry("400x300")
    label1 = tk.Label(window, text="Rauchen ist tödlich",
                fg = 'white', #Vordergrundfarbe
                bg ='red', #Hintergrundfarbe
                font = ('arial',25,'bold','italic'),#Schriefart und Schrieftgröße setzen
                height=20,
                width=30,
                anchor= 'center') #ausrichtung
    label1.pack()
    window.mainloop()

def NoSmoker():

    window2 = tk.Toplevel(mainWindow)
    window2.geometry("400x300")
    label2 = tk.Label(window2, text = "Very Good ^^",
                      fg = "black",
                      bg = "#9FE2BF",
                      font = ("Georgia",25,"bold"),
                      height = 20,
                      width = 30,
                      anchor = "center")
    label2.pack()
    window2.mainloop()


#create Mainwindow with yes and no window
mainWindow = tk.Tk()
mainWindow.geometry("400x300")

frage = tk.Label(mainWindow, text = "Rauchst du?",font = ("arial",20))

buttonYes = tk.Button(mainWindow,text = "Yes, I do.", command = Smoker)

buttonNo = tk.Button(mainWindow, text = "No, I don't.", command = NoSmoker)

frage.pack()
buttonYes.pack()
buttonNo.pack()

mainWindow.mainloop()