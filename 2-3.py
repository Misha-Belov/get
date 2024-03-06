import RPi.GPIO as GPIO
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

rng = range(0, 8)

while(True):
    for i in rng:
        GPIO.output(leds, GPIO.input(aux[i]))
        


GPIO.output(leds, 0)
GPIO.cleanup()