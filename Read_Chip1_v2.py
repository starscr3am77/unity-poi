#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
import MFRC522
import time
import signal
import os

plate1 = [136, 4, 121, 65, 180]
indicator1 = 0
counter = 0
cat = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    state = GPIO.input(16)
    #print (state)

    if indicator1 == 1 and state == 0:
        GPIO.output(12, GPIO.LOW)
    elif counter == 9:
        GPIO.output(12, GPIO.HIGH)

    if indicator1 == 1 and state == 0 and cat == 0:
        os.system('mpg123 -q cat.mp3 &')
        time.sleep(6)
        os.system('pkill -9 mpg123')
        cat = 1

    indicator1 = 0
    counter = counter + 1
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        #print ("Card detected")
    
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        #print (status)

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            #print (uid[:5])
            if uid[:5] == plate1 and state == 0:
                #print ("Plate 1 in position")
                indicator1 = 1
                counter = 0
            else:
                #print ("Find plate 1")
                indiator1 = 0

