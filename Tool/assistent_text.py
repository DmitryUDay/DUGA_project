import pygame as pg
from os import system

system('cls')

while True:
    size = 30
    try:
        size = int(size)
        text = input('Введите текст: ')

        if size == 0 or text == '0':
            break
        else:
            pg.init()
            text = pg.font.SysFont('arial', size)

            text_match = text.render(f'{text}',1, (255,255,255))
            x, y = text_match.get_rect().size
            print(f'X:{x}/y:{y}')
    except:
        print('Ошибка!')