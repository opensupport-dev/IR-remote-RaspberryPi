#!/usr/bin/env python3

import os
os.environ['DISPLAY'] = ':0'
#os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
#import sys
#sys.path.append("/home/pi/.local/lib/python3.7/site-packages")
#sys.path

from lirc import RawConnection
#from gpiozero import LED
import RPi.GPIO as GPIO
import time
import pyautogui
#print(pyautogui.position())

#redLED = LED(18)
#redLED.off()

#conn = RawConnection()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 16 #gpio16을 LED1 용도로 사용함
led_pin2 = 20 #gpio20을 LED2 용도로 사용함
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

p1 = GPIO.PWM(led_pin1, 100) #channel=16, frequency=50hz
p1.start(0)
p2 = GPIO.PWM(led_pin2, 100) #channel=20, frequency=50hz
p2.start(0)

led1_light_step = 5   # 1~10 step
led2_light_setp = 5   # 1~10 step

led_onoff = False

def ProcessReadLedInfo():
    global  led_onoff
    global  led1_light_step
    global  led2_light_setp
    #format =  led_onoff False led1_light_step 5
    with open('led-info.txt', 'r') as ledOpenFile:
        ledString = ledOpenFile.read()
        #print(ledString)
        #print(ledString.split(' ')[0], ': ', ledString.split(' ')[1], ' / ', ledString.split(' ')[2], ': ', ledString.split(' ')[3])
        split_ledinfo = ledString.split(' ')
        if split_ledinfo[1] == '0':
            led_onoff =  False
        elif split_ledinfo[1] == '1':
            led_onoff = True
        led1_light_step = int(split_ledinfo[3])
        led2_light_step = int(split_ledinfo[3])
        # no need for MyFile.close()
    print('led_onoff: ',led_onoff,', led1_light_step: ', led1_light_step -1)


def ProcessWriteLedInfo():
    #format =  led_onoff False led1_light_step 5
    global  led_onoff
    global  led1_light_step
    global  led2_light_setp
    lines = ['led_onoff ', '0' , ' led1_light_step ', '5' ]
    if led_onoff == False:
        lines[1] = '0' 
    elif led_onoff == True:
        lines[1] = '1'
    lines[3] = str(led1_light_step)
    #lines[3] = str(led2_light_step)
    with open('led-info.txt', 'w') as ledWriteFile:
        ledStr = ledWriteFile.writelines(lines)
    print('led_onoff: ',led_onoff,', led1_light_step: ', led1_light_step -1)


#LED Step(1~10)
def setLight(light, p):
      p.ChangeDutyCycle(light*10)

def setLED(led_pin, step, p):
    GPIO.output(led_pin, True)
    #GPIO.output(led_pin2, True)
    #p1.ChangeDutyCycle(i*10)
    setLight(step, p)
    #time.sleep(1)

def closeHWsetting():
    global  p1
    global  p2
    global GPIO
    p1.stop()
    p2.stop()
    GPIO.cleanup()

def processCommand(strcommand):
    global  led_onoff
    global  led1_light_step
    global  led2_light_step
    global  p1
    global  p2
    if strcommand == "KEY_POWER": #리모콘의 전원버튼을 눌렀을때
        print(strcommand," powering down...")
        #p0.stop()
        #p1.stop()
        #GPIO.cleanup()
        #closeHWsetting()
        pyautogui.hotkey('ctrl','q') #VLC플레이어의 키보드핫키 "ctrl"과 "q"를 동시에 눌렀을때
        closeHWsetting()
        os.system("sudo systemctl poweroff -i")

    elif strcommand == "KEY_C": #리모콘의 C버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True

        elif led_onoff == True:
            led_onoff = False

        if led_onoff == True:
            if led1_light_step < 1:
                led1_light_step = 1
                led2_light_step = 1
            elif led1_light_step > 10:
                led1_light_step = 10
                led2_light_step = 10

            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_setp, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            setLED(led_pin1, 0, p1)
            setLED(led_pin2, 0, p2)
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_0": #리모콘의 0번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 1
            led2_light_step = 1
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_1": #리모콘의 1번 버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 2
            led2_light_step = 2
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_2": #리모콘의 2번버튼을 눌렀을 때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 3
            led2_light_step = 3
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_3": #리모콘의 3번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 4
            led2_light_step = 4
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_4": #리모콘의 4번버튼을 눌렀으때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 5
            led2_light_step = 5
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_5": #리모콘의 5번버튼을 눌렀을 때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 6
            led2_light_step = 6
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_6": #리모콘의 6번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 7
            led2_light_step = 7
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_7": #리모콘의 7번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 8
            led2_light_step = 8
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_8": #리모콘의 8번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 9
            led2_light_step = 9
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_9": #리모콘의 9번버튼을 눌렀을때
        if led_onoff == False:
            led_onoff = True
        if led_onoff == True:
            led1_light_step = 10
            led2_light_step = 10
            setLED(led_pin1, led1_light_step, p1)
            setLED(led_pin2, led2_light_step, p2)
            print(strcommand, ', led: ', led_onoff, ', step: ', (led1_light_step - 1))
        elif led_onoff == False:
            print(strcommand, ', led: ', led_onoff)
        ProcessWriteLedInfo()
        
    elif strcommand == "KEY_MENU": #리모콘의 "MENU"버튼을 눌렀을 때
        #pyautogui.hotkey('i') #전체화면에서 조작바 보이기
        pyautogui.hotkey('f') #VLC플레이어의 키보드핫키 "f"를 눌렀을때
        print(strcommand, ' control-bar on/off')

    elif strcommand == "KEY_T": #리모콘의 "TEST"버튼을 눌렀을때
        pyautogui.hotkey('r') #Random on and off #VLC플레이어의 키보드핫키 "r"를 눌렀을때
        print(strcommand, ' Random-play on/off')

    elif strcommand == "KEY_UP": #리모콘의 "+"버튼을 눌렀을때 
        pyautogui.hotkey('ctrl', 'up') #VLC플레이어의 키보드핫키 "ctrl"과 "up방향키"를 동시에 눌렀을때
        print(strcommand, ' volume up')

    elif strcommand == "KEY_BACK": #리모콘의 "<--"버튼을 눌렀을때
        pyautogui.hotkey('l') #'L' #VLC플레이어의 키보드핫키 "l"를 눌렀을때
        print(strcommand, ' Loop off, one or all')

    elif strcommand == "KEY_LEFT": #리모콘의 "<<"버튼을 눌렀을때
        pyautogui.hotkey('p') #VLC플레이어의 키보드핫키 "p"를 눌렀을때
        print(strcommand, ' previous track')

    elif strcommand == "KEY_PLAY": #리모콘의 ">"버튼을 눌렀을때
        pyautogui.hotkey('space') #VLC플레이어의 키보드핫키 "스페이스바"를 눌렀을때
        print(strcommand, ' play / pause')

    elif strcommand == "KEY_RIGHT": #리모콘의 ">>"버튼을 눌렀을때
        pyautogui.hotkey('n') #VLC플레이어의 키보드핫키 "n"를 동시에 눌렀을때
        print(strcommand, ' next track')

    elif strcommand == "KEY_DOWN": #리모콘의 "--"버튼을 눌렀을때
        pyautogui.hotkey('ctrl', 'down') #VLC플레이어의 키보드핫키 "ctrl"과 "down방향키"를 동시에 눌렀을때
        print(strcommand, ' volume down')

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

def initLED():
    global  led_onoff
    global  led1_light_step
    global  led2_light_step
    global  p1
    global  p2
    if led_onoff == True:
        if led1_light_step < 1:
            led1_light_step = 1
            led2_light_step = 1
        elif led1_light_step > 10:
            led1_light_step = 10
            led2_light_step = 10
        setLED(led_pin1, led1_light_step, p1)
        setLED(led_pin2, led2_light_setp, p2)
        print('led: ', led_onoff, ', step: ', (led1_light_step - 1))
    elif led_onoff == False:
        setLED(led_pin1, 0, p1)
        setLED(led_pin2, 0, p2)
        print('led: ', led_onoff)
    #ProcessWriteLedInfo()

#define Global
conn = RawConnection()

print("Starting Up...")
ProcessReadLedInfo()
initLED()
try:
      while True:
        ProcessIRRemote()

except KeyboardInterrupt:
      pass

finally:
      p1.stop()
      p2.stop()
      GPIO.cleanup()

