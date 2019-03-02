from tkinter import *
import math
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
from sense_hat import SenseHat
sense = SenseHat()
def maak_hsi():
    #blaat
    ATTITUDE_HOOGTE = 300
    ATTITUDE_BREEDTE = 400
    middellijnhoogte = ATTITUDE_HOOGTE / 2

    return Canvas(scherm, width=ATTITUDE_BREEDTE, height=ATTITUDE_HOOGTE, background="brown")

def bijwerken(scherm, attitude_indicator):
    ATTITUDE_HOOGTE = 300
    ATTITUDE_BREEDTE = 400
    middellijnhoogte = ATTITUDE_HOOGTE / 2

    attitude_indicator.place(x = 5, y = 650)

    hoek = sense.get_orientation()['roll']
    print(hoek)
    degtorad = lambda deg: deg * math.pi / 180

    AANLIGGENDE = ATTITUDE_BREEDTE / 2
    overstaande = math.tan(degtorad(hoek)) * AANLIGGENDE

    attitude_indicator.create_polygon(0, 0, 0, middellijnhoogte + overstaande, ATTITUDE_BREEDTE, middellijnhoogte - overstaande, ATTITUDE_BREEDTE, 0, fill = "cyan")


    attitude_indicator.create_line(0, middellijnhoogte, ATTITUDE_BREEDTE, middellijnhoogte, fill = "yellow")

    scherm.after(500, bijwerken, scherm, attitude_indicator)

scherm.after(500, bijwerken, scherm, maak_hsi())
scherm.mainloop()
