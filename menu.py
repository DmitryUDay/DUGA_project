tema = 1
from img.imageImportGame import *
def menu_starter(win):
    global tema
    import pygame as pg
    from pygame import mixer as mx
    from random import randint
    from random import choice
    from helper import getFont,langu
    from time import sleep
    import threading
    import math

    pg.init()
    mx.init()
    widch = win.get_width()
    height = win.get_height()
    text_option = pg.font.SysFont('Arial Black',40)
    textMenu = pg.font.SysFont('Arial Black',60)
    text = pg.font.SysFont('Arial Black',20)
    nightLam = open('data_user/nightUser.txt','r')
    night = nightLam.read()
    nightLam.close()
    version = text.render('betta 1.16',1,(255,255,255))


    DUGA_copyright = text.render('DUGA от UDay project©',1,(255,255,255))
    walback = text_option.render('Приветствуйте обновление Бетта 1.16',1,(255,255,255))
    Ncontinues = textMenu.render(f'Продолжить {night}',1,(138,129,80))
    new_game = textMenu.render('Новая смена',1,(138,129,80))
    option = textMenu.render('Параметры',1,(138,129,80))
    exit_in_game = textMenu.render('Выход',1,(138,129,80))



    kursour = textMenu.render('>>',1,(138,129,80))




    contra = pg.image.load('img/menu/logo_controler.png')
    contra = pg.transform.scale(contra,(50,50))

    # Загружаем анимацию и фоны (не сокращал, чтобы не поломать ссылки)
    oneSt = pg.transform.scale(pg.image.load('img/loading/1.png'), (500,500))
    twoSt = pg.transform.scale(pg.image.load('img/loading/2.png'), (500,500))
    threeSt = pg.transform.scale(pg.image.load('img/loading/3.png'), (500,500))
    foreSt = pg.transform.scale(pg.image.load('img/loading/4.png'), (500,500))
    fiveSt = pg.transform.scale(pg.image.load('img/loading/5.png'), (500,500))
    sixSt = pg.transform.scale(pg.image.load('img/loading/6.png'), (500,500))
    sevenSt = pg.transform.scale(pg.image.load('img/loading/7.jpg'), (500,500))
    eightSt = pg.transform.scale(pg.image.load('img/loading/8.jpg'), (500,500))
    nineSt = pg.transform.scale(pg.image.load('img/loading/9.jpg'), (500,500))
    tenSt = pg.transform.scale(pg.image.load('img/loading/10.jpg'), (500,500))
    elevenSt = pg.transform.scale(pg.image.load('img/loading/11.jpg'), (500,500))
    twelveSt = pg.transform.scale(pg.image.load('img/loading/12.jpg'), (500,500))
    freetinSt = pg.transform.scale(pg.image.load('img/loading/13.jpg'), (500,500))
    foretinSt = pg.transform.scale(pg.image.load('img/loading/14.jpg'), (500,500))
    fivetinSt = pg.transform.scale(pg.image.load('img/loading/15.jpg'), (500,500))

    fone = pg.transform.scale(pg.image.load('img/menu/foneImage.png'), (widch,height))
    tems = [pg.transform.scale(pg.image.load(f'img/temnenie/{i}.png'), (widch,height)) for i in range(1, 11)]

    statik = [tem10,tem9,tem8,tem7,tem6,tem5,tem4,tem3,tem2,tem1]
    tema = 1
    def drawTem():
        global tema
        if tema != 10:
            ar = tema-1
            win.blit(statik[ar],(0,0))
            tema+=1


    def ng():
        clock = pg.time.Clock()
        widch = win.get_width()
        height = win.get_height()
        # -------------------------------
        # 1. Крутящийся кружок
        # -------------------------------
        def loading_spinner(surface, t, scale=1.0):
            """Анимация крутящегося спиннера с регулировкой размера.
            scale = 1.0 — обычный размер, <1 — меньше, >1 — больше.
            """
            base_radius = 50 * scale          # Радиус большого круга
            dot_base_size = 8 * scale         # Базовый размер точки
            dot_size_variation = 4 * scale    # Разброс размера точки
            offset = 10 * scale               # Отступ от края

            x_center, y_center = widch - base_radius - offset, height - base_radius - offset

            for i in range(12):
                angle = i * (360 / 12) + t * 300
                rad = math.radians(angle)
                x = x_center + math.cos(rad) * base_radius
                y = y_center + math.sin(rad) * base_radius
                size = int(dot_base_size + dot_size_variation * math.sin(math.radians(angle + t * 500)))
                pg.draw.circle(surface, (255,255,255), (int(x), int(y)), size)



            # -------------------------------
            # ГЛАВНЫЙ ЦИКЛ ДЛЯ ТЕСТА
            # -------------------------------

        time_start = pg.time.get_ticks()

        for i in range(0,100):
            dt = clock.tick(60) / 1000
            t = (pg.time.get_ticks() - time_start) / 1000

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            win.fill((0,0,0))
            loading_spinner(win, t, scale=0.5)  # маленький
            pg.display.flip()
        return 'NG'

    title = mx.Sound('sound/menu/title.mp3')
    title.play(-1)

    enter = mx.Sound('sound/menu/select.mp3')
    notselect = mx.Sound('sound/menu/nselect.mp3')
    biz = mx.Sound('sound\game\select.mp3')

    def drawContent():
        nonlocal Ncontinues, exit_in_game, new_game, option
        rnd = randint(1,100)
        text_val = 'ОНИ НЕ СПЯТ'
        if rnd in (70,80,90,100):
            if rnd == 70: Ncontinues = textMenu.render(text_val,1,(138,129,80))
            elif rnd == 80: exit_in_game = textMenu.render(text_val,1,(138,129,80))
            elif rnd == 90: new_game = textMenu.render(text_val,1,(138,129,80))
            elif rnd == 100: option = textMenu.render(text_val,1,(138,129,80))
        else:
            Ncontinues = textMenu.render(f'Продолжить {night}',1,(138,129,80))
            new_game = textMenu.render('Новая смена',1,(138,129,80))
            option = textMenu.render('Параметры',1,(138,129,80))
            exit_in_game = textMenu.render('Выход',1,(138,129,80))


        win.blit(walback,(5,5))
        win.blit(version,(5,height-5-getFont(version,'y')))
        win.blit(DUGA_copyright,(widch-getFont(DUGA_copyright,'x')-5, height-getFont(DUGA_copyright,'y')-5))
        win.blit(Ncontinues,(widch-getFont(Ncontinues,'x')-50,360))
        win.blit(new_game,(widch-getFont(new_game,'x')-50,360+10+getFont(Ncontinues,'y')))
        win.blit(option,(widch-getFont(option,'x')-50,360+20+getFont(new_game,'y')*2))
        win.blit(exit_in_game,(widch-getFont(exit_in_game,'x')-50,360+30+getFont(new_game,'y')*3))


    def stopMus():
        """Плавно уменьшает громкость до 0 за duration секунд"""
        start_volume = title.get_volume()  # текущая громкость (0.0-1.0)
        steps = 50  # количество шагов изменения громкости
        delay = 1 / steps

        for i in range(steps):
            # Вычисляем новую громкость
            new_volume = start_volume * (1 - i / steps)
            title.set_volume(new_volume)
            sleep(delay)

        # В конце громкость 0 и останавливаем музыку
        title.set_volume(0)
        title.stop()

    def animat(pos):
        startINI = threading.Thread(target=stopMus)
        startINI.start()
        for cadr in tems:
            win.blit(fone,(0,0))
            drawContent()
            win.blit(cadr,(0,0))
            pg.display.flip()
            pg.time.Clock().tick(24)
        if pos == 'new_game':
            nightLam = open('data_user/nightUser.txt','w')
            nightLam.write('1')
            nightLam.close()
            return ng()
        elif pos == 'continues':
            return ng()
        elif pos == 'option':
            return "option"

    # Первый запуск — эффект появления
    # for cadr in reversed(tems):
    #     win.blit(fone,(0,0))
    #     drawContent()
    #     win.blit(cadr,(0,0))
    #     pg.display.flip()
    #     pg.time.Clock().tick(24)

    # Главный цикл меню
    while True:
        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            elif event.type == pg.MOUSEBUTTONDOWN:
                biz.play()
                # Кнопка контроллера
                if widch-55 <= mouse[0] <= widch-5 and 5 <= mouse[1] <= 55:
                    from Help_controller import bt_load
                    bt_load()

                # ПРОДОЛЖИТЬ
                elif 0 <= mouse[0] <= widch and 360 <= mouse[1] <= 360+getFont(Ncontinues,'y'):
                    return animat('continues')  # Здесь можно будет добавить логику

                # НОВАЯ ИГРА
                elif 0 <= mouse[0] <= widch and 360+10+getFont(Ncontinues,'y') <= mouse[1] <= 360+10+getFont(Ncontinues,'y')+getFont(Ncontinues,'y'):
                    return animat('new_game')

                # НАСТРОЙКИ
                elif 0 <= mouse[0] <= widch and 360+20+getFont(option,'y')*2 <= mouse[1] <= 360+20+getFont(option,'y')*2+getFont(option,'y'):
                    return animat('option')

                # ВЫХОД
                elif 0 <= mouse[0] <= widch and 360+20+getFont(exit_in_game,'y')*3 <= mouse[1] <= 360+20+getFont(exit_in_game,'y')*3+getFont(exit_in_game,'y'):
                    title.stop()
                    exit()

        # Отрисовка кадра
        win.blit(fone,(0,0))
        drawContent()

        # Подсветка курсора
        if 0 <= mouse[0] <= widch and 360 <= mouse[1] <= 360+getFont(Ncontinues,'y'):
            win.blit(kursour,(widch-getFont(Ncontinues,'x')-50-10-getFont(kursour,'x'),360))
        elif 0 <= mouse[0] <= widch and 360+10+getFont(Ncontinues,'y') <= mouse[1] <= 360+10+getFont(Ncontinues,'y')+getFont(Ncontinues,'y'):
            win.blit(kursour,(widch-getFont(new_game,'x')-50-10-getFont(kursour,'x'),360+10+getFont(Ncontinues,'y')))
        elif 0 <= mouse[0] <= widch and 360+20+getFont(option,'y')*2 <= mouse[1] <= 360+20+getFont(option,'y')*2+getFont(option,'y'):
            win.blit(kursour,(widch-getFont(option,'x')-50-10-getFont(kursour,'x'), 360+20+getFont(new_game,'y')*2))
        elif 0 <= mouse[0] <= widch and 360+20+getFont(exit_in_game,'y')*3 <= mouse[1] <= 360+20+getFont(exit_in_game,'y')*3+getFont(exit_in_game,'y'):
            win.blit(kursour,(widch-getFont(exit_in_game,'x')-50-10-getFont(kursour,'x'),360+30+getFont(new_game,'y')*3))
        drawTem()

        pg.display.flip()
