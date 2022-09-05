#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile




# Create your objects here.
ev3 = EV3Brick()
touch = TouchSensor(Port.S1)
klo = Motor(Port.C)
line_sensor = Color.Sensor(Port.S2)

#Motor objekter
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.b)
robot = Drivebase(left_wheel, right_wheel, wheel_diameter=55.5, axle_track=100)

#Farvers grænseværdi
black = 9
white = 85
treshold = (black + white) / 2


rettelse_tilføj = 1.2


# Write your program here.

def klo(close):
     while True
     touch.pressed():
        robot.run(0, 0):
        #klo.run_target(500, 1000)
        klo.run_untill_stalled(500, duty_limit=70)
        robot.run_target(500, 1000)
        robot.turn(180, then=stop.HOLD, wait=True)

def klo(open):
    while True
     touch.pressed():
        robot.run(0, 0):
        #klo.run_target(500, 1000)
        klo.run_untill_stalled(500, duty_limit=70)
        robot.run_target(500, -1000)
        robot.turn(180, then=stop.HOLD, wait=True)

def linje(test):
    while True
        #regner afvigelsen fra grænseværdien
        deviation = line_sensor.reflection() - treshold
        #Beregner hvor hurtigt robotten skal dreje for at rette sig op
        turn_rate = rettelse_tilføj * deviation

        robot.drive(DRIVE_SPEED, turn_rate)
        klo('close')
        
    
linje('test')



    

    




