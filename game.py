from img.imageImportGame import *  # твой импорт ассетов как был
import pygame as pg
from pygame import mixer
from time import sleep, time
from random import randint
from helper import *
import threading


# Глобальные состояния (инициализируемые в gamee)
pos = 'office'
flash = False
positionBillRoom = 'не активен'
positionRudiRoom = 'не активен'




nightLam = open('data_user/nightUser.txt','r')
night = int(nightLam.read())
nightLam.close()

# AI-параметры (не менял)
cicleBear = True
roomBilly = 1
pointBilly = 0
cicleCroco = True
roomRudolphu = 1
pointRudolphu = 0

dopCicle = True
cicleAlertB = False
cicleAlertR = False
fone_event = 0
tema = 1


# Контроль потоков/сцен
cicleGamee = True
cicleGameTime = True
kill_flag = None  # будет 'setKillScene' или 'menu' или 'win'

# Пара флагов для синхронизации с главным потоком
pending_scare = None        # None / 'Billy' / 'Rudolphu' — выставляют потоки
pending_transition = False  # если True — главный цикл вызовет animat(win)

# Частота игрового цикла
GAME_FPS = 60
FLASHLIGHT_RADIUS = 250

# --------------------------
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (из твоей версии)
# --------------------------

def stopGamee(tip):
    """Остановить игровые процессы и выставить kill_flag. Вызывается из главного потока или потоков."""
    global cicleGamee, cicleBear, dopCicle, cicleAlertB, cicleCroco, cicleAlertR, cicleGameTime, kill_flag
    cicleBear = False
    cicleCroco = False
    dopCicle = False
    cicleAlertB = False
    cicleAlertR = False
    cicleGameTime = False
    try:
        foneGOOL.stop()
    except Exception:
        pass
    pg.mouse.set_visible(True)
    if tip == 'win':
        kill_flag = 'win'
    elif tip == 'kill':
        kill_flag = 'setKillScene'
    elif tip == 'menuGO':
        kill_flag = 'menu'

# --------------------------
# АНИМАЦИОННЫЕ ФУНКЦИИ (как в твоём коде)
# --------------------------

def create_flashlight_mask(radius):
    mask = pg.Surface((radius*2, radius*2), pg.SRCALPHA)
    for r in range(radius, 0, -1):
        alpha = int(255 * (1 - r / radius))  # мягкий градиент
        pg.draw.circle(mask, (0, 0, 0, alpha), (radius, radius), r)
    return mask

flashlight_mask = create_flashlight_mask(FLASHLIGHT_RADIUS)

def animat(win):
    """Короткая анимация бега/перемещения — пример. Блокирует главный цикл пока идёт."""
    if pos == 'office':
        seats.play()
    else:
        runTO.play()

    # statik = [stm1l, stm2l, stm3l, stm4l, stm5l, stm6l, stm7l, stm8l]
    statik = [stm8l, stm7l, stm6l, stm5l, stm4l, stm3l, stm2l, stm1l]
    clock = pg.time.Clock()
    for _ in range(2):
        for imgPos in statik:
            win.blit(imgPos, (0, 0))
            pg.display.flip()
            clock.tick()

def jumScare(monster, win):
    """Джампскэр — как у тебя, блокирующая отрисовка (выполняется в главном потоке)."""
    try:
        jumper.play()
    except Exception:
        pass
    clock = pg.time.Clock()

    if monster == 'Billy':
        try:
            sX = open('data_user/animKill.txt', 'w')
            sX.write('Billy')
            sX.close()
        except Exception:
            pass
        frames = [globals().get(n) for n in ('one','two','three','fore','five','six','seven','eight','nine','ten','eleven','twelve','freetin')]
        frames = [f for f in frames if f is not None]
        for frame in frames:
            win.blit(fone_event,(0,0))
            win.blit(frame, (0,0))
            pg.display.flip()
            clock.tick(10)
    elif monster == 'Rudolphu':
        try:
            sX = open('data_user/animKill.txt', 'w')
            sX.write('Rudi')
            sX.close()
        except Exception:
            pass
        frames = [globals().get(n) for n in ('oneR','twoR','threeR','foreR','fiveR','sixR','sevenR','eightR','nineR','tenR','elevenR','twelveR')]
        frames = [f for f in frames if f is not None]
        for frame in frames:
            win.blit(fone_event,(0,0))
            win.blit(frame, (0,0))
            pg.display.flip()
            clock.tick(24)

    try:
        jumper.stop()
    except Exception:
        pass
    return 'setKillScene'

# --------------------------
# AI-потоки (не менял)
# --------------------------

def AIBear_thread():
    global positionBillRoom, roomBilly, pointBilly, cicleBear, cicleAlertB, dopCicle, night, pending_scare
    while dopCicle:
        sleeper = randint(1, 3) if night in (1,2) else randint(1,2)
        while cicleBear and dopCicle:
            if pointBilly >= 5:
                pointBilly = 0
                roomBilly += 1

            if roomBilly >= 8:
                positionBillRoom = 'активен'
                cicleBear = False
                cicleAlertB = True
                try:
                    BillCnock.play()
                except Exception:
                    pass
                threading.Thread(target=timerAwaitBill, daemon=True).start()
                break
            pointBilly += 1
            sleep(sleeper)

def AICroco_thread():
    global positionRudiRoom, roomRudolphu, pointRudolphu, cicleCroco, cicleAlertR, dopCicle, night, pos, pending_scare
    while dopCicle:
        sleeper = randint(1, 3) if night in (1,2) else randint(1,2)
        while cicleCroco and dopCicle:
            if pointRudolphu >= 5:
                pointRudolphu = 0
                roomRudolphu += 1

            if roomRudolphu >= 8:
                positionRudiRoom = 'активен'
                cicleCroco = False
                cicleAlertR = True
                try:
                    if pos == 'office':
                        ARL.play()
                    elif pos == 'holl' or pos == 'roomBill':
                        ARC.play()
                    elif pos == 'kitchen' or pos == 'roomBill':
                        ARR.play()
                except Exception:
                    pass
                threading.Thread(target=timerAwaitRudi, daemon=True).start()
                break
            pointRudolphu += 1
            sleep(sleeper)

def timerAwaitBill():
    global cicleAlertB, night, pending_scare
    counter = 0
    limit = 8 if night in (1,2) else 5
    while cicleAlertB and counter < limit:
        sleep(1)
        counter += 1
    if cicleAlertB:
        pending_scare = 'Billy'

def timerAwaitRudi():
    global cicleAlertR, night, pending_scare
    counter = 0
    if night == 1 or night == 2:
        limit = 8
    else:
        limit = 5
    while cicleAlertR and counter < limit:
        sleep(1)
        counter += 1
    if cicleAlertR:
        pending_scare = 'Rudolphu'

# --------------------------
# fnafOS (встроенные переменные и функции)
# --------------------------
# Я использую твой код почти без изменений, но переношу цикл в переменные,
# которые будут обновляться в основном цикле gamee() когда os_open == True.

# UI constants (взяты из твоего файла)
WHITE = (158, 158, 158)
GRAY = (50, 50, 50)
DARK_GRAY = (30, 30, 30)
DARK_GRAY = (30, 30, 30)
BLUE = (0, 120, 215)
BLACK = (0, 0, 0)
MONI = (0, 255, 85)

# tasks_structure — можно вставить сюда, но ты уже определял аналогичный выше.
# Если хочешь, можно поддерживать единый tasks_structure — я оставил тот, который у тебя был в fnafOS.

def randi():
    if night == 1 or night == 2:
        rnd = randint(3,7)
    else:
        rnd = randint(7,9)
    return rnd




TAB_TASKS = "Задачи"
TAB_SENSOR = "Датчик движения"

def draw_tabs(surface, tabs, active_tab, pos_xy=(0,0), size=(800, 40)):
    # size[0] по факту будет widch, но мы используем переданное
    tab_width = size[0] // len(tabs)
    for i, tab in enumerate(tabs):
        rect = pg.Rect(pos_xy[0] + i * tab_width, pos_xy[1], tab_width, size[1])
        color = BLUE if tab == active_tab else DARK_GRAY
        pg.draw.rect(surface, color, rect, 3)
        txt_surf = pg.font.SysFont("Arial Black", 16).render(tab, True, WHITE)
        txt_rect = txt_surf.get_rect(center=rect.center)
        surface.blit(txt_surf, txt_rect)

def all_tasks_done(tasks_struct):
    for main_task in tasks_struct.values():
        for subtask in main_task["Подзадачи"]:
            if not subtask["done"]:
                return False
    return True

def gamee(win):
    from helper import getFont
    import time
    from helper import buttonDraw,textus,power_button,langu
    global pos, flash, positionBillRoom, positionRudiRoom, night
    global cicleBear, roomBilly, pointBilly, dopCicle, cicleAlertB
    global cicleCroco, roomRudolphu, pointRudolphu, cicleAlertR
    global cicleGamee, cicleGameTime, kill_flag
    global pending_scare, pending_transition, fone_event,tema

    pg.init()
    try:
        mixer.init()
    except Exception:
        pass

    # Инициализация значений
    pos = 'office'
    flash = False
    positionBillRoom = 'не активен'
    positionRudiRoom = 'не активен'
    nightLam = open('data_user/nightUser.txt','r')
    night = int(nightLam.read())
    nightLam.close()
    cicleBear = True
    roomBilly = 1
    pointBilly = 0
    cicleCroco = True
    roomRudolphu = 1
    pointRudolphu = 0
    dopCicle = True
    cicleAlertB = False
    cicleAlertR = False
    cicleGamee = True
    cicleGameTime = True
    kill_flag = None

    # fnafOS встроенные состояния (переменные режима монитора)
    os_open = False
    # vars from iniMoni()
    widch = win.get_width()
    height = win.get_height()
    fnaf_font = pg.font.SysFont("Arial Black", 16)
    loadFont = pg.font.SysFont("Arial Black", 20)
    fnaf_small_font = pg.font.SysFont("Arial Black", 16)

    active_tab = TAB_TASKS
    showing_subtasks_for = None
    loading_subtask = None
    loading_start_time = None
    scanning_active = False
    scan_start_time = None
    scan_duration = 5
    scan_finished = False
    message_show_start = None
    toch = '.'
    pointDraw = 0
    elePosDraw = 1
    point = 0
    popa = 1
    pointPopa = 0
    moniTor = False
    tema = 1




    text = pg.font.SysFont('Arial Black', 30)
    clock = pg.time.Clock()
    tasks_structure = {
        "Заказать поставки": {
            "Подзадачи": [
                {"name": "Проверка поставок аккумуляторов", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3' },   # , 'sound': ''
                {"name": "Заказ новых проводов", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Сверка счетов по электроэнергии", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Обработка возврата товара", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Отчёт по зарплатам сотрудников", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Планирование бюджета на следующий месяц", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
            ]
        },
        "Проверка оборудования": {
            "Подзадачи": [
                {"name": "Проверка состояния датчиков движения", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Тестирование камер видеонаблюдения", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Диагностика системы питания", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Калибровка сигнализации", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
            ]
        },
        "Печать документов": {
            "Подзадачи": [
                {"name": "Печать накладной товара", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "Платежная ведомость", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "Зарплата", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "НДС", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "Выписка", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "Платежное поручение", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
                {"name": "Оптимизация работы системы", "done": False, "time": randi(), 'sound': 'sound\game\printPaper.mp3'},
            ]
        },
        "Отчеты": {
            "Подзадачи": [
                {"name": "Ежедневный финансовый отчёт", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Отчёт о расходах на материалы", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Отчёт по времени работы оборудования", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Отчёт о состоянии складских запасов", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Расчитать зарплату", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Итоговый месячный отчёт", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
            ]
        },
        "Инвентаризация остатков": {
            "Подзадачи": [
                {"name": "сравнить учеты", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Обозначить дефицитные позиции", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
                {"name": "Фиксация отчетов", "done": False, "time": randi(), 'sound': 'sound/game/await.mp3'},
            ]
        }
    }
    
    lamtext = text.render(f'Тишина', 1, (250,250,250))
    ###===Инициализация кнопок перемещения и прочей дряни===###
    buttonBack = pg.Rect(widch//2-175, height-100, 350,100)
    buttonLeft = pg.Rect(0, height//2-175,100,350)
    buttonRight = pg.Rect(widch-100, height//2-175,100,350)
    peace = pg.Rect(widch-getFont(lamtext,'x'), height-getFont(lamtext,'x'),getFont(lamtext,'x'),getFont(lamtext,'x'))
    buttonPower = pg.Rect(widch-getFont(lamtext,'x'), height-getFont(lamtext,'x'),getFont(lamtext,'x'),getFont(lamtext,'x'))
    ###===Инициализация кнопок перемещения и прочей дряни===###




    def drawNight():
        nightText = text.render(f'Смена {night}', 1, (250,250,250))
        night_surface = pg.Surface(nightText.get_size(), pg.SRCALPHA)
        night_surface.blit(nightText, (0, 0))
        for alpha in range(255, -1, -5):  # от 255 до 0
            night_surface.set_alpha(alpha)
            win.blit(
                night_surface,
                (widch // 2 - nightText.get_width() // 2,
                height // 2 - nightText.get_height() // 2)
            )
            pg.time.delay(24)  # задержка для плавности




    # Запуск фоновых потоков AI (как у тебя)
    threading.Thread(target=AIBear_thread, daemon=True).start()
    threading.Thread(target=AICroco_thread, daemon=True).start()

    # Установка начального перехода (можно проиграть анимацию входа)
    threading.Thread(target=drawNight, daemon=True).start()
    foneGOOL.play(-1)

    statik = [tem10,tem9,tem8,tem7,tem6,tem5,tem4,tem3,tem2,tem1]
    def drawTem():
        global tema
        if tema != 10:
            ar = tema-1
            win.blit(statik[ar],(0,0))
            tema+=1



    # for cadr in statik:
    #     win.blit(office12, (0,0))
    #     win.blit(cadr,(0,0))
    #     pg.display.flip()
    #     pg.time.Clock().tick(22)

    # Создаём turnButton координаты заранее, чтобы не было NameError
    # (параметры будут пересчитываться при отрисовке офиса)
    turnButton = pg.Rect(0,0,1,1)

    def toDrawLoad(element):
        """|    /   -   \
           
           1    2   3   4
        """


        if element == 1:#|,/,-,\,|,/,-,\,|
            return '|'
        elif element == 2:
            return '/'
        elif element == 3:
            return '-'
        elif element == 4:
            return '\\'
        elif element == 5:
            return '|'
        elif element == 6:
            return '/'
        elif element == 7:
            return '-'
        elif element == 8:
            return '\\'
    osos = False
    while cicleGamee:
        helpertext = text.render('Перемещайтесь стрелками или крестовиной на геймпаде', 1, (250,250,250))

        dt = clock.tick(GAME_FPS) / 1000.0

        key = pg.key.get_pressed()
        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return None

            # Общие клавиши
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    stopGamee('menuGO')
                elif event.key == pg.K_SPACE:
                    if pos == 'roomBill' or pos == 'roomRUdi':
                        try:
                            flashLight.play()
                        except Exception:
                            pass
                        flash = not flash

            # Мышь / переходы (кликаем по офису чтобы открыть монитор)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if os_open:


                    if osos == False:
                        osos = True
                        PCq.play(-1)



                    mx, my = mouse
                    if buttonBack.collidepoint(mouse[0], mouse[1]):
                        os_open = False


                    elif my <= 40:
                        tab_width = widch // 2
                        if mx < tab_width:
                            active_tab = TAB_TASKS
                            showing_subtasks_for = None
                        else:
                            active_tab = TAB_SENSOR

                    elif active_tab == TAB_TASKS:
                        y_start = 100
                        button_height = 50
                        button_margin = 15
                        buttons = []
                        for i, main_task_name in enumerate(tasks_structure.keys()):
                            rect = pg.Rect(100, y_start + i * (button_height + button_margin), 300, button_height)
                            buttons.append((main_task_name, rect))

                        if showing_subtasks_for is None:
                            for main_task_name, rect in buttons:
                                if rect.collidepoint(mx, my):
                                    showing_subtasks_for = main_task_name
                            
                        else:
                            subtasks = tasks_structure[showing_subtasks_for]["Подзадачи"]
                            y_start_sub = 150
                            button_height_sub = 40
                            button_margin_sub = 10
                            for i, subtask in enumerate(subtasks):
                                if subtask["done"]:
                                    continue
                                rect = pg.Rect(150, y_start_sub + i * (button_height_sub + button_margin_sub), 400, button_height_sub)
                                if rect.collidepoint(mx, my):
                                    loading_subtask = subtask
                                    loading_start_time = time.time()
                                    try:
                                        if "sound" in subtask:
                                            s = pg.mixer.Sound(subtask["sound"])
                                            s.play(-1)  # зацикливаем пока выполняется
                                            subtask["_sound_obj"] = s  # сохраним, чтобы потом остановить
                                    except Exception:
                                        pass
                            back_rect = pg.Rect(10, 80, widch - 20, 40)
                            if back_rect.collidepoint(mx, my):
                                showing_subtasks_for = None
                                loading_subtask = False

                    elif active_tab == TAB_SENSOR:
                        onButtons = fnaf_font.render("Начать", True, WHITE)
                        button_x = 100
                        button_y = 80
                        popa = 1
                        try:
                            button_width = getFont(onButtons, 'x') + 20
                            button_height = getFont(onButtons, 'y') + 10
                        except Exception:
                            button_width = 100
                            button_height = 30
                        turnButton_os = pg.Rect(button_x, button_y, button_width, button_height)
                        if turnButton_os.collidepoint(mx, my) and not scanning_active and not scan_finished:
                            scanning_active = True
                            scan_start_time = time.time()
                            scan_finished = False
                            message_show_start = None




                else:
                    if osos == True:
                        PCq.stop()
                        osos = False
                    # Обработка клика по turnButton в офисе (открыть монитор)
                    if pos == 'office':
                        w,h = widch//3+100,height//3+50
                        turnButton = pg.Rect(widch//2-w//2, height//2-h//2-50, w, h)
                        if turnButton.collidepoint(mouse[0], mouse[1]):
                            if moniTor:
                                os_open = True
                            # Скрываем курсор под монитор (можно оставить видимым если хочешь)
                            pg.mouse.set_visible(True)

                    if pos == 'office':
                        if buttonLeft.collidepoint(mouse[0], mouse[1]):
                            pending_transition = True
                            pos = 'holl'
                        elif buttonPower.collidepoint(mouse[0],mouse[1]):
                            if moniTor:
                                moniTor = False
                            else:
                                moniTor = True

                    elif pos == 'holl':
                        if buttonRight.collidepoint(mouse[0], mouse[1]):
                            pending_transition = True
                            pos = 'office'
                        elif 140 <= mouse[0] <= 140+250 and 185 <= mouse[1] <= 185+660:
                            pending_transition = True
                            pos = 'kitchen'
                        elif 500 <= mouse[0] <= 500+250 and 210 <= mouse[1] <= 210+520:
                            pending_transition = True
                            pos = 'roomBill'
                        elif 885 <= mouse[0] <= 885+190 and 418 <= mouse[1] <= 418+407:
                            pending_transition = True
                            pos = 'roomRUdi'

                    elif pos == 'kitchen':
                        if buttonBack.collidepoint(mouse[0], mouse[1]):
                            pending_transition = True
                            pos = 'holl'
                        

                    elif pos == 'roomBill':
                        if buttonBack.collidepoint(mouse[0], mouse[1]):
                            pos = 'holl'
                            pending_transition = True
                        elif peace.collidepoint(mouse[0], mouse[1]):
                            if positionBillRoom == 'активен':
                                peaceBill.play()
                                cicleAlertB = False
                                pointBilly = 0
                                roomBilly = 1
                                positionBillRoom = 'не активен'
                                cicleBear = True
                        else:
                            flashLight.play()
                            flash = not flash

                    elif pos == 'roomRUdi':
                        if buttonBack.collidepoint(mouse[0], mouse[1]):
                            if positionRudiRoom == 'активен' and flash == True:
                                ARL.stop()
                                ARR.stop()
                                ARC.stop()
                                cicleAlertR = False
                                pointRudolphu = 0
                                roomRudolphu = 1
                                positionRudiRoom = 'не активен'
                                cicleCroco = True
                            pending_transition = True
                            pos = 'holl'
                        else:
                            flashLight.play()
                            flash = not flash
            # конец обработки событий

        # -----------------------
        # Отрисовка текущей локации (или fnafOS если os_open)   
        # -----------------------
        if os_open:
            win.fill((1, 16, 38))
            # Рендер монитора — встроенная версия iniMoni.main(), но неблокирующая
            mx, my = pg.mouse.get_pos()
            draw_tabs(win, [TAB_TASKS, TAB_SENSOR], active_tab, pos_xy=(0,0), size=(widch, 40))

            # Логика вкладки задач
            if active_tab == TAB_TASKS:
                scanning_active = False
                if showing_subtasks_for is None:
                    y_start = 100
                    button_height = 50
                    button_margin = 15
                    for i, (main_task_name, task_data) in enumerate(tasks_structure.items()):
                        if all(subtask["done"] for subtask in task_data["Подзадачи"]):
                            continue
                        rect = pg.Rect(100, y_start + i * (button_height + button_margin), 300, button_height)
                        pg.draw.rect(win, GRAY, rect, 3, border_radius=10)
                        text_surf = fnaf_font.render(main_task_name, True, WHITE)
                        win.blit(text_surf, (rect.x + 10, rect.y + 10))
                        buttonDraw(win,buttonBack)
                else:
                    subtasks = tasks_structure[showing_subtasks_for]["Подзадачи"]
                    y_start = 150
                    button_height = 40
                    button_margin = 10
                    for i, subtask in enumerate(subtasks):
                        if subtask["done"]:
                            continue
                        rect = pg.Rect(150, y_start + i * (button_height + button_margin), 400, button_height)
                        pg.draw.rect(win, GRAY, rect, 3, border_radius=10)
                        text_surf = fnaf_small_font.render(subtask["name"], True, WHITE)
                        win.blit(text_surf, (rect.x + 10, rect.y + 8))
                    back_rect = pg.Rect(10, 80, widch - 20, 40)
                    pg.draw.rect(win, BLUE, back_rect, 3, border_radius=5)
                    back_text = fnaf_font.render("Назад", True, WHITE)
                    win.blit(back_text, (back_rect.x + 10, back_rect.y + 5))

            # Логика вкладки датчика движения
            elif active_tab == TAB_SENSOR:
                loading_subtask = False
                buttonDraw(win,buttonBack)
                if scanning_active:
                    if point == 15:
                        point = 0
                        if toch == '...':
                            toch = '.'
                        else:
                            toch += '.'
                    else:
                        point += 1
                    elapsed = time.time() - scan_start_time
                    progress = min(elapsed / scan_duration, 1)
                    if popa == 1:
                        drawScan = text.render(f"Инициализация сенсоров {toch}", True, WHITE)
                    elif popa == 2:
                        drawScan = text.render(f"Анализ данных {toch}", True, WHITE)
                    elif popa == 3:
                        drawScan = text.render(f"Определение позиции {toch}", True, WHITE)
                    win.blit(drawScan, (widch//2-getFont(drawScan,'x')//2,height-10-getFont(drawScan,'y')))

                    
                    

                    if elapsed >= scan_duration:
                        scanning_active = False
                        scan_finished = True
                        message_show_start = time.time()
                        popa = 1


                        
                elif scan_finished:
                    
                    if roomRudolphu >= 6 or roomBilly >= 6:
                        msg = text.render("Обнаруженно движение по близости!", True, (255,0,0))
                    else:
                        msg = text.render("Движений не обнаружено", True, (0,255,0))
                    win.blit(msg, (widch//2-getFont(msg,'x')//2,height//2-getFont(msg,'y')//2))
                    if time.time() - message_show_start > 3:
                        scan_finished = False
                        message_show_start = None
                else:
                    info_text = fnaf_font.render("Хотите начать сканирование склада?", True, WHITE)
                    onButtons = fnaf_font.render("Начать", True, WHITE)
                    try:
                        button_width = getFont(onButtons, 'x') + 20
                        button_height = getFont(onButtons, 'y') + 10
                    except Exception:
                        button_width = 100
                        button_height = 30
                    button_x = 100
                    button_y = 80
                    turnButton_os = pg.Rect(button_x, button_y, button_width, button_height)
                    pg.draw.rect(win, BLUE, turnButton_os, 3, border_radius=5)
                    win.blit(onButtons, (turnButton_os.x + 10, turnButton_os.y + 5))
                    win.blit(info_text, (100, 150))

            # Отображаем индикатор загрузки для подзадачи, если есть
            if loading_subtask:
                elapsed = time.time() - loading_start_time
                progress = elapsed / loading_subtask["time"]
                if progress >= 1:
                    loading_subtask["done"] = True
                    # if "_sound_obj" in loading_subtask:
                    loading_subtask["_sound_obj"].stop()
                    loading_subtask = None
                    loading_start_time = None
                    if all_tasks_done(tasks_structure):
                        
                        stopGamee('win')
                        # если все задания выполнены — можно дать какое-то вознаграждение/событие
                        # Я оставил поведение простым: закрываем монитор и возвращаемся в офис.
                        os_open = False
                else:
                    if pointDraw == 5:
                        pointDraw = 0
                        if pointPopa == 10:
                            pointPopa = 0
                            if popa != 3:
                                popa += 1

                        else:
                            pointPopa += 1

                        if elePosDraw != 8:
                            elePosDraw += 1
                        else:
                            elePosDraw = 1
                    else:
                        pointDraw += 1
                    loading_text = loadFont.render(f"Пожалуйста подождите {toDrawLoad(elePosDraw)}", True, WHITE)
                    # getFont может отсутствовать — безопасный вариант:
                    try:
                        x_text = widch // 2 - getFont(loading_text, 'x') // 2
                        y_text = height - getFont(loading_text, 'y') - 10
                    except Exception:
                        x_text = 100
                        y_text = height - 30
                    win.blit(loading_text, (x_text, y_text))









            pg.display.update()

        else:
            # Обычная игровая отрисовка (как у тебя)
            if pos == 'office':
                scanning_active = False
                loading_subtask = False
                active_tab = TAB_TASKS
                w,h = widch//3+100,height//3+50
                turnButton = pg.Rect(widch//2-w//2, height//2-h//2-50, w, h)
                pg.draw.rect(win, (0,255,0), turnButton, 3, border_radius=5)
                if turnButton.collidepoint(mouse[0], mouse[1]):
                    if moniTor:
                        helpertext = text.render('Нажмите на монитор для выполнения заданий', 1, (250,250,250))
                    else:
                        helpertext = text.render('Включите монитор кнопкой включения снизу', 1, (250,250,250))

                    # pos = 'fnafOS'  # больше не меняем тут — открываем через os_open флаг
                if moniTor:
                    win.blit(officeOn, (0,0))
                    fone_event = officeOn
                else:
                    win.blit(office12, (0,0))
                    fone_event = office12


                buttonDraw(win,buttonLeft,direction='left')
                if moniTor == False:
                    power_button(win,buttonPower,'off')
                else:
                    power_button(win,buttonPower,'on')
                win.blit(helpertext, (5,5))

            elif pos == 'holl':
                flash = False
                win.blit(hollN, (0,0))
                darkness = pg.Surface((widch, height), pg.SRCALPHA)
                darkness.fill((0, 0, 0, 250))  # Полутёмный черный с прозрачностью

                mask_pos = (mouse[0] - FLASHLIGHT_RADIUS, mouse[1] - FLASHLIGHT_RADIUS)
                darkness.blit(flashlight_mask, mask_pos, special_flags=pg.BLEND_RGBA_SUB)
                win.blit(darkness, (0, 0))
                pg.draw.circle(win, (255, 255, 255), (mouse[0], mouse[1]), 3)
                buttonDraw(win,buttonRight,direction='right')
                fone_event = hollN

            elif pos == 'kitchen':
                helpertext = text.render('Свети ему в лицо', 1, (250,250,250))
                pg.mouse.set_visible(False)
                win.blit(room_1, (0,0))
                darkness = pg.Surface((widch, height), pg.SRCALPHA)
                darkness.fill((0, 0, 0, 250))
                mask_pos = (mouse[0] - FLASHLIGHT_RADIUS, mouse[1] - FLASHLIGHT_RADIUS)
                darkness.blit(flashlight_mask, mask_pos, special_flags=pg.BLEND_RGBA_SUB)
                win.blit(darkness, (0, 0))
                pg.draw.circle(win, (255, 255, 255), (mouse[0], mouse[1]), 3)
                buttonDraw(win,buttonBack)
                win.blit(helpertext,(5,5))
                fone_event = room_1

            elif pos == 'roomBill':
                helpertext = text.render('Создайте полную тишину если он здесь', 1, (250,250,250))
                if not flash:
                    win.blit(room_2, (0,0)); fone_event = room_2
                else:
                    if positionBillRoom == 'активен':
                        win.blit(room_2_st1, (0,0)); fone_event = room_2_st1
                    else:
                        win.blit(room_2_light, (0,0)); fone_event = room_2_light
                buttonDraw(win,buttonBack)
                textus(win,peace,'Тишина',text)
                win.blit(helpertext,(5,5))

            elif pos == 'roomRUdi':
                helpertext = text.render('Уходите с включенным фонариком если он здесь', 1, (250,250,250))
                if not flash:
                    win.blit(room_3, (0,0)); fone_event = room_3
                else:
                    if positionRudiRoom == 'активен':
                        win.blit(room_3_st1, (0,0)); fone_event = room_3_st1
                    else:
                        win.blit(room_3_light, (0,0)); fone_event = room_3_light
                buttonDraw(win,buttonBack)
                win.blit(helpertext,(5,5))

            # если pending_transition — проигрываем анимацию
            if pending_transition:
                pending_transition = False
                animat(win)


            drawTem()
            pg.display.flip()
            # Видимость курсора в зависимости от локации
            if pos == 'kitchen' or pos == 'holl':
                pg.mouse.set_visible(False)
            else:
                pg.mouse.set_visible(True)
        # Если выставлен pending_scare — главный поток проигрывает джампскэр (блокирующе)
        if pending_scare is not None:
            monster = pending_scare
            pending_scare = None
            stopGamee('kill')
            return jumScare(monster, win)

        # Проверяем флаги, выставленные потоками
        if kill_flag == 'setKillScene':
            return 'setKillScene'
        elif kill_flag == 'menu':
            return 'menu'
        elif kill_flag == 'win':
            smen = text.render(f'=== СМЕНА {night}/5 ЗАВЕРШЕНА ===', 1, (250,250,250))

            if night != 5:
                night += 1
                nightLam = open('data_user/nightUser.txt','w')
                nightLam.write(str(night))
                nightLam.close()

                statik = [tem1,tem2,tem3,tem4,tem5,tem6,tem7,tem8,tem8,tem10]
                for cadr in statik:
                    win.blit(cadr,(0,0))
                    pg.display.flip()
                    pg.time.Clock().tick(24)
                win.fill((0,0,0))
                win.blit(smen,(widch//2-getFont(smen,'x')//2,height//2-getFont(smen,'y')//2))
                pg.display.flip()
                pg.time.Clock().tick(1)
                pg.time.Clock().tick(1)
                pg.time.Clock().tick(1)
                statik = [tem1,tem2,tem3,tem4,tem5,tem6,tem7,tem8,tem8,tem10]
                for cadr in statik:
                    win.blit(cadr,(0,0))
                    pg.display.flip()
                    pg.time.Clock().tick(24)
                
                return 'menu'
            else:
                return 'menu'

    return kill_flag