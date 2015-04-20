#!/usr/bin/python   

import os 
from time import sleep, gmtime, strftime
import Adafruit_BBIO.GPIO as GPIO

PINS = ["","P9_14","P9_15","P9_18"]

while True:

  if(GPIO.input(PINS[1])==True and GPIO.input(PINS[2])==True):
    if(GPIO.input(PINS[3])==False):
      print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
      os.system('mpg321 /home/BraveRadio/audio/PardonMe.mp3 &')
      time.sleep(3)

  if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==True):
    if(GPIO.input(PINS[3])==False):
      print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
      os.system('mpg321 /home/BraveRadio/audio/WeinerDog.mp3 &')
      time.sleep(3)

  if(GPIO.input(PINS[2])==False and GPIO.input(PINS[1])==True):
    if(GPIO.input(PINS[3])==False):
      print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
      os.system('mpg321 /home/BraveRadio/audio/Soul_Injection.mp3 &')
      time.sleep(3)

  if(GPIO.input(PINS[1])==False and GPIO.input(PINS[2])==False):
    if(GPIO.input(PINS[3])==False):
      print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
      os.system('mpg321 /home/BraveRadio/audio/Codes.mp3 &')
      time.sleep(3)