from helper import getFont  # можно оставить, если используешь где-то ещё
import pygame as pg
import sys
from img.imageImportGame import *

def game_over_init(win):
    pg.init()

    widch, height = win.get_width(), win.get_height()
    pg.display.set_caption("Анимация аниматроника")

    # Загрузка аниматроника
    aniName = 'None'
    lambdaS = open('data_user/animKill.txt', 'r')
    animatronik_name = lambdaS.read()
    if animatronik_name == 'Rudi':
        aniImg = pg.image.load('img/menu/Rudolphu.PNG').convert_alpha()
        aniName = 'Рудольфом'
    elif animatronik_name == 'Billy':
        aniImg = pg.image.load('img/menu/Billy_bob.png').convert_alpha()
        aniName = 'Билли Бобом'
    else:
        aniImg = pg.Surface((512, 768), pg.SRCALPHA)

    # Начальные и конечные размеры/позиции
    start_w, start_h = 1024, 1536
    end_w, end_h = 512, 768
    start_x = widch // 2 - start_w // 2
    start_y = height // 2 - start_h // 2
    end_x = widch - 600
    end_y = height // 2 - end_h // 2

    clock = pg.time.Clock()
    steps = 50

    # Анимация уменьшения и смещения аниматроника
    ctc = [stm1,stm2,stm3,stm4,stm5,stm6,stm7,stm8]
    pshh.play()
    for i in range(0,15):
        for cadr in ctc:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            win.fill((0,0,0))
            win.blit(cadr, (0,0))
            pg.display.flip()
            clock.tick(60)
    pshh.stop()

    stat.play(-1)
    ani_scaled = None
    for step in range(steps + 10):
        frac = step / steps
        w = max(1, int(start_w + (end_w - start_w) * frac))
        h = max(1, int(start_h + (end_h - start_h) * frac))
        x = int(start_x + (end_x - start_x) * frac)
        y = int(start_y + (end_y - start_y) * frac)

        ani_scaled = pg.transform.smoothscale(aniImg, (w, h))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        win.fill((0, 0, 0))
        win.blit(ani_scaled, (x, y))
        pg.display.flip()
        clock.tick(60)

    # Подготовка текста меню
    textMenu = pg.font.SysFont('Arial Black', 50)
    replay_txt = 'Переиграть еще раз'
    menu_txt = 'В меню'
    exit_txt = 'Выйти'

    w_replay, h_replay = textMenu.size(replay_txt)
    w_menu,   h_menu   = textMenu.size(menu_txt)
    w_exit,   h_exit   = textMenu.size(exit_txt)

    # Позиции меню (высотно выровнены относительно пункта menu)
    base_y = height // 2 - h_menu // 2
    replay_y = base_y - h_replay - 10
    menu_y   = base_y
    exit_y   = base_y + h_replay + 10

    # Анимация подъезда текста слева -> до target_i
    i = -w_replay  # начинаем слева за экраном
    target_i = 50
    slide_speed = 10
    while i < target_i:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        i += slide_speed
        if i > target_i:
            i = target_i

        win.fill((0, 0, 0))
        win.blit(ani_scaled, (x, y))
        win.blit(textMenu.render(replay_txt, True, (255,255,255)), (i, replay_y))
        win.blit(textMenu.render(menu_txt,   True, (255,255,255)), (i, menu_y))
        win.blit(textMenu.render(exit_txt,   True, (255,255,255)), (i, exit_y))
        pg.display.flip()
        clock.tick(60)

    tems = [pg.transform.scale(pg.image.load(f'img/temnenie/{i}.png'), (widch,height)) for i in range(1, 11)]

    def anim():
        for cadr in tems:
            win.blit(cadr,(0,0))
            pg.display.flip()



    running = True
    text = pg.font.SysFont('Arial Black',20)
    nameBot = text.render(f'Вы не уследили за {aniName}',1,(255,255,255))
    while running:
        mouse = pg.mouse.get_pos()
        clicked = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

        # хитбоксы
        replay_rect = pg.Rect(i, replay_y, w_replay, h_replay)
        menu_rect   = pg.Rect(i, menu_y,   w_menu,   h_menu)
        exit_rect   = pg.Rect(i, exit_y,   w_exit,   h_exit)

        # цвета по умолчанию
        color_replay = (255, 255, 255)
        color_menu   = (255, 255, 255)
        color_exit   = (255, 255, 255)

        # проверка наведения + клик
        if replay_rect.collidepoint(mouse):
            color_replay = (138, 129, 80)
            if clicked:
                anim()
                stat.stop()
                return 'game'
        elif menu_rect.collidepoint(mouse):
            color_menu = (138, 129, 80)
            if clicked:
                anim()
                stat.stop()
                return 'menu'
        elif exit_rect.collidepoint(mouse):
            color_exit = (138, 129, 80)
            if clicked:
                return None

        # отрисовка кадра
        win.fill((0, 0, 0))
        win.blit(ani_scaled, (x, y))
        win.blit(textMenu.render(replay_txt, True, color_replay), replay_rect.topleft)
        win.blit(textMenu.render(menu_txt,   True, color_menu),   menu_rect.topleft)
        win.blit(textMenu.render(exit_txt,   True, color_exit),   exit_rect.topleft)
        nameBot_x = x + ani_scaled.get_width() // 2 - nameBot.get_width() // 2
        nameBot_y = y + ani_scaled.get_height() + 10  # 10 — отступ вниз
        win.blit(nameBot, (nameBot_x, nameBot_y))

        pg.display.flip()
        clock.tick(60)
