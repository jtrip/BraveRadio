#!/usr/bin/python   

import os 
from time import sleep, gmtime, strftime
import Adafruit_BBIO.GPIO as GPIO

PINS = ["Debug","P9_16","P9_17","P9_18"]

for pin in PINS:
    GPIO.setup(pin, GPIO.IN)

while True:

    if(GPIO.input(PINS[1])==True and GPIO.input(PINS[2])==True):
        if(GPIO.input(PINS[3])==False):
            print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 /Audio/PardonMe.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==True):
        if(GPIO.input(PINS[3])==False):
            print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 /Audio/WeinerDog.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[2])==False and GPIO.input(PINS[1])==True):
        if(GPIO.input(PINS[3])==False):
            print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            os.system('mpg321 /Audio/Soul_Injection.mp3 &')
            sleep(3)

    if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==False):
        if(GPIO.input(PINS[3])==False):
            print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            # os.system('mpg321 /Audio/Codes.mp3 &')
            print('debug log file path')
            sleep(3)