def des():
    import pygame as pg
    pg.init()
    win = pg.display.set_mode((0,0), pg.FULLSCREEN)
    widch = win.get_width()
    height = win.get_height()
    option = pg.font.SysFont(None,60)

    lang = open('data_user\language.txt','r')
    language = lang.read()
    smile = option.render(':-(',1,(250,250,250))
    if language == 'RU':
        forward = option.render('Кажется, эта функция недоступна или находится в разработке',1,(250,250,250))
        text = option.render('Возвращайтесь сюда в новой версии DUGA',1,(250,250,250))
    elif language == 'EN':
        forward = option.render('Oop, this is function unavailabla or located in developemnt',1,(250,250,250))
        text = option.render('come back here in new version DUGA',1,(250,250,250))

    pressA = pg.image.load('img\XboxJ\A.png')    
    pressA = pg.transform.scale(pressA,(25,25))

    while True:
        try:
            joystick = pg.joystick.Joystick(0)
            joystick.init()
            pg.joystick.init()
            joy = 'ACT'
            session = 'True'
            hats = joystick.get_numhats()
            for i in range(hats):
                hat = joystick.get_hat(i)
        except:
            session = 'False'
            joy = 'NF'
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                import menu
                menu.menu_starter()
            if session == 'True' and joy == 'ACT':
                if joystick.get_button(0):
                    import menu
                    menu.menu_starter()
        win.fill((0,0,0))
        #FILL TO TEXT
        pg.display.flip()
des()