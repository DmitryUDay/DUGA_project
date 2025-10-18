import pygame as pg
import math
from helper import *
pg.init()

font = pg.font.SysFont("arial", 30)


def loadingScene(win):
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
    return 'game'




def home(win):
    widch, height = win.get_width(), win.get_height()
    clock = pg.time.Clock()

    # ===== Заранее грузим фон =====
    fone = formGet('orig', height)
    fone_width = fone.get_width()

    # ===== Параметры игрока =====
    player_x = 300
    player_y = height - 600
    player_speed = 400

    # ===== Загрузка анимаций один раз =====
    size = (350, 600)#250
    idle_frames = load_animation([
        'img/cutGame/animation/playerIDLE1.png',
        'img/cutGame/animation/playerIDLE2.png'
    ], size)

    walk_frames_right = load_animation([
        'img/cutGame/animation/goRight1.png',
        'img/cutGame/animation/goRight2.png'
    ], size)

    walk_frames_left = [pg.transform.flip(f, True, False) for f in walk_frames_right]

    current_frames = idle_frames
    frame_index = 0
    frame_time = 0
    frame_duration = .4

    # ===== Камера =====
    camera_x = fone_width - widch
    camera_speed = player_speed

    # ===== Переменные состояния =====
    driver = 'sleep'
    aprove = True
    havka = 'не взял'
    dialog = 'none'
    cicle = True

    while cicle:
        dt = clock.tick(60) / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYUP:
                if event.key == pg.K_e:
                    if aprove:
                        aprove = False
                        if driver == 'goExoo':
                            if havka == 'взял':
                                cicle = False
                                return loadingScene(win)
                        driver = ''
                                
                    else:
                        aprove = True
                        if dialog == 'tv':
                            driver = 'tvDialog'
                        elif dialog == 'bedToSleep':
                            driver = 'todoSleep'
                        elif dialog == 'getFood':
                            driver = 'todoFood'
                            havka = 'взял'
                            fone = formGet('fodd', height)
                        elif dialog == 'windows':
                            driver = 'goWindows'
                        elif dialog == 'exoo':
                            driver = 'goExoo'
                            





        keys = pg.key.get_pressed()
        moving = False

        if not aprove:
            if keys[pg.K_LEFT]:
                moving = True
                current_frames = walk_frames_left
                if player_x > widch * 0.3:
                    player_x -= player_speed * dt
                else:
                    camera_x = max(0, camera_x - camera_speed * dt)
            elif keys[pg.K_RIGHT]:
                moving = True
                current_frames = walk_frames_right
                if player_x < widch * 0.7:
                    player_x += player_speed * dt
                else:
                    camera_x = min(fone_width - widch, camera_x + camera_speed * dt)

        if not moving:
            current_frames = idle_frames

        # ===== Обновление кадра =====
        frame_time += dt
        if frame_time >= frame_duration:
            frame_time = 0
            frame_index = (frame_index + 1) % len(current_frames)

        # ===== Рендер =====
        win.blit(fone, (0, 0), (int(camera_x), 0, widch, height))
        win.blit(current_frames[frame_index], (player_x, player_y))

        world_x = player_x + camera_x
        dialog = 'none'

        if not aprove:
            if 1113 <= world_x <= 1666:
                dialog = 'tv'
                blitTask(win, 'Телевизор', player_x, player_y)
            elif 2507 <= world_x <= 3156:
                dialog = 'bedToSleep'
                blitTask(win, 'Поспать', player_x, player_y)
            elif 2051 <= world_x <= 2418:
                dialog = 'windows'
                blitTask(win, 'окно', player_x, player_y)
            elif 1930 <= world_x <= 2171 and havka == 'не взял':
                dialog = 'getFood'
                blitTask(win, 'Взять перекус', player_x, player_y)
            elif 454 <= world_x <= 735:
                dialog = 'exoo'
                blitTask(win, 'Выйти', player_x, player_y)

        if aprove:
            if driver == 'sleep':
                draw_text_rect(win, 'новое утро - новый день!', font, (255, 255, 255), widch, height)
            elif driver == 'tvDialog':
                draw_text_rect(win, 'Этот телевизор мне отдал мой начальник. Вечно шипит. А ведь я его вчера чинил...', font, (255, 255, 255), widch, height)
            elif driver == 'todoSleep':
                draw_text_rect(win, 'Прекрасно бы выспаться, но боюсь начальник этого не одобрит', font, (255, 255, 255), widch, height)
            elif driver == 'todoFood':
                draw_text_rect(win, 'Всё взял, теперь можно идти на работу.', font, (255, 255, 255), widch, height)
            elif driver == 'goWindows':
                draw_text_rect(win, 'опять этот туман... Уже третий день как молоко. Ни фонарей, ни людей...', font, (255, 255, 255), widch, height)
            elif driver == 'goExoo':
                if havka == 'взял':
                    draw_text_rect(win, 'Еще одну ночь. Может, в этот раз я просто поработаю и уйду без приключений!?', font, (255, 255, 255), widch, height)
                else:
                    draw_text_rect(win, 'Я не успел позавтракать. Возьму с собой термос и бутерброд.', font, (255, 255, 255), widch, height)

        pg.display.flip()


# def home(win):
#     widch, height = win.get_width(), win.get_height()
#     clock = pg.time.Clock()

#     # ===== Заранее грузим фон =====
#     fone = formGet('orig', height)
#     fone_width = fone.get_width()

#     # ===== Параметры игрока =====
#     player_x = 300
#     player_y = height - 600
#     player_speed = 400

#     # ===== Загрузка анимаций один раз =====
#     size = (350, 600)#250
#     idle_frames = load_animation([
#         'img/cutGame/animation/playerIDLE1.png',
#         'img/cutGame/animation/playerIDLE2.png'
#     ], size)

#     walk_frames_right = load_animation([
#         'img/cutGame/animation/goRight1.png',
#         'img/cutGame/animation/goRight2.png'
#     ], size)

#     walk_frames_left = [pg.transform.flip(f, True, False) for f in walk_frames_right]

#     current_frames = idle_frames
#     frame_index = 0
#     frame_time = 0
#     frame_duration = .4

#     # ===== Камера =====
#     camera_x = fone_width - widch
#     camera_speed = player_speed

#     # ===== Переменные состояния =====
#     driver = 'sleep'
#     aprove = True
#     havka = 'не взял'
#     dialog = 'none'
#     cicle = True

#     while cicle:
#         dt = clock.tick(60) / 1000

#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 return
#             if event.type == pg.KEYUP:
#                 if event.key == pg.K_e:
#                     if aprove:
#                         aprove = False
#                         if driver == 'goExoo':
#                             if havka == 'взял':
#                                 cicle = False
#                                 loadingScene(win)
#                         driver = ''
                                
#                     else:
#                         aprove = True
#                         if dialog == 'tv':
#                             driver = 'tvDialog'
#                         elif dialog == 'bedToSleep':
#                             driver = 'todoSleep'
#                         elif dialog == 'getFood':
#                             driver = 'todoFood'
#                             havka = 'взял'
#                             fone = formGet('fodd', height)
#                         elif dialog == 'windows':
#                             driver = 'goWindows'
#                         elif dialog == 'exoo':
#                             driver = 'goExoo'
                            





#         keys = pg.key.get_pressed()
#         moving = False

#         if not aprove:
#             if keys[pg.K_LEFT]:
#                 moving = True
#                 current_frames = walk_frames_left
#                 if player_x > widch * 0.3:
#                     player_x -= player_speed * dt
#                 else:
#                     camera_x = max(0, camera_x - camera_speed * dt)
#             elif keys[pg.K_RIGHT]:
#                 moving = True
#                 current_frames = walk_frames_right
#                 if player_x < widch * 0.7:
#                     player_x += player_speed * dt
#                 else:
#                     camera_x = min(fone_width - widch, camera_x + camera_speed * dt)

#         if not moving:
#             current_frames = idle_frames

#         # ===== Обновление кадра =====
#         frame_time += dt
#         if frame_time >= frame_duration:
#             frame_time = 0
#             frame_index = (frame_index + 1) % len(current_frames)

#         # ===== Рендер =====
#         win.blit(fone, (0, 0), (int(camera_x), 0, widch, height))
#         win.blit(current_frames[frame_index], (player_x, player_y))

#         world_x = player_x + camera_x
#         dialog = 'none'

#         if not aprove:
#             if 1113 <= world_x <= 1666:
#                 dialog = 'tv'
#                 blitTask(win, 'Телевизор', player_x, player_y)
#             elif 2507 <= world_x <= 3156:
#                 dialog = 'bedToSleep'
#                 blitTask(win, 'Поспать', player_x, player_y)
#             elif 2051 <= world_x <= 2418:
#                 dialog = 'windows'
#                 blitTask(win, 'окно', player_x, player_y)
#             elif 1930 <= world_x <= 2171 and havka == 'не взял':
#                 dialog = 'getFood'
#                 blitTask(win, 'Взять перекус', player_x, player_y)
#             elif 454 <= world_x <= 735:
#                 dialog = 'exoo'
#                 blitTask(win, 'Выйти', player_x, player_y)

#         if aprove:
#             if driver == 'sleep':
#                 draw_text_rect(win, 'новое утро - новый день!', font, (255, 255, 255), widch, height)
#             elif driver == 'tvDialog':
#                 draw_text_rect(win, 'Этот телевизор мне отдал мой начальник. Вечно шипит. А ведь я его вчера чинил...', font, (255, 255, 255), widch, height)
#             elif driver == 'todoSleep':
#                 draw_text_rect(win, 'Прекрасно бы выспаться, но боюсь начальник этого не одобрит', font, (255, 255, 255), widch, height)
#             elif driver == 'todoFood':
#                 draw_text_rect(win, 'Всё взял, теперь можно идти на работу.', font, (255, 255, 255), widch, height)
#             elif driver == 'goWindows':
#                 draw_text_rect(win, 'опять этот туман... Уже третий день как молоко. Ни фонарей, ни людей...', font, (255, 255, 255), widch, height)
#             elif driver == 'goExoo':
#                 if havka == 'взял':
#                     draw_text_rect(win, 'Еще одну ночь. Может, в этот раз я просто поработаю и уйду без приключений!?', font, (255, 255, 255), widch, height)
#                 else:
#                     draw_text_rect(win, 'Я не успел позавтракать. Возьму с собой термос и бутерброд.', font, (255, 255, 255), widch, height)

#         pg.display.flip()
