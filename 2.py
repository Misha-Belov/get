import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

PIN = 26

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

GPIO.output(PIN, 1)
sleep(1)
GPIO.output(PIN, 0)
sleep(1)

GPIO.output(PIN, 1)
sleep(1)
GPIO.output(PIN, 0)
sleep(1)


GPIO.output(PIN, 1)
sleep(1)
GPIO.output(PIN, 0)
sleep(1)

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)

GPIO.output(PIN, 1)
sleep(0.5)
GPIO.output(PIN, 0)
sleep(0.5)