import sys, os, pygame as pg
from pygame import mixer as mx
from helper import ScreenFader, getFont
import threading
from time import sleep
from random import randint

running = True

def initSys(win):
    global running

    def hmh():
        global running
        os.system('cls')
        print("\n  *****          **    **         *****            **     ")
        print("  **    **       **    **       **     **           ****    ")
        print("  **    **       **    **       **                 **  **   ")
        print("  **    **       **    **       **                 **  **   ")
        print("  **    **       **    **       **  ****         ********** ")
        print("  **    **       **    **       **     **        **      ** ")
        print("  *****            ****           ******         **      **  UDay©\n")
        print("Это окно предназначенно для вывода данных. Если игра зависнет, закройте его.")

        widch, height = win.get_size()
        pg.init()
        mx.init()
        clock = pg.time.Clock()
        fader = ScreenFader(win)

        copyrut = pg.font.SysFont(None, 30).render('UDay©', True, (250,250,250))
        dra = pg.font.SysFont(None, 80)
        lagMachine = pg.transform.scale(pg.image.load('img/start/gluck.png'), (widch, height))
        logotype = pg.transform.scale(pg.image.load('img/start/logo_game.png'), (500,500))

        # --- Загрузка и анимация текста ---
        win.fill((0,0,0))
        win.blit(copyrut, (widch-getFont(copyrut,'x')-10, height-getFont(copyrut,'y')-10))
        pg.display.flip()

        text = "Загрузка конфигурации архива Дуга"
        pustota = ""
        one = mx.Sound('sound/menu/1.mp3')
        two = mx.Sound('sound/menu/2.mp3')
        three = mx.Sound('sound/menu/3.mp3')
        fore = mx.Sound('sound/menu/4.mp3')

        for simbool in text:
            rnd = randint(1,4)
            if rnd == 1: one.play()
            elif rnd == 2: two.play()
            elif rnd == 3: three.play()
            else: fore.play()

            pustota += simbool
            lilo = dra.render(pustota, True, (250,250,250))
            win.fill((0,0,0))
            win.blit(lilo, (widch//2-getFont(lilo,'x')//2, height//2-getFont(lilo,'y')//2))
            win.blit(copyrut, (widch-getFont(copyrut,'x')-10, height-getFont(copyrut,'y')-10))
            pg.display.flip()
            clock.tick(15)
        sleep(2)

        # --- Фоновые мерцания ---
        mx.music.load('sound/menu/meha.mp3')
        mx.music.play()
        for _ in range(50):
            win.blit(lagMachine, (randint(0,widch), randint(0,100)))
            win.blit(copyrut, (widch-getFont(copyrut,'x')-10, height-getFont(copyrut,'y')-10))
            pg.display.flip()
            clock.tick(24)
        mx.music.stop()

        # --- Фейдер + логотип ---
        fader.start("out", speed=2, block=True, clock=clock)

        mx.music.load('sound/menu/whu.mp3')
        mx.music.play()

        # Фейд "in" (из черного) — плавно через цикл
        fader.start("in", speed=10)  # активируем фейд
        while fader.is_active():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit(1)
            # Сначала рисуем логотип
            win.fill((0,0,0))  # если нужно, можно убрать, чтобы фон был логотип
            win.blit(logotype, (widch//2-250, height//2-250))

            # Затем накладываем фейдер
            fader.update()
            win.blit(copyrut, (widch-getFont(copyrut,'x')-10, height-getFont(copyrut,'y')-10))

            pg.display.flip()
            clock.tick(60)

        sleep(2)

        # Фейд "out" (в черный) — блокирующий
        fader.start("out", speed=2, block=True, clock=clock)

        running = False
        # --- Ждём закрытия ---

    threading.Thread(target=hmh, daemon=True).start()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(1)
        if running == False:
            return 'goWarning'
