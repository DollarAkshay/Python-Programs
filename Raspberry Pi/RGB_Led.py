import RPi.GPIO as GPIO
import time


vcc = 18
red = 11                            # No Resistor
green = 12                          # 3k Resistor
blue = 13                           # 2k Resistor

GPIO.setmode(GPIO.BOARD)
GPIO.setup(vcc, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(red, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(green, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(blue, GPIO.OUT, initial=GPIO.HIGH)

print("Starting...")

rp = GPIO.PWM(red, 500)
rp.start(0)
gp = GPIO.PWM(green, 500)
gp.start(100)
bp = GPIO.PWM(blue, 500)
bp.start(100)

time.sleep(0.5)

for x in range(0, 101):
    rp.ChangeDutyCycle(x)
    gp.ChangeDutyCycle(100-x)
    time.sleep(0.04)


for x in range(0, 101):
    gp.ChangeDutyCycle(x)
    bp.ChangeDutyCycle(100-x)
    time.sleep(0.04)

for x in range(0, 101):
    bp.ChangeDutyCycle(x)
    rp.ChangeDutyCycle(100-x)
    time.sleep(0.04)

time.sleep(0.5)
    
print("Cleaning GPIO")
GPIO.cleanup()

