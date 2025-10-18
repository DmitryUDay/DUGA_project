def deskrypt_or_kut_scene():
    import pygame as pg
    from pygame import mixer as mx
    pg.init()
    mx.init()
    icon = pg.image.load('img\start\logo_game.png')
    win = pg.display.set_mode((0,0), pg.FULLSCREEN)
    pg.display.set_icon(icon)
    widch = win.get_width()
    height = win.get_height()
    lang = open('data_user\language.txt','r')
    language = lang.read()
    # if language == 'RU':
    #     desc = pg.image.load('img/end/deskripte.png')
    #     desc = pg.transform.scale(desc,(700,1000))
    # elif language == 'EN':
    #     desc = pg.image.load('img/end/deskripteEN.png')
    #     desc = pg.transform.scale(desc,(700,1000))

    text_option = pg.font.SysFont(None,40)
    if language == 'RU':
        one = text_option.render('Альфа проект DUGA версии 1.15 alpha',1,(250,250,250))
        two = text_option.render('Последнее изменение 20.09.2024',1,(250,250,250))

        three = text_option.render('Разработчики:',1,(250,250,250))

        fore = text_option.render('Осипов Дмитрий',1,(250,250,250))
        five = text_option.render('Батищев Фёдор',1,(250,250,250))

        six = text_option.render('Сценарист',1,(250,250,250))

        seven = text_option.render('Тимошечкин Дмитрий',1,(250,250,250))

        eight = text_option.render('Художники',1,(250,250,250))

        nine = text_option.render('Исхаков Арсений',1,(250,250,250))
        ten = text_option.render('Южанов Дмитрий',1,(250,250,250))

        eleven = text_option.render('Powered by UDay studios game',1,(250,250,250))

    elif language == 'EN':
        one = text_option.render('Alpha Project DUGA version 1.15 alpha',1,(250,250,250))
        two = text_option.render('Last modified 20.09.2024',1,(250,250,250))

        three = text_option.render('Developer:',1,(250,250,250))

        fore = text_option.render('Osipov Dmitry',1,(250,250,250))
        five = text_option.render('Batichev Fedor',1,(250,250,250))

        six = text_option.render('Screenwriter',1,(250,250,250))

        seven = text_option.render('Timoshechkin Dmitry',1,(250,250,250))

        eight = text_option.render('Painter',1,(250,250,250))

        nine = text_option.render('Ishakov Arseniy',1,(250,250,250))
        ten = text_option.render('Yujanov Dmitry',1,(250,250,250))

        eleven = text_option.render('Powered by UDay studios game',1,(250,250,250))


    dest = mx.Sound('sound\end\sound_track_tlt.mp3')
    dest.play()


    speed = .1

    p1 = height-200
    p2 = height-200+28+10
    p3 = height-200+28*2+15
    p4 = height-200+28*3+20
    p5 = height-200+28*4+25
    p6 = height-200+28*5+30
    p7 = height-200+28*6+35

    p8 = height-200+28*7+40
    p9 = height-200+28*8+45
    p10 = height-200+28*9+50
    p11 = height-200+28*10+55


    while True:
        for event in pg.event.get():
            mouse = pg.mouse.get_pressed()
            if event.type == pg.MOUSEBUTTONDOWN and mouse[0]:
                dest.stop()
                from menu import menu_starter
                menu_starter()
        if p11 <= -30:
            dest.stop()
            from menu import menu_starter
            menu_starter()

        win.fill((0,0,0))
        win.blit(one,(widch/2-(526/2),p1))
        win.blit(two,(widch/2-(453/2),p2))
        win.blit(three,(widch/2-(197/2),p3))
        win.blit(fore,(100,p4))
        win.blit(five,(100,p5))
        win.blit(six,(widch/2-(145/2),p6))
        win.blit(seven,(100,p7))
        win.blit(eight,(widch/2-(157/2),p8))

        win.blit(nine,(100,p9))
        win.blit(ten,(100,p10))
        win.blit(eleven,(widch/2-(424/2),p11))

        pg.display.flip()

        p1 -= speed
        p2 -= speed
        p3 -= speed
        p4 -= speed
        p5 -= speed
        p6 -= speed
        p7 -= speed
        p8 -= speed
        p9 -= speed
        p10 -= speed
        p11 -= speed

deskrypt_or_kut_scene()