import pygame, sys, random, os
from pygame.locals import *
from pygame import surface
from math import fabs
from time import sleep
mute = True#False
speed = 7
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((1024, 768))#, RESIZABLE)
pygame.display.set_caption("Jetpack Joyride")
try:
    pygame.display.set_icon(pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/icon.png"))
except Exception as x:
    input(x)
width= 1024
height = 768
score = 0
global ralt, lalt, f4
ralt, lalt, f4 = 0, 0, 0

def crop(surface, rect):
    cropped = pygame.Surface((rect.width, rect.height))
    cropped.blit(surface, (-(rect.x), -(rect.y)))
    return cropped  

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def FinalSpin():

    global money, die,spintokens, stevey, invincible, mute
    global speed
    pygame.font.init()
    if not mute:
        pygame.mixer.init()
        spinningsound= pygame.mixer.Sound(os.path.dirname(sys.argv[0])+"/Img1/spin/spinning.wav")
        waitingsound=[False, 0]
        winsound= pygame.mixer.Sound(os.path.dirname(sys.argv[0])+"/Img1/spin/win.wav")
        stopsound= pygame.mixer.Sound(os.path.dirname(sys.argv[0])+"/Img1/spin/stop.wav")
        stopsound.set_volume(.3)
    spinsleft=pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\spins left.png")
    Font=pygame.font.Font(os.path.dirname(sys.argv[0])+"/Img1/New Athletic M54.ttf", 65)
    startleverpos=[816, 221]
    screen = pygame.display.set_mode((1024, 768))#, pygame.FULLSCREEN)
    pygame.display.set_caption("Jetpack Joyride")
    finalspin = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/final spin blank.png")
    finalspin.convert_alpha()
    lever=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/spin/spin lever.png")
    leverbgframe=0
    leverbg=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/spin/lever bg"+str(leverbgframe)+".png")

    behind=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
    behind.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))
    behind.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/final spin behind.png"), (0, 0))
    cuttouts=[crop(behind, pygame.Rect(33, 612, 717, 120)), crop(behind, pygame.Rect(26, 115, 717, 131)), crop(behind, pygame.Rect(768, 222, 208, 102))]
    cuttoutcoors=[[36, 612], [26, 115], [768, 222]]
    end = False
    ralt, lalt, f4=0, 0, 0
    mouseDown=False
    amountpull=0
    leverpos=list(startleverpos)
    extra=[0, 0]
    stop=False
    prizecoor=[]
    for i in [160, 403, 642]:
        for l in [254, 254+118, 254+118+118]:
            prizecoor.append([i, l])
    leverbg=[]
    for i in range(3):
            leverbg.append(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/spin/lever bg"+str(i)+".png"))
    prizes=[]
    prizesurf=[]
    prizesurfn=[r"Img1\spin\3 spin tokens.png", r"Img1\spin\1 coin.png", r"Img1\spin\heart.png", r"Img1\spin\3 coins.png", r"Img1\spin\stack of coins.png"]#, r"Img1\spin\double coins.png", r"Img1\spin\speed.png"]
#    prizesurfn=[r"Img1\spin\speed.png"]
    for i in prizesurfn:
        i = prizesurf.append(pygame.image.load(os.path.dirname(sys.argv[0])+"/"+i))

    prizenames=[]
    for i in range(9):
        prizenames.append(random.choice(prizesurfn))
        prizes.append(pygame.image.load(os.path.dirname(sys.argv[0])+"/"+prizenames[-1]))

    spinspeed=[25, 25, 25]
    counter = pygame.time.Clock()
    fps=[]
    waitframes=50
    lastspintokens=""
    if not mute:
        spinningsound.play(loops=-1)
    lightsurface=[pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\red light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png")]
    lcy=[285, 349, 413, 479, 541]
    lcx=[773, 950]
    lightcoors=[]
    for x in lcx:
        for y in lcy:
            lightcoors.append([x, y])
    lightframes=20
    while end == False and spintokens>0:
        
        ev = pygame.event.get()
        for event in ev:
            if event.type == QUIT:
                endall()
            if event.type == KEYDOWN:
                if event.key == K_F4:
                    f4=1
                if event.key == K_RALT:
                    ralt=1
                if event.key == K_LALT:
                    lalt=1
            if event.type == KEYUP:
                if event.key == K_F4:
                    f4=0
                if event.key == K_RALT:
                    ralt=0
                if event.key == K_LALT:
                    lalt=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(768, 698, 208, 62).collidepoint(pygame.mouse.get_pos()):
                    money+=50
                    spintokens-=1
                extra=pygame.mouse.get_pos()[1]-startleverpos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                extra=0
                leverpos=list(startleverpos)
        if pygame.mouse.get_pressed()[0]:
            leverpos=[startleverpos[0], list(pygame.mouse.get_pos())[1]]
            leverpos[1]-=extra
        if leverpos[1]>=513:
            leverpos[1]=513
            if not mute:
                spinningsound.stop()
                stopsound.play()
            stop=True
        elif leverpos[1] >= 420:
            leverbgframeb=2
        elif leverpos[1] >= 334:
            leverbgframeb=1
        elif leverpos[1]<=334 and leverpos[1]>=221:
            leverbgframeb=0
        elif leverpos[1]<221:
            leverpos[1]=221
            leverbgframeb=0
        for i in range(len(prizecoor)):
            if i>=6:
                prizecoor[i][1]+=spinspeed[2]
            elif i>=3:
                prizecoor[i][1]+=spinspeed[1]
            else:
                prizecoor[i][1]+=spinspeed[0]
            if prizecoor[i][1]>608:
                hgf=1
                prizecoor[i][1]=254
                prizepickfrom=[]
                if 0 in spinspeed:
                    for d in range(len(prizecoor)):
                        if prizecoor[d][1] == 432:
                            prizepickfrom.append(prizenames[d])
                            hgf=0
                else:
                    prizenames[i]=random.choice(prizesurfn)
                if hgf:
                    prizenames[i]=random.choice(prizesurfn)
                elif random.choice([0, 0, 1]):
                    prizenames[i]=random.choice(prizepickfrom)
                else:
                    prizenames[i]=random.choice(prizesurfn)
                prizes[i]=pygame.image.load(os.path.dirname(sys.argv[0])+"/"+prizenames[i])
                
        screen.blit(behind, (0, 0))
        if spintokens!=lastspintokens:
            fontsurface=Font.render("%02d" % (spintokens), 1, (0, 0, 0))
            fontrect=fontsurface.get_rect()
            fontrect.center=(909 - 792, 153 -120)
            spinsleft=pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\spins left.png")
            spinsleft.blit(fontsurface,fontrect)
        spinsleftf = pygame.transform.scale(spinsleft, (spinsleft.get_width(), int(spinsleft.get_height()-((leverpos[1]-221)/30))))
        screen.blit(spinsleftf, (792,120+((leverpos[1]-221)/5)))
        lastspintokens=spintokens
        for i in range(9):
            rectt=prizes[i].get_rect()
            rectt.center=(prizecoor[i][0], prizecoor[i][1])
            screen.blit(prizes[i], rectt)
        for i in range(len(cuttouts)):
            screen.blit(cuttouts[i], cuttoutcoors[i])
        screen.blit(finalspin, (0, 0))
        screen.blit(leverbg[leverbgframeb], (815, 334))
        screen.blit(lever, (leverpos[0], leverpos[1]))
        lightframes-=1
        if lightframes<=0:
            lightframes=20
            lightsurface=shift(lightsurface, -1)
        for i in range(len(lightsurface)):
            screen.blit(lightsurface[i], lightcoors[i])
            screen.blit(lightsurface[i], lightcoors[i+5])
        pygame.display.update()
        if (ralt or lalt) and f4:
            endall()
        if stop :
            for i in range(len(prizecoor)):
                if prizecoor[i][1] <= 432+20 and prizecoor[i][1] >= 432-20 and random.choice([0, 0, 0, 0, 1]):
                    if i>=6:
                        spinspeed[2]=0

                    elif i>=3:
                        spinspeed[1]=0
                    else:
                        spinspeed[0]=0
                    buffer=prizecoor[i][1]-432
                    
                    if i%3==0:
                        prizecoor[i][1] -= buffer
                        prizecoor[i+1][1] -= buffer
                        prizecoor[i+2][1] -= buffer
                    if i%3==1:
                        prizecoor[i-1][1] -= buffer
                        prizecoor[i][1] -= buffer
                        prizecoor[i+1][1] -= buffer
                    if i%3==2:
                        prizecoor[i-2][1] -= buffer
                        prizecoor[i-1][1] -= buffer
                        prizecoor[i][1] -= buffer
            if spinspeed==[0, 0, 0]:
                winners=[]
                for i in range(len(prizecoor)):
                    if prizecoor[i][1]==432:
                        winners.append(prizenames[i])
                waitframes-=1
                if waitframes<=0:
                    if winners[1:] == winners[:-1]:
                        if not mute:
                            spinningsound.stop()
                        if not mute:
                            winsound.play()
                        print(winners[0])
                        if winners[0]==r"Img1\spin\3 spin tokens.png":
                            spintokens+=3
                            print("added 3 spin tokens")
                        elif winners[0]==r"Img1\spin\speed.png":
                            speed=20
                            print("sped you up!")
                        elif winners[0]==r"Img1\spin\1 coin.png":
                            money+=100
                            print("you won $100")
                        elif winners[0]==r"Img1\spin\heart.png":
                            die=False
                            end=True
                            invincible=True
                            print("you get another life!")
                        elif winners[0]==r"Img1\spin\3 coins.png":
                            money+=500
                            print("you won $500!")
                        elif winners[0]==r"Img1\spin\stack of coins.png":
                            money+=1000
                            print("YOU WON $1000!")
                        elif winners[0]==r"Img1\spin\double coins.png":
                            print("DOUBLE COINS!")
                    if not mute:
                        spinningsound.play(loops=-1)
                    spinspeed=[25, 25, 25]
                    waitframes=50
                    stop=False
                    spintokens-=1
            if spintokens<=0:
                end=True
        fps.append(counter.tick())
    if not mute:
        spinningsound.stop()
    spintokens=0
    print("the spin fps is:", round(1000/(sum(fps)/len(fps)), 3))


def firstscreen():
    global ralt, lalt, f4
    global font, distf
    first=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/first screen.png")
    hs=font.render("{:,}".format(distf), 1, (86, 113, 149))
    if hs.get_width()/90>hs.get_height()/28:
        hs=pygame.transform.scale(hs, (90, int((90/hs.get_width())*hs.get_height())))
    else:
        hs=pygame.transform.scale(hs, (int((28/hs.get_height())*hs.get_width()), 28))
       
    first.blit(hs, (860-(hs.get_width()/2), 530-(hs.get_height()/2)))
    end=1
    while end:
        
        screen.blit(first, (0, 0))
        ev = pygame.event.get()
        for event in ev:
                
            if event.type == KEYDOWN:
                if event.key == K_F4:
                    f4=1
                if event.key == K_RALT:
                    ralt=1
                if event.key == K_LALT:
                    lalt=1
            if event.type == KEYUP:
                if event.key == K_F4:
                    f4=0
                if event.key == K_RALT:
                    ralt=0
                if event.key == K_LALT:
                    lalt=0
       
            if event.type == QUIT:
                endall()
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                end=0
        pygame.display.update()
        if (ralt or lalt) and f4:
            endall()
def outlineit(x, y, outline, size, string, font, color, most):
    global verysmallfont
    x0 = 0
    y0 = 0
    for i in string:
        if i == "m":
            font = verysmallfont
            x = 115
            y += 18
        if i !=" ":
            insideObj = font.render(i, 1, color)
            outsideObj = font.render(i, 1, (0, 0, 0))
            
            screen.blit(outsideObj, (x-outline, y-outline))
            screen.blit(outsideObj, (x-outline, y))
            screen.blit(outsideObj, (x-outline, y+outline))
            screen.blit(outsideObj, (x, y-outline))
            screen.blit(outsideObj, (x, y+outline))
            screen.blit(outsideObj, (x+outline, y-outline))
            screen.blit(outsideObj, (x+outline, y))
            screen.blit(outsideObj, (x+outline, y+outline))
            screen.blit(insideObj, (x, y))

            x+=most
try:
    pygame.mixer.music.load(os.path.dirname(sys.argv[0])+"/Img1/Jetpack Joyride Music.wav")
except:
    try:
        pygame.mixer.music.load(os.path.dirname(sys.argv[0])+"/Img1/Jetpack Joyride Music smaller.wav")
    except:
        print("there was no music file :( contact your system administrator (Ari Fiorino)")
        
    
def thestash():
    global ralt, lalt, f4
    global stash, screen
    stash = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/the stash.png")
    end = False
    while end == False:

        ev = pygame.event.get()

        for event in ev:

            if event.type == QUIT:
                endall()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pos[0]>55 and pos[0]<155 and pos[1] >5 and pos[1]<68:
                    end = True
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp"), (0, 0))
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),(0,0))
                elif pos[0]>55 and pos[0]<254 and pos[1] >224 and pos[1]<423:
                    print("you want to see clothing")


            if event.type == KEYDOWN:
                if event.key == K_F4:
                    f4=1
                if event.key == K_RALT:
                    ralt=1
                if event.key == K_LALT:
                    lalt=1
            if event.type == KEYUP:
                if event.key == K_F4:
                    f4=0
                if event.key == K_RALT:
                    ralt=0
                if event.key == K_LALT:
                    lalt=0
        if (ralt or lalt) and f4:
            endall()
                    

        screen.blit(stash, (0, 0))
        pygame.display.update()


    
def main():
    global ralt, lalt, f4
    global distf, dists, distt, bestscreens
    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp"), (0, 0))
    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))

    bestscreen=random.choice(bestscreens)
                                 
    if not(mute):
        pygame.mixer.music.fadeout(5)
    mainmenu = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/newmain.png")
    randombestscreen=random.randint(0, len(bestscreens)-1)
    bestscreen=bestscreens[randombestscreen]
    mainmenu.blit(pygame.transform.rotate(bestscreen, 5), (85, 325))
    end = False
    
    while end == False:

        ev = pygame.event.get()

        for event in ev:

            if event.type == QUIT:
                endall()
                
            if event.type == KEYDOWN:
                if event.key == K_F4:
                    f4=1
                if event.key == K_RALT:
                    ralt=1
                if event.key == K_LALT:
                    lalt=1
            if event.type == KEYUP:
                if event.key == K_F4:
                    f4=0
                if event.key == K_RALT:
                    ralt=0
                if event.key == K_LALT:
                    lalt=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pos[0]>525 and pos[0]<974 and pos[1] >528 and pos[1]<685:
                    end = True
                elif pos[0]> 524 and pos[1]>320 and pos[0]<889 and pos[1]<478:
                    thestash()
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp"), (0, 0))
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))
                elif pos[0]>0 and pos[0]<135 and pos[1] >0 and pos[1]<71:

                    clickout = False
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))
                    while clickout == False:
                        credit = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/main credits.png")
                        
                        screen.blit(credit, ( screen.get_width()/2-(credit.get_width()/2 ),  screen.get_height()/2-(credit.get_height()/2 )))
                        pygame.display.update()
                        
                        ev = pygame.event.get()

                        for event in ev:
                            if event.type == QUIT:
                                endall()


                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if (pos[0]>screen.get_width()/2-(credit.get_width()/2 ) + credit.get_width() or pos[0]< screen.get_width()/2-(credit.get_width()/2 )) or (pos[1] >screen.get_height()/2-(credit.get_height()/2 ) +credit.get_height() or pos[1]<screen.get_height()/2-(credit.get_height()/2 )):

                                    clickout =True
                                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp"), (0, 0))
                                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))


                elif pos[0]>153 and pos[0]<306 and pos[1] >0 and pos[1]<73:
                    clickout = False
                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))
                    while clickout == False:
                        instruction = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/main instruction.png")

                        screen.blit(instruction, ( screen.get_width()/2-(instruction.get_width()/2 ),  screen.get_height()/2-(instruction.get_height()/2 )))
                        pygame.display.update()
                        
                        ev = pygame.event.get()

                        for event in ev:
                            if event.type == QUIT:
                                endall()


                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if (pos[0]>screen.get_width()/2-(instruction.get_width()/2 ) + instruction.get_width() or pos[0]< screen.get_width()/2-(instruction.get_width()/2 )) or (pos[1] >screen.get_height()/2-(instruction.get_height()/2 ) +instruction.get_height() or pos[1]<screen.get_height()/2-(instruction.get_height()/2 )):
                                    clickout =True
                                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp"), (0, 0))
                                    screen.blit(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png"),( 0,0))
                                    
        
        screen.blit(mainmenu, (0, 0))
        moneysurface=smallfont.render(str(int(money)), 1, (255, 255, 255))
        screen.blit(moneysurface, (745-moneysurface.get_width(), 445-(moneysurface.get_height()/2)))
        screen.blit( pygame.transform.rotate(  extremefont.render(str(int(distance))+"m", 1, (246, 142, 1)) ,5.5  ), (86, 120))
        screen.blit( pygame.transform.rotate(  verysmallfont.render(str(int(score)), 1, (213, 199, 96)) ,5.5  ), (307, 264))
        ast, bst, cst = distf, dists, distt
        a, b, c = verysmallfont.render(str(int(ast)), 1, (124, 137, 160)), verysmallfont.render(str(int(bst)), 1, (124, 137, 160)), verysmallfont.render(str(int(cst)), 1, (124, 137, 160))
        screen.blit( verysmallfont.render(str(int(ast)), 1, (124, 137, 160)), (968-a.get_width(), 132))
        screen.blit( verysmallfont.render(str(int(bst)), 1, (124, 137, 160)), (968-b.get_width(), 178))
        screen.blit( verysmallfont.render(str(int(cst)), 1, (124, 137, 160)), (968-c.get_width(), 228))
        if (ralt or lalt) and f4:
            endall()
        pygame.display.update()
##################################################################################################################################################################

def Quit():
    global die, stevex, stevey, steve, floor, invincible
    steve=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1\dead.png")
    direction=random.choice([-1,1])
    screen.blit(bg1, (bg1x, bg1y))
    screen.blit(bg2, (bg2x, bg2y))
    zapper_a.blit()
    zapper_b.blit()
    for i in range(len(coins)):
        coins[i].blit()
    screen.blit(pause, (width-pause.get_width(), 0))
    outlineit(0, 50, 2, 40, str(score).zfill(3), smallfont, (255,140, 0), 23)
    outlineit(0, 0, 2, 50, str(int(distance)).zfill(4)+" m", font, (160, 160, 160), 27)
    pygame.display.update()
    e=1
    while e:
        e=0
        try:
            pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
        except:
            e=1

    ss=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
    c=0
    Imgg=steve
    m=stevex+steve.get_height()
    rotation=0
    while m<=floor:
        stevey+=random.randint(100, 200)/100
        stevex+=.1*direction
        if c%5==0:
            screen.blit(ss, (0, 0))
            steve=pygame.transform.rotate(Imgg, rotation)
            screen.blit(steve, (stevex, stevey))
            pygame.display.update()
        c+=1
        rotation+=.25
        m=stevey
    screen.blit(ss, (0, 0))
    steve=pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1\end.png")

    screen.blit(steve, (stevex, floor+steve.get_height()+20))
    pygame.display.update()
    sleep(1)
    die = True
class Zapper():
    
    x, y = 0, 0
    rotate = False
    image = random.choice([os.path.dirname(sys.argv[0])+"/Img1/zap2.png", os.path.dirname(sys.argv[0])+"/Img1/zap3.png", os.path.dirname(sys.argv[0])+"/Img1\zap.png", os.path.dirname(sys.argv[0])+"/Img1\zap1.png"])
    Object = pygame.image.load(image)
    spinObj = pygame.image.load(os.path.dirname(sys.argv[0])+"\Img1\zap4.png")
    rect = Object.get_rect()
    spinamount = 0
    rect.x = x
    rect.y = y
    addx, addy = 0, 0
    def setx(self, x):
        self.x = x
    def spin(self, rect, amount):

        self.Object = pygame.transform.rotate(self.spinObj, amount)
        self.addx, self.addy = (self.spinObj.get_width()-self.Object.get_width())/2, (self.spinObj.get_height()-self.Object.get_height())/2

    def spinobj(self, rect):
        return pygame.transform.rotate(self.spinObj, self.spinamount)
    
    def randompic(self):
        self.image = random.choice([os.path.dirname(sys.argv[0])+"/Img1/zap2.png", os.path.dirname(sys.argv[0])+"/Img1/zap3.png", os.path.dirname(sys.argv[0])+"/Img1\zap.png", os.path.dirname(sys.argv[0])+"/Img1\zap1.png"])#, "Img1\zap4.png"])
        if  self.image == os.path.dirname(sys.argv[0])+"/Img1\zap4.png":
            self.rotate = True
        else:
            self.rotate = False
        self.Object = pygame.image.load(self.image)
    def blit(self):
        if self.rotate:
            screen.blit(self.Object, (self.x+self.addx, self.y+self.addy))
        else:
            screen.blit(self.Object, (self.x, self.y))
    def intersecting(self, steverect):
        global steve, stevex, steveyf, stevewidth, invincible
        if self.rotate:
            Obj = self.spinobj(self.spinObj.get_rect())
            x, y = self.x+self.addx, self.y+self.addy
            ourrect = self.rect
            ourrect.x = x
            ourrect.y = y
        else:
            Obj = self.Object
            x, y = self.x, self.y
            ourrect = self.rect


        if ourrect.colliderect( steverect ) and not invincible:
            if (self.image == os.path.dirname(sys.argv[0])+"/Img1/zap2.png" or self.image == os.path.dirname(sys.argv[0])+"/Img1/zap3.png"):
                if ourrect.collidepoint(stevex, stevey):
                    rgb=Obj.get_at((int(fabs( stevex - x) ), int(fabs(stevey- y)))  )
                    if rgb != (255, 255, 255, 0) and rgb != (0, 0, 0, 255):
                        pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                        Quit()
                    #top right
                elif ourrect.collidepoint(stevex + stevewidth,  stevey):
                    rgb=Obj.get_at(( (int(fabs(x-(stevex + stevewidth))))  , int(fabs(y-stevey)) ))
                    if rgb != (255, 255, 255, 0) and rgb != (0, 0, 0, 255):
                        pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                        Quit()
                    #bottom left

                elif ourrect.collidepoint(stevex, stevey + steveheight  ):
                    rgb=Obj.get_at(( int(fabs(x-stevex) ), int(fabs(y-(stevey + steveheight)))) )
                    if rgb != (255, 255, 255, 0) and rgb != (0, 0, 0, 255):
                        pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                        Quit()
                    #bottom right
                elif ourrect.collidepoint(stevex + stevewidth , stevey + steveheight  ):
                    rgb=Obj.get_at(        ((int(fabs(x-(stevex + stevewidth))) ,int(fabs( y-(stevey + steveheight)))) ) )
                    if rgb != (255, 255, 255, 0) and rgb != (0, 0, 0, 255):
                        pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                        Quit()
            else:
                pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                Quit()

                   
    def update(self):
        global largesty, speed, floor
        self.x-=speed
        speed+=.0005
        if self.x<=-largesty:
            self.x = float(bg1.get_width())
            self.y = float(random.randint(100, floor-self.Object.get_height()))
            zaprand = random.randint(1, 4)
            self.randompic()
        if  self.rotate:

            self.spinamount+=1
            randobj = self.spinObj.get_rect()
            randobj.x = self.x
            randobj.y = self.y
            self.spin(self.spinObj.get_rect(), self.spinamount)
            
        self.rect = self.Object.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = random.choice([os.path.dirname(sys.argv[0])+"/Img1/zap2.png", os.path.dirname(sys.argv[0])+"/Img1/zap3.png", os.path.dirname(sys.argv[0])+"/Img1\zap.png", os.path.dirname(sys.argv[0])+"/Img1\zap1.png"])
        self.Object = pygame.image.load(self.image)
        self.rect = self.Object.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
#######################################

class Coin():
    
    floor = screen.get_height()-190
    x, y = random.randint(0, screen.get_width()), random.randint(0+125, floor)
    touch = False
    point = False
    imgs = []
    imgnum = 0
    for i in range(6):
        imgs.append(pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/Coin"+str(i)+"1.png"))
    CoinObject = imgs[imgnum]
    rect = CoinObject.get_rect()
    rect.x = x
    rect.y = y
    spintoken=False
    spintokenimage=pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\spin token.png")
    #oamount=0
    #oscillating=False
    #oy=0
    def __init__(self):

        self.spintoken=False
        self.x, self.y = random.randint(0, screen.get_width()), random.randint(0+125, self.floor)
        self.rect = self.CoinObject.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.touch = False
        self.point = False
        self.tokenrandom=[1]
        self.tokenrandom.extend([0]*40)
#        self.tokenrandom=[1]
#        print(len(self.tokenrandom))
    def changeimage(self):
        self.imgnum = (self.imgnum+1)%6
        self.CoinObject = self.imgs[self.imgnum]
        
    def update(self):
#        print("oy", self.oy)
        global speed, stevey
        self.rect.x = self.x
        self.rect.y = self.y
        self.x-=(speed )
        if self.spintoken:

                if self.y>stevey:
                    self.y-=((self.y-stevey)/80)
                else:
                    self.y+=((stevey-self.y)/80)
                
                
        if self.x<= - self.CoinObject.get_width() *2:
#            print("back to right")
#            print(len(self.tokenrandom))
            if random.choice(self.tokenrandom):
                self.spintoken=True

            else:
                self.spintoken=False
            floor = screen.get_height()-190
            self.x, self.y = screen.get_width(), random.randint(100, floor)
            self.touch = False
            self.rect.x = self.x
            self.rect.y = self.y
            self.point = False
    def intersecting(self, steverect):
        global score, spintokens
        if self.rect.colliderect( steverect ):
#            print("back to right")
            self.touch = True
            if self.spintoken:
                spintokens+=1
            elif self.point == False:
                score+=1
                self.point = True
            floor = screen.get_height()-190
            self.x, self.y = screen.get_width(), random.randint(100, floor)
            self.rect.x = self.x
            self.rect.y = self.y
            self.touch = False
            self.point = False
#            print(len(self.tokenrandom))
            if random.choice(self.tokenrandom):
#                print("token")
                self.spintoken=True
            else:
                self.spintoken=False
                
        return self.touch

    def blit(self):
        global steverect
        self.intersecting(steverect)
        if not self.spintoken:
            screen.blit(self.CoinObject, (self.x, self.y))
        else:
            screen.blit(self.spintokenimage, (self.x, self.y))
ifmain = True

bg1 = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/bg6.jpg")
bg2 = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/bg6.jpg")
pause = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/pause.png")

highscore = open(os.path.dirname(sys.argv[0])+'/Img1/Highscore.txt', 'r+')
rdl = list(highscore.readlines())
bew = []
for i in rdl:
    if i != "\n":
        bew.append(i.rstrip("\n"))
try:
    [distf, dists, distt] = list(bew)
except ValueError:
    distf, dists, distt = 0, 0, 0
distf, dists, distt = int(float(distf)), int(float(dists)), int(float(distt))
try:
    money = int(open(os.path.dirname(sys.argv[0])+'/Img1/money.txt', 'r').readlines()[0])
except:
    money = 0
    open(os.path.dirname(sys.argv[0])+'/Img1/money.txt', 'w').write("0")
pause.set_colorkey(pygame.Color(0, 0, 0))
paused = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/paused.png")
font = pygame.font.Font(os.path.dirname(sys.argv[0])+"/Img1/New Athletic M54.ttf", 50)
smallfont = pygame.font.Font(os.path.dirname(sys.argv[0])+"/Img1/New Athletic M54.ttf", 40)
verysmallfont = pygame.font.Font(os.path.dirname(sys.argv[0])+"/Img1/New Athletic M54.ttf", 30)
extremefont = pygame.font.Font(os.path.dirname(sys.argv[0])+"/Img1/New Athletic M54.ttf", 130)
steve = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/walk1.png")
darker = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/darker screen.png")
moneytxt = open(os.path.dirname(sys.argv[0])+'/Img1/money.txt', 'w')
steveimages = [pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/walk1.png"), pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/walk2.png"), pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/flying1.png"), pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/beggining.png")]
invincibleframesl=200
distance = 0
score = 0
rocketimgs=[pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket warning.png"), pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket warning almost.png"), pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket.png")]

def endall():
    global highscore, distf, dists, distt, moneytxt
#    print("fini!!")
    highscore.seek(0)
    highscore.truncate()
    highscore.write(str(distf)+"\n"+str(dists)+"\n"+str(distt))
    highscore.close()

    moneytxt.seek(0)
    moneytxt.truncate()
    moneytxt.write(str(int(money)))
    moneytxt.close()
    
    pygame.quit()
    sys.exit()

def updatehighscore():
    global distf, dists, distt, highscore, distance
    score = distance
    rdl = list(highscore.readlines())
    if rdl == []:
        rdl =  [0, 0, 0]
    if int(score)>int(distf):
        distf, dists, distt = score, distf, dists
    elif int(score)>int(dists):
        distf, dists, distt = distf, score, dists
    elif int(score)>int(distt):
        distf, dists, distt = distf, dists, score

def rocket():
    global rocketimgs, rocketstage, rockety, rocketx, stevey
    if rocketstage==0 or rockety==1:
        if rockety<stevey:
            rockety+=.1
    
    
        
        
        
rockety=(screen.get_width()/2)-(rocketimgs[2].get_height()/2)
rocketx=screen.get_width()-rocketimgs[0].get_width()
rocketstage=0    
bestscreens=[]
ifmain=False
counter = pygame.time.Clock()
firsttime=True
spintokens=0
invincible=False
rocketimgs=[pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket warning.png"), pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket warning almost.png"), pygame.image.load(os.path.dirname((sys.argv[0]))+"/Img1/rocket.png")]

while True:
#####################################FLOOR?
    moneytxt.write(str(int(score+money)))
    money = int(score+money)
    floor = bg1.get_height()-190
    stevex, stevey = 100, floor
    mstevey = 0
    bg1x, bg1y = float(bg1.get_width()), 0.0
    bg2x, bg2y = 0.0, 0.0
    keydown = False
    change = 0
    stevewidth = steve.get_width()
    steveheight = steve.get_height()
    end = False
    walkcount = 0
    largesty = 550.0
    ifpause = False
    blitshell = False
    blitbullet = False
    zapper_a = Zapper()
    zapper_b = Zapper()
    zapper_b.setx(screen.get_width()/2)
    steverect = steve.get_rect()
    speed = 7
    coins = []
    i = 0
    die = False
    while i < 5:
        coins.append(Coin())
        i+=1
#######################################################################################WHILE LOOP#############################################################################################

    updatehighscore()
    counter.tick()
    if not firsttime:
        print("the fps is:", round(1000/(sum(fps)/len(fps)), 2))
    else:
        firstscreen()
    fps=[]
##    if spintokens>0:
###        print("spin")
##        pygame.mixer.music.pause()
##        FinalSpin()
##        pygame.mixer.music.unpause()
    if ifmain and not firsttime:
        main()
    bestscreens=[]
    ifmain = True
    score = 0
    if not(mute):
        pygame.mixer.music.play(-1)
    count = 0
    distance = 0
    screenshotcount=0
    firsttime=False
    invincibleframesl=100
    while die != True:
        if random.randint(0, 200)==50 or distance==0 or distance==5:
            screenshotcount=distance
            screenradius=[180, 145]
            stevecenter=[stevex+(steve.get_width()/2), stevey+(steve.get_height()/2)]
            bestscr=pygame.Surface((screenradius[0]*2, screenradius[1]*2), pygame.SRCALPHA, 32).convert_alpha()
            bestscr.blit(screen, (0, 0), (stevecenter[0]-screenradius[0], stevecenter[1]-screenradius[1], screenradius[0]*2, screenradius[1]*2))
            bestscreens.append(bestscr)
        steverect.x = stevex
        steverect.y = stevey
        for i in range(len(coins)):
            coins[i].intersecting(steverect)
        count+=1
        count%=5
        if count ==0:
            distance +=.5
            for i in range(len(coins)):
                coins[i].changeimage()
        
        if zapper_a.intersecting(steverect):
                endall()

        if zapper_b.intersecting(steverect):
                endall()

        for i in range(len(coins)):
            coins[i].update()
        walkcount+=1

        if int(walkcount%10) ==int(0) and stevey>=floor and keydown!="falling":
            steve = steveimages[0]
        elif int(walkcount%5) ==int(0):
            steve = steveimages[1]
        if keydown == True  and stevey<=floor-steveheight:
            steve = steveimages[2]
        elif keydown == True:
            steve = steveimages[3]
        if keydown == "falling":
            steve = steveimages[3]
                
        if stevey>=floor and keydown == "falling":
            keydown = False
            mstevey = 0
            change = 0
            stevey = floor
        if keydown == True:
            if stevey>=0 :
                change-=.01
                mstevey+=change
        if keydown == "falling":
            change+=.02
            mstevey+=change
        
        for event in pygame.event.get():
            if event.type == QUIT:
                endall()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    keydown = True
                    change = 0
                    mstevey = 0
                if event.key == K_F4:
                    f4=1
                if event.key == K_RALT:
                    ralt=1
                if event.key == K_LALT:
                    lalt=1
                    

       
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    keydown = "falling"
                    mstevey = 0
                    change = 0

                if event.key == K_F4:
                    f4=0
                if event.key == K_RALT:
                    ralt=0
                if event.key == K_LALT:
                    lalt=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not(pos[1] >=0 and pos[1]<=pause.get_height() and pos[0]>=(width-pause.get_width()) and pos[0]<=width):
                    keydown = True
                    change = 0
                    mstevey = 0                                 
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[1] >=0 and pos[1]<=pause.get_height() and pos[0]>=(width-pause.get_width()) and pos[0]<=width:
                    if ifpause == False:
                        ifpause = True
                    else:
                        ifpause = False
                else:
                    keydown = "falling"
                    mstevey = 0
                    change = 0
                    
        if stevey>=100 or keydown == "falling":
            stevey+=mstevey

        if end == False:
            bg1x-=speed
            bg2x-=speed
            
        if bg1x<=-screen.get_width():
            bg1x = screen.get_width()
        if bg2x<=-screen.get_width():
            bg2x = screen.get_width()
            
        if (ralt or lalt) and f4:
            endall()
            
        zapper_a.update()
        zapper_b.update()
        
        if invincible:
            invincibleframesl-=1
            if invincibleframesl<=0:
                invincible=False
                invincibleframesl=200

        if ifpause == False and not die:
            screen.blit(bg1, (bg1x, bg1y))
            screen.blit(bg2, (bg2x, bg2y))
            zapper_a.blit()
            zapper_b.blit()
            for i in range(len(coins)):
                coins[i].blit()
            if invincibleframesl%16==invincibleframesl%8:
                screen.blit(steve, (stevex, stevey))

            screen.blit(pause, (width-pause.get_width(), 0))
            outlineit(0, 50, 2, 40, str(score).zfill(3), smallfont, (255,140, 0), 23)
            
            outlineit(0, 0, 2, 50, str(int(distance)).zfill(4)+" m", font, (160, 160, 160), 27)
#########################################################################################################################
            
        elif not die:
            if not(mute):
                pygame.mixer.music.pause()
            if ifpause:
                pygame.image.save(screen, os.path.dirname(sys.argv[0])+"/Img1/screenshot.bmp")
                for i in range(1):
                    screen.blit(darker,( 0,0))
                    pygame.display.update()

            while ifpause == True:
            
                screen.blit(paused, (0, 0))
                if mute:
                    muteObj = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/mute.png")
                else:
                    muteObj = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/unmute.png")
                muteObjx, muteObjy = 876, 12
                screen.blit(muteObj,( 876, 12))
                pygame.display.update()
                for eventa in pygame.event.get():
                    if eventa.type == QUIT:
                        endall()

                    if eventa.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > muteObjx and pos[0] < muteObjx + muteObj.get_width() and pos[1] > muteObjy and pos[1] < muteObjy + muteObj.get_height() :
                            mute = not(mute)

                            if mute:
                                muteObj = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/mute.png")
                            else:
                                muteObj = pygame.image.load(os.path.dirname(sys.argv[0])+"/Img1/unmute.png")

                            if not(mute):
                                pygame.mixer.music.play(-1)
                                pygame.mixer.music.pause()

                                   
                        if pos[0] > 643 and pos[0] < 872 and pos[1] > 614 and pos[1] < 692:
                            ifpause = False

                        if pos[0] > 391 and pos[0] < 618 and pos[1] > 614 and pos[1] < 690:
                            ifpause = False
                            die = True
                            ifmain = False

                        if pos[0] > 150 and pos[0] < 369 and pos[1] > 614 and pos[1] < 692:

                            ifpause = False
                            die = True
                    
                    if eventa.type == KEYDOWN:
                        if eventa.key == K_F4:
                            f4=1
                        if eventa.key == K_RALT:
                            ralt=1
                        if eventa.key == K_LALT:
                            lalt=1
                    if eventa.type == KEYUP:
                        if eventa.key == K_F4:
                            f4=0
                        if eventa.key == K_RALT:
                            ralt=0
                        if eventa.key == K_LALT:
                            lalt=0
                if (ralt or lalt) and f4:
                    endall()
            if not(mute):
                pygame.mixer.music.unpause()
                
        if spintokens>0 and die:
#        print("spin")
            pygame.mixer.music.pause()
            FinalSpin()
            pygame.mixer.music.unpause()


        pygame.display.update()
        fps.append(counter.tick())
##        else:
##            if invinciblefamesl%2:

            

