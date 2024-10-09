import pygame as pg

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((800,600))

class ball:
    def __init__(self):
        self.hitbox = pg.Rect(370, 540, 60,60)
        self.accel = 3
        self.spdy = 0
    def update(self):
        self.hitbox[1] += self.spdy
        if self.hitbox[1]<540:
            self.spdy += self.accel
        if self.hitbox[1] >= 540:
            self.hitbox[1] = 540
            self.spdy = 0
    def draw(self):
        pg.draw.ellipse(screen, (255,0,0), self.hitbox)
    def landed(self):
        if self.hitbox[1] >= 540:
            landed = True
        else:
            landed = False
        return landed

ball = ball()
jump = False

while True:
    pg.event.pump()

    ball.update()

    keys = pg.key.get_pressed()
    
    if keys[pg.K_SPACE] and not jump:
        jump = True
        ball.spdy = -40
    elif ball.landed():
        jump = False
    
    screen.fill((0,0,0))
    ball.draw()
    pg.display.flip()
    clock.tick(30)