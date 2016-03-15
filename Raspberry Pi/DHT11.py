import Adafruit_DHT as dht
import time

while True:
    h,t = dht.read_retry(dht.DHT11, 4)
    print 'Temp =', t, 'Humidity =', h
    time.sleep(1)
    
