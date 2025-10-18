import pygame as pg
import sys 
pg.init() 
clock = pg.time.Clock()
win = pg.display.set_mode((0,0), pg.FULLSCREEN) 
base_font = pg.font.Font(None, 32)
user_text = ''
ex = 0
while True:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit() 
            sys.exit()
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_BACKSPACE: 
                user_text = user_text[:-1] 
            elif event.key == pg.K_RETURN: 
                pg.quit()
                ex = 1
            else: 
                user_text += event.unicode
    if ex == 1:
        break
    win.fill((255,255,255))
    pg.draw.rect(win,(0,0,0), (5,5,200,40), border_radius=5)
    text_surface = base_font.render(user_text, True, (255,255,255))
    win.blit(text_surface,(10,10))
    pg.display.flip()
    
print(user_text)