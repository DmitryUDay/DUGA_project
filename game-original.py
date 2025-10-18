import pygame as pg
from time import sleep
from random import randint
# from random import choice
from pygame import mixer
import threading

#--INIT--#
pg.init()
mixer.init()

joy = 'deactivate'

session = 'KEYBOARD'
sound_connect_joy = 1
fone_event = 'none'

one_anim = True

timer_alert = 0

ignore_joy = 'none'


text = pg.font.SysFont('arial', 30)
pres_A = mixer.Sound('sound/system/press_a.mp3')
turn_ON = mixer.Sound('sound/system/tON.mp3')
turn_OFF = mixer.Sound('sound/system/tOFF.mp3')
try:
    joystick = pg.joystick.Joystick(0)
    joystick.init()
    pg.joystick.init()
    joy = 'ACT'

    press_A = text.render(f'Нажмите "A" для продолжения',1, (255,255,255))
    session = 'True'
except:
    session = 'False'
    joy = 'NF'

tOFF = text.render(f'Устройство отключенно',1, (255,255,255))

show_connect = 0

#--INIT--#
wait = pg.time.Clock()
secret_persone = False

# random_secret = choice(1,1000) #Random RetCet
# if random_secret == 72:
#     secret_persone = True

# if secret_persone == True:
#     radom_time = choice(84,210) # == 100

# show = radom_time
# show += 10


# secret_persone = True
# radom_time = 10
# show = radom_time
# show += 100


mesto = 'office'#holl,room_1,room_2,room_3

#OPTION AI#
kill_playerB = 0
#---BILL_OPTIONS---#
prognat_bill = 0
att = 0
bill_lv = 0
point_Bill = 0 # Дефолт 0
room_Bill = 1# Дефолт 1
#---BILL_OPTIONS---#

#---RUD_OPTION---#
prognat_rud = 0
Ratt = 0
rud_lv = 0
kill_playerR = 0
point_RUd = 0 # Дефолт 0
room_RUd = 1# Дефолт 1
#---RUD_OPTION---#

#OPTION AI#

kislorod = 100

reloadVentelation = text.render('Нажмите (r), для вентиляции',1, (250,250,250))

pause = text.render('Пауза',1, (255,255,255))
gplay = text.render('Геймплей приостановлен',1, (255,255,255))


contr = text.render('продолж.',1, (250, 250, 250))
go_menu = text.render('В меню',1, (250, 250, 250))
go_retry = text.render('Заново',1, (250, 250, 250))
go_exit = text.render('Выход',1, (250, 250, 250))


shd_gameplay = text.render('Текущая игра завершится',1, (250, 250, 250))
alert_menu = text.render('Выйти в меню?',1, (250, 250, 250))
alert_retry = text.render('Начать заново?',1, (250, 250, 250))
alert_exit = text.render('Точно выйти?',1, (250, 250, 250))

widch_open = open('data_user\data_file_game\widch.txt', 'r')
height_open = open('data_user\data_file_game\height.txt', 'r')
widch_read = widch_open.read()
height_read = height_open.read()
widch = int(widch_read)
height = int(height_read)

cont = height/2-75
gmenu = height/2-75+40
grety = height/2-75+40*2
gexit = height/2-75+40*3

ps = cont#con,menu,retry,exit


win_player = 0
ch_player = 0
cicle_time = True
cicle_game = True
kill_playerB = 0
#FLASH_LIGHT
flash = 0
#RANDOM#
tik = 0
tik_RUd = 0
#CICLE MOV#
movie_Bill = True
movie_RUd = True

#DOOR#
x_seredina,y_seredina = widch-widch+400, height-height+178
x_left,y_left = widch-widch+30,height-640
x_right,y_right = widch-widch+764,height-height+356
#BACK BUTTON#
x_back_room_1, y_back_room_1 = widch/2-200,height-100 #убрать
x_back_room_2, y_back_room_2 = widch/2-200,height-100
x_back_room_3, y_back_room_3 = widch/2-200,height-100


#IMAGE#
light_image = pg.image.load("img\game\light.png") # Фонарик в 1 комнате
light_image = pg.transform.scale(light_image,(3000,2000))



office12 = pg.image.load('img\game\office_12.png') # Оффис
office12 = pg.transform.scale(office12,(widch,height))
office1 = pg.image.load('img\game\office_1.png') # Оффис
office1 = pg.transform.scale(office1,(widch,height))
office2 = pg.image.load('img\game\office_2.png') # Оффис
office2 = pg.transform.scale(office2,(widch,height))
office3 = pg.image.load('img\game\office_3.png') # Оффис
office3 = pg.transform.scale(office3,(widch,height))
office4 = pg.image.load('img\game\office_4.png') # Оффис
office4 = pg.transform.scale(office4,(widch,height))
office5 = pg.image.load('img\game\office_5.png') # Оффис
office5 = pg.transform.scale(office5,(widch,height))
office6 = pg.image.load('img\game\office_6.png') # Оффис
office6 = pg.transform.scale(office6,(widch,height))
office7 = pg.image.load('img\game\office_7.png') # Оффис
office7 = pg.transform.scale(office7,(widch,height))




hollN = pg.image.load('img/game/night_holl.png') # Ночной холл
hollN = pg.transform.scale(hollN,(widch,height))
holl = pg.image.load('img\game\holl.jpg') # холл
holl = pg.transform.scale(holl,(widch,height))
room_1 = pg.image.load('img/game/room_1.jpg') # комната 1
room_1 = pg.transform.scale(room_1,(widch,height))
room_2 = pg.image.load('img/game/room_2.png') # комната 2
room_2 = pg.transform.scale(room_2,(widch,height))
room_2_light = pg.image.load('img/game/flash_light_room_2.png') # Свет комнаты 2
room_2_light = pg.transform.scale(room_2_light,(widch,height))
room_2_st1 = pg.image.load('img/game/Billy_st1.png') # комната 2 билли стадия 1
room_2_st1 = pg.transform.scale(room_2_st1,(widch,height))
room_3 = pg.image.load('img/game/room_3.png') # комната 3
room_3 = pg.transform.scale(room_3,(widch,height))
room_3_light = pg.image.load('img/game/flash_light_room_3.png') # свет комнаты 3
room_3_light = pg.transform.scale(room_3_light,(widch,height))
room_3_st1 = pg.image.load('img\game\RUdolphu_st1.png') # комната 3 РУдольф стадия 1
room_3_st1 = pg.transform.scale(room_3_st1,(widch,height))

#Billy_J#
one = pg.image.load('img\game\Jumpscare_Billy_Bob/1.jpg')
one = pg.transform.scale(one,(widch,height))
two = pg.image.load('img\game\Jumpscare_Billy_Bob/2.jpg')
two = pg.transform.scale(two,(widch,height))
three = pg.image.load('img/game/Jumpscare_Billy_Bob/3.jpg')
three = pg.transform.scale(three,(widch,height))
fore = pg.image.load('img/game/Jumpscare_Billy_Bob/4.jpg')
fore = pg.transform.scale(fore,(widch,height))
five = pg.image.load('img/game/Jumpscare_Billy_Bob/5.jpg')
five = pg.transform.scale(five,(widch,height))
six = pg.image.load('img/game/Jumpscare_Billy_Bob/6.jpg')
six = pg.transform.scale(six,(widch,height))
seven = pg.image.load('img/game/Jumpscare_Billy_Bob/7.jpg')
seven = pg.transform.scale(seven,(widch,height))
eight = pg.image.load('img/game/Jumpscare_Billy_Bob/8.jpg')
eight = pg.transform.scale(eight,(widch,height))
nine = pg.image.load('img/game/Jumpscare_Billy_Bob/9.jpg')
nine = pg.transform.scale(nine,(widch,height))
ten = pg.image.load('img/game/Jumpscare_Billy_Bob/10.jpg')
ten = pg.transform.scale(ten,(widch,height))
eleven = pg.image.load('img/game/Jumpscare_Billy_Bob/11.jpg')
eleven = pg.transform.scale(eleven,(widch,height))
twelve = pg.image.load('img/game/Jumpscare_Billy_Bob/12.jpg')
twelve = pg.transform.scale(twelve,(widch,height))
freetin = pg.image.load('img/game/Jumpscare_Billy_Bob/13.jpg')
freetin = pg.transform.scale(freetin,(widch,height))
screamer_Bill = [one,two,three,fore,five,six,seven,eight,nine,ten,eleven,twelve,freetin]
#Billy_J#

#RUdolphu_J#
oneR = pg.image.load('img/game/Jumpscare_Rudolphu/1.jpg')
oneR = pg.transform.scale(oneR,(widch,height))
twoR = pg.image.load('img/game/Jumpscare_Rudolphu/2.jpg')
twoR = pg.transform.scale(twoR,(widch,height))
threeR = pg.image.load('img/game/Jumpscare_Rudolphu/3.jpg')
threeR = pg.transform.scale(threeR,(widch,height))
foreR = pg.image.load('img/game/Jumpscare_Rudolphu/4.jpg')
foreR = pg.transform.scale(foreR,(widch,height))
fiveR = pg.image.load('img/game/Jumpscare_Rudolphu/5.jpg')
fiveR = pg.transform.scale(fiveR,(widch,height))
sixR = pg.image.load('img/game/Jumpscare_Rudolphu/6.jpg')
sixR = pg.transform.scale(sixR,(widch,height))
sevenR = pg.image.load('img/game/Jumpscare_Rudolphu/7.jpg')
sevenR = pg.transform.scale(sevenR,(widch,height))
eightR = pg.image.load('img/game/Jumpscare_Rudolphu/8.jpg')
eightR = pg.transform.scale(eightR,(widch,height))
nineR = pg.image.load('img/game/Jumpscare_Rudolphu/9.jpg')
nineR = pg.transform.scale(nineR,(widch,height))
tenR = pg.image.load('img/game/Jumpscare_Rudolphu/10.jpg')
tenR = pg.transform.scale(tenR,(widch,height))
elevenR = pg.image.load('img/game/Jumpscare_Rudolphu/11.jpg')
elevenR = pg.transform.scale(elevenR,(widch,height))
twelveR = pg.image.load('img/game/Jumpscare_Rudolphu/12.jpg')
twelveR = pg.transform.scale(twelveR,(widch,height))
screamerR = [oneR,twoR,threeR,foreR,fiveR,sixR,sevenR,eightR,nineR,tenR,elevenR,twelveR]
#RUdolphu_J#

#--MOVIE_STATIK--#
stm1 = pg.image.load('img/game/statik_mov/1.png')
stm1 = pg.transform.scale(stm1,(widch,height))
stm2 = pg.image.load('img/game/statik_mov/2.png')
stm2 = pg.transform.scale(stm2,(widch,height))
stm3 = pg.image.load('img/game/statik_mov/3.png')
stm3 = pg.transform.scale(stm3,(widch,height))
stm4 = pg.image.load('img/game/statik_mov/4.png')
stm4 = pg.transform.scale(stm4,(widch,height))
stm5 = pg.image.load('img/game/statik_mov/5.png')
stm5 = pg.transform.scale(stm5,(widch,height))
stm6 = pg.image.load('img/game/statik_mov/6.png')
stm6 = pg.transform.scale(stm6,(widch,height))
stm7 = pg.image.load('img/game/statik_mov/7.png')
stm7 = pg.transform.scale(stm7,(widch,height))
stm8 = pg.image.load('img/game/statik_mov/8.png')
stm8 = pg.transform.scale(stm8,(widch,height))
statik = [stm1,stm2,stm3,stm4,stm5,stm6,stm7,stm8]
#--MOVIE_STATIK--#

#BUTTON#
bdown = pg.image.load('img/button/button_down.jpg')
bdown = pg.transform.scale(bdown,(676,101))

bup = pg.image.load('img/button/button_up.jpg')
bup = pg.transform.scale(bup,(676,101))

bleft = pg.image.load('img/button/button_left.jpg')
bleft = pg.transform.scale(bleft,(101,676))

bright = pg.image.load('img/button/button_right.jpg')
bright = pg.transform.scale(bright,(101,676))

break_bill = pg.image.load('img/button/make_sound.png')
break_bill = pg.transform.scale(break_bill,(358,87))
#BUTTON#

#ANIMATION#
tem1 = pg.image.load('img/temnenie/1.png')    
tem1 = pg.transform.scale(tem1,(widch,height))
tem2 = pg.image.load('img/temnenie/2.png')    
tem2 = pg.transform.scale(tem2,(widch,height))
tem3 = pg.image.load('img/temnenie/3.png')    
tem3 = pg.transform.scale(tem3,(widch,height))
tem4 = pg.image.load('img/temnenie/4.png')    
tem4 = pg.transform.scale(tem4,(widch,height))
tem5 = pg.image.load('img/temnenie/5.png')    
tem5 = pg.transform.scale(tem5,(widch,height))
tem6 = pg.image.load('img/temnenie/6.png')    
tem6 = pg.transform.scale(tem6,(widch,height))
tem7 = pg.image.load('img/temnenie/7.png')    
tem7 = pg.transform.scale(tem7,(widch,height))
tem8 = pg.image.load('img/temnenie/8.png')    
tem8 = pg.transform.scale(tem8,(widch,height))
tem9 = pg.image.load('img/temnenie/9.png')
tem9 = pg.transform.scale(tem9,(widch,height))
tem10 = pg.image.load('img/temnenie/10.png')
tem10 = pg.transform.scale(tem10,(widch,height))
#ANIMATION#


option_text = pg.font.SysFont(None, 30)


JS = mixer.Sound('sound\game\jump_scare.mp3')
ultra_sound = mixer.Sound('sound/game/breaker_bill_sound.mp3')
fone_game = mixer.Sound('sound/game/fone.mp3')
start_night = mixer.Sound('sound/game/night_start.mp3')


icon = pg.image.load('img\start\logo_game.png')
win = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.display.set_icon(icon)
pg.display.set_caption('DUGA')

def iniVarible():
    global joy,session,sound_connect_joy,fone_event,one_anim,timer_alert,ignore_joy,show_connect,secret_persone,mesto,kill_playerB,prognat_bill,att,bill_lv,point_Bill,room_Bill,prognat_rud,Ratt,rud_lv,kill_playerR,point_RUd,room_RUd,kislorod,ps,win_player,ch_player,cicle_time,cicle_game,kill_playerB,flash,tik,tik_RUd,movie_Bill,movie_RUd
    joy =               'deactivate'
    session =           'KEYBOARD'
    sound_connect_joy = 1
    fone_event =        'none'
    one_anim =          True
    timer_alert =       0
    ignore_joy =        'none' 
    show_connect =      0
    secret_persone =    False
    mesto =             'office'
    kill_playerB =      0
    prognat_bill =      0
    att =               0
    bill_lv =           0
    point_Bill =        0
    room_Bill =         1
    prognat_rud =       0
    Ratt =              0
    rud_lv =            0
    kill_playerR =      0
    point_RUd =         0
    room_RUd =          1
    kislorod =          100
    ps =                cont
    win_player =        0
    ch_player =         0
    cicle_time =        True
    cicle_game =        True
    kill_playerB =      0
    flash =             0
    tik =               0
    tik_RUd =           0
    movie_Bill =        True
    movie_RUd =         True

iniVarible()#Clear data


#---------Billy---------#
def random_Billy():
    global tik
    tik = randint(1,3)
    widacha_Billy()
def widacha_Billy():
    global point_Bill
    sleep(tik)
    point_Bill += 2
#---------Billy---------#

#--------RUdolphu--------#
def random_RUdolphu():
    global tik_RUd
    tik_RUd = randint(1,3)
    widacha_RUdolphu()
def widacha_RUdolphu():
    global point_RUd
    sleep(tik_RUd)
    point_RUd += 2
#--------RUdolphu--------#

def kis_min():
    global kislorod
    while True:
        wait.tick(1)
        wait.tick(1)
        kislorod -= 1
        wait.tick(1)
        wait.tick(1)


def AI_Billy():
    global event_room2,room_2_st1,point_Bill,room_Bill,movie_Bill,att
    movie_Bill = True
    while movie_Bill:
        if point_Bill >= 5:
            if room_Bill == 1:
                point_Bill = 0
                room_Bill = 2
            elif room_Bill == 2:
                point_Bill = 0
                room_Bill = 3
            elif room_Bill == 3:
                point_Bill = 0
                room_Bill = 4
            elif room_Bill == 4:
                point_Bill = 0
                room_Bill = 5
            elif room_Bill == 5:
                point_Bill = 0
                room_Bill = 6
            elif room_Bill == 6:
                point_Bill = 0
                room_Bill = 7
            elif room_Bill == 7:
                point_Bill = 0
                room_Bill = 8

                spiker_random = randint(1,2)
                if spiker_random == 1:
                    movie_Bill = False
                    inwin = mixer.Sound('sound\game\in_window.mp3')
                    inwin.play()
                    sleep(1)
                    inwin.stop()
                else:
                    movie_Bill = False
                att = 1#Атаковочный таймер включить
        else:
            sleep(tik_RUd)
            random_Billy()


def attention():#Запуск таймера Билли
    global prognat_bill,kill_playerB,bill_lv
    for ignor_cicle_Bill in range(0,7,1):
        if ignor_cicle_Bill != 6 and prognat_bill == 1:
            bill_lv = 1
            break
        elif ignor_cicle_Bill == 6 and prognat_bill != 1:
            kill_playerB = 1
        sleep(1)



def AI_croco():
    global event_room3,room_3_st1,point_RUd,room_RUd,movie_RUd,Ratt
    while movie_RUd:
        if point_RUd >= 5:
            if room_RUd == 1:
                point_RUd = 0
                room_RUd = 2
            elif room_RUd == 2:
                point_RUd = 0
                room_RUd = 3
            elif room_RUd == 3:
                point_RUd = 0
                room_RUd = 4
            elif room_RUd == 4:
                point_RUd = 0
                room_RUd = 5
            elif room_RUd == 5:
                point_RUd = 0
                room_RUd = 6
            elif room_RUd == 6:
                point_RUd = 0
                room_RUd = 7
            elif room_RUd == 7:
                point_RUd = 0
                room_RUd = 8
                # spiker_RU = randint(1,2)
                # if spiker_RU == 1:
                if mesto == 'office':
                    step = mixer.Sound('sound/game/left_RUdolphu.mp3')
                    step.play()
                elif mesto == 'holl':
                    step = mixer.Sound('sound\game\in_roorm_RUdolphu.mp3')
                    step.play()
                elif mesto == 'room_1':
                    step = mixer.Sound('sound/game/right_Rudolhu.mp3')
                    step.play()
                elif mesto == 'room_2':
                    step = mixer.Sound('sound/game/right_Rudolhu.mp3')
                    step.play()
                    sleep(1)
                    step.stop()
                elif mesto == 'room_3':
                    step = mixer.Sound('sound\game\in_roorm_RUdolphu.mp3')
                    step.play()
                movie_RUd = False#выключить цикл передвижения
                Ratt = 1#запуск таймера атаки РУДОЛЬФА
        else:
            random_RUdolphu()


def attention_croco():#Таймер атаки РУДОЛЬФА
    global prognat_rud,kill_playerR,rud_lv
    for ignor_cicle_rud in range(0,9,1):
        if ignor_cicle_rud != 8 and prognat_rud == 1:
            rud_lv = 1
            break
        elif ignor_cicle_rud == 8 and prognat_rud != 1:
            kill_playerR = 1
        sleep(1)

def winer():
    global win_player,ch_player
    while cicle_time:
        sleep(1)
        if ch_player == 336: # ~~5 минут 36 секунд~~ 
            win_player = 1
            break
        else:
            ch_player += 1
        print(ch_player)


def movie_statik():
    global statik
    for i in range(0,8,1):
        win.fill((0,0,0))
        win.blit(statik[0],(0,0))
        pg.display.flip()
        statik.pop(0)
        pg.time.Clock().tick(8)
    statik = [stm1,stm2,stm3,stm4,stm5,stm6,stm7,stm8]


win_alert = threading.Thread(target=winer)
win_alert.start()

kiska = threading.Thread(target=kis_min)
kiska.start()


AI_Billy_starter = threading.Thread(target=AI_Billy)
AI_Billy_starter.start()


AI_Rudi_start = threading.Thread(target=AI_croco)
AI_Rudi_start.start()

def JSound():
    JS.play()


def kill():
    global movie_Bill,movie_RUd,cicle_time,cicle_game
    movie_Bill = False
    movie_RUd = False
    cicle_time = False
    cicle_game = False
    fone_game.stop()
    JS.stop()
    ultra_sound.stop()
    from game_over import game_over_init
    game_over_init()


def died_from_Bill():
    global cicle_time, movie_RUd, movie_Bill,screamer_Bill
    JSound()
    if joy == 'ACT' and session == 'True':
        joystick.rumble(1, 1, 3000)
    for i in range(0,13,1):
        win.fill((0,0,0))
        win.blit(screamer_Bill[0],(0,0))
        pg.display.flip()
        screamer_Bill.pop(0)
        pg.time.Clock().tick(10)
    screamer_Bill = [one,two,three,fore,five,six,seven,eight,nine,ten,eleven,twelve,freetin]
    movie_Bill = False
    movie_RUd = False
    cicle_time = False
    kill()

def died_from_RUdolphu():
    global cicle_time, movie_RUd, movie_Bill,screamerR
    JSound()
    if joy == 'ACT' and session == 'True':
        joystick.rumble(1, 1, 3000)
    for i in range(0,12,1):
        win.fill((0,0,0))
        win.blit(screamerR[0],(0,0))
        pg.display.flip()
        screamerR.pop(0)
        pg.time.Clock().tick(10)
    screamerR = [oneR,twoR,threeR,foreR,fiveR,sixR,sevenR,eightR,nineR,tenR,elevenR,twelveR]
    movie_Bill = False
    movie_RUd = False
    cicle_time = False
    kill()

# if secret_persone == True:#Секр. персона. в Холле
#     if ch_player > show:
#         win.blit(hollN,(0,0))
#     if ch_player == radom_time:
#         secretik = pg.image.load('img/menu/ret_cet.png')
#         secretik = pg.transform.scale(secretik,(400,600))
#         win.blit(secretik,(widch-400,height-90))

# pg.draw.rect(win,(10,10,10),[x_seredina,y_seredina,300,400])
# pg.draw.rect(win,(10,10,10),[x_left,y_left,300,500]) # Визуализация перехода в комнату
# pg.draw.rect(win,(10,10,10),[x_right,y_right,300,300])

event_room2 = room_2#события комнат
event_room3 = room_3
event_holl = hollN #ADD mechanick to event holl the night
# event_holl = holl

fone_game.play(-1)
#ALERT#
def go_alert_menu():
    global movie_Bill,movie_RUd,cicle_time,joy
    while True:
        key = pg.key.get_pressed()
        if session == 'True':
            try:
                joystick = pg.joystick.Joystick(0)
                joystick.init()
                pg.joystick.init()
                joy = 'ACT'
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
            except:
                joy = 'NF'
                movie_Bill = False
                movie_RUd = False
                cicle_time = False
                turn_OFF.play()
                JNot_found()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            elif joy == 'ACT' and session == 'True':
                if joystick.get_button(0):
                    movie_Bill = False
                    movie_RUd = False
                    cicle_time = False
                    fone_game.stop()

                    from menu import menu_starter
                    menu_starter()
                elif joystick.get_button(1):
                    menu()
            
            if key[pg.K_ESCAPE]:
                menu()
            if key[pg.K_RETURN]:
                from menu import menu_starter
                menu_starter()#EVENT
        
        win.blit(fone_event,(0,0))
        pg.draw.rect(win,(0,0,0), (widch/2-155,90,310,180))
        win.blit(shd_gameplay,(widch/2-152,100))
        win.blit(alert_menu,(widch/2-88,140))


        pg.display.flip()

def go_alert_exit():
    global movie_Bill,movie_RUd,cicle_time,joy
    while True:
        key = pg.key.get_pressed()
        if session == 'True':
            try:
                joystick = pg.joystick.Joystick(0)
                joystick.init()
                pg.joystick.init()
                joy = 'ACT'
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
            except:
                joy = 'NF'
                movie_Bill = False
                movie_RUd = False
                cicle_time = False
                turn_OFF.play()
                JNot_found()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            elif joy == 'ACT' and session == 'True':
                if joystick.get_button(0):
                    exit()
                elif joystick.get_button(1):
                    menu()

            if key[pg.K_ESCAPE]:
                menu()
            if key[pg.K_RETURN]:
                exit()#EVENT

        win.blit(fone_event,(0,0))
        pg.draw.rect(win,(0,0,0), (widch/2-155,90,310,180))
        win.blit(shd_gameplay,(widch/2-152,100))
        win.blit(alert_exit,(widch/2-80,140))
        pg.display.flip()



def vib_joy():#Если геймпад канектнули во время без сеанса   
    global ignore_joy,session 
    while True:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if widch/2-300 <= mouse[0] <= widch/2-300+700 and 50 <= mouse[1] <= 50+45:
                    ignore_joy = 'ignoring'
                    menu()

                elif widch/2-300 <= mouse[0] <= widch/2-300+700 and 100 <= mouse[1] <= 100+45:
                    session = 'True'
                    menu()


        try:
            joystick = pg.joystick.Joystick(0)
            joystick.init()
            pg.joystick.init()
            name = joystick.get_name()
            #Если геймпад будет подключен при не активном сеансе#

            ignore_joy_session = text.render(f'Проигнорировать {name}',1, (255,255,255))#Проигнорировать Xbox 360 controller
            connect_joy_session = text.render(f'Подключить {name}',1, (255,255,255))

            win.blit(fone_event,(0,0))

            pg.draw.rect(win,(0,0,0), (widch/2-300,50,700,45))
            pg.draw.rect(win,(0,0,0), (widch/2-300,100,700,45))# Height = 55 первый выбор + 45 текст + 5 пикселей для стиля

            if widch/2-300 <= mouse[0] <= widch/2-300+700 and 50 <= mouse[1] <= 50+45:
                pg.draw.rect(win,(189,2,2), (widch/2-300,50,700,45))
            elif widch/2-300 <= mouse[0] <= widch/2-300+700 and 100 <= mouse[1] <= 100+45:
                pg.draw.rect(win,(106,166,186), (widch/2-300,100,700,45))

            win.blit(ignore_joy_session,(widch/2-295,55))
            win.blit(connect_joy_session,(widch/2-295,105))

            pg.display.flip()

        except:
            menu()

#ALERT#
def menu():
    global ps,movie_Bill,movie_RUd,cicle_time

    movie_Bill = False
    movie_RUd = False
    cicle_time = False
    while True:
        key = pg.key.get_pressed()
        
        if session == 'True':
            try:
                joystick = pg.joystick.Joystick(0)
                joystick.init()
                pg.joystick.init()
                joy = 'ACT'
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
            except:
                joy = 'NF'
                movie_Bill = False
                movie_RUd = False
                cicle_time = False
                turn_OFF.play()
                JNot_found()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if session == 'True' and joy == 'ACT':
                if hat[1] == 1:
                    if ps == cont:
                        ps = gexit
                    elif ps == gmenu:
                        ps = cont
                    elif ps == grety:
                        ps = gmenu
                    elif ps == gexit:
                        ps = grety

                elif hat[1] == -1:

                    if ps == cont:
                        ps = gmenu
                    elif ps == gmenu:
                        ps = grety
                    elif ps == grety:
                        ps = gexit
                    elif ps == gexit:
                        ps = cont

                elif joystick.get_button(0):
                    if ps == gmenu:
                        go_alert_menu()

                    elif ps == grety:
                        # go_alert_retry()
                        pass

                    elif ps == gexit:
                        go_alert_exit()
                    elif ps == cont:
                        movie_Bill = True
                        movie_RUd = True
                        cicle_time = True
                        AI_Billy_starter = threading.Thread(target=AI_Billy)
                        AI_Billy_starter.start()
                        AI_Rudi_start = threading.Thread(target=AI_croco)
                        AI_Rudi_start.start()
                        win_alert = threading.Thread(target=winer)
                        win_alert.start()
                        game_play()


                elif joystick.get_button(7) or joystick.get_button(1):
                    movie_Bill = True
                    movie_RUd = True
                    cicle_time = True
                    AI_Billy_starter = threading.Thread(target=AI_Billy)
                    AI_Billy_starter.start()
                    AI_Rudi_start = threading.Thread(target=AI_croco)
                    AI_Rudi_start.start()
                    win_alert = threading.Thread(target=winer)
                    win_alert.start()
                    game_play()
                

            if key[pg.K_UP]:
                if ps == cont:
                    ps = gexit
                elif ps == gmenu:
                    ps = cont
                elif ps == grety:
                    ps = gmenu
                elif ps == gexit:
                    ps = grety
            
            elif key[pg.K_DOWN]:
                if ps == cont:
                    ps = gmenu
                elif ps == gmenu:
                    ps = grety
                elif ps == grety:
                    ps = gexit
                elif ps == gexit:
                    ps = cont

            elif key[pg.K_RETURN]:
                if ps == cont:
                    movie_Bill = True
                    movie_RUd = True
                    cicle_time = True
                    AI_Billy_starter = threading.Thread(target=AI_Billy)
                    AI_Billy_starter.start()
                    AI_Rudi_start = threading.Thread(target=AI_croco)
                    AI_Rudi_start.start()
                    win_alert = threading.Thread(target=winer)
                    win_alert.start()
                    game_play()

                elif ps == gmenu:
                    go_alert_menu()

                elif ps == grety:
                    pass

                elif ps == gexit:
                    go_alert_exit()

            elif key[pg.K_ESCAPE]:
                movie_Bill = True
                movie_RUd = True
                cicle_time = True
                AI_Billy_starter = threading.Thread(target=AI_Billy)
                AI_Billy_starter.start()
                AI_Rudi_start = threading.Thread(target=AI_croco)
                AI_Rudi_start.start()
                win_alert = threading.Thread(target=winer)
                win_alert.start()
                game_play()



        win.blit(fone_event,(0,0))
        pg.draw.rect(win,(0,0,0), (widch/2-50,height/2-80,120,160))#Dashboard menu
        pg.draw.rect(win,(2,121,168), (widch/2-45,ps,115,40))#KURSOR

        win.blit(pause,(widch/2-35,100))
        win.blit(gplay,(widch/2-147,140))

        win.blit(contr,(widch/2-45,height/2-75))
        win.blit(go_menu,(widch/2-45,height/2-75+40))
        win.blit(go_retry,(widch/2-45,height/2-75+40*2))
        win.blit(go_exit,(widch/2-45,height/2-75+40*3))

        pg.display.flip()


def JNot_found():
    global joy,sound_connect_joy
    while True:
        try:
            joystick = pg.joystick.Joystick(0)
            joystick.init()
            pg.joystick.init()
            joy = 'ACT'
        except:
            joy = 'NF'

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        win.blit(fone_event,(0,0))
        pg.draw.rect(win,(98,99,99), (widch/2-300,height-55,600,45))#600/45
        if joy == 'ACT':
            if sound_connect_joy == 1:
                sound_connect_joy = 0            
                turn_ON.play()

            if joystick.get_button(0):
                pres_A.play()
                sound_connect_joy = 1
                joystick = pg.joystick.Joystick(0)
                name = joystick.get_name()
                gamepadID = text.render(f'Подключено устройство {name}',1, (255,255,255))
                win.blit(gamepadID,(widch/2-295,height-60))
                pg.display.flip()
                pg.time.Clock().tick(1)
                pg.time.Clock().tick(1)
                pg.time.Clock().tick(1)
                joy = 'ACT'
                menu()
            else:
                win.blit(press_A,(widch/2-295,height-60))
                pg.display.flip()
        else:
            win.blit(tOFF,(widch/2-295,height-60))
            pg.display.flip()


class keys:
    def klava():
        global ch_player,mesto,flash,event_room2,event_room3,prognat_bill,prognat_rud,point_RUd,room_RUd,prognat_rud,room_RUd,point_RUd,movie_RUd,event_room3,event_room2,movie_Bill,cicle_time

        if session == 'True':
            try:
                joystick = pg.joystick.Joystick(0)
                joystick.init()
                pg.joystick.init()
                joy = 'ACT'
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
            except:
                joy = 'NF'
                movie_Bill = False
                movie_RUd = False
                cicle_time = False
                turn_OFF.play()
                JNot_found()
            if joy == 'ACT':
                if hat[0] == -1:
                    if mesto == 'holl':
                        pass
                    
                    elif mesto == 'room_1':
                        mesto = 'holl'
                        movie_statik()

                    elif mesto == 'office':
                        mesto = 'holl'
                        movie_statik()

                    elif mesto == 'room_2':
                        event_room2 = room_2
                        if room_Bill == 8: #если игрок уходит при аниматронике то 
                            if prognat_bill != 1: #иначе скример
                                died_from_Bill()
                        else:#иначе если аниматроник не пришёл то игнор
                            mixer.music.load('sound/game/run.mp3')
                            mixer.music.play()
                            event_room2 = room_2
                            mesto = 'holl'
                            movie_statik()

                    elif mesto == 'room_3':
                        event_room3 = room_3
                        if room_RUd == 8:
                            if flash == 1:
                                prognat_rud = 1
                                room_RUd = 1
                                point_RUd = 0
                                event_room3 = room_3_light
                                movie_RUd == True
                                movie_RUd = True
                                point_RUd = 0
                                room_RUd = 1
                                AI_Rudi_start = threading.Thread(target=AI_croco)
                                AI_Rudi_start.start()
                            else:
                                flash = 0
                                cicle_time = False
                                movie_RUd = False
                                movie_Bill = False
                                fone_game.stop()
                                JSound()
                                died_from_RUdolphu()
                        else:
                            mesto = 'holl'
                            movie_statik()

                        



                elif hat[0] == 1:
                    if mesto == 'room_1' or mesto == 'room_2' or mesto == 'room_3':
                        pass
                    else:
                        if mesto == 'office':
                            pass
                        else:
                            mixer.music.load('sound/game/run.mp3')
                            mixer.music.play()
                            mesto = 'office'
                            movie_statik()
                
                elif hat[1] == 1:
                    ch_player = 335
                    # if mesto == 'room_2':
                    #     if room_Bill == 8:
                    #         event_room2 = room_2_st1
                    #         prognat_bill = 1
                    #         ultra_sound.play()
                    #         sleep(4)
                elif joystick.get_button(6):
                    menu()


        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            if mesto == 'office':
                mesto = 'holl'
                movie_statik()

            elif mesto == 'room_1':
                mixer.music.load('sound/game/run.mp3')
                mixer.music.play()
                mesto = 'holl'
                movie_statik()

            elif mesto == 'room_2':
                event_room2 = room_2
                if room_Bill == 8: #если игрок уходит при аниматронике то 
                    if prognat_bill != 1: #иначе скример
                        died_from_Bill()
                else:#иначе если аниматроник не пришёл то игнор
                    mixer.music.load('sound/game/run.mp3')
                    mixer.music.play()
                    mesto = 'holl'
                    movie_statik()


            elif mesto == 'room_3':
                event_room3 = room_3
                if room_RUd == 8:
                    if prognat_rud != 1:
                        died_from_RUdolphu()
                else:
                    mixer.music.load('sound/game/run.mp3')
                    mixer.music.play()
                    mesto = 'holl'
                    movie_statik()

        elif key[pg.K_RIGHT]:
            if mesto == 'room_1' or mesto == 'room_2' or mesto == 'room_3':
                pass
            else:
                if mesto == 'office':
                    pass
                else:
                    mixer.music.load('sound/game/run.mp3')
                    mixer.music.play()
                    mesto = 'office'
                    movie_statik()




#---------------------------------BUTTON------------------------------------------------------------------------------------#
            # elif joystick.get_button(0):
            #     if mesto == 'room_2':
            #         if flash == 0:
            #             mixer.music.load('sound/game/flash_light.mp3')
            #             mixer.music.play()
            #             flash = 1
            #             if event_room3 != room_3_st1:
            #                 event_room3 = room_3_light
            #         else:
            #             flash = 0
            #             mixer.music.load('sound/game/flash_light.mp3')
            #             mixer.music.play()
            #             event_room2 = room_2

            #     elif mesto == 'room_3':
            #         if flash == 0:
            #             mixer.music.load('sound/game/flash_light.mp3')
            #             mixer.music.play()
            #             flash = 1
            #             event_room3 = room_3_light
            #         else:
            #             flash = 0
            #             mixer.music.load('sound/game/flash_light.mp3')
            #             mixer.music.play()
            #             event_room3 = room_3

#---------------------------------BUTTON------------------------------------------------------------------------------------#
fone_event = office12
def game_play():
    global show_connect,rud_lv,one_anim,cicle_game,mesto,flash,fone_event,event_room2,event_room3,room_Bill,room_RUd,point_Bill,point_RUd,prognat_bill,prognat_rud,cicle_time,movie_Bill,movie_RUd,bill_lv,Ratt,att
    while cicle_game:
        press = pg.mouse.get_pressed()#получение данных нажатия мышки
        mouse = pg.mouse.get_pos()
        key = pg.key.get_pressed()


        if ignore_joy != 'ignoring':
            if one_anim == True:
                one_anim = False
                statik = [tem10,tem9,tem8,tem7,tem6,tem5,tem4,tem3,tem2,tem1]
                for i in range(1,11,1):
                    
                    win.blit(office12,(0,0))
                    win.blit(statik[0],(0,0))
                    pg.display.flip()
                    statik.pop(0)
                    pg.time.Clock().tick(15)
                statik = [tem10,tem9,tem8,tem7,tem6,tem5,tem4,tem3,tem2,tem1]

            if session == 'True':
                try:
                    joystick = pg.joystick.Joystick(0)
                    joystick.init()
                    pg.joystick.init()
                    joy = 'ACT'
                    hats = joystick.get_numhats()
                    for i in range(hats):
                        hat = joystick.get_hat(i)
                except:
                    joy = 'NF'
                    movie_Bill = False
                    movie_RUd = False
                    cicle_time = False
                    turn_OFF.play()
                    JNot_found()
            else:
                try:
                    joystick = pg.joystick.Joystick(0)
                    joystick.init()
                    pg.joystick.init()
                    joy = 'ACT'
                    movie_Bill = False
                    movie_RUd = False
                    cicle_time = False
                    vib_joy()
                except:
                    joy = 'NF'

        for event in pg.event.get(): #цикл для событий выхода и тд
            if event.type == pg.QUIT:
                menu()

            if event.type == pg.KEYUP and key[pg.K_ESCAPE]:
                menu()

            if event.type == pg.MOUSEBUTTONUP and press[0]:#Воизбежании ложного нажатия при переходе с офиса в холл не открывалась кухня, создан блок команды реагирующий только на поднятие кнопки мыши а другой реагирует на ее нажатие
                if mesto == 'office':
                    if 0 <= mouse[0] <= 0+101 and height/2-338 <= mouse[1] <= height/2-338+338:#holl
                        mesto = 'holl'
                        movie_statik()

            elif event.type == pg.MOUSEBUTTONDOWN:
                if mesto == 'holl':
                    if widch-101 <= mouse[0] <= widch-101+101 and height/2-338 <= mouse[1] <= height/2-338+338:#go office
                        mesto = 'office'
                        movie_statik()
                    if x_left <= mouse[0] <= x_left+300 and y_left <= mouse[1] <= y_left+500:#go room1
                        mixer.music.load('sound/game/run.mp3')
                        mixer.music.play()
                        mesto = 'room_1'
                        movie_statik()
                    elif x_seredina <= mouse[0] <= x_seredina+300 and y_seredina <= mouse[1] <= y_seredina+500:#go room2
                        mixer.music.load('sound/game/run.mp3')
                        mixer.music.play()
                        mesto = 'room_2'
                        movie_statik()
                    elif x_right <= mouse[0] <= x_right+300 and y_right <= mouse[1] <= y_right+300:#go room3
                        mixer.music.load('sound/game/run.mp3')
                        mixer.music.play()
                        mesto = 'room_3'
                        movie_statik()
                    

                elif mesto == 'room_1':#комната-заглушка
                    if widch/2-338 <= mouse[0] <= widch/2-338+607 and height-101 <= mouse[1] <= height-101+101:#Если нажали на кнопку выхода в комнате 1
                        mixer.music.load('sound/game/run.mp3')
                        mixer.music.play()
                        mesto = 'holl'
                        movie_statik()

                elif mesto == 'room_2':
                    event_room2 = room_2
                    if widch/2-338 <= mouse[0] <= widch/2-338+676 and height-101 <= mouse[1] <= height-101+101:#кн. выхода комнаты 2
                        if room_Bill == 8: #если игрок уходит при аниматронике то 
                            if prognat_bill != 1: #иначе скример
                                died_from_Bill()
                        else:#иначе если аниматроник не пришёл то игнор
                            flash = 0
                            mixer.music.load('sound/game/run.mp3')
                            mixer.music.play()
                            flash = 0
                            event_room2 = room_2
                            mesto = 'holl'
                            movie_statik()
                #-----------------------------------------------------------#
                #---ФОНАРИК К2---#
                    if mesto == 'room_2':
                        if widch-358 <= mouse[0] <= widch and height-87 <= mouse[1] <= height:
                            if room_Bill == 8:
                                event_room2 = room_2_st1
                                prognat_bill = 1
                                ultra_sound.play()
                                sleep(4)
                        else:
                            if flash == 0:
                                mixer.music.load('sound/game/flash_light.mp3')
                                mixer.music.play()
                                flash = 1
                                if room_Bill == 8:
                                    event_room2 = room_2_st1
                                else:
                                    event_room2 = room_2_light
                            else:
                                flash = 0
                                mixer.music.load('sound/game/flash_light.mp3')
                                mixer.music.play()
                                event_room2 = room_2
                #---ФОНАРИК К2---#
                #-----------------------------------------------------------#

                
                elif mesto == 'room_3':
                    event_room3 = room_3
                    if widch/2-338 <= mouse[0] <= widch/2-338+676 and height-101 <= mouse[1] <= height-101+101:
                        if room_RUd == 8:
                            if flash == 1:
                                prognat_rud = 1
                                room_RUd = 1
                                point_RUd = 0
                                event_room3 = room_3_light
                                movie_RUd == True
                                point_RUd = 0
                                room_RUd = 1
                                AI_Rudi_start = threading.Thread(target=AI_croco)
                                AI_Rudi_start.start()
                            else:
                                flash = 0
                                cicle_time = False
                                movie_RUd = False
                                movie_Bill = False
                                fone_game.stop()
                                JSound()
                                died_from_RUdolphu()
                        else:
                            flash = 0
                            mixer.music.load('sound/game/run.mp3')
                            mixer.music.play()
                            mesto = 'holl'
                            movie_statik()
                            
                    #-----------------------------------------------------------#
                    #---ФОНАРИК К3---#
                    if event.type == pg.MOUSEBUTTONDOWN and mesto == 'room_3':
                        if flash == 0:
                            mixer.music.load('sound/game/flash_light.mp3')
                            mixer.music.play()
                            flash = 1
                            if room_RUd == 8:
                                event_room3 = room_3_st1
                            else:
                                event_room3 = room_3_light
                        else:
                            flash = 0
                            mixer.music.load('sound/game/flash_light.mp3')
                            mixer.music.play()
                            event_room3 = room_3
                    
                    #---ФОНАРИК К3---#
                    #-----------------------------------------------------------#

    #-------------------------------------------------------------------------------------------------------------------------------#
            if session == 'True':
                if joy == 'ACT':
                    if event.type == pg.JOYBUTTONDOWN:
                        if mesto == 'holl':
                            if joystick.get_button(2):#go room1
                                mixer.music.load('sound/game/run.mp3')
                                mixer.music.play()
                                mesto = 'room_1'
                                movie_statik()
                            elif joystick.get_button(3):#go room2
                                mixer.music.load('sound/game/run.mp3')
                                mixer.music.play()
                                mesto = 'room_2'
                                movie_statik()
                            elif joystick.get_button(1):#go room3
                                mixer.music.load('sound/game/run.mp3')
                                mixer.music.play()
                                mesto = 'room_3'
                                movie_statik()

                        #-----------------------------------------------------------#
                        #---ФОНАРИК К2---#
                        elif mesto == 'room_2':
                            if joystick.get_button(0):
                                if flash == 0:
                                    mixer.music.load('sound/game/flash_light.mp3')
                                    mixer.music.play()
                                    flash = 1
                                    if prognat_bill == 0 and room_Bill == 8:
                                        event_room2 = room_2_st1
                                    else:
                                        event_room2 = room_2_light
                                else:
                                    flash = 0
                                    mixer.music.load('sound/game/flash_light.mp3')
                                    mixer.music.play()
                                    event_room2 = room_2
                        #---ФОНАРИК К2---#
                        #-----------------------------------------------------------#
                        elif mesto == 'room_3':
                            if joystick.get_button(0):
                                if flash == 0:
                                    mixer.music.load('sound/game/flash_light.mp3')
                                    mixer.music.play()
                                    flash = 1
                                    if room_RUd == 8:
                                        event_room3 = room_3_st1
                                    else:
                                        event_room3 = room_3_light
                                else:
                                    flash = 0
                                    mixer.music.load('sound/game/flash_light.mp3')
                                    mixer.music.play()
                                    event_room3 = room_3
                            #-----------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------------------------------#
        
        if bill_lv == 1:
            bill_lv = 0
            room_Bill = 1
            point_Bill = 0
            movie_Bill == True
            prognat_bill = 0
            AI_Billy_starter = threading.Thread(target=AI_Billy)
            AI_Billy_starter.start()
        
        if rud_lv == 1:
            rud_lv = 0
            room_RUd = 1
            point_RUd = 0
            movie_RUd = True
            prognat_rud = 0
            AI_Rudi_start = threading.Thread(target=AI_croco)
            AI_Rudi_start.start()

        if mesto == 'office':
            if ch_player >= 0 and ch_player <= 42:
                win.blit(office12,(0,0))
                fone_event = office12
            elif ch_player >= 42 and ch_player <= 84:
                win.blit(office1,(0,0))
                fone_event = office1
            elif ch_player >= 84 and ch_player <= 126:
                win.blit(office2,(0,0))
                fone_event = office2
            elif ch_player >= 126 and ch_player <= 168:
                win.blit(office3,(0,0))
                fone_event =  office3
            elif ch_player >= 168 and ch_player <= 210:
                win.blit(office4,(0,0))
                fone_event = office4
            elif ch_player >= 210 and ch_player <= 252:
                win.blit(office5,(0,0))
                fone_event = office5
            elif ch_player >= 252 and ch_player <= 294:
                win.blit(office6,(0,0))
                fone_event = office6
            elif ch_player >= 294 and ch_player <= 336:
                win.blit(office7,(0,0))
                fone_event = office7

            win.blit(bleft,(0,height/2-338))
            pos = text.render(f'Воздух: {kislorod}%',1, (250,250,250))
            win.blit(pos,(5,5))

        elif mesto == 'holl':
            flash = 0
            win.blit(event_holl,(0,0))
            win.blit(bright,(widch-101,height/2-338))
            fone_event = hollN

        elif mesto == 'room_1':
            win.blit(room_1,(0,0))
            win.blit(bdown,(widch/2-338, height-101))
            fone_event = room_1

        elif mesto == 'room_2':
            win.blit(event_room2,(0,0))
            win.blit(bdown,(widch/2-338, height-101))   
            win.blit(break_bill,(widch/2-338+338+358, height-101))
            fone_event = event_room2

        elif mesto == 'room_3':
            win.blit(event_room3,(0,0))
            win.blit(bdown,(widch/2-338, height-101))
            fone_event = event_room3



        if win_player == 1:
            movie_RUd = False
            movie_Bill = False
            cicle_game = False
            fone_game.stop()
            succes = open('data_user\succes.txt', 'w')
            succes.write('true')
            succes.close()
            import player_succes_one as ps
            ps.succes()

        if att == 1:
            att = 0
            atta = threading.Thread(target=attention)
            atta.start()

        if Ratt == 1:
            Ratt = 0
            attaR = threading.Thread(target=attention_croco)
            attaR.start()

        if kill_playerB == 1:
            died_from_Bill()

        if kill_playerR == 1:
            died_from_RUdolphu()
        keys.klava()

        pg.display.flip()

game_play()