# op 11.1 volt is 1250 zweven
import os
import time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1)
import pigpio



ESC=23
ESC2=18
ESC3=25
ESC4=24
ESC5=7
ESC6=8


pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)
pi.set_servo_pulsewidth(ESC5, 0)
pi.set_servo_pulsewidth(ESC6, 0)

error = "Dit is een error."
beta = "Dit is nog in de beta!"

max_value = 1400
min_value = 700
print("Als je de eerste keer opstart, selecteer dan calibrate")
print ("Wees wel precies")
print ("calibrate OF manual OF control OF arm OF stop OF auto (Autiomatisch)")
def manual_drive():
    print ("Manual geselecteerd - geef een waarde tussen 0 en de max-waarde"    )
    while True:
        inp = input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break   
        else:
            pi.set_servo_pulsewidth(ESC,inp)
            pi.set_servo_pulsewidth(ESC2,inp)
            pi.set_servo_pulsewidth(ESC3,inp)
            pi.set_servo_pulsewidth(ESC4,inp)
            pi.set_servo_pulsewidth(ESC5,inp)
            pi.set_servo_pulsewidth(ESC6,inp)
                
def calibrate():
    pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0)
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.set_servo_pulsewidth(ESC5, 0)
    pi.set_servo_pulsewidth(ESC6, 0)
    print("Koppel de batterij af en druk op enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        pi.set_servo_pulsewidth(ESC2, max_value)
        pi.set_servo_pulsewidth(ESC3, max_value)
        pi.set_servo_pulsewidth(ESC4, max_value)
        pi.set_servo_pulsewidth(ESC5, max_value)
        pi.set_servo_pulsewidth(ESC6, max_value)
        print("Sluit de batterij aan, wacht op de piepjes en druk op Enter.")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
            pi.set_servo_pulsewidth(ESC5, min_value)
            pi.set_servo_pulsewidth(ESC6, min_value)
            print ("Even wachten...")
            print ("Nog even wachten...")
            print ("PIZZA!")
            pi.set_servo_pulsewidth(ESC, 0)
            pi.set_servo_pulsewidth(ESC2, 0)
            pi.set_servo_pulsewidth(ESC3, 0)
            pi.set_servo_pulsewidth(ESC4, 0)
            pi.set_servo_pulsewidth(ESC5, 0)
            pi.set_servo_pulsewidth(ESC6, 0)
            print ("INITIAL WHOEMM")
            pi.set_servo_pulsewidth(ESC, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
            pi.set_servo_pulsewidth(ESC5, min_value)
            pi.set_servo_pulsewidth(ESC6, min_value)
            print ("Ik zei het toch")
            arm()
def vooruit():
    global speed
    global speed2
    global ESC
    global ESC2
    print(beta)
    speed -= 100
    speed2 -= 100
    print("speed = %d" % speed)
    print("speed2 = %d" % speed2)
    pi.set_servo_pulsewidth(ESC, speed)
    pi.set_servo_pulsewidth(ESC2, speed2)    
    speed2 += 100
    speed += 100
    print("speed = %d" % speed)
    print("speed2 = %d" % speed2)
    pi.set_servo_pulsewidth(ESC, speed)
    pi.set_servo_pulsewidth(ESC2, speed2)
def achteruit():
    global speed5
    global speed6
    global ESC5
    global ESC6
    print(beta)
    speed5 -= 10
    speed6 -= 10
    print("speed5 = %d" % speed5)
    print("speed6 = %d" % speed6)
    pi.set_servo_pulsewidth(ESC5, speed5)
    pi.set_servo_pulsewidth(ESC6, speed6)    
    speed5 += 10
    speed6 += 10
    print("speed5 = %d" % speed5)
    print("speed6 = %d" % speed6)
    pi.set_servo_pulsewidth(ESC5, speed5)
    pi.set_servo_pulsewidth(ESC6, speed6)    
    
def links():
    print(error)
    print(beta)
    
def rechts():
    print(error)
    print(beta)

def links_draaien():
    print(error)
    print(beta)

def rechts_draaien():
    print(error)
    print(beta)
    
def control(): 
    print ("De motor moet nu aangaan!")
    time.sleep(1)
    #De snelheden hieronder zijn startsnelheden. speed = 700 = uit aan het begin.
    speed = 700
    speed2 = 700
    speed3 = 700
    speed4 = 700
    speed5 = 700
    speed6 = 700
    global speed
    global speed2
    global ESC
    global ESC2
    global speed5
    global speed6
    global ESC5
    global ESC6
    print ("Als je de controls wilt snappen: LEES DE CODE!")
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        pi.set_servo_pulsewidth(ESC2, speed2)
        pi.set_servo_pulsewidth(ESC3, speed3)
        pi.set_servo_pulsewidth(ESC4, speed4)
        pi.set_servo_pulsewidth(ESC5, speed5)
        pi.set_servo_pulsewidth(ESC6, speed6)
        inp = input()
        
        if inp == "q":
            speed -= 100
            print ("speed = %d" % speed)
        elif inp == "w":    
            speed += 100
            print ("speed = %d" % speed)
        elif inp == "a":
            speed += 10
            print ("speed = %d" % speed)
        elif inp == "s":
            speed -= 10
            print ("speed = %d" % speed)
        elif inp == "e":
            speed2 -= 100
            print ("speed2  = %d" % speed2)
        elif inp == "r":    
            speed2 += 100
            print ("speed2 = %d" % speed2)
        elif inp == "d":
            speed2 += 10
            print ("speed2 = %d" % speed2)
        elif inp == "f":
            speed2 -= 10
            print ("speed2 = %d" % speed2)
        elif inp == "t":
            speed3 -= 100
            print ("speed3  = %d" % speed3)
        elif inp == "y":  
            speed3 += 100
            print ("speed3 = %d" % speed3)
        elif inp == "g":
            speed3 += 10
            print ("speed3 = %d" % speed3)
        elif inp == "h":
            speed3 -= 10
            print ("speed3 = %d" % speed3)
        elif inp == "u":
            speed4 -= 100
            print ("speed4  = %d" % speed4)
        elif inp == "i":  
            speed4 += 100
            print ("speed4 = %d" % speed4)
        elif inp == "j":
            speed4 += 10
            print ("speed4 = %d" % speed4)
        elif inp == "k":
            speed4 -= 10
            print ("speed4 = %d" % speed4)
        elif inp == "z":
            speed5 -= 100
            print ("speed5  = %d" % speed5)
        elif inp == "x":  
            speed5 += 100
            speed6 += 100
            print ("speed5 = %d" % speed5)
        elif inp == "c":
            speed5 += 10
            print ("speed5 = %d" % speed5)
        elif inp == "v":
            speed5 -= 10
            print ("speed6 = %d" % speed5)
        elif inp == "b":
            speed6 -= 100
            print ("speed6  = %d" % speed6)
        elif inp == "n":  
            speed6 += 100
            print ("speed6 = %d" % speed6)
        elif inp == "m":
            speed6 += 10
            print ("speed6 = %d" % speed6)
        elif inp == ",":
            speed6 -= 10
            print ("speed6 = %d" % speed6)
        elif inp == "9":
            speed += 100
            speed2 += 100
            speed3 += 100
            speed4 += 100
            speed5 += 100
            speed6 += 100
            print(speed, speed2, speed3, speed4, speed5, speed6, "(Alles + 100)")
        elif inp == "7":
            speed -= 100
            speed2 -= 100
            speed3 -= 100
            speed4 -= 100
            speed5 -= 100
            speed6 -= 100
            print(speed, speed2, speed3, speed4, speed5, speed6, "(Alles - 100)")
        elif inp == "3":
            speed += 10
            speed2 += 10
            speed3 += 10
            speed4 += 10
            speed5 += 10
            speed6 += 10
            print(speed, speed2, speed3, speed4, speed5, speed6, "(Alles + 10)")
        elif inp == "1":
            speed -= 10
            speed2 -= 10
            speed3 -= 10
            speed4 -= 10
            speed5 -= 10
            speed6 -= 10
            print(speed, speed2, speed3, speed4, speed5, speed6, "(Alles - 10)")
        elif inp == "5":
            speed = 700
            speed2 = 700
            speed3 = 700
            speed4 = 700
            speed5 = 700
            speed6 = 700
        elif inp == "stop":
            stop()
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break
        elif inp == "8":
            vooruit()
        elif inp == "2":
            achteruit()
        elif inp == "4":
            links()
        elif inp == "6":
            rechts()
        elif inp == "/":
            links_draaien()
        elif inp == "-":
            rechts_draaien()
        else:
            print ("Dit is geen geldig antwoord")
            
def arm():
    print ("Sluit de batterij aan en druk op Enter")
    inp = input()    
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        pi.set_servo_pulsewidth(ESC4, 0)
        pi.set_servo_pulsewidth(ESC5, 0)
        pi.set_servo_pulsewidth(ESC6, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        pi.set_servo_pulsewidth(ESC2, max_value)
        pi.set_servo_pulsewidth(ESC3, max_value)
        pi.set_servo_pulsewidth(ESC4, max_value)
        pi.set_servo_pulsewidth(ESC5, max_value)
        pi.set_servo_pulsewidth(ESC6, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        pi.set_servo_pulsewidth(ESC2, min_value)
        pi.set_servo_pulsewidth(ESC3, min_value)
        pi.set_servo_pulsewidth(ESC4, min_value)
        pi.set_servo_pulsewidth(ESC5, min_value)
        pi.set_servo_pulsewidth(ESC6, min_value)
        time.sleep(1)
        control() 
def automatisch():
    calibrate()
def stop():
    pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0)
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.set_servo_pulsewidth(ESC5, 0)
    pi.set_servo_pulsewidth(ESC6, 0)
    pi.stop()

inp = input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print ("Dit is geen geldig antwoord")
