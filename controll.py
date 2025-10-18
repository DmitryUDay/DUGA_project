import pygame as pg
from tkinter import messagebox
pg.init()

try:

    lambdaS = open('data_user\display.txt', 'r')
    lambdaSRead = lambdaS.read()
    if lambdaSRead == 'Full screen':
        win = pg.display.set_mode((0,0), pg.FULLSCREEN)
        screen_width = win.get_width()
        screen_height = win.get_height()


        sX = open('data_user\data_file_game\widch.txt', 'w')
        sX.write(str(screen_width))
        sX.close()


        sX = open('data_user\data_file_game\height.txt', 'w')
        sX.write(str(screen_height))
        sX.close()
    elif lambdaSRead == 'auto':
        info = pg.display.Info()  # получаем инфо о мониторе
        win = pg.display.set_mode((info.current_w, info.current_h), pg.RESIZABLE)
        screen_width = win.get_width()
        screen_height = win.get_height()
        sX = open('data_user\data_file_game\widch.txt', 'w')
        sX.write(str(screen_width))
        sX.close()


        sX = open('data_user\data_file_game\height.txt', 'w')
        sX.write(str(screen_height))
        sX.close()

    pg.display.set_caption('DUGA')
    pg.display.set_icon(pg.image.load('img\start\logo_game.png'))

    #GAMESCENE#
    from menu import menu_starter as ms
    from option import options as opt
    from startUP import initSys
    from warning_by_stUP import des_start
    from game import gamee
    from game_over import game_over_init
    from userWin import wini
    from sujet import home
    #GAMESCENE#

    clock = pg.time.Clock()

    def main():
        scene = 'loadStart'

        cicle = True
        while cicle:
            if scene == 'menu':
                sceneNow = ms(win)
            elif scene == 'option':
                sceneNow = opt(win)
            elif scene == 'loadStart':
                sceneNow = initSys(win)
            elif scene == 'goWarning':
                sceneNow = des_start(win)
            elif scene == 'game':
                sceneNow = gamee(win)
            elif scene == 'setKillScene':
                sceneNow = game_over_init(win)
            elif scene == 'win':
                sceneNow = wini(win)
            elif scene == 'NG':
                sceneNow = gamee(win)
                # sceneNow = home(win)

            else:
                break

            if sceneNow:
                scene = sceneNow
            else:
                cicle = False


        pg.quit()

    if __name__ == "__main__":
        main()
except  Exception as e:
    pg.quit()
    messagebox.showerror('Червячок-Worma',f'Червяк съел игру. Ошибка: "{e}"')
