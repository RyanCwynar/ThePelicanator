import time 
import RPi.GPIO as GPIO
import sys
from RpiMotorLib import RpiMotorLib

def doQuarterTurn():
    # This code snippet is for Version 1.2 
    steps = 50/4
    wait = .02
    delay = .05
    GpioPins = [18, 17, 27, 22]
    
    # Declare an named instance of class pass a name and type of motor
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
    time.sleep(0.1)
    # call the function pass the parameters
    mymotortest.motor_run(GpioPins , wait, steps / 2, False, False, "full", delay)
    mymotortest.motor_run(GpioPins , wait, steps, True, False, "full", delay)
    mymotortest.motor_run(GpioPins , wait, steps / 2, False, False, "full", delay)

    # good practise to cleanup GPIO at some point before exit
   
