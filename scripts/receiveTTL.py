#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:10:03 2022

This script requires setting Linux environment variables with the name, duration (in minutes), and frame rate.
To do this, before running this script either run the below commands in a terminal (using your own desired values), 
or add these to your .bashrc file if they will not change (video names will have a date && Pi ID to appended them).

export vidName='NameOfVideo'
export vidLength=60
export vidFPS=30

If you are unsure if you are exporting variables correctly, after you run the export command above 
you can see the variable in the terminal using the 'echo' command and putting a $ in front of the variable name,
for example putting this into the terminal should print 60:
echo $vidName

 

@author: James M. Welsh & Alexander Smith
"""
import RPi.GPIO as GPIO
from time import sleep
import subprocess
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    vidName=os.environ['vidName']
except KeyError:
    print("No environment variable set for vidName, create one by exporting one in a terminal, for example:\n export vidName='exampleVideoName'")
try:
    vidLength = os.environ['vidLength']
except KeyError:
    print("No environment variable set for vidLength, create one by exporting one in a terminal, for example:\n export vidLength=60")
try:
    vidFPS = os.environ['vidFPS']
except KeyError:
    print("No environment variable set for vidFPS, create one by exporting one in a terminal, for example:\n export vidFPS=60")

print("Ready to receive TTL")
while True:
	if GPIO.input(4) == 0:
		break

GPIO.cleanup()

subprocess.Popen(["./recordVideo.sh " + ' '.join([str(vidName) + str(vidLength) + str(vidFPS)])],shell=True)

