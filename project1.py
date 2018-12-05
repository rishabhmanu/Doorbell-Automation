import RPi.GPIO as GPIO
import time
import requests
import datetime as d

url='https://api.thingspeak.com/update'
key='SFY1JWR6MH6X8MK4'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)      #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)      #LED output pin
while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print("No intrusion")
        GPIO.output(3, 0)    #Turn OFF LED
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print("Intruder detected")
        GPIO.output(3, 1)    #Turn ON LED
        data={'api_key':key,'field1':d.datetime.now()}
	requests.post(url,data)
	time.sleep(0.1)
