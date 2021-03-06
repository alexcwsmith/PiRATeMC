#!/usr/bin/env python
"""
This script sends out a 500ms TTL pulse, and can be started simultaneously with
recordVideo.sh (run on a separate RPi or a second user account on the same RPi) to send TTLs via BNC (pin 11 / BCM 17) 
to a fiber photometry system (or whatever third-party equipment), and will illuminate an LED simultaneously (pin 15 / GPIO22) that you can have
in the frame of the behavioral video recording for DLC to track behavior and data that is time-stamped by TTLs.
See included pictures for help wiring. The breadboard/resistor for the LED is not absolutely necessary but is suggested to protect the LED from high voltage.
"""
    import RPi.GPIO as GPIO
except ImportError:
    print("RPi.GPIO module not found. Install it with pip install RPi.GPIO")
import time

GPIO.setmode(GPIO.BOARD) #mode GPIO.BOARD uses pin numbering in order 1-40, using mode GPIO.BCM uses the pin numbering here: https://pinout.xyz/
GPIO.setup(15, GPIO.OUT, initial=0)
GPIO.setup(11, GPIO.OUT, initial=0)
for i in range(20):
    print("Step " + str(i)) #Only useful if you have Pi plugged into PiTFT touchscreen or another display.
    GPIO.output(15, 1)
    GPIO.output(11, 1)
    time.sleep(0.5) #TODO: Make time decrease based on i, so pulse duration is quantitative indicator of how long into session it occurs. May want to change the TTL pin from 11 to 32 (PWM0, GPIO.BCM mode Pin 12) and LED from Pin 15 to Pin 33 (PWM1, BCM mode pin 13) to take advantage of pulse width modulation.
    GPIO.output(15, 0)
    GPIO.output(11, 0)
    time.sleep(29.5) #TODO: Change sleep time in accordance with adjusting pulse time above.

GPIO.cleanup()

#TODO: See if multithreading is possible to be able to run this script and the recordVideo.sh script separately at the same time from same ssh session, rather than running from separate ssh session or separate RPi.
