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
import MFRC522_Chip2
import MFRC522
import signal

plate1 = [222, 86, 127, 87, 246]
plate2 = [86, 126, 214, 255, 87]

indicator1 = 0
indicator2 = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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
MIFAREReader_Chip2 = MFRC522_Chip2.MFRC522()

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for chip 1   
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    #print (status)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card 1 detected")
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        if indicator1 == 1:
            GPIO.setup(12, GPIO.OUT)
            GPIO.output(12, GPIO.LOW)
            print ("!")
        else:
            GPIO.setup(12, GPIO.OUT)
            GPIO.output(12, GPIO.HIGH)

        indicator1 = 0

        print (uid)

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            if uid[:5] == plate1:
                print ("Plate 1 in position")
                indicator1 = 1
            else:
                ("Find plate 1")
                indiator1 = 0
    
    # Scan for chip 2   
    (status,TagType) = MIFAREReader_Chip2.MFRC522_Request(MIFAREReader_Chip2.PICC_REQIDL)

    #print (status)

    # If a card is found
    if status == MIFAREReader_Chip2.MI_OK:
        print ("Card 2 detected")
        # Get the UID of the card
        (status,uid) = MIFAREReader_Chip2.MFRC522_Anticoll()

        if indicator2 == 1:
            GPIO.setup(16, GPIO.OUT)
            GPIO.output(16, GPIO.LOW)
            print ("?")
        else:
            GPIO.setup(16, GPIO.OUT)
            GPIO.output(16, GPIO.HIGH)

        indicator2 = 0

        print (uid)

        #If we have the UID, continue
        if status == MIFAREReader_Chip2.MI_OK:

            if status == MIFAREReader.MI_ERR:
                if uid[:5] == plate2:
                    print ("Plate 2 in position")
                    indicator2 = 1
                else:
                    print("Find plate 2")
                    indiator2 = 0
