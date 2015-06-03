##Escape from the Ronin ii
##Johnathan Hinebrook
##12-16-14
##Python 3.X 
##Pygame 1.9.2


import pygame,sys,random,time,os
from pygame.locals import *

pygame.init()

###############################################################
#
#Globals
#
###############################################################
sWIDTH = 800
sHEIGHT = 600
window = pygame.display.set_mode((sWIDTH,sHEIGHT))
pygame.display.set_caption("Escape From the Ronin II | Johnathan Hinebrook")
clock = pygame.time.Clock()
Name = 'Takeo'
key = 0        #Main varible runs tuought script should start at zero
tx = 60
ty = 420
spc = 0
m = 0
x = 611
nulname = 1
playerName='John'
mobname='???'
px = 568
py = 487
plhp = 4
vohp = 4
mob1hp = 4                    #hp defalt is 4
mob2hp = 4
mobSeed = 1
CurrentImage = 1
mobName = "Salvager"
mobspawntoken = random.randint(1,3)
mobposx1 = 159
mobposy1 = 313
mobposx2 = 90 
mobposy2 = 286
music = pygame.mixer.Sound("media/sounds/bkmusic/ffvii.wav")
fanfare = pygame.mixer.Sound("media/sounds/bkmusic/fanfare.wav")
hello = pygame.mixer.Sound("media/sounds/soundsvofa/Hello.wav")
eh = pygame.mixer.Sound("media/sounds/soundsvofa/eh.wav")

turn = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (151,151,151,8)
tmp = 0
y = 185

###############################################################
#
#tuples,lists,and Dicts
#
###############################################################



dicttext = {0: "media/img/text/smp0.png",
            1: "media/img/text/smp1.png",
            2:"media/img/text/smp2.png",
            3:"media/img/text/smp3.png",
            4:"media/img/text/smp4.png",
            5:"media/img/text/smp5.png",
            6:"media/img/text/smp6.png",
            7:"media/img/text/smp7.png",
            8:"media/img/text/smp8.png",
            9:"media/img/text/smp9.png",
            10:"media/img/text/smp10.png",
            11:"media/img/text/smp11.png",
            12:"media/img/text/smp12.png",
            13:"media/img/text/smp13.png",
            14:"media/img/text/smp14.png"}

dictguihp = {0: "media/img/Battle/hp0.png",
             1: "media/img/Battle/hp1.png",
             2: "media/img/Battle/hp2.png",
             3: "media/img/Battle/hp3.png",
             4:"media/img/Battle/hp4.png"}

dictPlayer = {1: "media/img/Battle/walk1.png",
              2: "media/img/Battle/walk2.png",
              3: "media/img/Battle/walk3.png",
              4:"media/img/Battle/walk4.png",
              5:"media/img/Battle/walk5.png",
              6:"media/img/Battle/walk6.png",
              7:"media/img/Battle/walk7.png",
              8:"media/img/Battle/walk8.png",
              9:"media/img/Battle/walk9.png"}

dictPlayers = {1: "media/img/Battle/swalk1.png",
              2: "media/img/Battle/swalk2.png",
              3: "media/img/Battle/swalk3.png",
              4:"media/img/Battle/swalk4.png",
              5:"media/img/Battle/swalk5.png",
              6:"media/img/Battle/swalk6.png",
              7:"media/img/Battle/swalk7.png",
              8:"media/img/Battle/swalk8.png",
              9:"media/img/Battle/swalk9.png"}


dictVofa = {1: "media/img/Battle/vwalk1.png",
            2: "media/img/Battle/vwalk2.png",
            3: "media/img/Battle/vwalk3.png",
            4:"media/img/Battle/vwalk4.png",
            5:"media/img/Battle/vwalk5.png",
            6:"media/img/Battle/vwalk6.png",
            7:"media/img/Battle/vwalk7.png",
            8:"media/img/Battle/vwalk8.png",
            9:"media/img/Battle/vwalk9.png"}

mob1avi = {1: "media/img/Battle/loot1.png",
              2: "media/img/Battle/loot2.png",
              3: "media/img/Battle/loot3.png",
              4:"media/img/Battle/loot4.png",
              5:"media/img/Battle/loot1.png",
              6:"media/img/Battle/loot2.png",
              7:"media/img/Battle/loot3.png",
              8:"media/img/Battle/loot4.png",
              9:"media/img/Battle/loot4.png"}

mob2avi = {1: "media/img/Battle/mage1.png",
              2: "media/img/Battle/mage2.png",
              3: "media/img/Battle/mage3.png",
              4:"media/img/Battle/mage4.png",
              5:"media/img/Battle/mage1.png",
              6:"media/img/Battle/mage2.png",
              7:"media/img/Battle/mage3.png",
              8:"media/img/Battle/mage4.png",
              9:"media/img/Battle/mage4.png"}

mob3avi = {1: "media/img/Battle/as1.png",
              2: "media/img/Battle/as2.png",
              3: "media/img/Battle/as3.png",
              4:"media/img/Battle/as4.png",
              5:"media/img/Battle/as1.png",
              6:"media/img/Battle/as2.png",
              7:"media/img/Battle/as3.png",
              8:"media/img/Battle/as4.png",
              9:"media/img/Battle/as4.png"}



###############################################################
#
#Classes
#
###############################################################



class hpgui(object):
    def hphphp(cur4,FileLocation,x,y):
        hp4 = pygame.image.load(FileLocation[4])
        hp3 = pygame.image.load(FileLocation[3])
        hp2 = pygame.image.load(FileLocation[2])
        hp1 = pygame.image.load(FileLocation[1])
        hp0 = pygame.image.load(FileLocation[0])
        if cur4 > 4:
            cur4 = 4
        if cur4 == 4:
            m1 = hp4
        if cur4 == 3:
            m1 = hp3
        if cur4 == 2:
            m1 = hp2
        if cur4 == 1:
            m1 = hp1
        if cur4 ==0:
            m1 = hp0
        window.blit(m1, (x,y))
        
class textbox(object):
    def box(txt,FONTSIZE,txtcolor,boxColor,posx,posy):
        basicFont = pygame.font.SysFont(None, FONTSIZE)
        text = basicFont.render(txt, True, txtcolor, boxColor)
        textRect = text.get_rect()
        textRect.centerx = posx
        textRect.centery = posy
        window.blit(text, textRect)

class mob(object):
    def animat(FileLocation,AviLocX,AviLocY):
        global CurrentImage

        m1 = pygame.image.load(FileLocation[1])
        m2 = pygame.image.load(FileLocation[2])
        m3 = pygame.image.load(FileLocation[3])
        m4 = pygame.image.load(FileLocation[4])
        m5 = pygame.image.load(FileLocation[5])
        m6 = pygame.image.load(FileLocation[6])
        m7 = pygame.image.load(FileLocation[7])
        m8 = pygame.image.load(FileLocation[8])
        m9 = pygame.image.load(FileLocation[9])       
        if (CurrentImage==1):
            window.blit(m1, (AviLocX,AviLocY))           
        if (CurrentImage==2):
            window.blit(m2, (AviLocX,AviLocY))
            CurrentImage=2
        if (CurrentImage==3):
            window.blit(m3, (AviLocX,AviLocY))
            CurrentImage=3
        if (CurrentImage==4):
            window.blit(m4, (AviLocX,AviLocY))
            CurrentImage=4
        if (CurrentImage==5):
            window.blit(m5, (AviLocX,AviLocY))
            CurrentImage=5
        if (CurrentImage==6):
            window.blit(m6, (AviLocX,AviLocY))
            CurrentImage=6
        if (CurrentImage==7):
            window.blit(m7, (AviLocX,AviLocY))
            CurrentImage=7
        if (CurrentImage==8):
            window.blit(m8, (AviLocX,AviLocY))
            CurrentImage=8
        if (CurrentImage==9):
            window.blit(m9, (AviLocX,AviLocY))
            CurrentImage=1        
        else:
            CurrentImage+=1; #adds 1 to counter




class IMGLOAD():
    def avi(v,x,y):
        #Loads a avi. mainly used for bliting vofa
        vofa = pygame.image.load(v)
        window.blit(vofa,(x, y))    #good defalt is 100*90

    def BAK(ImageTobeUsed):
        #loads  jpg/png as background and blits to 0,0
        b1 = pygame.image.load(ImageTobeUsed)
        background = pygame.transform.scale(b1,( sWIDTH, sHEIGHT))
        window.blit(background,(0,0))



class formatin():
    def textBox(w,h,t,c,tx,ty):
        s = pygame.Surface((w, h))    # the size of the box 700x150
        s.set_alpha(t)                # alpha level  185
        s.fill(c)                     # this fills the entire surface
        window.blit(s, (tx, ty,))     # (0,0) are the top-left coordinates

    def nameBox(txt,tx,ty,sz):

        basicFont = pygame.font.SysFont(None, sz)
        text = basicFont.render(txt, True, WHITE,)
        textRect = text.get_rect()
        textRect.centerx = tx + 45
        textRect.centery = ty -20
        window.blit(text, textRect)
    def YouWon(txt,tx,ty,sz):
        global m,plhp

        basicFont = pygame.font.SysFont(None, sz)
        text = basicFont.render(txt, True, BLACK,WHITE)
        textRect = text.get_rect()
        textRect.centerx = tx + 45
        textRect.centery = ty -20
        window.blit(text, textRect)
        m = 0
        plhp = 4

def battle():
    global Name
    Name = 'Takeo'
    playera = mob.animat(dictPlayer,576, 312)
    volfaa = mob.animat(dictVofa,675, 294)
    if mob1hp >0:
        mobin = mob.animat(dictgoblen,mobposx1,mobposy1)
    if mob2hp >0:
        mobin2 = mob.animat(dictgoblen,mobposx2,mobposy2)
###########GUI
    #                     txt  fsz txc   bc  x   y    
    plnmGUI = textbox.box(Name,34,BLACK,RED,728, 497)
    Player_hp = hpgui.hphphp(plhp,dictguihp,px,py)
    vonmGUI = textbox.box('Vofa',34,BLACK,RED,728, 540)
    Vofa_hp = hpgui.hphphp(vohp,dictguihp,568, 540)
    Mob_name1 =  textbox.box(mobName,34,BLACK,RED,72, 487)
    Mob_name2 = textbox.box(mobName,34,BLACK,RED,72, 540)
    
    Mob1_hp = hpgui.hphphp(mob1hp,dictguihp,125, 487)
    Mob2_hp = hpgui.hphphp(mob2hp,dictguihp,125, 540)
    
    AtkGUI = textbox.box('Attack(A)',34,BLACK,RED,335,495)
    HeaGUI = textbox.box('Heal(S)',34,BLACK,RED,335,550)
    DefGUI = textbox.box('Defend(D)',34,BLACK,RED,455,495)
    FinGUI = textbox.box('Final(F)',34,BLACK,RED,455,550)


    BattleTurn()


def BattleKeepAlive():
    if mob2hp <= 0:       
        music.stop()
        fanfare.play()
        global key
        k = key
        key = k + 1

        


def box():
    global tx,ty,GRAY,Name
##                width,height,opacity,color,x,y  
    formatin.textBox(150,40,185,GRAY,tx,ty -45)    
    formatin.textBox(700,150,185,GRAY,tx,ty)
    formatin.nameBox(Name,tx+15,ty+1,48)


def fullbox():
    global tx,ty,GRAY,Name
##                width,height,opacity,color,x,y  
    formatin.textBox(700,550,220,GRAY,tx,ty- 400)

def keyup():
    global key
    k = key
    key = k + 1
##    print(key)



        

def musica():
    global m
    if m == 0:
        music.play(loops=-1)
        m = 1


def ATK(NUL):
    DAM = random.randint(1,3)
    global turn
    if NUL == 1:
        slash = pygame.image.load(r"media\img\Battle\slash1.png")
        window.blit(slash,(mobposx1,mobposy1))
        pygame.display.flip()
        time.sleep(0.5)
        global mob1hp
        hp = mob1hp
        nhp = hp - DAM
        if nhp < 0 :
            nhp = 0
        mob1hp = nhp
       
        t = turn
        turn = t + 1
        
    if NUL == 2:
        slash = pygame.image.load(r"media\img\Battle\slash1.png")
        window.blit(slash,(mobposx2,mobposy2))
        pygame.display.flip()
        time.sleep(0.5)
        global mob2hp
        hp = mob2hp
        nhp = hp - DAM
        if nhp < 0 :
            nhp = 0
        mob2hp = nhp
        
        t = turn
        turn = t + 1

    if NUL == 3:
        nDAM = 1
        slash = pygame.image.load(r"media\img\Battle\slash1.png")
        window.blit(slash,(576, 312))
        pygame.display.flip()
        time.sleep(0.5)
        global plhp
        hp = plhp
        nhp = hp - nDAM
        if nhp < 0 :
            nhp = 0
        plhp = nhp         
    
def DEF():
    global plhp
    hp = plhp
    plhp = hp + 1
    global turn
    t = turn
    turn = t + 1

def HEAL():
    global plhp
    slash = pygame.image.load(r"media\img\Battle\heal.png")
    window.blit(slash,(576, 312))
    pygame.display.flip()
    time.sleep(0.5)
    h = random.randint(1,2)
    hp = plhp
    if hp > 4:
        hp = 4
    plhp = hp + h
    global turn
    t = turn
    turn = t + 1
    
def FINAL():
    global mob1hp,mob2hp
    if mob1hp and mob2hp <=2:
        mob1hp = 0
        mob2hp = 0
    global turn
    t = turn
    turn = t + 1

    
def arrow(x,y):
    IMGLOAD.avi(r"media\img\Battle\arrow.png",x,y)
    pygame.display.flip()

    
def fight_restart():
    global mob1hp,mob2hp
    mob1hp = 4
    mob2hp = 4
    
def BattleTurn():
    global turn

    if turn == 1:
        #Player Turn
        global plhp
        arrow(595, 233)
        
    if turn == 2:
        #Vofas turn
        arrow(708, 233)
        time.sleep(.03)
        global plhp,mob1hp,mob2hp
        if plhp <3:
            HEAL()
        if mob1hp > 0:
            ATK(1)
        if mob1hp < 0:
            ATK(2)
        t = turn
        turn = t + 1
        
    if turn == 3:
        #mobTurn
        arrow(190, 233)
        ATK(3)
        time.sleep(.03)
        t = turn
        turn = t + 1
        
        
    if turn == 4:
        #mobTurn
        arrow(190, 233)
        ATK(3)
        time.sleep(.03)
##        print("PASS")
        t = turn
        turn = t + 1
    if turn > 4:
        turn = 1


def mobcheck():
    global key,dictgoblen
    k = key
    if k == 9:
        dictgoblen = mob1avi
    if k == 18:
        dictgoblen = mob1avi
    if k == 22:
        dictgoblen = mob2avi
    if k == 25:
        dictgoblen = mob2avi
    if k == 28:
        dictgoblen = mob3avi
    


class TextWalker(object):
    def text(key,FileLocation,tx,ty):

        global Name,sWIDTH, sHEIGHT,x,y

        hp0 = pygame.image.load(FileLocation[0])
        hp1 = pygame.image.load(FileLocation[1])
        hp2 = pygame.image.load(FileLocation[2])
        hp3 = pygame.image.load(FileLocation[3])
        hp4 = pygame.image.load(FileLocation[4])
        hp5 = pygame.image.load(FileLocation[5])
        hp6 = pygame.image.load(FileLocation[6])
        hp7 = pygame.image.load(FileLocation[7])
        hp8 = pygame.image.load(FileLocation[8])
        hp9 = pygame.image.load(FileLocation[9])
        hp10 = pygame.image.load(FileLocation[10])
        hp11 = pygame.image.load(FileLocation[11])
        hp12 = pygame.image.load(FileLocation[12])
        hp13 = pygame.image.load(FileLocation[13])
        hp14 = pygame.image.load(FileLocation[14])
##


        if key < 0:
            IMGLOAD.BAK(r"media\img\bk\Error0.png") #r means raw string for file path. its is used so I dont get error



        if key == 0:
            
            
            IMGLOAD.BAK(r"media\img\bk\spaceport.png")
            formatin.textBox(700,150,185,GRAY,tx,ty)
            m1 = hp0
            window.blit(m1,(60,420))
            


        if key == 1:
           IMGLOAD.BAK(r"media\img\bk\spaceport.png")
           fullbox()
           m1 = hp1
           window.blit(m1,(60,12))
            
            

        if key == 2:
            Name = 'Takeo'
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg") 
            box()
            m1 = hp2
            window.blit(m1,(60,420))               

        if key == 3:
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            box()
            m1 = hp3
            window.blit(m1,(60,420))

        if key == 4:
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            box()
            m1 = hp4
            window.blit(m1,(60,420))
            
        if key == 5:
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            box()
            m1 = hp5
            window.blit(m1,(60,420))
            
        if key == 6:
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            box()
            m1 = hp6
            window.blit(m1,(60,420))
            
        if key == 7:
            t= 0.08
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",700,90)
            box()
            pygame.display.flip()
            time.sleep(t)
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",400,90)
            box()
            pygame.display.flip()
            time.sleep(t)
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            box()
            keyup()
            global j
            j = 0


        if key == 8:
            global j
            if j == 0:
                hello.play(loops=0)
                j = 1
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            Name = "Vofa"
            box()
            m1 = hp7
            window.blit(m1,(60,420))


        if key == 9:
            global j
            j = 0
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_mad.png",100,90)
            box()
            m1 = hp8
            window.blit(m1,(60,420))

        if key == 10:
            tmp = 0
            musica()
            IMGLOAD.BAK(r"media\img\Battle\fight.jpg")
            battle()
            BattleKeepAlive()

        if key == 11:
            formatin.YouWon("You Won!",400,100,120)
            formatin.YouWon("You Earned 30 XP!!!",550,150,20)
            formatin.YouWon("Spacebar to Advance",550,165,20)
            fight_restart()

        if key == 12:
            IMGLOAD.BAK(r"media\img\bk\bedroom.jpg")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            box()
            m1 = hp9
            window.blit(m1,(60,420))

        if key == 13:
            IMGLOAD.BAK(r"media\img\bk\Ronin.png")

        if key == 14:
            IMGLOAD.BAK(r"media\img\bk\hall.png")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            box()
            m1 = hp10
            window.blit(m1,(60,420))

        if key == 15:
            IMGLOAD.BAK(r"media\img\bk\Ronin.png")
        if key == 16:
            IMGLOAD.BAK(r"media\img\bk\Roninshot.png")
        if key == 17:
            IMGLOAD.BAK(r"media\img\bk\Roninhole.png")


        if key == 18:
            IMGLOAD.BAK(r"media\img\bk\hall.png")
            global j
            if j == 0:
                eh.play(loops=0)
                j = 1
            IMGLOAD.avi(r"media\img\sprite\i_surprised.png",100,90)
            box()
            m1 = hp11
            window.blit(m1,(60,420))


        if key == 19:
            global j
            j = 0
            tmp = 0
            musica()
            IMGLOAD.BAK(r"media\img\Battle\fight.jpg")
            battle()
            BattleKeepAlive()

        if key == 20:
            formatin.YouWon("You Won!",400,100,120)
            formatin.YouWon("You Earned 30 XP!!!",550,150,20)
            formatin.YouWon("Spacebar to Advance",550,165,20)
            fight_restart()

        if key == 21:
            IMGLOAD.BAK(r"media\img\bk\hall.png")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            box()
            m1 = hp12
            window.blit(m1,(60,420))

        if key == 22:
            IMGLOAD.BAK(r"media\img\bk\map.png")
                 
            playera = mob.animat(dictPlayers,x, y)  
            y = 305
            playera = mob.animat(dictPlayers,x, y)


        if key == 23:
            tmp = 0
            musica()
            IMGLOAD.BAK(r"media\img\Battle\fight1.jpg")
            battle()
            BattleKeepAlive()

        if key == 24:
            formatin.YouWon("You Won!",400,100,120)
            formatin.YouWon("You Earned 30 XP!!!",550,150,20)
            formatin.YouWon("Spacebar to Advance",550,165,20)
            fight_restart()

        if key == 25:
            IMGLOAD.BAK(r"media\img\bk\map.png")
                
            x = 426
            y = 325
            playera = mob.animat(dictPlayers,x, y)
            keyup()

        if key == 26:
            tmp = 0
            musica()
            IMGLOAD.BAK(r"media\img\Battle\fight2.jpg")
            battle()
            BattleKeepAlive()        
            
            
        if key == 27:
            formatin.YouWon("You Won!",400,100,120)
            formatin.YouWon("You Earned 30 XP!!!",550,150,20)
            formatin.YouWon("Spacebar to Advance",550,165,20)
            fight_restart()
        
        if key == 28:
            IMGLOAD.BAK(r"media\img\bk\map.png")
                
            x = 270
            y = 318
            playera = mob.animat(dictPlayers,x, y)



        if key == 29:
            IMGLOAD.BAK(r"media\img\bk\hall.png")
            IMGLOAD.avi(r"media\img\sprite\i_happy.png",100,90)
            box()
            m1 = hp13
            window.blit(m1,(60,420))

        if key == 30:
            IMGLOAD.BAK(r"media\img\bk\2.png")


        if key == 31:
            IMGLOAD.BAK(r"media\img\bk\3.png")


        if key == 32:
            IMGLOAD.BAK(r"media\img\bk\4.png")

        if key == 33:
            IMGLOAD.BAK(r"media\img\bk\5.png")


        if key ==  34:
            IMGLOAD.BAK(r"media\img\bk\5.png")
            fullbox()
            m1 = hp14
            window.blit(m1,(60,12))

        if key > 34:
            key = 34

##############################################################################
     


def skrp():    #More/less my main. runs the class wath changes seens
    mobcheck()
    TextWalker.text(key,dicttext,tx,ty)




##    All key bindings are stored here
##    V     Link to doc on keybinding      V
##    http://www.pygame.org/docs/ref/key.html
##
def controlbindings():
        global key
##        print(event)
        if (event.type==pygame.QUIT):                 #red x button
            gameLoop=False
            pygame.quit()
            sys.exit()
            
        if event.type == KEYUP:                       #when key is released
            if event.key == K_BACKQUOTE :             #   ` quit game (my Esc key is broken)
                gameLoop=False
                pygame.quit()
                sys.exit()
            if event.key == K_u :
                print(notice)
            if event.key == K_s:
                HEAL()

            if event.key == K_o:
                window = pygame.display.set_mode((sWIDTH,sHEIGHT),pygame.FULLSCREEN)   #fullscreen mode

            if event.key ==  K_p:
                window = pygame.display.set_mode((sWIDTH,sHEIGHT))   #Org res mode
            if event.key == K_SPACE:
##                print(key)
                k = key
                nk = k + 1
                key = nk
##                print(key)
                global spc
                tmpvar = spc + 1
                spc = tmpvar
##                print(spc)

            if event.key == K_a:
                if mob1hp > 0:
                    ATK(1)
                if mob1hp == 0:
                    ATK(2)
            if event.key == K_m:
                    ATK(3)
            if event.key == K_8:
                    key = 1


            if event.key == K_b:
                k = key
                nk = k - 1
                if nk <= 0:
                    nk = 0
                key = nk
    
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()
                
            if event.key == K_f :
                FINAL()

                
            if event.key == K_y :
                n = vohp - 1
                vohp = n
                if vohp <=0:
                    n = vohp + 4
                    vohp = n



def main():
    global event,x,y
    gameLoop=True
    while gameLoop:
        notice ='key has been pressed'
        for event in pygame.event.get():
            controlbindings()
        skrp()       
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()




main()





















            
