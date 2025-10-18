import pygame as pg
import sqlite3 as sq
import math
sX = open('data_user\data_file_game\widch.txt', 'r')
whh = int(sX.read())
sX = open('data_user\data_file_game\height.txt', 'r')
hhh = int(sX.read())

def getFont(text, pos):
    text_rect = text.get_rect()
    if pos == 'x':
        return text_rect.width
    elif pos == 'y':
        return text_rect.height



# def getTer(patch,operand,operandVari,searchIndex):
#     tabl = 'userData'
#     conn = sq.connect(f'./{patch}.db')
#     cursor = conn.cursor()
#     cursor.execute(f"SELECT * FROM {tabl} WHERE {operand} = ?", (operandVari,))
#     getter = cursor.fetchone()
#     conn.close()
#     try:
#         getter = getter[int(searchIndex)]
#     except:
#         getter = ''
#     return getter


# def UpdateBase(patch,nameTablition,tableFROM,defaultTable,TableValueFROM,defaultValueTable):
#     conn = sq.connect(f'{ptc}/{patch}')
#     cursor = conn.cursor()
#     cursor.execute(f"""
#     UPDATE {nameTablition}
#     SET {tableFROM} = ?
#     WHERE {defaultTable} = ?
#     """, (TableValueFROM, defaultValueTable,))
#     conn.commit()
#     conn.close()


def subtitleDraw(text):
    pass



def draw_text_rect(surface, text, font, text_color, widch,height, padding=10):
    """
    Рисует текст с переносом по словам внутри прямоугольника rect с отступами.
    """
    rect = pg.Rect(5, height - 100 - 5, widch - 10, 95)
    x, y, w, h = rect
    pg.draw.rect(surface, (0,0,0), rect, border_radius=5)

    words = text.split(' ')
    space_width, space_height = font.size(' ')
    line = ''
    line_height = font.get_linesize()
    y_offset = y + padding

    for word in words:
        # Проверяем ширину строки, если добавить слово
        test_line = line + word + ' '
        test_width, _ = font.size(test_line)
        if test_width > w - 2 * padding:
            # Выводим текущую строку
            rendered_line = font.render(line, True, text_color)
            surface.blit(rendered_line, (x + padding, y_offset))
            y_offset += line_height
            line = word + ' '
        else:
            line = test_line

    # Выводим последнюю строку
    if line:
        rendered_line = font.render(line, True, text_color)
        surface.blit(rendered_line, (x + padding, y_offset))
    
    font = pg.font.SysFont("arial", 25)
    eToContinue = font.render('[E]', True, (255,255,255))
    surface.blit(eToContinue,(widch-10-getFont(eToContinue,'x')-5, height-15-getFont(eToContinue,'y')))

def blitTask(win,content,x,y):
    TASK_COLOR = (173, 216, 230)
    OUTLINE_COLOR = (0, 0, 0)
    TASK_FONT = pg.font.SysFont("Arial", 32, bold=True)
    content = f'{content} (e)'
    rect = TASK_FONT.render(content, True, TASK_COLOR).get_rect(center=(x, y - 60))
    win.blit(TASK_FONT.render(content, True, OUTLINE_COLOR), rect.move(1,1))
    win.blit(TASK_FONT.render(content, True, TASK_COLOR), rect)

def load_animation(path_list, size):
    """Загрузка кадров анимации"""
    frames = []
    for path in path_list:
        img = pg.image.load(path).convert_alpha()
        if size:
            img = pg.transform.scale(img, size)
        frames.append(img)
    return frames

def formGet(goga, height):
    """Загрузка и масштабирование фона"""
    if goga == 'orig':
        path = 'img/cutGame/homePlayer.png'
    elif goga == 'fodd':
        path = 'img/cutGame/homePlayer2.png'
    else:
        path = 'img/cutGame/homePlayer.png'

    fone_orig = pg.image.load(path).convert()
    scale_factor = height / fone_orig.get_height()
    new_width = int(fone_orig.get_width() * scale_factor)
    return pg.transform.scale(fone_orig, (new_width, height))


WHITE = (240, 240, 240)
# def draw_button(surface, rect, text, font):
#     # полупрозрачный фон
#     button_surf = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
#     button_surf.fill((50, 50, 50, 200))  # альфа ~ 80%

#     # рамка
#     pg.draw.rect(button_surf, WHITE, button_surf.get_rect(), width=2, border_radius=10)

#     # текст
#     text_surf = font.render(text, True, WHITE)
#     text_rect = text_surf.get_rect(center=(rect.width // 2, rect.height // 2 - 5))
#     button_surf.blit(text_surf, text_rect)

#     # треугольник вниз
#     triangle = [
#         (rect.width // 2 - 8, rect.height - 12),
#         (rect.width // 2 + 8, rect.height - 12),
#         (rect.width // 2, rect.height - 4)
#     ]
#     pg.draw.polygon(button_surf, WHITE, triangle)

#     # выводим на экран
#     surface.blit(button_surf, rect.topleft)

def textus(win,rect,content,font):
    button_surf = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    button_surf.fill((50, 50, 50, 200))  # альфа ~ 80%

    # рамка
    pg.draw.rect(button_surf, WHITE, button_surf.get_rect(), width=2, border_radius=10)

    # текст
    text_surf = font.render(content, True, WHITE)
    text_rect = text_surf.get_rect(center=(rect.width // 2, rect.height // 2 - 5))
    button_surf.blit(text_surf, text_rect)

    # выводим на экран
    win.blit(button_surf, rect.topleft)



def buttonDraw(win, rect, direction="down"):
    # поверхность с альфой
    button_surf = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    button_surf.fill((50, 50, 50, 200))  # прозрачный фон

    # рамка
    pg.draw.rect(button_surf, WHITE, button_surf.get_rect(), width=2, border_radius=10)

    # центр и размер треугольника
    tri_size = min(rect.width, rect.height) // 3
    cx, cy = rect.width // 2, rect.height // 2

    if direction == "down":
        triangle = [(cx - tri_size, cy - tri_size//2),
                    (cx + tri_size, cy - tri_size//2),
                    (cx, cy + tri_size)]
    elif direction == "up":
        triangle = [(cx - tri_size, cy + tri_size//2),
                    (cx + tri_size, cy + tri_size//2),
                    (cx, cy - tri_size)]
    elif direction == "left":
        triangle = [(cx + tri_size//2, cy - tri_size),
                    (cx + tri_size//2, cy + tri_size),
                    (cx - tri_size, cy)]
    elif direction == "right":
        triangle = [(cx - tri_size//2, cy - tri_size),
                    (cx - tri_size//2, cy + tri_size),
                    (cx + tri_size, cy)]

    pg.draw.polygon(button_surf, WHITE, triangle)

    # рендерим кнопку на экран
    win.blit(button_surf, rect.topleft)

def power_button(win, rect,posi):
    # поверхность с альфой
    button_surf = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    if posi == 'off':
        button_surf.fill((50, 50, 50, 200))  # фон ~80% прозрачности
    else:
        button_surf.fill((50, 89, 50, 200))  # фон ~80% прозрачности

    # рамка кнопки
    pg.draw.rect(button_surf, WHITE, button_surf.get_rect(), width=2, border_radius=10)

    # центр и размеры иконки
    cx, cy = rect.width // 2, rect.height // 2
    radius = min(rect.width, rect.height) // 4

    # круг (дуга сверху, как у кнопки питания)
    rect_circle = pg.Rect(cx - radius, cy - radius, radius * 2, radius * 2)
    pg.draw.arc(button_surf, WHITE, rect_circle, math.radians(120), math.radians(420), width=4)

    # вертикальная палочка сверху
    pg.draw.line(button_surf, WHITE, (cx, cy - radius - 2), (cx, cy - radius // 2), width=4)

    # рисуем на экране
    win.blit(button_surf, rect.topleft)

def langu():
    with open('data_user\language.txt') as file:
        file.read()
    if file == 'RU':
        return True
    return False



class ScreenFader:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.surface = pg.Surface((self.width, self.height))
        self.surface.fill((0, 0, 0))
        self.active = False
        self.mode = "out"  # "out" или "in"
        self.alpha = 0      # текущая прозрачность
        self.speed = 5      # скорость фейда

    def start(self, mode="out", speed=5, block=False, clock=None):
        """Запускаем фейд.
        mode: "out" (в чёрный), "in" (из чёрного)
        block: если True → ждём, пока фейд завершится
        clock: нужен, если block=True (чтобы тикать кадры)
        """
        self.active = True
        self.mode = mode
        self.speed = speed
        if mode == "out":
            self.alpha = 0
        else:
            self.alpha = 255

        if block:
            # блокирующая петля (например, для out)
            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        raise SystemExit

                self.update()
                pg.display.flip()
                if clock:
                    clock.tick(60)
                if not self.active:
                    running = False

    def update(self):
        """Вызывать каждый кадр в основном цикле игры"""
        if not self.active:
            return

        # --- плавное изменение альфа ---
        if self.mode == "out":
            self.alpha += self.speed
            if self.alpha >= 255:
                self.alpha = 255
                self.active = False
        elif self.mode == "in":
            self.alpha -= self.speed
            if self.alpha <= 0:
                self.alpha = 0
                self.active = False

        # --- наложение прозрачной поверхности ---
        self.surface.set_alpha(max(0, min(255, self.alpha)))
        self.screen.blit(self.surface, (0, 0))

    def is_active(self):
        return self.active

