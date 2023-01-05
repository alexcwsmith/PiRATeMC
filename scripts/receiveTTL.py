#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:10:03 2022

This script requires setting Linux environment variables with the name, duration (in minutes), and frame rate.
To do this, before running this script either run the below commands in a terminal (using your own desired values), or add these to your .bashrc file if they will not change (video names will have a date && Pi ID to appended them).

export vidName='NameOfVideo'
export vidLength=60
export vidFPS=30

@author: James M. Welsh & Alexander Smith
"""
import RPi.GPIO as GPIO
from time import sleep
import subprocess
import os
from datetime import datetime as dt

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    vidName = os.environ['vidName']
except KeyError:
    print("No system variable 'vidName' set, defaulting to 'Unnamed video' with the date and time.")
    now = dt.now()
    timestamp = now.strftime('%m-%d-%y_%Hh_%Mm_%Ss')
    vidName = 'UnnamedVideo_'+timestamp
try:
    vidLength = os.environ['vidLength']
except KeyError:
    print("No system variable 'vidLength' set, defaulting to 20 minutes")
    vidLength=20
try:
    vidFPS = os.environ['vidFPS']
except KeyError:
    print("No system variable 'vidFPS' set, defaulting to 30")
    vidFPS=30

print("Ready to receive TTL")
while True:
	if GPIO.input(4) == 0:
		break

GPIO.cleanup()

subprocess.Popen(["./recordVideo.sh " + ' '.join([str(vidName) + str(vidLength) + str(vidFPS)])],shell=True)

