import sys
import os
from abc import ABC, abstractmethod
import pygame
pygame.init()
pygame.mixer.init()
import time
#from PIL import Image
import random
from itertools import permutations

global currenttextrun
currenttextrun = "placeholder"
global moveonoption

#Music
def WaltzForLilly():
  WaltzForLilly = pygame.mixer.music.load("Waltz For Lilly - 3nd.mp3")
  pygame.mixer.music.play(-1)
def Spain():
  Spain = pygame.mixer.music.load("Spain - Chick Corea.mp3")
  pygame.mixer.music.play(-1)
def Ether():
  Ether = pygame.mixer.music.load("Ether - Sungazer.mp3")
  pygame.mixer.music.play(-1)
def Slip():
  Slip = pygame.mixer.music.load("Slip - Shubh Saran.mp3")
  pygame.mixer.music.play(-1)
def Monad():
  Monad = pygame.mixer.music.load("Monad - Soil and Pimp Sessions.mp3")
  pygame.mixer.music.play(-1)
def StGeorge():
  StGeorge = pygame.mixer.music.load("St George - Wordclock.mp3")
  pygame.mixer.music.play(-1)
def Cafo():
  Cafo = pygame.mixer.music.load("Cafo - Animals as Leaders.mp3")
  pygame.mixer.music.play(-1)
def SkatinginCentralPark():
  SkatinginCentralPark = pygame.mixer.music.load("Skating in Central Park - Bill Evans and Jim Hall.mp3")
  pygame.mixer.music.play(-1)
def BlueinKyoto():
  BlueinKyoto = pygame.mixer.music.load("Blue in Kyoto - Yusuke Shima.mp3")
  pygame.mixer.music.play(-1)
def Soil():
  Soil = pygame.mixer.music.load("Soil - Mouse on the Keys.mp3")
  pygame.mixer.music.play(-1)
def YinYang():
  YingYang = pygame.mixer.music.load("Yin and Yang - Uyama Hiroto.mp3")
  pygame.mixer.music.play(-1)
def Goat():
  Goat = pygame.mixer.music.load("GOAT - Polyphia.mp3")
  pygame.mixer.music.play(-1)
#Sound Effects

Bruh = pygame.mixer.Sound("BruhSoundEffect.mp3")
Gamestartsfx = pygame.mixer.Sound("Startup.mp3")
DripGokuSoundEffect = pygame.mixer.Sound("DripGokuSound.mp3")
Objection = pygame.mixer.Sound("Objection.mp3")
Running = pygame.mixer.Sound("Running.mp3")
Transform = pygame.mixer.Sound("Tranform.mp3")
Pizza = pygame.mixer.Sound("Vine.mp3")
LesGo = pygame.mixer.Sound("Lets Go.mp3")
ExplosionSound = pygame.mixer.Sound("ExplosionSound.mp3")

class GameObject(ABC):

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def hitbox(self):
        pass

    @abstractmethod
    def tick(self):
        pass


class Player(GameObject):
    SPEED = 5
    SIZE = 30

    def __init__(self, x, y, game_size_x, game_size_y):
        self.x = x
        self.y = y
        self.game_size_x = game_size_x
        self.game_size_y = game_size_y
        self.alive = True

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Player.SIZE, Player.SIZE)

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x = max(0, min(self.x - Player.SPEED,
                                self.game_size_x - Player.SIZE))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x = max(0, min(self.x + Player.SPEED,
                                self.game_size_x - Player.SIZE))
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y = max(0, min(self.y - Player.SPEED,
                                self.game_size_y - Player.SIZE))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y = max(0, min(self.y + Player.SPEED,
                                self.game_size_y - Player.SIZE))

    def draw(self, surface):
        if self.alive:
            color = (pygame.Color('white') if self.alive
                     else pygame.Color('black'))
            pygame.draw.rect(surface, color,
                             (self.x, self.y, Player.SIZE, Player.SIZE))


class Bullet(GameObject):
    SIZE = 10

    def __init__(self, x, y, x_speed, y_speed, color=pygame.Color('white')):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Bullet.SIZE, Bullet.SIZE)

    def tick(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, Bullet.SIZE, Bullet.SIZE))
class Game:

    def __init__(self, size_x, size_y, ticks_per_bullet=10):
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.field = pygame.Rect(0, 0, size_x, size_y)
        self.player = Player(self.size_x // 2, self.size_y // 2,
                             self.size_x, self.size_y)
        self.bullets = []
        self.font = pygame.font.Font(None, 30)
        self.score = 0
        self.ticks_per_bullet = ticks_per_bullet

    def tick(self):
        self.player.tick()
        for bullet in self.bullets:
            bullet.tick()

        bullet_hitboxes = [b.hitbox() for b in self.bullets]

        self.bullets = [self.bullets[i] for i
                        in self.field.collidelistall(bullet_hitboxes)]

        if (self.player.alive and
                self.player.hitbox().collidelist(bullet_hitboxes) != -1):
            self.player.alive = False
            self.bullets += Game.death_explosion(self.player.x, self.player.y)

        if self.player.alive:
            self.score += 1

        if self.player.alive and not random.randrange(self.ticks_per_bullet):
            self.bullets.append(self.random_bullet())

    def draw(self, surface):
        self.player.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        self.draw_score(surface)
        if not self.player.alive:
            self.draw_newgame_message(surface)

    def random_bullet(self):
        max_speed = 3
        speed_x, speed_y = 0, 0
        while speed_x == 0 and speed_y == 0:
            speed_x = random.randrange(-max_speed, max_speed)
            speed_y = random.randrange(-max_speed, max_speed)
        axis = random.choice('xy')
        if axis == 'x':
            position_x = random.randrange(self.size_x)
            position_y = 0 if speed_y > 0 else self.size_y
        else:
            position_y = random.randrange(self.size_y)
            position_x = 0 if speed_x > 0 else self.size_x
        return Bullet(position_x, position_y, speed_x, speed_y)

    def draw_score(self, surface):
        rendered_text = self.font.render('{}'.format(self.score), True,
                                         pygame.Color('white'))
        surface.blit(rendered_text, (10, 10))

    def draw_newgame_message(self, surface):
        rendered_text = self.font.render('Press SPACE for new game', True,
                                         pygame.Color('white'))
        surface.blit(rendered_text,
                     (10, self.size_y - rendered_text.get_height() - 10))

    def death_explosion(x, y):
        pygame.mixer.Sound.play(Bruh)
        return list([Bullet(x, y, xs, ys, pygame.Color('white')) for xs, ys
                     in permutations(list(range(-10, 10)), 2)
                     if (xs, ys) != (0, 0)])

font = pygame.font.Font('freesansbold.ttf', 16)
black = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((1250, 750)) #Creates the window
pygame.display.set_caption("Sprite Test") #Window caption
clock = pygame.time.Clock()

images = [
pygame.image.load("Amber Angry.png"), 
pygame.image.load("Amber Default.png"), 
pygame.image.load("Amber Happy.png"), 
pygame.image.load("Cadence Angry.png"), 
pygame.image.load("Cadence Default.png"), 
pygame.image.load("Cadence Happy.png"), 
pygame.image.load("Rosie Angry.png"), 
pygame.image.load("Rosie Default.png"), 
pygame.image.load("Rosie Happy.png"), 
pygame.image.load("Sam Angry.png"), 
pygame.image.load("Sam Default.png"), 
pygame.image.load("Sam Happy.png"), 
pygame.image.load("Goku.png")
] #Just creates a list of the images

titlebg = pygame.image.load("Title BG.png")
bg1 = pygame.image.load("Mountain BG.png")
bg2 = pygame.image.load("Classroom BG.png")
bg3 = pygame.image.load("Goku BG.png")
bg4 = pygame.image.load("Jazz BG.png")
bg5 = pygame.image.load("Soccer BG.png")
bb = pygame.image.load("Battlebox.png")
bd = pygame.image.load("Backdrop.png")
tb = pygame.image.load("Text Box.png")
ch = pygame.image.load("Character Holder.png")
bg6 = pygame.image.load("Credit BG.png")
fakebg1 = pygame.image.load("Cheat.png")
fakebg2 = pygame.image.load("Cheat2.png")
fakebg3 = pygame.image.load("Cheat3.png")
fakebg4 = pygame.image.load("Cheat4.png")
fakebg5 = pygame.image.load("Cheat5.png")
x = 50
y= 100
width = 100
height = 100

currenttextrun = ""


#Sets initial values so that everything doesn't pop up at once
sprite1load = False 
sprite2load = False
sprite3load = False
sprite4load = False
sprite5load = False
sprite6load = False
sprite7load = False
sprite8load = False
sprite9load = False
sprite10load = False
sprite11load = False
sprite12load = False
sprite13load = False

#Loads the images
AmberAng = pygame.image.load("Amber Angry.png")
AmberAngSmol = pygame.image.load("Amber Angry smol.png")
AmberDef = pygame.image.load("Amber Default.png")
AmberDefSmol = pygame.image.load("Amber Default smol.png")
AmberHap = pygame.image.load("Amber Happy.png")
AmberHapSmol = pygame.image.load("Amber Happy smol.png")
CadenceAng = pygame.image.load("Cadence Angry.png")
CadenceAngSmol = pygame.image.load("Cadence Angry smol.png")
CadenceDef = pygame.image.load("Cadence Default.png")
CadenceDefSmol = pygame.image.load("Cadence Default smol.png")
CadenceHap = pygame.image.load("Cadence Happy.png")
RosieAng = pygame.image.load("Rosie Angry.png")
RosieAngSmol = pygame.image.load("Rosie Angry smol.png")
RosieDef = pygame.image.load("Rosie Default.png")
RosieDefSmol = pygame.image.load("Rosie Default smol.png")
RosieHap = pygame.image.load("Rosie Happy.png")
RosieHapSmol = pygame.image.load("Rosie Happy smol.png")
SamAng = pygame.image.load("Sam Angry.png")
SamAngSmol = pygame.image.load("Sam Angry smol.png")
SamDef = pygame.image.load("Sam Default.png")
SamDefSmol = pygame.image.load("Sam Default smol.png")
SamHap = pygame.image.load("Sam Happy.png")
SamHapSmol = pygame.image.load("Sam Happy smol.png")
ExclamationMark = pygame.image.load("Exclamation Mark.png")
Goku = pygame.image.load("Goku.png")
Objectionimg = pygame.image.load("Objection.png")
DaBaby = pygame.image.load("DaBaby.png")
Convertible = pygame.image.load("Convertible.png")
Explosion = pygame.image.load("Explode.png")
Creators = pygame.image.load("Creators.png")


def redrawWindow():
  win.fill((255,255,255))
  win.blit(bg5, (0,0))
  win.blit(Goku, (x,y))

SIZE_X = 500
SIZE_Y = 500


def Level1():
  WaltzForLilly()
  def accgame():
    TICKS_PER_BULLET = 50
    def text1():
      win.blit(AmberDef, (x, y))    
      text = font.render('Ok let\'s begin. Start by moving up, down, left and right with ', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 650)
      win.blit(text, textRect)
      text2 = font.render('W, S, A and D', True, black)
      textRect2 = text2.get_rect()
      textRect2.center = (600, 675)
      win.blit(text2, textRect2)
      pygame.display.update()
    def text2():
      win.blit(AmberHap, (x, y))    
      text = font.render('Great job!', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text3():
      win.blit(AmberDef, (x, y))    
      text = font.render('Make sure to avoid all of the white pellets!', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text4():
      win.blit(AmberHap, (x, y))    
      text = font.render('Nice going!', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text5():
      win.blit(AmberDef, (x, y))    
      text = font.render('Now try to get your score all the way to 5000! Your score is', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 650)
      win.blit(text, textRect)
      text2 = font.render('in the corner', True, black)
      textRect2 = text2.get_rect()
      textRect2.center = (600, 675)
      win.blit(text2, textRect2)
      pygame.display.update()
    def drawfunc():
      win.blit(bg1, (0,0)) #Draws the Background
      win.blit(bd, (360, 100)) #This where the game will go
      #win.blit(bb, (325,50))
      win.blit(tb, (350, 600))
      win.blit(ch, (50, 100))
      pygame.display.update()
    def wincon():
      pygame.QUIT
    def bullethellgame():
      k = 0
      
      screen = win#pygame.display.set_mode((SIZE_X, SIZE_Y))
      #clock = pygame.time.Clock(

      game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
      game_exit = False
      while not game_exit:
        if k == 0:
            drawfunc()
            text1()
        if k == 600:
            drawfunc()
            text2()
        if k == 900:
            drawfunc()
            text3()
        if k == 1500:
            drawfunc()
            text4()
        if k == 1800:
            drawfunc()
            text5()
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          accgame()
            
        def gamergame():
          game.tick()
          game.draw(foreground)
          screen.blit(fakebg1, (360, 100))
          screen.blit(foreground, (360, 100))
          pygame.display.flip()
        if k <= 5000:
          gamergame()
        k += 1
        if k == 5000:
          pygame.mixer.music.pause()
          scene2()
        clock.tick(60)

      pygame.quit()
    bullethellgame()
  accgame()

def Level2():
  Slip()
  def accgame():
    TICKS_PER_BULLET = 20
    def text1():
      win.blit(CadenceDef, (x, 100))    
      text = font.render('And a 1, and 2, and 3, and 4, and lets go', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text2():
      win.blit(CadenceAng, (x, 100))    
      text = font.render("You're not bad, for RCM Level 2 material", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text3():
      win.blit(CadenceAng, (x, 100))    
      text = font.render("Please, what do you know about reharmonization", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text4():
      win.blit(CadenceDef, (x, 100))    
      text = font.render("Oops, looks like I played a bit chromatic", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update() 
    def drawfunc():
      win.blit(bg4, (0,0))
      win.blit(bd, (360, 100)) #This where the game will go
      #win.blit(bb, (325,50))
      win.blit(tb, (350, 600))
      win.blit(ch, (50, 100))
      pygame.display.update() #Updates screen
    def wincon():
      pygame.QUIT
    def bullethellgame():
      k = 0
      
      screen = win#pygame.display.set_mode((SIZE_X, SIZE_Y))
      #clock = pygame.time.Clock(

      game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
      game_exit = False
      while not game_exit:
        if k == 0:
            drawfunc()
            text1()
        if k == 500:
            drawfunc()
            text2()
        if k == 2500:
            drawfunc()
            text3()
        if k == 5000:
            drawfunc()
            text4()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          if k >= 5000:
              pygame.mixer.music.pause()
              scene3()
          else:
              accgame()
        def gamergamer():
          game.tick()
          game.draw(foreground)
          screen.blit(fakebg2, (360, 100))
          screen.blit(foreground, (360, 100))
          pygame.display.flip()
        if k <= 5000:
          gamergamer()
        k += 1

        clock.tick(60)

      pygame.quit()
    bullethellgame()
  accgame()

def Level3():
  Ether()
  def accgame():
    TICKS_PER_BULLET = 15
    def text1():
      win.blit(RosieHap, (x, 100))    
      text = font.render('Pawn to e4', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text2():
      win.blit(RosieDef, (x, 100))    
      text = font.render("Careful not to blunder!", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text3():
      win.blit(RosieHap, (x, 100))    
      text = font.render("Knight takes on f5", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text4():
      win.blit(RosieAng, (x, 100))    
      text = font.render("Ah, the classic smothermate", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update() 
    def drawfunc():
      win.blit(bg2, (0,0))
      win.blit(bd, (360, 100)) #This where the game will go
      #win.blit(bb, (325,50))
      win.blit(tb, (350, 600))
      win.blit(ch, (50, 100))
      pygame.display.update() #Updates screen
    def wincon():
      pygame.QUIT
    def bullethellgame():
      k = 0
      
      screen = win#pygame.display.set_mode((SIZE_X, SIZE_Y))
      #clock = pygame.time.Clock(

      game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
      game_exit = False
      while not game_exit:
        if k == 0:
            drawfunc()
            text1()
        if k == 500:
            drawfunc()
            text2()
        if k == 2500:
            drawfunc()
            text3()
        if k == 5000:
            drawfunc()
            text4()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          if k >= 5000:
              pygame.mixer.music.pause()
              scene4()
          else:
              accgame()
        def gamergame():
          game.tick()
          game.draw(foreground)
          screen.blit(fakebg3, (360, 100))
          screen.blit(foreground, (360, 100))
          pygame.display.flip()
        if k <= 5000:
          gamergame()
        k += 1

        clock.tick(60)

      pygame.quit()
    bullethellgame()
  accgame()

def Level4():
  Monad()
  def accgame():
    TICKS_PER_BULLET = 10
    def text1():
      win.blit(SamDef, (x, 100))    
      text = font.render('Get ready to throw the pigskin around', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text2():
      win.blit(SamHap, (x, 100))    
      text = font.render("Alright nice pass", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text3():
      win.blit(SamAng, (x, 100))    
      text = font.render("COME ON GUYS WE NEED TO WIN THIS", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def text4():
      win.blit(SamDef, (x, 100))    
      text = font.render("I can't believe we lost", True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update() 
    def drawfunc():
      win.blit(bg5, (0,0))
      win.blit(bd, (360, 100)) #This where the game will go
      #win.blit(bb, (325,50))
      win.blit(tb, (350, 600))
      win.blit(ch, (50, 100))
      pygame.display.update() #Updates screen
    def wincon():
      pygame.QUIT
    def bullethellgame():
      k = 0
      
      screen = win#pygame.display.set_mode((SIZE_X, SIZE_Y))
      #clock = pygame.time.Clock(

      game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
      game_exit = False
      while not game_exit:
        if k == 0:
            drawfunc()
            text1()
        if k == 500:
            drawfunc()
            text2()
        if k == 2500:
            drawfunc()
            text3()
        if k == 5000:
            drawfunc()
            text4()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          if k >= 5000:
              pygame.mixer.music.pause()
              scene5()
          else:
              accgame()
        elif keys[pygame.K_1]:
          k = 5000
        def gamergame():
          game.tick()
          game.draw(foreground)
          screen.blit(fakebg4, (360, 100))
          screen.blit(foreground, (360, 100))
          pygame.display.flip()
        if k <= 5000:
          gamergame()
        k += 1

        clock.tick(60)

      pygame.quit()
    bullethellgame()
  accgame()

def Level5():
  Cafo()
  def accgame(): 
    TICKS_PER_BULLET = 1
    def text1():
      win.blit(Goku, (x, 100))    
      text = font.render('when the imposter is sus', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 665)
      win.blit(text, textRect)
      pygame.display.update()
    def drawfunc():
      win.blit(bg3, (0,0))
      win.blit(bd, (360, 100)) #This where the game will go
      #win.blit(bb, (325,50))
      win.blit(tb, (350, 600))
      win.blit(ch, (50, 100))
      pygame.display.update() #Updates screen
    def wincon():
      pygame.QUIT
    def bullethellgame():
      k = 0
      
      screen = win#pygame.display.set_mode((SIZE_X, SIZE_Y))
      #clock = pygame.time.Clock(

      game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
      game_exit = False
      while not game_exit:
        if k == 0:
            drawfunc()
            text1()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          if k >= 5000:
              GokuScene()
          else:
              accgame()
        elif keys[pygame.K_1]:
          k = 5000
        def gamergame():
          game.tick()
          game.draw(foreground)
          screen.blit(fakebg5, (360, 100))
          screen.blit(foreground, (360, 100))
          pygame.display.flip()
        if k <= 5000:
          gamergame()
        k += 1

        clock.tick(60)

      pygame.quit()
    bullethellgame()
  accgame()

  
def TitleScreen(): #This is where the fade isnt working
  Spain()

  def drawfunc():
    win.fill((255,255,255))
    win.blit(titlebg, (0,0))
    pygame.display.update() #Updates screen
  def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((255,255,255))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        drawfunc()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
  win.blit(titlebg, (0,0))
  pygame.display.update()
  run = True
  while run: #Main function
     #Updates screen
    clock.tick(60) #60FPS
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          pygame.mixer.music.pause()
          pygame.mixer.Sound.play(Gamestartsfx)
          fade(1250, 773)
          gamestart()
        elif event.key == pygame.K_e:
          pass
  pygame.quit



def gamestart():

  SkatinginCentralPark()

  def text2():
    text = font.render('Have you played the new Bullet Hell? It\'s all the rage', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text3():
    win.blit(AmberHapSmol, (440, 170))    
    text = font.render('Here I\'ll teach you how to play!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text4():
    win.blit(AmberHapSmol, (440, 170))    
    text = font.render('Don\'t you remember me? It\'s Amber!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def drawfunc():
    win.blit(bg5, (0, 0))
    win.blit(AmberDefSmol, (440, 170))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text = font.render('Hey there Y/N! It\'s been a while!', True, black)
  textRect = text.get_rect()
  textRect.center = (500, 565)
  win.blit(text, textRect)
  pygame.display.update()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text4()
            i += 1
          elif i == 1:
            drawfunc()
            text2()
            i += 1
          elif i == 2:
            drawfunc()
            text3()
            i += 1
          elif i == 3:
            pygame.mixer.music.pause()
            Level1()
          
def scene2():

  BlueinKyoto()
  def text2():
    win.blit(AmberAngSmol, (440, 170))    
    text = font.render('Oh would you look at that. It\'s Cadence' , True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text3():
    win.blit(AmberAngSmol, (440, 170))    
    text = font.render('She\'s the leader of the Jazz Band and a total snob', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text4():
    win.blit(CadenceAngSmol, (440, 170))    
    text = font.render('Well hello there Amber. Funny seeing you around', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text5():
    win.blit(CadenceDefSmol, (440, 170))    
    text = font.render('Haven\'t seen you before. Amber your GF?', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 550)
    win.blit(text, textRect)
    text2 = font.render('Poor taste if you ask me', True, black)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 575)
    win.blit(text2, textRect2)
    pygame.display.update()
  def text6():
    win.blit(CadenceAngSmol, (440, 170))    
    text = font.render('Whatever, doesn\'t matter. Let\'s see who\'s better at', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 550)
    win.blit(text, textRect)
    text2 = font.render('Space Invaders', True, black)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 575)
    win.blit(text2, textRect2)
    pygame.display.update()      
  def text7():
    win.blit(AmberAngSmol, (440, 170))    
    text = font.render('Grrrr, go get her Y/N', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()     
  def text1():
    win.blit(AmberHapSmol, (440, 170))
    text = font.render('Well that was fun!', True, black)
    textRect = text.get_rect()
    textRect.center = (500, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def drawfunc():
    win.blit(bg2, (0, 0))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text1()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text2()
            i += 1
          elif i == 1:
            drawfunc()
            text3()
            i += 1
          elif i == 2:
            drawfunc()
            text4()
            i += 1
          elif i == 3:
            drawfunc()
            text5()
            i += 1
          elif i == 4:
            drawfunc()
            text6()
            i += 1
          elif i == 5:
            drawfunc()
            text7()
            i += 1
          elif i == 6:
            pygame.mixer.music.pause()
            Level2()

def scene3():
  Soil()
  def text2():
    win.blit(CadenceAngSmol, (440, 170))    
    text = font.render('Looks like I\'ve got to go practice' , True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text3():
    win.blit(AmberDefSmol, (440, 170))    
    text = font.render('Next up we have Rosie, leader of the chess club', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text4():
    win.blit(RosieHapSmol, (440, 170))    
    text = font.render('Hey there Amber, good to see you!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text5():
    win.blit(RosieDefSmol, (440, 170))    
    text = font.render('Are you the new competitor?', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text6():
    win.blit(RosieHapSmol, (440, 170))    
    text = font.render('I look forward to our match!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()      
  def text7():
    win.blit(AmberHapSmol, (440, 170))    
    text = font.render('Good luck! Y/N', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()     
  def text1():
    win.blit(AmberHapSmol, (440, 170))
    text = font.render('Great job Y/N', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def drawfunc():
    win.blit(bg2, (0, 0))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text1()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text2()
            i += 1
          elif i == 1:
            drawfunc()
            text3()
            i += 1
          elif i == 2:
            drawfunc()
            text4()
            i += 1
          elif i == 3:
            drawfunc()
            text5()
            i += 1
          elif i == 4:
            drawfunc()
            text6()
            i += 1
          elif i == 5:
            drawfunc()
            text7()
            i += 1
          elif i == 6:
            pygame.mixer.music.pause()
            Level3()

def scene4():
  YinYang()
  def text2():
    win.blit(AmberDefSmol, (440, 170))    
    text = font.render('Our next opponent is Sam, the captain of the football team.' , True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text3():
    win.blit(AmberDefSmol, (440, 170))    
    text = font.render('They\'re just getting ready for their next game', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text4():
    win.blit(SamDefSmol, (440, 170))    
    text = font.render('You the new guy?', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text5():
    win.blit(SamHapSmol, (440, 170))    
    text = font.render('Alright let\'s get ready!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text1():
    win.blit(RosieHapSmol, (440, 170))
    text = font.render('Good Game!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def drawfunc():
    win.blit(bg2, (0, 0))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text1()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text2()
            i += 1
          elif i == 1:
            drawfunc()
            text3()
            i += 1
          elif i == 2:
            drawfunc()
            text4()
            i += 1
          elif i == 3:
            drawfunc()
            text5()
            i += 1
          elif i == 4:
            pygame.mixer.music.pause()
            Level4()

def scene5():
  StGeorge()
  def text2():
    win.blit(AmberDefSmol, (440, 170))    
    text = font.render('Ok so up next we have...' , True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text3():
    win.blit(ExclamationMark, (440, 170))    
    text = font.render('', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text4():
    win.blit(Goku, (440, 170))
    text = font.render('', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
    pygame.mixer.Sound.play(DripGokuSoundEffect)
  def text5():
    win.blit(Goku, (440, 170))    
    text = font.render('OH MY GOD IT\'S FUCKING GOKU', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def text1():
    win.blit(AmberHapSmol, (440, 170))
    text = font.render('Nice one Y/N!', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def drawfunc():
    win.blit(bg2, (0, 0))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text1()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text2()
            i += 1
          elif i == 1:
            drawfunc()
            text3()
            i += 1
          elif i == 2:
            drawfunc()
            text4()
            i += 1
          elif i == 3:
            drawfunc()
            text5()
            i += 1
          elif i == 4:
            pygame.mixer.music.pause()
            Level5()


def GokuScene():
  def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((255,255,255))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)
  def text2():
    win.blit(DaBaby, (440, 170))    
    text = font.render('DABABY??!.' , True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
    pygame.mixer.Sound.play(LesGo)
    pygame.mixer.Sound.play(Transform)
  def text4():
    drawfunc()
    win.blit(Convertible, (440, 170))    
    text = font.render('HOLY FUCKING SHIT', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
  def dababymove():
      drawfunc()
      win.blit(Goku, (440, 170))    
      text = font.render('HOLY FUCKING SHIT', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 565)
      win.blit(text, textRect)
      pygame.display.update()
      time.sleep(2.5)
      drawfunc()
      win.blit(Goku, (440, 170))    
      win.blit(Explosion, (340, 170))
      text = font.render('HOLY FUCKING SHIT', True, black)
      textRect = text.get_rect()
      textRect.center = (600, 565)
      win.blit(text, textRect)
      pygame.display.update()
      pygame.mixer.Sound.play(ExplosionSound)
      pygame.mixer.Sound.play(Pizza)
  def text5():
    text = font.render('You Win', True, black)
    textRect = text.get_rect()
    textRect.center = (625, 380)
    win.blit(text, textRect)
    pygame.display.update()
  def text1():
    win.blit(Objectionimg, (440, 170))
    text = font.render('STOP RIGHT THERE CRIMINAL SCUM', True, black)
    textRect = text.get_rect()
    textRect.center = (600, 565)
    win.blit(text, textRect)
    pygame.display.update()
    pygame.mixer.Sound.play(Objection)
  def drawfunc():
    win.blit(bg3, (0, 0))
    win.blit(tb, (350, 500))
    pygame.display.update()
  drawfunc()
  text1()
  i = 0
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if i == 0:
            drawfunc()
            text2()
            i += 1
          elif i == 1:
            fade(1250, 773)
            text4()
            i += 1
          elif i == 2:
            drawfunc()
            dababymove()
            i += 1
          elif i == 3:
            drawfunc()
            text5()
            i += 1
          elif i == 4:
            pygame.mixer.music.pause()
            Credits()

def Credits():
  Goat()
  win.blit(bg6, (0, 0))
  win.blit(Creators, (425, 150))
  text = font.render('Made by Ciaran Morris, and Selasie Gifa-Johnson', True, white)
  textRect = text.get_rect()
  textRect.center = (600,500)
  win.blit(text, textRect)
  pygame.display.update()
  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          pygame.QUIT

#def resizer():
#  basewidth = 350
#  img = Image.open('Cadence Default.png')
#  wpercent = (basewidth/float(img.size[0]))
#  hsize = int((float(img.size[1])*float(wpercent)))
#  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#  img.save('Cadence Default smol.png')

def levelselector():
  levelselect = input("Please choose a level (1/2/3/4/5)")
  if levelselect == "1":
    Level1()
  elif levelselect == "2":
    Level2()
  elif levelselect == "3":
    Level3()
  elif levelselect == "4":
    Level4()
  elif levelselect == "5":
    Level5()
  elif levelselect == "title":
    TitleScreen()
  elif levelselect == "scene1":
    gamestart()
  #elif levelselect == "resize":
  #  resizer()
  elif levelselect == "scene2":
    scene2()
  elif levelselect == "scene3":
    scene3()
  elif levelselect == "scene4":
    scene4()
  elif levelselect == "scene5":
    scene5()
  elif levelselect == "Goku":
    GokuScene()
  elif levelselect == "Credits":
    Credits()
  #elif levelselect == "bh":
   # bullethellgame()
  #elif levelselect == "GokuIntro":
    #GokuIntro()
  else:
    print("Error, please try again")
    levelselector()
TitleScreen()



#Friday:
#1.) Fix the fading in line 327 Done
#2.) Continue the scene scripting (at least finish first scene)
#3.) MOST IMPORTANT: Get level 5 Bullethell to work 
#4.) Print to textboxes
#Saturday:
#1.) Fix any bugs
#2.) Get space invaders at least semi working
#3.) Scene script up to battle 3
#Sunday:
#1.) Fix any bugs
#2.) Finish all scene scipting except for last level finale
#3.) Add slow text and any sound effects
#Monday:
#1.) ALL BUGS MUST BE FIXED
#2.) Do finale scene scripting
#3.) Add admin panel
#4.) Finalize the project
#5.) Any other changes made. DUE TUESDAY!!
#Make it pretty if we have time1
#https://replit.com/join/twbdzqdf-ciaranmorris