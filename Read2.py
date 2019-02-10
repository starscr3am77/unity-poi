#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import time
import signal
import os

plate1 = [101, 23, 24, 169, 195]

indicator1 = 0
indicator2 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    print ("Reading")
    print (indicator1)
    
    if indicator1 == 1:
        GPIO.output(18,GPIO.HIGH)
    else:
        GPIO.output(18,GPIO.LOW)

    indicator1 = 0

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    #if status == MIFAREReader.MI_OK:
    #    print("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        print (uid[:5])
        
        if uid[:5] == plate1:
            print ("Plate 1")
            indicator1 = 1

        else:
            print ("Wrong Plate")
            indicator1 = 0

        
            

