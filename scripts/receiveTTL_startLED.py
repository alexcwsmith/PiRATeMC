#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:39:03 2023

@author: smith
"""

import RPi.GPIO as GPIO
from time import sleep
import subprocess
import os
from datetime import datetime as dt

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def callback_on(self):
    GPIO.output(17, 1)

def callback_off(self):
    GPIO.output(17, 0)

GPIO.add_event_detect(4, GPIO.FALLING, bouncetime=50)
GPIO.add_event_callback(4, callback_on)

GPIO.add_event_detect(4, GPIO.RISING, bouncetime=50)
GPIO.add_event_callback(4, callback_off)
