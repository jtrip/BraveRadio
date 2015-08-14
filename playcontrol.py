#!/usr/bin/python   

import os 
from time import sleep, gmtime, strftime
import Adafruit_BBIO.GPIO as GPIO

PINS = ["P9_11","P9_12","P9_13"]
path = '/home/debian/audio/audio/'

for pin in PINS:
    GPIO.setup(pin, GPIO.IN)

while True:

    if(GPIO.input(PINS[1])==True and GPIO.input(PINS[2])==True):
        if(GPIO.input(PINS[0])==False):
            print('A: '+ strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 ' + path + 'PardonMe.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==True):
        if(GPIO.input(PINS[0])==False):
            print('B: '+ strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 ' + path + 'WeinerDog.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[2])==False and GPIO.input(PINS[1])==True):
        if(GPIO.input(PINS[0])==False):
            print('C: '+ strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 ' + path + 'Soul_Injection.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==False):
        if(GPIO.input(PINS[0])==False):
            print('D: '+ strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 ' + path + 'Codes.mp3 &')
            sleep(3)
