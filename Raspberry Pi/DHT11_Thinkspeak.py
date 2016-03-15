import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import httplib, urllib
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        h,t = dht.read_retry(dht.DHT11, 4)
        print("Humidity :", h, "Temp :", t)
        params = urllib.urlencode({'key':'ACBM2MHBTLBJ0XK9'})
        urllib.urlopen("https://api.thingspeak.com/update?field1=5",data=params)
        print("Updated")
        time.sleep(15)
        
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally:  
    GPIO.cleanup()
    print ("GPIO Cleaned")
