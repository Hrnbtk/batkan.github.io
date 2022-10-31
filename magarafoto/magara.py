from audioop import add
from typing_extensions import Self
import pygame
pygame.init()
#from enemy import Enemy
#import enemy
import random

H=500
W=480

win = pygame.display.set_mode((H,W),pygame.RESIZABLE)

pygame.display.set_caption("First Game")
game_icon=pygame.image.load('ninja_icon.png')
pygame.display.set_icon(game_icon)

walkRight = [pygame.image.load('kos1.png'), pygame.image.load('kos2.png'), pygame.image.load('kos3.png'), pygame.image.load('kos4.png'), pygame.image.load('kos5.png')] # pygame.image.load('kos2.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')#]

walkLeft = [pygame.image.load('stop1.png'),pygame.image.load('stop2.png'),pygame.image.load('stop3.png'),pygame.image.load('stop4.png'),pygame.image.load('stop5.png')]#pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('background.png')
bg=pygame.transform.scale(bg,(500,480))

rg=(0,0,0)
char = [pygame.image.load('stop1.png'),pygame.image.load('stop2.png'),pygame.image.load('stop3.png'),pygame.image.load('stop4.png'),pygame.image.load('stop5.png')]

jumpings=[pygame.image.load("jump2.png"),pygame.image.load("jump3.png"),pygame.image.load("jump4.png"),pygame.image.load("jump5.png"),pygame.image.load("jump6.png"),
pygame.image.load("jump7.png"),pygame.image.load("jump8.png"),pygame.image.load("jump9.png")]

dıj=pygame.image.load("enmy.png")
dıj=pygame.transform.scale(dıj,(50,50))



dıj1=dıj.copy()

#dıj1=pygame.image.load("enmy2.png")

dıj_kon=dıj.get_rect()
dıj_kx=(random.randint(50,400))
dıj_ky=(random.randint(0,400))
dıj1=pygame.transform.scale(dıj1,(50,50))
dıj22=[dıj,dıj1]


siyah=(0,0,0)
beyaz=(255,255,255)





j=0
char[j].set_colorkey(beyaz)
konums=char[j].get_rect()
walkRight[j].set_colorkey(beyaz)
konums=walkRight[j].get_rect()
walkLeft[j].set_colorkey(beyaz)
konums=walkLeft[j].get_rect()
j+1


clock = pygame.time.Clock()

klm=100

mlk=300


class player(object):


    def __init__(self,x,y,width,height,i,score,hel):
        self.x = konums.x
        self.y = konums.y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.jump=False
        self.i=i
        self.sel=True
        self.xy=dıj_kon.x
        self.yx=dıj_kon.y


    
        self.score=0
        self.hel=100
        self.h=0

        
        
        

    def draw(self, win):


        

        if self.walkCount + 1 == 6:
            self.walkCount = 0
        elif self.left:
            z=0
            win.blit(walkLeft[self.walkCount], (self.x,self.y+300))
            
            walkRight[z].set_colorkey(beyaz)
            z+=1
            self.walkCount += 1
            pygame.draw.rect(win,(255,0,0),(self.x,self.y+300,60,100),4)
        elif self.right:
            k=0
            win.blit(walkRight[self.walkCount], (self.x,self.y+300))
            walkLeft[k].set_colorkey(beyaz)
            k+=1
            self.walkCount +=1
            pygame.draw.rect(win,(255,0,0),(self.x,self.y+300,90,100),4)

        elif self.isJump==True :
            
         
         
            win.blit(jumpings[self.h],(self.x,self.y+300))
            self.h+=1
            pygame.draw.rect(win,(255,0,0),(self.x,self.y+300,80,110),4)
            if self.h==7:
                self.h=0
                
            else:
                self.h+=1

            
          

        else:
            
            win.blit(char[self.i], (self.x,self.y+300))
            char[self.i].set_colorkey(beyaz)
            #self.i+=1
            pygame.draw.rect(win,(255,0,0),(self.x,self.y+300,60,100),4)
            if not self.i==4:
               self.i +=1
               #re+=1
            else :
                self.i =0  
            

        if self.sel == True:

            self.i=0
            win.blit(dıj22[self.i],(self.xy,self.yx))
            if self.yx == W:
                self.score+=1
                if self.score==5:
                   self.xy*1.5  
                   self.yx*1.2
                   win.blit(dıj22[self.i],(self.xy,self.yx))
                   win.blit(dıj22[self.i],(self.xy,self.yx))
                    
                self.yx=0
                self.xy=random.randint(0,480)
                win.blit(dıj22[self.i],(self.xy,self.yx))
   

            elif not self.i==1:
               self.i+=1
               self.yx+=5
               
            else :
              self.i==0
              #self.yx+=20
        

        helth_x=konums.x-20
        helth_y=konums.y-20

        helth_bar=self.score+10
        helty_bar=self.hel
        h_thick=5 # health bar kalınlığı

        r_x=50
        r_y=50



        #pygame.draw.rect(win,(255,0,0),(self.x,self.y,60,100),4)
        pygame.draw.rect(win,(255,255,0),(self.xy,self.yx,r_x,r_y),4) #enemy frame
        pygame.draw.rect(win,(0,255,0),(helth_x,helth_y,helth_bar,h_thick),5) #helth bar

        pygame.draw.rect(win,(0,255,0),(0,20,helty_bar,h_thick),5)
        pygame.draw.rect(win,(0,255,0),(0,20,helth_bar,h_thick),5)
        pygame.draw.rect(win,(255,0,0),(0,20,helth_bar,h_thick),5)

        if konums.colliderect(dıj_kon):
            helty_bar-=25
            helth_bar+=10
            
        
            

        

        


        
    def enemy(self,win):

        if self.sel == True:

            self.i=0
            win.blit(dıj22[self.i],(self.xy,self.yx))
            if self.yx == W:
                self.score+=1
                if self.score==5:
                   self.xy*1.5  
                   self.yx*1.2
                   win.blit(dıj22[self.i],(self.xy,self.yx))
                   win.blit(dıj22[self.i],(self.xy,self.yx))
                    
                self.yx=0
                self.xy=random.randint(0,480)
                win.blit(dıj22[self.i],(self.xy,self.yx))
   

            elif not self.i==1:
               self.i+=1
               self.yx+=5
               
            else :
              self.i==0
              #self.yx+=20

        




def redrawGameWindow():
    win.blit(bg, (0,0))
    text=font.render('score : '+str(man.score),20,(255,255,255))
    text1=font1.render('Health : ',20,(255,255,255))
    win.blit(text,(300,25))
    win.blit(text1,(10,25))

    man.draw(win)
    
    pygame.display.update()


#mainloop
man = player(100, 300, 64,64,0,score=0,hel=100)
man.enemy(win)
font=pygame.font.SysFont('comicsans',30,True)
font1=pygame.font.SysFont('comicsansms',30,True)
print(font1)


run = True
fps=30
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            #z=0
            #win.blit(jumpings[z](man.x,man.y))
            #z+=1
           # char[self.i].set_colorkey((0,0,0))
           
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    


    bar=pygame.draw.rect(win,beyaz,(100,20,200,10),5)


    

            
    redrawGameWindow()

pygame.quit()


'''
'arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 
'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'holomdl2assets', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', '
lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue', 
'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 
'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 
'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsun', 'nsimsun', 'simsunextb', '
sitkasmall', 'sitkatext', 'sitkasubheading', 'sitkaheading', 'sitkadisplay', 'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 
'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular', 'yugothicuisemilight', 'agencyfb', 
'algerian', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'berlinsansfbdemi', 'bernardcondensed', 'blackadderitc', 'bodoni', 'bodoniblack', 
'bodonicondensed', 'bodonipostercompressed', 'bookantiqua', 'bookmanoldstyle', 'bookshelfsymbol7', 'bradleyhanditc', 'britannic', 'broadway', 'brushscript', 'californianfb',
 'calisto', 'castellar', 'centaur', 'century', 'centurygothic', 'centuryschoolbook', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 
 'dubairegular', 'edwardianscriptitc', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'footlight', 'forte', 'franklingothicbook', 
 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'garamond', 'gigi', 'gillsans', 
 'gillsanscondensed', 'gillsansextcondensed', 'gillsansultra', 'gillsansultracondensed', 'gloucesterextracondensed', 'goudyoldstyle', 'goudystout', 'haettenschweiler', 
 'harlowsolid', 'harrington', 'hightowertext', 'imprintshadow', 'informalroman', 'jokerman', 'juiceitc', 'kristenitc', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy',
  'lucidafax', 'lucidafaxregular', 'lucidahandwriting', 'lucidasansroman', 'lucidasansregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'lucidasanstypewriterregular',
   'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'monotypecorsiva', 'msoutlook', 'msreferencesansserif', 'msreferencespecialty', 'extra', 'niagaraengraved',
    'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 
    'qtquickcontrols', 'rage', 'ravie', 'rockwell', 'rockwellcondensed', 'rockwellextra', 'script', 'showcardgothic', 'snapitc', 'stencil', 'tempussansitc', 'twcen', 
    'twcencondensed', 'twcencondensedextra', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin', 'wingdings2', 'wingdings3', 'leelawadee', 'leelawadeekalın', 
    'microsoftuighurkalın', 'microsoftuighur', 'cascadiacoderegular', 'cascadiamonoregular']
'''
