import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

PIN = 26

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

while True:
    if GPIO.input(25):
        GPIO.output(PIN, GPIO.input(25))
    else:
        GPIO.output(PIN, 1)
        sleep(0.5)
        GPIO.output(PIN, 0)
        sleep(0.5)


