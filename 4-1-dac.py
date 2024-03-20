import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Type a number from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Voltage is {voltage:.4} V")
            else:
                if num < 0:
                    print("Number have to be >=0")
                elif num > 255:
                    print("Number have to be <= 255")  
        except Exception:
            if num == "q": break
            print("not a number")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
