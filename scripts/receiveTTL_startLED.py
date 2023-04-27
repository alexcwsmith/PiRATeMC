#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script uses Raspberry Pi GPIO to receive a TTL and turn on an LED for the duration of the TTL. See image at github.com/alexcwsmith/PiRATeMC/tree/master/docs/TTL_and_LED_Wiring.png
for example of how to wire this.

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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN) #TTL
GPIO.setup(11, GPIO.OUT) #LED

def callback_on(self):
    GPIO.output(11, 1)
    logging.info('START TTL, LED ON')

def callback_off(self):
    GPIO.output(11, 0, 'END TTL, LED OFF')

GPIO.add_event_detect(15, GPIO.FALLING, bouncetime=50)
GPIO.add_event_callback(15, callback_on)

GPIO.add_event_detect(15, GPIO.RISING, bouncetime=50)
GPIO.add_event_callback(15, callback_off)
