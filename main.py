from tkinter import *
import math
import time

#TODO: NEERSTORT-ALERT, CHECKLIST-AID

FPS = 2
updates_bliep_bloep_geen_naam = int(FPS) * 1000

scherm = Tk()
scherm.geometry("900x1000")

sense_aan = False

checklist = "preflight"

PreFlightChecklistText = "PREFLIGHT: \n \nHDMI > CLEAR\nUSB1 > CLEAR\nUSB2 > CLEAR\n5V > CLEAR\nBACKFEED > CONNECT\nFOTO > TEST\nAREA > CLEAR\nBATTS > CONNECT\nBRIEFING > DONE\nKNOPJES > VAST"
BeforeTakeOffChecklistText = "BEFORE TAKEOFF: \n \nENGINE > TEST\n"
AfterLandingChecklistText = "AFTER LANDING: \n \n5V > CONNECT\nBACKFEED > DISCONNECT\nBATTS > DISCONNECT\nDRAADJES > CHECK"

checklistDisplay = Label(scherm, text=PreFlightChecklistText)
checklistDisplay.place(x=650, y=5)



def switch_CHECKLIST():
    global checklist
    global checklistDisplay
    if checklist == "preflight":
        checklist = "beforetakeoff"
        checklistDisplay.configure(text=BeforeTakeOffChecklistText)
    elif checklist == "beforetakeoff":
        checklist = "afterlanding"
        checklistDisplay.configure(text=AfterLandingChecklistText)
    elif checklist == "afterlanding":
        checklist = "preflight"
        checklistDisplay.configure(text=PreFlightChecklistText)
    else:
        print("Ewa bro tantoe niffo er werkt iets  niet meer.")

    print(checklist)

checklistButton = Button(scherm, text="Switch Checklist", command=switch_CHECKLIST)
checklistButton.place(x=450, y=280)

def importeer_sense():
    try:
        from sense_hat import SenseHat
        sense = SenseHat()
        sense_aan = True
        print("sense geimporteerd")

    except:
        print("Je zit niet op een Pi!")


    time.wait(100)
    sense_aan = False
    
import_sense = Button(scherm, text = "Import Sense.", command = importeer_sense)
import_sense.place(x = 150, y = 70)

global motorkracht
motorkracht = Scale(scherm, tickinterval = 40, orient=HORIZONTAL, from_ = 700, to = 1200, length = 600)
motorkracht.place(x = 5, y = 5)

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
        print("error: hey! niemand stuurd!")

    print(stuurder)
    label1.configure(text = stuurder)

def maak_foto():
    print("foto gemaakt!!")

global label1
label1 = Label(scherm, text = stuurder)
label1.place(x = 25, y = 100)

knop = Button(scherm, text = "switch stuurder", command = switch_stuurder)
knop.place(x = 5,y = 70)

foto_maken = Button(scherm, text = "maak foto", command = maak_foto)
foto_maken.place(x = 300, y = 70)

foto = PhotoImage(file = "plaatjes/kip.png")
foto_laten_zien = Button(scherm, image = foto, command = maak_foto, height = 300, width = 400)
foto_laten_zien.place(x = 500, y = 325)

global HDMIstate
HDMIstate = Label(scherm, text="HDMI: " + "--------x--------")
HDMIstate.place(x=450, y=130)

USB1state = Label(scherm, text="USB 1: " + "--------x--------")
USB1state.place(x=450, y=150)

USB2state = Label(scherm, text="USB 2: " + "--------x--------")
USB2state.place(x=450, y=170)

VoltState = Label(scherm, text="5 Volts: " + "--------x--------")
VoltState.place(x=450, y=200)

VoltBackfeedState = Label(scherm, text="Backfeed: " + "--------x--------")
VoltBackfeedState.place(x=450, y=220)

global HDMI
HDMI = "aan"
USB1 = "aan"
USB2 = "aan"
Volt = "aan"
Backfeedbloep = "uit"


def switch_HDMI():
    global HDMI
    global HDMIstate
    if HDMI == "aan":
        HDMI = "uit"
    elif HDMI == "uit":
        HDMI = "aan"
    else:
        print("error")

    print(HDMI)
    HDMIstate.configure(text="HDMI 1: " + HDMI)


def switch_USB1():
    global USB1
    global USB1state
    if USB1 == "aan":
        USB1 = "uit"
    elif USB1 == "uit":
        USB1 = "aan"
    else:
        print("error")

    print(USB1)
    USB1state.configure(text="USB 1: " + USB1)


def switch_USB2():
    global USB2
    global USB2state
    if USB2 == "aan":
        USB2 = "uit"
    elif USB2 == "uit":
        USB2 = "aan"
    else:
        print("error")

    USB2state.configure(text="USB 2: " + USB2)


def switch_VOLTS():
    global Volt
    global VoltState
    if Volt == "aan":
        Volt = "uit"
    elif Volt == "uit":
        Volt = "aan"
    else:
        print("error")

    VoltState.configure(text="5 Volts: " + Volt)


def switch_BACKFEEd():
    global Backfeedbloep
    global VoltBackfeedState
    if Backfeedbloep == "aan":
        Backfeedbloep = "uit"
    elif Backfeedbloep == "uit":
        Backfeedbloep = "aan"
    else:
        print("error")

    VoltBackfeedState.configure(text="Backfeed: " + Backfeedbloep)




#HDMI-state
HDMIstateButton = Button(scherm, text="HDMI-kabel", command=switch_HDMI)
HDMIstateButton.place(x=5, y=280)
#USB1-state
USB1stateButton = Button(scherm, text="USB 1-kabel", command=switch_USB1)
USB1stateButton.place(x=90, y=280)
#USB2-state
USB2stateButton = Button(scherm, text="USB 2-kabel", command=switch_USB2)
USB2stateButton.place(x=180, y=280)
#5V-state
VoltstateButton = Button(scherm, text="5V-kabel", command=switch_VOLTS)
VoltstateButton.place(x=270, y=280)
#5Vbackfeed-state
VoltbackfeedStateButton = Button(scherm, text="5V-Backfeed", command=switch_BACKFEEd)
VoltbackfeedStateButton.place(x=360, y=280)

#GyroX
GyroXlabel = Label(scherm, text="Gyroscope X: " + "--.-- degrees")
GyroXlabel.place(x = 5, y = 130)
#GyroY
GyroYlabel = Label(scherm, text="Gyroscope Y: " + "--.-- degrees")
GyroYlabel.place(x = 5, y = 150)
#GyroZ
GyroZlabel = Label(scherm, text="Gyroscope Z: " + "--.-- degrees")
GyroZlabel.place(x = 5, y = 170)
#AccelX
AccelXlabel = Label(scherm, text="Acceleratometer X: " + "--.-- m/s/s")
AccelXlabel.place(x = 200, y = 130)
#AccelY
AccelYlabel = Label(scherm, text="Acceleratometer Y: " + "--.-- m/s/s")
AccelYlabel.place(x = 200, y = 150)
#AccelZ
AccelZlabel = Label(scherm, text="Acceleratometer Z: " + "--.-- m/s/s")
AccelZlabel.place(x = 200, y = 170)
#Magnetometer
MagnetoLabel = Label(scherm, text="Heading: " + "--.-- degrees")
MagnetoLabel.place(x = 5, y = 200)
#Baro
BaroLabel = Label(scherm, text="BaroMeter: " + "--.-- HktPscl")
BaroLabel.place(x = 5, y = 220)
#Baro height
BaroHeightLabel = Label(scherm, text="BaroMeter: " + "--.-- CentiMeter")
BaroHeightLabel.place(x = 5, y = 240)
#Temp pi
TemperatureLabel = Label(scherm, text="Temperature Pi: " + "--.-- graden Celsius")
TemperatureLabel.place(x = 200, y = 200)
#Relative Humidity
RelativeHumidityLabel = Label(scherm, text="Relative Humidity: " + "--.-- procent")
RelativeHumidityLabel.place(x = 200, y = 220)

def maak_data_displays():
    global sense_aan
    if sense_aan == True:
        print("Sense-feedback uit.")
        #GYRO X
        #GYRO Y
        #GYRO Z
        #ACCEL X
        #ACCEL Y
        #ACCEL Z
        #MAGNETO
        #BARO
        #BARO HOOGTE
        #TEMP PI
        #Relative Humidity
    elif sense_aan == False:
        print("Sense-feedback aan")

while sense_aan == True:
    def maak_hoek_sense_roll():
        global hoek
        hoek = sense.get_orientation()['roll']
else:
    hoek = 0

ATTITUDE_HOOGTE = 300
ATTITUDE_BREEDTE = 400
middellijnhoogte = ATTITUDE_HOOGTE / 2

attitude_indicator = Canvas(scherm, width=ATTITUDE_BREEDTE, height=ATTITUDE_HOOGTE, background="brown")
attitude_indicator.place(x = 5, y = 325)

hoek = -10

degtorad = lambda deg: deg * math.pi / 180

AANLIGGENDE = ATTITUDE_BREEDTE / 2
overstaande = math.tan(degtorad(hoek)) * AANLIGGENDE

attitude_indicator.create_polygon(0, 0, 0, middellijnhoogte + overstaande, ATTITUDE_BREEDTE, middellijnhoogte - overstaande, ATTITUDE_BREEDTE, 0, fill = "cyan")
attitude_indicator.create_line(0, middellijnhoogte, ATTITUDE_BREEDTE, middellijnhoogte, fill = "yellow")

def maak_hsi():
    print("deze functie is buiten gebruik!")

def bijwerken(scherm, attitude_indicator):
    maak_hsi()
    global updates_bliep_bloep_geen_naam
    scherm.after(int(updates_bliep_bloep_geen_naam), bijwerken, scherm, attitude_indicator)

scherm.after(int(updates_bliep_bloep_geen_naam), bijwerken, scherm, maak_hsi())
scherm.mainloop()
