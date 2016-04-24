import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import httplib, urllib
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        h,t = dht.read_retry(dht.DHT11, 4)
        print"Humidity :", h, "Temp :", t
        params = urllib.urlencode({'field1':t, 'field2':h, 'key':'ACBM2MHBTLBJ0XK9'})
        try :
            urllib.urlopen("https://api.thingspeak.com/update",data=params)
            print("Updated...")
        except KeyboardInterrupt:
            print ("Forced Key Exit")
        except:
            pass
        time.sleep(15)
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally:  
    GPIO.cleanup()
    print ("GPIO Cleaned")
