import pygame as pg
import math

pg.init()
win = pg.display.set_mode((800,500))
WHITE = (255, 255, 255)


rect = pg.Rect(20,20,200,200)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    win.fill((0,0,0))
    power_button(win, pg.Rect(100, 100, 120, 120))
    pg.display.flip()