import RPi.GPIO as GPIO

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)

p.start(0)

try:
    while(1):
        x = int(input("Input the duty cycle: "))
        p.ChangeDutyCycle(x)
        print("Volt: ", 3.3*x/100)

finally:
    p.stop()
    GPIO.output(pin,0)
    GPIO.cleanup()