from tkinter import *
import math
import time

# TODO: NEERSTORT-ALERT, MOTOR-DATA

FPS = 2
updates_bliep_bloep_geen_naam = int(FPS) * 1000

scherm = Tk()
afmetingVanScherm = "1250x1000"
scherm.geometry(afmetingVanScherm)
scherm.resizable(False, False)

motorkracht = 600
stuurder = "slider"
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
    finally:
        print("sense is wel/niet geimporteerd")


    time.wait(100)
    sense_aan = False
    
import_sense = Button(scherm, text = "Import Sense.", command = importeer_sense)
import_sense.place(x = 150, y = 70)




#global motorkracht
#motorkracht = Scale(scherm, tickinterval = 40, orient=HORIZONTAL, from_ = 700, to = 1200, length = 600)
#motorkracht.place(x = 5, y = 5)

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


#Alles met motor-data hieronder


motor1speed = 10
motor2speed = 10
motor3speed = 10
motor4speed = 10
motor5speed = 10
motor6speed = 10

#Motor Displays
motor1display = Label(scherm, text="Engine 1:\n" + str(motor1speed))
motor1display.place(x=950, y=325)

motor2display = Label(scherm, text="Engine 2:\n" + str(motor2speed))
motor2display.place(x=950, y=375)

motor3display = Label(scherm, text="Engine 3:\n" + str(motor3speed))
motor3display.place(x=950, y=425)

motor4display = Label(scherm, text="Engine 4:\n" + str(motor4speed))
motor4display.place(x=950, y=475)

motor5display = Label(scherm, text="Engine 5:\n" + str(motor5speed))
motor5display.place(x=950, y=525)

motor6display = Label(scherm, text="Engine 6:\n" + str(motor6speed))
motor6display.place(x=950, y=675)



motor1trim = 0
motor2trim = 0
motor3trim = 0
motor4trim = 0
motor5trim = 0
motor6trim = 0

def update_motor1data():
    global motor1speed
    motor1speed = motorkracht + motor1trim
    motor1display.configure(text="Engine 1:\n" + str(motor1speed))

def update_motor2data():
    global motor2speed
    motor2speed = motorkracht + motor2trim
    motor2display.configure(text="Engine 2:\n" + str(motor2speed))

def update_motor3data():
    global motor3speed
    motor3speed = motorkracht + motor3trim
    motor3display.configure(text="Engine 3:\n" + str(motor3speed))

def update_motor4data():
    global motor4speed
    motor4speed = motorkracht + motor4trim
    motor4display.configure(text="Engine 4:\n" + str(motor4speed))

def update_motor5data():
    global motor5speed
    motor5speed = motorkracht + motor5trim
    motor5display.configure(text="Engine 5:\n" + str(motor5speed))

def update_motor6data():
    global motor6speed
    motor6speed = motorkracht + motor6trim
    motor6display.configure(text="Engine 6:\n" + str(motor6speed))

update_motor1data()
update_motor2data()
update_motor3data()
update_motor4data()
update_motor5data()
update_motor6data()

motor3speed = motorkracht + motor3trim
motor4speed = motorkracht + motor4trim
motor5speed = motorkracht + motor5trim
motor6speed = motorkracht + motor6trim

def motor1trim_meer():
    global motor1trim
    motor1trim = motor1trim + 10
    update_motor1data()

def motor1trim_minder():
    global motor1trim
    motor1trim = motor1trim - 10
    update_motor1data()

def motor2trim_meer():
    global motor2trim
    motor2trim = motor2trim + 10
    update_motor2data()

def motor2trim_minder():
    global motor2trim
    motor2trim = motor2trim - 10
    update_motor2data()

def motor3trim_meer():
    global motor3trim
    motor3trim = motor3trim + 10
    update_motor3data()

def motor3trim_minder():
    global motor3trim
    motor3trim = motor3trim - 10
    update_motor3data()

def motor4trim_meer():
    global motor4trim
    motor4trim = motor4trim + 10
    update_motor4data()

def motor4trim_minder():
    global motor4trim
    motor4trim = motor4trim - 10
    update_motor4data()

def motor5trim_meer():
    global motor5trim
    motor5trim = motor5trim + 10
    update_motor5data()

def motor5trim_minder():
    global motor5trim
    motor5trim = motor5trim - 10
    update_motor5data()

def motor6trim_meer():
    global motor6trim
    motor6trim = motor6trim + 10
    update_motor6data()

def motor6trim_minder():
    global motor6trim
    motor6trim = motor6trim - 10
    update_motor6data()


def update_alle_motoren():
    update_motor1data()
    update_motor2data()
    update_motor3data()
    update_motor4data()
    update_motor5data()
    update_motor6data()

motor1meerTrim = Button(scherm, text = "10 meer trim", command= motor1trim_meer)
motor1meerTrim.place(x= 1005, y=325)

motor1minderTrim = Button(scherm, text = "10 minder trim", command= motor1trim_minder)
motor1minderTrim.place(x=1105, y=325)

motor2meerTrim = Button(scherm, text = "10 meer trim", command= motor2trim_meer)
motor2meerTrim.place(x= 1005, y=375)

motor2minderTrim = Button(scherm, text = "10 minder trim", command= motor2trim_minder)
motor2minderTrim.place(x=1105, y=375)

motor3meerTrim = Button(scherm, text = "10 meer trim", command= motor3trim_meer)
motor3meerTrim.place(x= 1005, y=425)

motor3minderTrim = Button(scherm, text = "10 minder trim", command= motor3trim_minder)
motor3minderTrim.place(x=1105, y=425)

motor4meerTrim = Button(scherm, text = "10 meer trim", command= motor4trim_meer)
motor4meerTrim.place(x= 1005, y=475)

motor4minderTrim = Button(scherm, text = "10 minder trim", command= motor4trim_minder)
motor4minderTrim.place(x=1105, y=475)

motor5meerTrim = Button(scherm, text = "10 meer trim", command= motor5trim_meer)
motor5meerTrim.place(x= 1005, y=525)

motor5minderTrim = Button(scherm, text = "10 minder trim", command= motor5trim_minder)
motor5minderTrim.place(x=1105, y=525)

motor6meerTrim = Button(scherm, text = "10 meer trim", command= motor6trim_meer)
motor6meerTrim.place(x= 1005, y=575)

motor6minderTrim = Button(scherm, text = "10 minder trim", command= motor6trim_minder)
motor6minderTrim.place(x=1105, y=575)



def motorBeetjeMinder():
    global motorkracht
    motorkracht = motorkracht - 10
    motorkracht_label.configure(text=str(motorkracht))
    update_alle_motoren()

def motorVeelMinder():
    global motorkracht
    motorkracht = motorkracht - 100
    motorkracht_label.configure(text=str(motorkracht))
    update_alle_motoren()

def motorBeetjeMeer():
    global motorkracht
    motorkracht = motorkracht + 10
    motorkracht_label.configure(text=str(motorkracht))
    update_alle_motoren()

def motorVeelMeer():
    global motorkracht
    motorkracht = motorkracht + 100
    motorkracht_label.configure(text=str(motorkracht))
    update_alle_motoren()

beetje_minder = Button(scherm, text="10 minder", command=motorBeetjeMinder)
beetje_minder.place(x=5, y=40)

veel_minder = Button(scherm, text="100 minder", command=motorVeelMinder)
veel_minder.place(x=5, y=5)

beetje_meer = Button(scherm, text="10 meer", command=motorBeetjeMeer)
beetje_meer.place(x=200, y=40)

veel_meer = Button(scherm, text="100 meer", command=motorVeelMeer)
veel_meer.place(x=200, y=5)

motorkracht = 600

motorkracht_label = Label(scherm, text=motorkracht)
motorkracht_label.place(x=100, y=5)



#Hier niet meer over motor-data

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


HDMI = "uit"
USB1 = "uit"
USB2 = "uit"
Volt = "uit"
Backfeedbloep = "aan"


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
   pass

def bijwerken(scherm, attitude_indicator):
    maak_hsi()
    global updates_bliep_bloep_geen_naam
    scherm.after(int(updates_bliep_bloep_geen_naam), bijwerken, scherm, attitude_indicator)

scherm.after(int(updates_bliep_bloep_geen_naam), bijwerken, scherm, maak_hsi())
scherm.mainloop()
