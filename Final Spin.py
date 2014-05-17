import pygame, sys, random
from pygame.locals import *
from pygame import surface

coins=0
spintokens=25
pygame.font.init()
Font=pygame.font.Font("Img1/New Athletic M54.ttf", 65)

startleverpos=[816, 221]
screen = pygame.display.set_mode((1024, 768))#, pygame.FULLSCREEN)
pygame.display.set_caption("Jetpack Joyride")
def endall():
    pygame.quit()
    sys.exit()
finalspin = pygame.image.load("Img1/final spin blank.png")
finalspin.convert_alpha()
lever=pygame.image.load("Img1/spin/spin lever.png")
leverbgframe=0
leverbg=pygame.image.load("Img1/spin/lever bg"+str(leverbgframe)+".png")

def crop(surface, rect):
    cropped = pygame.Surface((rect.width, rect.height))
    cropped.blit(surface, (-(rect.x), -(rect.y)))
    return cropped  

behind=pygame.image.load("Img1/screenshot.bmp")
behind.blit(pygame.image.load("Img1/darker screen.png"),( 0,0))
behind.blit(pygame.image.load("Img1/final spin behind.png"), (0, 0))
cuttouta=crop(behind, pygame.Rect(33, 612, 796, 120))
cuttoutb=crop(behind, pygame.Rect(26, 115, 956, 131))

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

prizes=[]
prizesurf=[pygame.image.load(r"Img1\spin\3 spin tokens.png"), pygame.image.load(r"Img1\spin\stack of coins.png"), pygame.image.load(r"Img1\spin\speed.png"), pygame.image.load(r"Img1\spin\1 coin.png"), pygame.image.load(r"Img1\spin\heart.png"), pygame.image.load(r"Img1\spin\3 coins.png")]

for i in range(9):
    prizes.append(random.choice(prizesurf))
speed=[30, 30, 30]

waitframes=50

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
            extra=pygame.mouse.get_pos()[1]-startleverpos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            extra=0
            leverpos=list(startleverpos)
    if pygame.mouse.get_pressed()[0]:
        leverpos=[startleverpos[0], list(pygame.mouse.get_pos())[1]]
        leverpos[1]-=extra
    if leverpos[1]>=513:
        leverpos[1]=513
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
            prizecoor[i][1]+=speed[2]
        elif i>=3:
            prizecoor[i][1]+=speed[1]
        else:
            prizecoor[i][1]+=speed[0]
        if prizecoor[i][1]>608:
            prizecoor[i][1]=254
            prizes[i]=random.choice(prizesurf)

    
    leverbg=pygame.image.load("Img1/spin/lever bg"+str(leverbgframeb)+".png")

   
    screen.blit(behind, (0, 0))
    for i in range(9):
        rectt=prizes[i].get_rect()
        rectt.center=(prizecoor[i][0], prizecoor[i][1])
        screen.blit(prizes[i], rectt)
    screen.blit(cuttouta, (33, 612))
    screen.blit(cuttoutb, (26, 115))
    screen.blit(finalspin, (0, 0))
    screen.blit(leverbg, (815, 334))    
    screen.blit(lever, (leverpos[0], leverpos[1]))
    
    fontsurface=Font.render("%02d" % (spintokens), 1, (0, 0, 0))
    fontrect=fontsurface.get_rect()
    fontrect.center=(909, 153)
    screen.blit(fontsurface,fontrect)
    
    pygame.display.update()
    if (ralt or lalt) and f4:
        endall()
    if stop:
        for i in range(len(prizecoor)):
            if prizecoor[i][1] <= 432+20 and prizecoor[i][1] >= 432-20 and random.choice([0, 0, 0, 1]):
                if i>=6:
                    speed[2]=0

                elif i>=3:
                    speed[1]=0

                else:
                    speed[0]=0

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
        if speed==[0, 0, 0]:
                
                waitframes-=1
                if waitframes<=0:
                    
                    speed=[30, 30, 30]
                    waitframes=50
                    stop=False
                    spintokens-=1
        if spintokens<=0:
            end=True
            
endall()
