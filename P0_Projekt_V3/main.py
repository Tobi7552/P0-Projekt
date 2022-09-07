#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Motor
right_wheel = Motor(Port.B)
left_wheel = Motor(Port.A)
robot = DriveBase(left_wheel, right_wheel, wheel_diameter = 55, axle_track = 157)
klo_motor = Motor(Port.C)


#Input
color = ColorSensor(Port.S1)
touch = TouchSensor(Port.S4)


#Farver
grey = color.reflection() + 2 
sort = grey / 3
hvid = 85
treshold = (grey + hvid)/2

rettelse = 3.5


# Write your program here.
ev3.speaker.beep(50,1000)
#robot.straight(500)


def linje():
    while True:
        deviation = color.reflection() - treshold
        turn_rate = rettelse * deviation
        turn_rate2 = rettelse * -deviation
        robot.drive(100, turn_rate)
        robot.drive(100, turn_rate2)
        if touch.pressed():
            klo_motor.run_target(500,-400, wait = True)
            klo_motor.run_target(500,400)
            

linje()

        
