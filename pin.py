import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


def blinktimes(count):
    for i in range(count):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.1)

def tryPin(pin):
    zahlstring = str(pin)
    zahlstring = zahlstring.zfill(4)
    print(zahlstring)
    liste = [int(i) for i in zahlstring]

    blinktimes(1)
    time.sleep(4)
    blinktimes(liste[0])
    time.sleep(3)
    blinktimes(liste[1])
    time.sleep(3)
    blinktimes(liste[2])
    time.sleep(3)
    blinktimes(liste[3])
    time.sleep(4)

    os.system("fswebcam -r 640x480 --jpeg 25 --save " + zahlstring + ".jpg")

for i in range(0,10000):
    tryPin(i)
