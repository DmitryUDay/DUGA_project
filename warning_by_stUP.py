from img.imageImportGame import *
from helper import ScreenFader
def des_start(win):
    import pygame as pg
    from helper import getFont,langu
    from pygame import mixer as mx
    pg.init()
    mx.init()
    widch = win.get_width()
    height = win.get_height()
    option_by = pg.font.SysFont(None, 50)
    clock = pg.time.Clock()
    fader = ScreenFader(win)
    descrypte = pg.image.load('img/start/descrypte.png')
    forward = option_by.render('Для продолжения нажмите на экран...',1, (250, 250, 250))
    fader.start("in", speed=5)  # активируем фейд



    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                fader.start("out", speed=5, block=True, clock=clock)
                return 'menu'
        
        # --- Сначала рисуем всё, что должно быть видно ---
        win.fill((0,0,0))
        win.blit(descrypte, (widch//2-643, 50))
        win.blit(forward, (widch//2-getFont(forward,'x')//2, height-getFont(forward,'y')-20))
        
        # --- Затем накладываем фейдер ---
        fader.update()
        
        pg.display.flip()
        clock.tick(60)
