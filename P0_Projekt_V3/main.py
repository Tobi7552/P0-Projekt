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
right_wheel = Motor(Port.D)
left_wheel = Motor(Port.C)
robot = DriveBase(left_wheel, right_wheel, wheel_diameter = 55, axle_track = 157)
klo_motor = Motor(Port.B)
klo_sensor = UltrasonicSensor(Port.S1)

#Input
color = ColorSensor(Port.S2)
touch = TouchSensor(Port.S4)


# Write your program here.

def linje(speed,a):                            
    if 65 <= color.reflection() <= 75 or color.reflection() <= 20:
        robot.drive(speed,0)
    elif color.reflection() > 75:
        robot.drive(speed, (a*-0.2)*(color.reflection()-75)**2)
    elif color.reflection() < 65:
        robot.drive(speed, (a*0.2)*(color.reflection()-75)**2)

level = 0

def sort(speed):
    if 5 < color.reflection() < 10:
        robot.straight(20)
        print(level+1)
        return 1
    return 0


def level1():
    robot.turn(45)
    robot.straight(180)
    robot.turn(-45)
    linje(90,1)

def level2():
    robot.turn(-45)
    robot.straight(180)
    robot.turn(45)
    linje(90,1)

def level3():
    while klo_sensor.distance() >= 33:
        linje(70,1)
    else:
        robot.drive(0,0)
        klo_motor.run_until_stalled(1000, then=Stop.HOLD,duty_limit=60)
        robot.drive(50,0)



def level4():
    robot.drive(0,0)
    klo_motor.run_until_stalled(-1000, then=Stop.HOLD,duty_limit=40)
    robot.straight(-50)
    robot.turn(-90)


def level5():
    robot.straight(80)
    robot.turn(-90)

def level6(x):
    robot.turn(10)
    robot.straight(120)
    robot.turn(-20)
    robot.straight(110)
    while color.reflection() >= 50:
        linje(90,1)
    robot.straight(400)
    robot.turn(x*80)
    if x == 1:
        robot.straight(50)
        robot.reset()
        while robot.distance() < 2400:
            linje(90,1) 
        while color.reflection() > 10:
            linje(45,1)


def level7():
    robot.reset()
    robot.turn(-45)
    robot.straight(100)
    robot.turn(45)
    while robot.distance() < 400:
        linje(90,1)
    robot.reset()
    robot.turn(-45)
    robot.straight(100)
    robot.turn(45)

def level8():
    robot.straight(80)
    robot.turn(-90)
    

def level9():
    robot.straight(120)
    robot.turn(80)
    robot.reset()
    while robot.distance() < 955:
        linje(90,-1)
    robot.turn(70)
    robot.straight(50)
    robot.reset()
    while klo_sensor.distance() > 33 and robot.distance() < 30:
        robot.drive(10,0)
    robot.drive(0,0)
    klo_motor.run_until_stalled(1000, then=Stop.HOLD,duty_limit=63)
    robot.reset()
    
    robot.straight(-430)
    klo_motor.run_until_stalled(-1000, then=Stop.HOLD,duty_limit=40)
    robot.straight(-260)
    robot.turn(-110)
    while color.reflection() > 60:
        robot.drive(100,0)
    robot.straight(50)
    robot.turn(-60)



def level11():
    while klo_sensor.distance() > 175:
        linje(35,1)
    robot.turn(45)
    robot.reset()
    while color.reflection() > 60:
        robot.drive(100,-17)
    robot.turn(45) 

def level12():
    robot.reset()
    while robot.distance() < 40:
        linje(35,1)
    robot.turn(45)
    robot.straight(50)
    robot.turn(-45)
    while klo_sensor.distance() > 230:
        robot.drive(70,0)
    while klo_sensor.distance() < 350:
        robot.drive(0,-10)
    robot.turn(-5)
    while klo_sensor.distance() > 300:
        robot.drive(70,0)
    while klo_sensor.distance() < 1000:
        robot.drive(70,24)
    robot.turn(15)
    robot.straight(120)
    while color.reflection() > 65:
        robot.drive(70,-12)

        
def level13():
    robot.straight(100)
    robot.turn(60)
    robot.straight(60)
    robot.turn(-60)
    robot.reset()
    while robot.distance() < 1150:
        linje(90,-1)
    robot.turn(-70)
    robot.straight(110)
    while True:
        robot.stop()


list_ = [['level1()', 0],['level2()', 0],['level3()', 0],['level4()', 0],['level5()', 0],['level6(1)', 0],['level6(-1)', 0],['level7()', 0],['level8()', 0],['level9()', 0],['level11()', 0],['level12()', 0],['level11()', 0],['level13()', 0]]
klo_motor.run_until_stalled(-1000, then=Stop.BRAKE,duty_limit=40)
while True:
    if not touch.pressed():
        level += sort(75)

        if list_[level-1][1] == 0 and level != 0:
            eval(list_[level-1][0])
            list_[level-1][1] = 1


        if level != 3:
            linje(90,1)


    else:
        robot.stop()
