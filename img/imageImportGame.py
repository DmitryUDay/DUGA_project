import pygame as pg
from pygame import mixer 
mixer.init()

sX = open('data_user\data_file_game\widch.txt', 'r')
widch = int(sX.read())
sX = open('data_user\data_file_game\height.txt', 'r')
height = int(sX.read())


# widch = 1024
# height = 600


###---SOUND---###
flashLight = mixer.Sound('sound/game/flash_light.mp3')
runTO = mixer.Sound('sound/game/run.mp3')
seats = mixer.Sound('sound\game\seatdoWN.mp3')
jumper = mixer.Sound('sound\game\jump_scare.mp3')
PCq = mixer.Sound('sound\game\PCshee.mp3')

foneGOOL = mixer.Sound('sound/game/fone.mp3')
pshh = mixer.Sound('sound\game_over\shhhhhhhhhh.mp3')
stat = mixer.Sound('sound\game_over\static.mp3')


ARR = mixer.Sound('sound/game/right_Rudolhu.mp3')
ARL = mixer.Sound('sound/game/left_RUdolphu.mp3')
ARC = mixer.Sound('sound/game/in_roorm_RUdolphu.mp3')
BillCnock = mixer.Sound('sound\game\in_window.mp3')
peaceBill = mixer.Sound('sound\game\peace.mp3')
###---SOUND---###


#--OFFICE---#
office12 = pg.image.load('img\game\office_12.png') # Оффис
office12 = pg.transform.scale(office12,(widch,height))
officeOn = pg.image.load('img\game\officeOffMoni.png') # Оффис
officeOn = pg.transform.scale(officeOn,(widch,height))
#--OFFICE---#

#---HOLL---#
hollN = pg.image.load('img/game/night_holl.png') # Ночной холл
hollN = pg.transform.scale(hollN,(widch,height))
#---HOLL---#

#--MOVIE_STATIK--#
stm1 = pg.image.load('img/temnenie/1.png')
stm1 = pg.transform.scale(stm1,(widch,height))
stm2 = pg.image.load('img/temnenie/2.png')
stm2 = pg.transform.scale(stm2,(widch,height))
stm3 = pg.image.load('img/temnenie/3.png')
stm3 = pg.transform.scale(stm3,(widch,height))
stm4 = pg.image.load('img/temnenie/4.png')
stm4 = pg.transform.scale(stm4,(widch,height))
stm5 = pg.image.load('img/temnenie/5.png')
stm5 = pg.transform.scale(stm5,(widch,height))
stm6 = pg.image.load('img/temnenie/6.png')
stm6 = pg.transform.scale(stm6,(widch,height))
stm7 = pg.image.load('img/temnenie/7.png')
stm7 = pg.transform.scale(stm7,(widch,height))
stm8 = pg.image.load('img/temnenie/8.png')
stm8 = pg.transform.scale(stm8,(widch,height))
#--MOVIE_STATIK--#

#--ROOM-1--#
room_1 = pg.image.load('img/game/room_1.jpg') # комната 1
room_1 = pg.transform.scale(room_1,(widch,height))
#--ROOM-1--#



#--ROOM-2--#
room_2 = pg.image.load('img/game/room_2.png') # комната 2
room_2 = pg.transform.scale(room_2,(widch,height))
room_2_light = pg.image.load('img/game/flash_light_room_2.png') # Свет комнаты 2
room_2_light = pg.transform.scale(room_2_light,(widch,height))
room_2_st1 = pg.image.load('img\game\Billy_st1.png') # комната 2 билли стадия 1
room_2_st1 = pg.transform.scale(room_2_st1,(widch,height))
#--ROOM-2--#



#--ROOM-3--#
room_3 = pg.image.load('img/game/room_3.png') # комната 3
room_3 = pg.transform.scale(room_3,(widch,height))
room_3_light = pg.image.load('img/game/flash_light_room_3.png') # свет комнаты 3
room_3_light = pg.transform.scale(room_3_light,(widch,height))
room_3_st1 = pg.image.load('img\game\RUdolphu_st1.png') # комната 3 РУдольф стадия 1
room_3_st1 = pg.transform.scale(room_3_st1,(widch,height))
#--ROOM-3--#

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

#TEMNENIE-EFFECT#
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
#TEMNENIE-EFFECT#


#STATIK#
stm1 = pg.image.load('img\game\statik\statik_1.jpg')
stm1 = pg.transform.scale(stm1,(widch,height))

stm2 = pg.image.load('img\game\statik\statik_2.jpg')
stm2 = pg.transform.scale(stm2,(widch,height))

stm3 = pg.image.load('img\game\statik\statik_3.jpg')
stm3 = pg.transform.scale(stm3,(widch,height))

stm4 = pg.image.load('img\game\statik\statik_4.jpg')
stm4 = pg.transform.scale(stm4,(widch,height))

stm5 = pg.image.load('img\game\statik\statik_5.jpg')
stm5 = pg.transform.scale(stm5,(widch,height))

stm6 = pg.image.load('img\game\statik\statik_6.jpg')
stm6 = pg.transform.scale(stm6,(widch,height))

stm7 = pg.image.load('img\game\statik\statik_7.jpg')
stm7 = pg.transform.scale(stm7,(widch,height))

stm8 = pg.image.load('img\game\statik\statik_8.jpg')
stm8 = pg.transform.scale(stm8,(widch,height))
#STATIK#



#STATIK#
stm1l = pg.image.load('img/game/statik_mov/1.png')
stm1l = pg.transform.scale(stm1l,(widch,height))

stm2l = pg.image.load('img/game/statik_mov/2.png')
stm2l = pg.transform.scale(stm2l,(widch,height))

stm3l = pg.image.load('img/game/statik_mov/3.png')
stm3l = pg.transform.scale(stm3l,(widch,height))

stm4l = pg.image.load('img/game/statik_mov/4.png')
stm4l = pg.transform.scale(stm4l,(widch,height))

stm5l = pg.image.load('img/game/statik_mov/5.png')
stm5l = pg.transform.scale(stm5l,(widch,height))

stm6l = pg.image.load('img/game/statik_mov/6.png')
stm6l = pg.transform.scale(stm6l,(widch,height))

stm7l = pg.image.load('img/game/statik_mov/7.png')
stm7l = pg.transform.scale(stm7l,(widch,height))

stm8l = pg.image.load('img/game/statik_mov/8.png')
stm8l = pg.transform.scale(stm8l,(widch,height))
#STATIK#