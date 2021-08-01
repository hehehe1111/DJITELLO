from djitellopy import tello
import KeyPressModule as Kp
import time
import cv2
Kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img

me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if Kp.getkey("LEFT"): lr = -speed
    elif Kp.getkey("RIGHT"): lr = speed

    if Kp.getkey("UP"): fb = speed
    elif Kp.getkey("DOWN"): fb = -speed

    if Kp.getkey("w"): ud = speed
    elif Kp.getkey("s"): ud = -speed

    if Kp.getkey("a"): yv = speed
    elif Kp.getkey("d"): yv = -speed

    if Kp.getkey("q"): me.land(); time.sleep(3)
    if Kp.getkey("e"): me.takeoff()

    if Kp.getkey("z"): cv2.imwrite(f'Resources/Images/{time.time()}.jpg')

    return [lr, fb, ud, yv]


while True:
    val = getKeyboardInput()
    me.send_rc_control(val[0], val[1], val[2], val[3])

    img = me.get_frame_read().frame

    scale_percent = 70  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation= cv2.INTER_AREA)
    cv2.imshow("Image", resized)
    cv2.waitKey(1)
    time.sleep(0.05)
