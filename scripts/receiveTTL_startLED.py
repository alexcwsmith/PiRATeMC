#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:39:03 2023

@author: smith
"""

import RPi.GPIO as GPIO
import logging
from datetime import datetime as dt

logging.basicConfig(filename=dt.now().strftime('%m-%d-%Y'),
                    filemode='a',
                    format='%(asctime)s,%(msecs)d, %(name)s, %(levelname)s, %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def callback_on(self):
    GPIO.output(17, 1)
    logging.info('START TTL, LED ON')

def callback_off(self):
    GPIO.output(17, 0, 'END TTL, LED OFF')

GPIO.add_event_detect(4, GPIO.FALLING, bouncetime=50)
GPIO.add_event_callback(4, callback_on)

GPIO.add_event_detect(4, GPIO.RISING, bouncetime=50)
GPIO.add_event_callback(4, callback_off)
