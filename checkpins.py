#!/usr/bin/python   

import os 
from time import sleep, gmtime, strftime
import Adafruit_BBIO.GPIO as GPIO


PINS_TO_CHECK = ["P9_11","P9_12","P9_13"]

for pin in PINS_TO_CHECK:
    GPIO.setup(pin, GPIO.IN)

while True:
    for pin in PINS_TO_CHECK:
        if GPIO.input(pin):
            print(pin +": HIGH")
        else:
            print(pin +": LOW")
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    sleep(1)