import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

# number = [0, 0, 0, 0, 0, 0, 0, 0] #0
# number = [0, 0, 0, 0, 0, 0, 0, 1] # 1
# number = [0, 0, 0, 0, 0, 0, 1, 0] #2
# number = [0, 0, 0, 0, 0, 0, 1, 1] # 3
number = [0, 0, 0, 0, 0, 1, 0, 0] # 4

# number = [0, 0, 0, 0, 0, 1, 0, 1] #5
# number = [0, 0, 1, 0, 0, 0, 0, 0] #32
# number = [0, 1, 0, 0, 0, 0, 1, 0] #64
# number = [0, 1, 1, 1, 1, 1, 1, 1] #127
# number = [1, 1, 1, 1, 1, 1, 1, 1] #255
# number = [0, 0, 0, 0, 0, 0, 0, 0] #256


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)
time.sleep(10)

GPIO.output(dac, 0)
GPIO.cleanup()


# 
# 
# graph = [0.04, 0.05, 0.08 , 0.09, 0.07,  0.11, 0.45, 0.89, 1.67, 3.25, 0.04]
# numb_ = [0, 1, 2, 3, 4, 5, 32, 64, 127, 255, 256]
# 