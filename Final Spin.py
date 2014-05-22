import pygame, sys, random, os
from pygame.locals import *
from pygame import surface

money=0
die = True
speed=7

def crop(surface, rect):
    cropped = pygame.Surface((rect.width, rect.height))
    cropped.blit(surface, (-(rect.x), -(rect.y)))
    return cropped  
spintokens=25
pygame.font.init()
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
#if not mute:
spinningsound.play(loops=-1)
lightsurface=[pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\red light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png"), pygame.image.load(os.path.dirname(sys.argv[0])+r"\Img1\spin\grey light.png")]
lcy=[285, 349, 413, 479, 541]
lcx=[773, 950]
lightcoors=[]
for x in lcx:
    for y in lcy:
        lightcoors.append([x, y])
lightframes=20
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
def endall():
    pygame.quit()
    sys.exit()
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
        #if not mute:
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
                    #if not mute:
                    spinningsound.stop()
                    #if not mute:
                    winsound.play()
                    #print(winners[0])
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
                #if not mute:
                spinningsound.play(loops=-1)
                spinspeed=[25, 25, 25]
                waitframes=50
                stop=False
                spintokens-=1
        if spintokens<=0:
            end=True
    fps.append(counter.tick())
#if not mute:
spinningsound.stop()
spintokens=0
print("the spin fps is:", round(1000/(sum(fps)/len(fps)), 3))
