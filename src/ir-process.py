
from lirc import RawConnection
#from gpiozero import LED
import RPi.GPIO as GPIO
import time

#redLED = LED(18
#redLED.off()

#conn = RawConnection()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 16
#led_pin2 = 20
GPIO.setup(led_pin1, GPIO.OUT)
#GPIO.setup(led_pin2, GPIO.OUT)

p1 = GPIO.PWM(led_pin1, 100) #channel=16, frequency=50hz
p1.start(0)
#p2 = GPIO.PWM(led_pin2, 100) #channel=20, frequency=50hz
#p2.start(0)

led1_light_step = 5   # 1~10 step
#led2_light_setp = 5   # 1~10 step

led_onoff = False

#LED Step(1~10)
def setLight(light, p):
      p.ChangeDutyCycle(light*10)

def setLED(led_pin, step, p):
    GPIO.output(led_pin, True)
    #GPIO.output(led_pin2, True)
    #p1.ChangeDutyCycle(i*10)
    setLight(step, p)
    time.sleep(1)

def processCommand(strcommand):
    global  led_onoff
    global  led1_light_step
    #global  led2_light_step
    global  p1
    #global  p2

    if strcommand == "KEY_POWER":
        print(strcommand)

    elif strcommand == "KEY_C":
        if led_onoff == False:
            led_onoff = True

        elif led_onoff == True:
            led_onoff = False

        if led_onoff == True:
            if led1_light_step < 1:
                led1_light_step = 1
            elif led1_light_step > 10:
                led1_light_step = 10

            setLED(led_pin1, led1_light_step, p1)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            setLED(led_pin1, 0, p1)
            print(strcommand, ', led: ', led_onoff)
    elif strcommand == "KEY_0":
        if led_onoff == True:
            led1_light_step = 1

        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_1":
        if led_onoff == True:
            led1_light_step = 2

        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_2":
        if led_onoff == True:
            led1_light_step = 3
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_3":
        if led_onoff == True:
            led1_light_step = 4
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_4":
        if led_onoff == True:
            led1_light_step = 5
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_5":
        if led_onoff == True:
            led1_light_step = 6
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_6":
        if led_onoff == True:
            led1_light_step = 7
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_7":
        if led_onoff == True:
            led1_light_step = 8
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_8":
        if led_onoff == True:
            led1_light_step = 9
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif strcommand == "KEY_9":
        if led_onoff == True:
            led1_light_step = 10
        setLED(led_pin1, led1_light_step, p1)
        print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))

    else:
        print(strcommand)


def ProcessIRRemote():

    #get IR command
    #keypress format = (hexcode, repeat_num, command_key, remote_id)
    #                = 0000000000ffa857 01 KEY_PLAY freeNanum
    try:
        keypress = conn.readline(.0001)
        #print(keypress)
    except:
        keypress=""

    if (keypress != "" and keypress != None):

        data = keypress.split()
        sequence = data[1]
        command = data[2]

        #ignore command repeats
        if (sequence != "00"):
           return

        # print "KEY_PLAY"
        print(command)
        #if command == "KEY_POWER":
        #   redLED.toggle()
        processCommand(command)


#define Global
conn = RawConnection()

print("Starting Up...")
try:
      while True:
        ProcessIRRemote()

except KeyboardInterrupt:
      pass

finally:
      GPIO.cleanup()

