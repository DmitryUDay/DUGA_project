from helper import *
def options(win):
    import pygame as pg
    from pygame import mixer as mx
    import sys
    import subprocess
    from helper import langu

    pg.init()
    mx.init()
    widch = win.get_width()
    height = win.get_height()


    headphot = pg.font.SysFont('Arial Black', 25)
    content = pg.font.SysFont('Arial Black', 50)

    text = headphot.render('Изменение экрана приведет к перезарпуску игры', True, (255,255,255))
    formatScreen = headphot.render('Экран',1, (255,255,255))
    language = headphot.render('Язык игры',1, (255,255,255))
    subtitle = headphot.render('Субтитры',1, (255,255,255))
    langSub = headphot.render('Язык субтитров',1, (255,255,255))
    exitToMenu = headphot.render('Выйти',1, (138,129,80))


    drawAlert = 0
    kursour = content.render('>>',1,(138,129,80))

    """Рисует и обрабатывает окно подтверждения"""
    clock = pg.time.Clock()

    # Размеры и позиция окна
    box_width, box_height = getFont(text,'x')+10, 200
    box_x = (widch - box_width) // 2
    box_y = (height - box_height) // 2

    # Кнопки
    btn_width, btn_height = 120, 50
    btn_yes = pg.Rect(box_x + 50, box_y + 120, btn_width, btn_height)
    btn_no = pg.Rect(box_x + box_width - 50 - btn_width, box_y + 120, btn_width, btn_height)
    # Загрузи заранее, один раз (внутри функции options)
    temsTo = [pg.transform.scale(pg.image.load(f'img/temnenie/{i}.png'), (widch, height)) for i in range(1, 11)]
    temsMe = list(reversed(temsTo))  # плавная обратная анимация

    clock = pg.time.Clock()

    def animat(direction):
        POPlanguage = content.render(configur('language','r'),1, (181, 171, 112))
        POPlangSub = content.render(configur('subLang','r'),1, (181, 171, 112))

        configSub = configur('subtitle','r')
        if configSub == 'on':
            configSub = 'Включены'
        else:
            configSub = 'Выключены'
        POPsubtitle = content.render(configSub,1, (181, 171, 112))
        POPformatScreen = content.render(configur('display','r'),1, (181, 171, 112))
        """
        direction: 'temTO' — затемнение
                'temME' — осветление
        """
        frames = temsTo if direction == 'temTO' else temsMe

        for frame in frames:
            drawContent(POPlanguage, POPlangSub, POPsubtitle, POPformatScreen)         # Рисуем всё что на экране (текст, кнопки и т.п.)
            win.blit(frame, (0, 0))  # Накладываем затемняющий кадр
            pg.display.flip()
            clock.tick(24)           # Ограничение FPS для плавности


    def drawContent(POPlanguage, POPlangSub, POPsubtitle, POPformatScreen):
        win.fill((0,0,0))

        win.blit(language, (200,100))
        win.blit(POPlanguage, (200 + machetta(getFont(language,'x'), getFont(POPlanguage,'x')), 100 + 20 + getFont(language,'y')))
        win.blit(langSub, (widch - getFont(langSub,'x') - 200, 100))
        win.blit(POPlangSub, (widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x')), 100 + 20 + getFont(langSub,'y')))
        win.blit(subtitle, (200, 500))
        win.blit(POPsubtitle, (200 + machetta(getFont(subtitle,'x'), getFont(POPsubtitle,'x')), 500 + 20 + getFont(subtitle,'y')))
        win.blit(formatScreen, (widch - getFont(formatScreen,'x') - 200, 500))
        win.blit(POPformatScreen, (widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x')), 500 + 20 + getFont(formatScreen,'y')))
        win.blit(exitToMenu, (widch - getFont(exitToMenu, 'x') - 50, height - getFont(exitToMenu, 'y') - 50))



    def configur(pos,tip):
        if pos == 'display':
            patch = 'data_user\display.txt'
        elif pos == 'language':
            patch = 'data_user\language.txt'
        elif pos == 'subtitle':
            patch = 'data_user\subtitle.txt'
        elif pos == 'subLang':
            patch = 'data_user\subtitleLang.txt'
        
        if tip == 'r':
            lambada = open(patch, 'r', encoding='utf8')
            lambdaReturn = lambada.read()
            lambada.close()
            return lambdaReturn
        else:
            lambada = open(patch, 'w')
            lambada.write(str(tip))
            lambada.close()


    def machetta(fontParrent,fontChild):

        mch1 = fontParrent-fontChild
        mch2 = mch1//2
        return mch2


    screenPos = configur('display','r')
    animat('intoo')
    while True:
        mouse = pg.mouse.get_pos()
        POPlanguage = content.render(configur('language','r'),1, (181, 171, 112))
        POPlangSub = content.render(configur('subLang','r'),1, (181, 171, 112))

        configSub = configur('subtitle','r')
        if configSub == 'on':
            configSub = 'Включены'
        else:
            configSub = 'Выключены'
        POPsubtitle = content.render(configSub,1, (181, 171, 112))
        POPformatScreen = content.render(configur('display','r'),1, (181, 171, 112))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            elif event.type == pg.MOUSEBUTTONDOWN:
                if drawAlert == 1:
                    if btn_yes.collidepoint(event.pos):
                        # Запускаем новый процесс
                        subprocess.Popen([sys.executable, "controll.py"])
                        exit()
                    elif btn_no.collidepoint(event.pos):
                        if configur('display', 'r') == 'Full screen':
                            configur('display', 'auto')
                        else:
                            configur('display', 'Full screen')
                        drawAlert = 0

                else:
                    if widch-getFont(exitToMenu, 'x')-50 <= mouse[0] <= widch-getFont(exitToMenu, 'x')-50+getFont(exitToMenu,'x') and height-getFont(exitToMenu, 'y')-50 <= mouse[1] <= height-getFont(exitToMenu, 'y')-50+getFont(exitToMenu,'y'):
                        if configur('display','r') != screenPos:
                            drawAlert = 1
                        else:
                            animat('temTO')
                            return 'menu'
                    elif 200+machetta(getFont(language,'x'),getFont(POPlanguage,'x')) <= mouse[0] <= 200+machetta(getFont(language,'x'),getFont(POPlanguage,'x'))+getFont(POPlanguage,'x') and 100+20+getFont(language,'y') <= mouse[1] <= 100+20+getFont(language,'y')+getFont(POPlanguage,'y'):
                        if configur('language', 'r') == 'RU':
                            configur('language', 'EN')
                        else:
                            configur('language', 'RU')


                    elif 200+machetta(getFont(subtitle,'x'),getFont(POPsubtitle,'x')) <= mouse[0] <= 200+machetta(getFont(subtitle,'x'),getFont(POPsubtitle,'x'))+getFont(POPsubtitle,'x') and 500+20+getFont(subtitle,'y') <= mouse[1] <= 500+20+getFont(subtitle,'y')+getFont(POPsubtitle,'y'):
                        if configur('subtitle', 'r') == 'on':
                            configur('subtitle', 'off')
                        else:
                            configur('subtitle', 'on')

                    elif widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x')) <= mouse[0] <= widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x')) + getFont(POPformatScreen,'x') and 500 + 20 + getFont(formatScreen,'y') <= mouse[1] <= 500 + 20 + getFont(formatScreen,'y') + getFont(POPformatScreen,'y'):
                        if configur('display', 'r') == 'Full screen':
                            configur('display', 'auto')
                        else:
                            configur('display', 'Full screen')

                    elif widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x')) <= mouse[0] <= widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x')) + getFont(POPlangSub,'x') and 100 + 20 + getFont(langSub,'y') <= mouse[1] <= 100 + 20 + getFont(langSub,'y') + getFont(POPlangSub,'y'):
                        if configur('subLang', 'r') == 'RU':
                            configur('subLang', 'EN')
                        else:
                            configur('subLang', 'RU')
                
                


        win.fill((0,0,0))
        
        drawContent(POPlanguage, POPlangSub, POPsubtitle, POPformatScreen)

        if 200+machetta(getFont(language,'x'),getFont(POPlanguage,'x')) <= mouse[0] <= 200+machetta(getFont(language,'x'),getFont(POPlanguage,'x'))+getFont(POPlanguage,'x') and 100+20+getFont(language,'y') <= mouse[1] <= 100+20+getFont(language,'y')+getFont(POPlanguage,'y'):
            win.blit(kursour,(200+machetta(getFont(language,'x'),getFont(POPlanguage,'x'))-10-getFont(kursour,'x'),100+20+getFont(language,'y')))


        elif 200+machetta(getFont(subtitle,'x'),getFont(POPsubtitle,'x')) <= mouse[0] <= 200+machetta(getFont(subtitle,'x'),getFont(POPsubtitle,'x'))+getFont(POPsubtitle,'x') and 500+20+getFont(subtitle,'y') <= mouse[1] <= 500+20+getFont(subtitle,'y')+getFont(POPsubtitle,'y'):
            win.blit(kursour,(200+machetta(getFont(subtitle,'x'),getFont(POPsubtitle,'x'))-10-getFont(kursour,'x'),500+20+getFont(subtitle,'y')))

        elif widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x')) <= mouse[0] <= widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x')) + getFont(POPformatScreen,'x') and 500 + 20 + getFont(formatScreen,'y') <= mouse[1] <= 500 + 20 + getFont(formatScreen,'y') + getFont(POPformatScreen,'y'):
            win.blit(kursour,(widch - getFont(formatScreen,'x') - 200 + machetta(getFont(formatScreen,'x'), getFont(POPformatScreen,'x'))-10-getFont(kursour,'x'),500 + 20 + getFont(formatScreen,'y')))

        elif widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x')) <= mouse[0] <= widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x')) + getFont(POPlangSub,'x') and 100 + 20 + getFont(langSub,'y') <= mouse[1] <= 100 + 20 + getFont(langSub,'y') + getFont(POPlangSub,'y'):
            win.blit(kursour,(widch - getFont(langSub,'x') - 200 + machetta(getFont(langSub,'x'), getFont(POPlangSub,'x'))-10-getFont(kursour,'x'), 100 + 20 + getFont(langSub,'y')))







        if drawAlert == 1:
            # Полупрозрачный фон
            overlay = pg.Surface((widch, height))
            overlay.set_alpha(150)
            overlay.fill((0,0,0))
            win.blit(overlay, (0, 0))

            # Рисуем окошко
            pg.draw.rect(win, (128,128,128), (box_x, box_y, box_width, box_height), border_radius=10)
            pg.draw.rect(win, (255,255,255), (box_x, box_y, box_width, box_height), 2, border_radius=10)

            # Текст вопроса
            win.blit(text, (box_x + (box_width - text.get_width()) // 2, box_y + 40))

            # Кнопка "Да"
            pg.draw.rect(win, (0,255,0), btn_yes, border_radius=8)
            yes_text = headphot.render("Да", True, (255,255,255))
            win.blit(yes_text, (btn_yes.x + (btn_width - yes_text.get_width()) // 2,
                                    btn_yes.y + (btn_height - yes_text.get_height()) // 2))

            # Кнопка "Нет"
            pg.draw.rect(win, (255,0,0), btn_no, border_radius=8)
            no_text = headphot.render("Нет", True, (255,255,255))
            win.blit(no_text, (btn_no.x + (btn_width - no_text.get_width()) // 2,
                                btn_no.y + (btn_height - no_text.get_height()) // 2))

            pg.display.flip()
            clock.tick(60)

        pg.display.flip()