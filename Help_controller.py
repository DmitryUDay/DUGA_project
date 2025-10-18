def bt_load():
    import pygame as pg
    from time import sleep
    from pygame import mixer as mx

    pg.init()
    mx.init()

    win = pg.display.set_mode((0,0),pg.FULLSCREEN)
    widch = win.get_width()
    height = win.get_height()


    option_by = pg.font.SysFont(None, 30)
    forward = option_by.render('Для продолжения нажмите на экран...',1, (250, 250, 250))

    instruction = pg.image.load('img\XboxJ\Xbox_managment.png')
    instruction = pg.transform.scale(instruction,(height,height))


    plh = height/2

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                from menu import menu_starter
                menu_starter()

        win.fill((0,0,0))
        win.blit(instruction,(widch/2-plh,height/2-plh))
        win.blit(forward,(widch/2-190,height-40))
        pg.display.flip()
bt_load()