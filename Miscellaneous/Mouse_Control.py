import win32api
import time
import math

i = 0
while True:
    win32api.SetCursorPos((int(math.cos(math.radians(i)) * 100 + 683), int(math.sin(math.radians(i)) * 100 + 381)))
    time.sleep(0.01)
    i += 1
    if i % 360 == 0:
        time.sleep(2)
