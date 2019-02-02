from tkinter import *
# TOET
scherm = Tk()
scherm.geometry("100x100")
# Kan ook: messagebox.show.. error, warning, info
#messagebox.showerror( "Drone", "alarm!!")
#messagebox.askquestion( "Drone", "alarm!!")
global motorkracht
motorkracht = Scale(scherm, tickinterval = 40, orient=HORIZONTAL, from_ = 700, to = 1350, length = 700)
motorkracht.place(x = 5, y = 30)

canvas = Canvas(scherm)
canvas.create_line(2, 2, 30000, 2)
canvas.place(x = 0, y = 200)

global stuurder
stuurder = "slider"


def switch_stuurder():
    global stuurder
    global label1
    if stuurder == "slider":
        stuurder = "joystick"
        motorkracht.configure(state=DISABLED)
    elif stuurder == "joystick":
        stuurder = "slider"
        motorkracht.configure(state=ACTIVE)
    else:
        print("error")

    print(stuurder)
    label1.configure(text = stuurder)

def maak_foto():
    print("foto gemaakt!!")


global label1
label1 = Label(scherm, text = stuurder)
label1.place(x = 5, y = 100)

knop = Button(scherm, text = "switch stuurder", command = switch_stuurder)
knop.place(x = 5,y = 5)

foto_maken = Button(scherm, text = "maak foto", command = maak_foto)
foto_maken.place(x = 5, y = 130)
# info laten zien: speed van alle motoren, hoogte, gyroscoop-dingen, foto-maken-knop
#---------#

foto = PhotoImage(file = "blaat.png")
foto_laten_zien = Button(scherm, image = foto, command = maak_foto)
foto_laten_zien.place(x = 5, y = 300)


scherm.mainloop()
