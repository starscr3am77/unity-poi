import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(18,GPIO.LOW)

GPIO.setup(21,GPIO.OUT)
print ("LED on")
GPIO.output(21,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(21,GPIO.LOW)
