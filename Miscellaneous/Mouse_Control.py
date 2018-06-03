import win32api
import time
import math
import os
import win32con

aspect_ratio = 16 / 9
i = 0
while True:
    x = int(math.cos(math.radians(i)) * 30000 / aspect_ratio + 65535 / 2)
    y = int(math.sin(math.radians(i)) * 30000 + 65535 / 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    win32api.Sleep(10)
    i += 1
    if i % 360 == 0:
        win32api.Sleep(6400)
