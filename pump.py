# Test the GPIO control of the relay
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def runPump():
    channel = 4
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, 1)
    print("switch is on")
    time.sleep(1)
    GPIO.output(channel,0)
    print("switch is off")
    GPIO.cleanup()
