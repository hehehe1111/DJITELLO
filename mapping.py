from djitellopy import tello
import pygame
import numpy as np
import KeyPressModule as Kp
from time import sleep
import cv2
import math

##parameters##
fspeed = 117/10 #forward speeed
aspeed = 360/10 #angular speed degrees
interval = 0.25

dInterval = fspeed*interval
aInterval = aspeed*interval
###
x, y = 500, 500
a = 0
yaw = 0
Kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
j

pygame.init()
win = pygame.display.set_mode((400, 400))

points = [(0, 0), (0, 0)]
def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    aspeed = 50
    d = 0
    global x, y, yaw, a
    if getkey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif getkey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180
    if getkey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif getkey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90
    if getkey("w"): ud = speed
    elif getkey("s"): ud = -speed

    if getkey("a"):
        yv = aspeed
        yaw -= aInterval
    elif getkey("d"):
        yv = -aspeed
        yaw += aInterval
    if getkey("q"): me.land()
    if getkey("e"): me.takeoff()

    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))
    return [lr, fb, ud, yv, x, y]

def drawPoints():
    for point in points:
        cv2.circle(img, point, 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, point, 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100} ,{(points[-1][1]- 500 )/ 100})m',
                (points[-1][0]+10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)

while True:
    val = getKeyboardInput()
    me.send_rc_control(val[0], val[1], val[2], val[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    if (points[-1][0] != val[4] or points[-1][1] != val[5]):
        points.append((val[4], val[5]))

    drawPoints()
    cv2.imshow("Output", img)
    cv2.waitKey(1)