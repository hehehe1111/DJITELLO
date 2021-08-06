import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    speed = 50
    if getKey("LEFT"):
        lr = -speed
    elif getKey("RIGHT"):
        lr = speed
    if getKey("UP"): fb = speed
    elif getKey("DOWN"): fb = -speed

    if getKey("w"): ud = speed
    elif getKey("s"): ud = -speed

    if getKey("a"): yv = speed
    elif getKey("d"): yv = -speed

    if getKey("q"): me.land()
    if Kp.getKey("e"): me.takeoff()


if __name__ == '__main__':
    init()
    while True:
       main()