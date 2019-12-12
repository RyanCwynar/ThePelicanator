# Test the GPIO control of the relay
import RPi.GPIO as GPIO
import time
import stepper

def runPump():
    channel = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, 1)
    print("switch is on")
    stepper.doQuarterTurn()
    GPIO.output(channel,0)
    print("switch is off")
    GPIO.cleanup()
