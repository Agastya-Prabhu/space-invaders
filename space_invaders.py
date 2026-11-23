import pygame
from pygame.locals import *
import time

clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Space Invaders")

def show_text(msg, x, y, color, size):
        fontobj = pygame.font.SysFont("freesans", size,bold = True, italic = False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))

player = pygame.image.load("SpaceInvadersPlayer-removebg-preview.png")
player = pygame.transform.scale(player,(100,75))
alien = pygame.image.load("SpaceInvadersAlien1-removebg-preview.png")
alien = pygame.transform.scale(alien,(40,25))
lazer = pygame.image.load("SpaceInvadersLazer-removebg-preview.png")
lazer = pygame.transform.scale(lazer,(20,25))
lazer = pygame.transform.rotate(lazer,90)

win = pygame.mixer.Sound("vadim_makes_sound-retro-arcade-level-up-552982.wav")
lose = pygame.mixer.Sound("freesound_community-080047_lose_funny_retro_video-game-80925.wav")
explosion = pygame.mixer.Sound("lumora_studios-pixel-explosion-319166.wav")

class Character:
    def __init__(self,x,y,image):
         self.x = x
         self.y = y
         self.image = image
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
class Alien(Character):
    def __init__(self,x,y,image):
         super().__init__(x,y,image)
         self.speed = 6
    def move(self):
         self.x += self.speed
class Player(Character):
     def __init__(self,x,y,image):
         super().__init__(x,y,image)
         self.playerspeed = 5
class Bullet(Character):
     def __init__(self,x,y,image):
          super().__init__(x,y,image)
          self.bulletspeed = 20    
     def move(self):
          self.y -= self.bulletspeed
         

aliens = []
x = 41
y = 30

bx = 435
by = 500
bullet = []
b = Bullet(bx,by,lazer)

for n in range(4):
    for q in range(6):
        a = Alien(x,y,alien)
        aliens.append(a)
        x += 100
    x = 41
    y += 100

p = Player(400,500,player)
r = False
l = False
a = True
buhlet = True
mooove = True

while True:
    screen.fill((0,0,0))
    down = False
    if a:
         p.draw()
    prect = p.image.get_rect(topleft = (p.x,p.y))
    for z in aliens:
         z.draw()
         if mooove:
              z.move()
         if z.x >= 860 or z.x <= 0:
              down = True  
    for q in bullet:
          q.draw()
          q.move()
          brect = q.image.get_rect(topleft = (q.x,q.y))
          for k in aliens:
               arect = k.image.get_rect(topleft = (k.x,k.y))
               if brect.colliderect(arect):
                    explosion.play()
                    aliens.remove(k)
                    bullet.remove(q)
          if q.y <= 0:
               boolet = False
               bullet.remove(q)
    for ay in aliens:
         arect = ay.image.get_rect(topleft = (ay.x,ay.y))
         if prect.colliderect(arect):
                    a = False  
                    buhlet = False
                    mooove = False
                    show_text("You Lose...", 300, 300, (255,0,0), 50)
                    lose.play()
                    pygame.display.update()
                    time.sleep(5)
                    pygame.quit()
                    exit()
    if len(bullet) >= 5:
         bullet.pop()

    if down:
         for n in aliens:
              n.y += 25
              n.speed *= -1 

    if l:
            p.x -= p.playerspeed

    if r:
            p.x += p.playerspeed   
      
    for event in pygame.event.get():
        if event.type == KEYDOWN:
             if event.key == K_SPACE:
                  if buhlet:
                       b = Bullet(p.x + 35,by,lazer)
                       bullet.append(b)
             if event.key == K_LEFT:
                  l = True
             if event.key == K_RIGHT:
                  r = True
        if event.type == KEYUP:
             if event.key == K_LEFT:
                  l = False
             if event.key == K_RIGHT:
                  r = False
                  
        if event.type == QUIT:
                pygame.quit()
                exit
    if len(aliens) == 0:
         show_text("You Win!", 300, 300, (200,200,100), 50)
         win.play()
         pygame.display.update()
         time.sleep(5)
         pygame.quit()
         exit()

    clock.tick(20)
    pygame.display.update()