from flask import Flask, request, render_template

import random, string
import time
from time import sleep

import cherrypy
import os

import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/process', methods=['ON1'])
def turn_it_on1():
    GPIO.setup(12, GPIO.OUT) 
    GPIO.output(12, GPIO.LOW)

    time.sleep(6);

    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)

    return "Opened door"

@app.route('/process', methods=['OFF1'])
def turn_it_off1():
	os.system("sudo shutdown -r now")
	
	return "Reboot Pi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
