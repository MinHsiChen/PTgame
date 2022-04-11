import pygame
import random
import os

#一些變數
WIDTH=1000
HEIGHT=700
FPS=60
WHITE=(255,255,255)

#建視窗
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('沉澱表小遊戲')
clock=pygame.time.Clock()
 
###############################################
font_name=os.path.join('FONT.ttf')

def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,(0,0,0)) 
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)

def draw_init():
    screen.blit(start_img,(0,0))
    draw_text(screen,'沉澱表小遊戲',64,WIDTH/2,HEIGHT/4)
    draw_text(screen,'A鍵往左 , D鍵往右 , 操控陰離子撞擊掉落的陽離子!',30,WIDTH/2,HEIGHT/2)
    draw_text(screen,'一個陰離子撞擊三個陽離子後換下一個，共六階段',30,WIDTH/2,HEIGHT/2+50)
    draw_text(screen,'按任意鍵開始遊戲',22,WIDTH/2,HEIGHT*3/4)
    pygame.display.update()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return True
            elif event.type==pygame.KEYUP:
                waiting=False
                return False

def hit_right():
    ai+=1
    score+=10
    if ai<6:
        anion.change(ai)
    else:
        end_game()

def hit_wrong():
    score-=10

def end_game():
    running=False


#陽離子cation
class Cation(pygame.sprite.Sprite):
    def __init__(self,i):
        pygame.sprite.Sprite.__init__(self)
        self.image=cation_imgs[i]
        self.rect=self.image.get_rect()
        self.rect.center=(random.randrange(0,WIDTH-self.rect.width),random.randrange(-100,-50))
        self.speedy=random.randrange(2,4)

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top>HEIGHT or self.rect.left>WIDTH or self.rect.right<0:
            self.rect.center=(random.randrange(0,WIDTH-self.rect.width),random.randrange(-100,-50))
            self.speedy=random.randrange(2,4)

#陰離子anion
class Anion(pygame.sprite.Sprite):
    def __init__(self,i):
        pygame.sprite.Sprite.__init__(self)
        self.image=anion_imgs[i]
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speedx=7

    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x+=self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x-=self.speedx

        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
    
    def change(self,i):
        self.image=anion_imgs[i]
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speedx=7


##################################################
#載圖片
background_img=pygame.image.load(os.path.join('img','cat.png')).convert()
start_img=pygame.image.load(os.path.join('img','start.jpg')).convert()
#玩家陰離子
anion_imgs=[]
anion_list=[      #撞到以下加分，否則扣分
    'Cl-.png',      #0,11,4,7?,13
    'CrO42-.png',   #12,2,11,0
    'C2O42-.png',   #11,2,4,12,8,7,13,14,3,0,5,1
    'OH-.png',      #11,4,8,7,13,14,3,0,5,1
    'SO42-.png',    #12,2,11
    'S2-.png'       #4,8,7,13,14,0,5,1
]
for image in anion_list:
    anion_imgs.append(pygame.image.load(os.path.join('img',image)).convert())

#掉落陽離子
cation_imgs=[]
cation_list=[
    'Ag+.png',      #0
    'Al3+.png',     #1
    'Ba2+.png',     #2
    'Cs+.png',      #3
    'Cu+.png',      #4
    'Cu2+.png',     #5
    'H+.png',       #6
    'Hg+.png',      #7
    'Hg22+.png',    #8
    'Na+.png',      #9
    'NH4+.png',     #10
    'Pb2+.png',     #11
    'Sr2+.png',     #12
    'Tl+.png',      #13
    'Tl3+.png'      #14
]
for image in cation_list:
    cation_imgs.append(pygame.image.load(os.path.join('img',image)).convert())

##############################################
ci_sprites=pygame.sprite.Group()
cr_sprites=pygame.sprite.Group()
c2_sprites=pygame.sprite.Group()
oh_sprites=pygame.sprite.Group()
so_sprites=pygame.sprite.Group()
s2_sprites=pygame.sprite.Group()


ai=0
anion=Anion(ai)


ci_sprites.add(anion)
cr_sprites.add(anion)
c2_sprites.add(anion)
oh_sprites.add(anion)
so_sprites.add(anion)
s2_sprites.add(anion)


def ncation_ci_up(i):
    cation_elem=Cation(i)
    ci_sprites.add(cation_elem)
    cations_ci_up.add(cation_elem)

def ncation_ci_dn(i):
    cation_elem=Cation(i)
    ci_sprites.add(cation_elem)
    cations_ci_dn.add(cation_elem)

cations_ci_up=pygame.sprite.Group() #得分群
ncation_ci_up(0)
ncation_ci_up(11)
ncation_ci_up(4)
ncation_ci_up(7)
ncation_ci_up(13)

cations_ci_dn=pygame.sprite.Group() #扣分群
ncation_ci_dn(1)
ncation_ci_dn(2)
ncation_ci_dn(3)
ncation_ci_dn(5)
ncation_ci_dn(6)
ncation_ci_dn(8)
ncation_ci_dn(9)
ncation_ci_dn(10)
ncation_ci_dn(12)
ncation_ci_dn(14)


def ncation_cr_up(i):
    cation_elem=Cation(i)
    cr_sprites.add(cation_elem)
    cations_cr_up.add(cation_elem)

def ncation_cr_dn(i):
    cation_elem=Cation(i)
    cr_sprites.add(cation_elem)
    cations_cr_dn.add(cation_elem)

cations_cr_up=pygame.sprite.Group()
ncation_cr_up(12)
ncation_cr_up(2)
ncation_cr_up(11)
ncation_cr_up(0)
cations_cr_dn=pygame.sprite.Group()
ncation_cr_dn(1)
ncation_cr_dn(3)
ncation_cr_dn(4)
ncation_cr_dn(5)
ncation_cr_dn(6)
ncation_cr_dn(7)
ncation_cr_dn(8)
ncation_cr_dn(9)
ncation_cr_dn(10)
ncation_cr_dn(13)
ncation_cr_dn(14)

def ncation_c2_up(i):
    cation_elem=Cation(i)
    c2_sprites.add(cation_elem)
    cations_c2_up.add(cation_elem)

def ncation_c2_dn(i):
    cation_elem=Cation(i)
    c2_sprites.add(cation_elem)
    cations_c2_dn.add(cation_elem)

cations_c2_up=pygame.sprite.Group()
ncation_c2_up(11)
ncation_c2_up(2)
ncation_c2_up(4)
ncation_c2_up(12)
ncation_c2_up(8)
ncation_c2_up(7)
ncation_c2_up(13)
ncation_c2_up(14)
ncation_c2_up(3)
ncation_c2_up(0)
ncation_c2_up(5)
ncation_c2_up(1)
cations_c2_dn=pygame.sprite.Group()
ncation_c2_dn(6)
ncation_c2_up(9)
ncation_c2_up(10)


def ncation_oh_up(i):
    cation_elem=Cation(i)
    oh_sprites.add(cation_elem)
    cations_oh_up.add(cation_elem)

def ncation_oh_dn(i):
    cation_elem=Cation(i)
    oh_sprites.add(cation_elem)
    cations_oh_dn.add(cation_elem)

cations_oh_up=pygame.sprite.Group()
ncation_oh_up(11)
ncation_oh_up(4)
ncation_oh_up(8)
ncation_oh_up(7)
ncation_oh_up(13)
ncation_oh_up(14)
ncation_oh_up(3)
ncation_oh_up(0)
ncation_oh_up(5)
ncation_oh_up(1)
cations_oh_dn=pygame.sprite.Group()
ncation_oh_dn(2)
ncation_oh_dn(6)
ncation_oh_dn(9)
ncation_oh_dn(10)
ncation_oh_dn(12)

def ncation_so_up(i):
    cation_elem=Cation(i)
    so_sprites.add(cation_elem)
    cations_so_up.add(cation_elem)

def ncation_so_dn(i):
    cation_elem=Cation(i)
    so_sprites.add(cation_elem)
    cations_so_dn.add(cation_elem)

cations_so_up=pygame.sprite.Group()
ncation_so_up(12)
ncation_so_up(2)
ncation_so_up(11)
cations_so_dn=pygame.sprite.Group()
ncation_so_dn(0)
ncation_so_dn(1)
ncation_so_dn(3)
ncation_so_dn(4)
ncation_so_dn(5)
ncation_so_dn(6)
ncation_so_dn(7)
ncation_so_dn(8)
ncation_so_dn(9)
ncation_so_dn(10)
ncation_so_dn(13)
ncation_so_dn(14)

def ncation_s2_up(i):
    cation_elem=Cation(i)
    s2_sprites.add(cation_elem)
    cations_s2_up.add(cation_elem)

def ncation_s2_dn(i):
    cation_elem=Cation(i)
    s2_sprites.add(cation_elem)
    cations_s2_dn.add(cation_elem)

cations_s2_up=pygame.sprite.Group()
ncation_s2_up(4)
ncation_s2_up(8)
ncation_s2_up(7)
ncation_s2_up(13)
ncation_s2_up(14)
ncation_s2_up(0)
ncation_s2_up(5)
ncation_s2_up(1)
cations_s2_dn=pygame.sprite.Group()
ncation_s2_dn(2)
ncation_s2_dn(3)
ncation_s2_dn(6)
ncation_s2_dn(9)
ncation_s2_dn(10)
ncation_s2_dn(11)
ncation_s2_dn(12)

cnt=0
score=0

#讓遊戲出來跑跑跑
show_init=True
running=True
while running: #視窗出來跑跑跑
    if show_init:
        close=draw_init()
        if close:
            break
        show_init=False

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #更新
    #背景
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))
    
    if ai==0:
        ci_sprites.update()
        
        hits=pygame.sprite.spritecollide(anion,cations_ci_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_ci_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0
            anion.change(ai)

        ci_sprites.draw(screen)
    elif ai==1:
        cr_sprites.update()

        hits=pygame.sprite.spritecollide(anion,cations_cr_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_cr_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0
            anion.change(ai)

        cr_sprites.draw(screen)
        
    elif ai==2:
        c2_sprites.update()

        hits=pygame.sprite.spritecollide(anion,cations_c2_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_c2_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0
            anion.change(ai)

        c2_sprites.draw(screen)

    elif ai==3:
        oh_sprites.update()

        hits=pygame.sprite.spritecollide(anion,cations_oh_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_oh_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0
            anion.change(ai)

        oh_sprites.draw(screen)

    elif ai==4:
        so_sprites.update()

        hits=pygame.sprite.spritecollide(anion,cations_so_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_so_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0
            anion.change(ai)

        so_sprites.draw(screen)

    elif ai==5:
        s2_sprites.update()

        hits=pygame.sprite.spritecollide(anion,cations_s2_up,True)
        for hit in hits:
            score+=1
            cnt+=1

        hits=pygame.sprite.spritecollide(anion,cations_s2_dn,True)
        for hit in hits:
            score-=1
            cnt+=1

        if cnt>3:
            ai+=1
            cnt=0

        s2_sprites.draw(screen)

    else:
        running=False

    draw_text(screen,'Score: '+str(score),30,WIDTH/2,20)
    pygame.display.update()

pygame.quit()
