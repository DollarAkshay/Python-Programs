import RPi.GPIO as GPIO
import sys
import time

out_pins = [29, 31, 33, 35, 36, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)
GPIO.setup( out_pins, GPIO.OUT)

GPIO.setup( out_pins, GPIO.OUT, initial=GPIO.LOW)

c = raw_input("\nEnter a character : ")
c = c[0]

try:
    while c!='x':
        a = ord(c)
        asciiart=""
        print 'Binary ASCII = ', bin(a)
        for i in range(8):
            if (a & (1<<i)) != 0:
                GPIO.output(out_pins[i], True)
                asciiart+="* "
            else:
                GPIO.output(out_pins[i], False)
                asciiart+="- "
        asciiart = asciiart[::-1]
        print(asciiart)
        
        time.sleep(1)
        c = raw_input("\nEnter a character : ")
        c = c[0]

except KeyboardInterrupt:
    print ("\n", counter)
except:
    pass
finally:  
    GPIO.cleanup()


