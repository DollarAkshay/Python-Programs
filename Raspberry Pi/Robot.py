import RPi.GPIO as GPIO
import time
import curses

leftf = 16
leftb = 18

rightf = 13
rightb = 11

def moveright():
    GPIO.output(leftf, 1)
    GPIO.output(leftb, 0)
    GPIO.output(rightf, 0)
    GPIO.output(rightb, 1)

def moveleft():
    GPIO.output(leftf, 0)
    GPIO.output(leftb, 1)
    GPIO.output(rightf, 1)
    GPIO.output(rightb, 0)

def moveforward():
    GPIO.output(leftf, 1)
    GPIO.output(leftb, 0)
    GPIO.output(rightf, 1)
    GPIO.output(rightb, 0)

def movebackward():
    GPIO.output(leftf, 0)
    GPIO.output(leftb, 1)
    GPIO.output(rightf, 0)
    GPIO.output(rightb, 1)

def stop():
    GPIO.output(leftf, 0)
    GPIO.output(leftb, 0)
    GPIO.output(rightf, 0)
    GPIO.output(rightb, 0)


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(leftf, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leftb, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(rightf, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rightb, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        key = screen.getch()

        if key == curses.KEY_UP:
            moveforward()
        elif key == curses.KEY_DOWN:
            movebackward()
        elif key == curses.KEY_RIGHT:
            moveright()
        elif key == curses.KEY_LEFT:
            moveleft()
        elif key==ord('x'):
            break
        else :
            stop()
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally :
    curses.endwin()
    GPIO.cleanup()
