import pygame as pg

pg.init()
clock = pg.time.Clock()
sw, sh = 1500,1000
screen = pg.display.set_mode((sw,sh))

w, h = 60,60

class ball:
    def __init__(self):
        self.hitbox = pg.Rect(50, 0, w,h)
        self.accel = 4
        self.spdy = 0
        self.spdx = 0
    def proj(self):
        self.hitbox[1] += self.spdy
        self.hitbox[0] += self.spdx
        if self.hitbox[1]< sh-h:
            self.spdy += self.accel
        if self.hitbox[1] >= sh-h:
            self.hitbox[1] = sh-h
            self.spdy = 0
            self.spdx = 0
        if self.hitbox[0] < 0:
            self.hitbox[0] = 0
            self.spdx = 0
        elif self.hitbox[0] > sw-w:
            self.hitbox[0] = sw-w
            self.spdx = 0
    def draw(self):
        pg.draw.ellipse(screen, (255,0,0), self.hitbox)
    def landed(self):
        if self.hitbox[1] >= sh-h:
            landed = True
        else:
            landed = False
        return landed

ball = ball()
jump = False
hold = False

while True:
    pg.event.pump()

    ball.proj()

    # keys = pg.key.get_pressed()
    mouse = pg.mouse.get_pressed()

    if mouse[0] and not hold and not jump:
        x1,y1 = pg.mouse.get_pos()
        hold = True
        jump = True
    elif not mouse[0] and hold and not jump:
        x2, y2 = pg.mouse.get_pos()
        hold = False
        jump = True
        ball.spdx = (x1 - x2)/4
        ball.spdy = (y1 - y2)/4
    elif ball.landed():
        jump = False
    
    # if keys[pg.K_SPACE] and not jump:
    #     jump = True
    #     ball.spdy = -40
    # elif ball.landed():
    #     jump = False
    
    screen.fill((0,0,0))
    ball.draw()
    pg.display.flip()
    clock.tick(30)