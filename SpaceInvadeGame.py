import pygame
import sys
import time
import random
import math
#from bulletHellObjects import Player, Bullet
from itertools import permutations

#from bulletHell import BHGame

"""
|----------|
|REFERENCES|
|----------|

FPS management:
https://www.youtube.com/watch?v=-GzQA_Q0Z_o

event handling:
https://riptutorial.com/pygame/example/18046/event-loop

general methods:
https://www.pygame.org/docs/

typewriter effect:
https://stackoverflow.com/questions/41101662/typewriter-effect-pygame

Level switching inspiration:
https://www.youtube.com/watch?v=A6eSzbllWbM&list=WL&index=28

Menu stuff:
https://www.youtube.com/watch?v=bmRFi7-gy5Y&list=WL&index=36
    
"""


"""
{
    "python.linting.pylint": [
    "- -ignored-modules=pygame"
    ]
}
"""

class Game():
#    def __init__(self):
 #       pygame.init()
  #      self.running, self.playing = True, False
   #     self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, F#alse, False
     #   self.DISPLAY_W, self.DISPLAY_H = 800, 600
      #  self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H)) # secondary surface
       # self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H))) #main screen
#        self.caption = pygame.display.set_caption('S.I.A-G.D.G') ##High School: a day i#n the life ## Space invaders with anime girls and drip Goku
  #      #self.font_name = 'fonts/NixieOne.ttf'
   #     #self.font_name = pygame.font.get_default_font()
    #    self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
     #   self.main_menu = MainMenu(self)
      #  self.Instructions = InstructionsMenu(self)
       # self.credits = CreditsMenu(self)
        #self.currMenu = self.main_menu
        self.level = 1 
 #       self.clock = pygame.time.Clock()
  #      self.FPS = 120



    def drawText(self, text, size, x, y, font='/usr/share/fonts/truetype/freefont/FreeSans.ttf', opacity=300 ):
        font = pygame.font.Font(font,size)
        textSurface = font.render(text, True, self.WHITE)
        textSurface.set_alpha(opacity)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)


    def clearScreen(self):
        self.display.fill(self.BLACK)

    def newDialog(self, text, height=350):
        self.clearScreen()
        self.drawText(text, 20, self.DISPLAY_W/2, height)
        self.drawText("press enter to continue", 10, self.DISPLAY_W/2, 480)
        self.window.blit(self.display, (0,0))

    def newDialogNoCls(self, text, height=350):
        self.drawText(text, 20, self.DISPLAY_W/2, height)
        self.drawText("press enter to continue", 10, self.DISPLAY_W/2, 480)
        self.window.blit(self.display, (0,0))

    def gameLoop(self):
        while self.playing:
            ## LEVEL ONE (TUTORIAL) LOOP ##
            while self.level == 1:
                self.clock.tick(self.FPS)
                self.LevelOneDia()
                if self.LevelOne() == 'win':
                    #add win stuff/pics here
                    pass
                elif self.LevelOne() == 'lose':
                    #add lose stuff/pics here
                    pass

                self.resetKeys()

            ## LEVEL TWO LOOP ##
            while self.level == 2:
                self.clock.tick(self.FPS)
                self.LevelTwoDia()
                if self.LevelTwo() == 'win':
                    #add win stuff/pics here
                    pass
                elif self.LevelTwo() == 'lose':
                    #add lose stuff/pics here
                    pass

                self.resetKeys()

            ## LEVEL THREE LOOP ##
            while self.level == 3:
                self.clock.tick(self.FPS)
                self.LevelThreeDia()
                if self.LevelThree() == 'win':
                    #add win stuff/pics here
                    pass
                elif self.LevelThree() == 'lose':
                    #add lose stuff/pics here
                    pass

                self.resetKeys()
            
            ## LEVEL FOUR LOOP ##
            while self.level == 4:
                self.clock.tick(self.FPS)
                self.LevelFourDia()
                if self.LevelFour() == 'win':
                    #add win stuff/pics here
                    pass
                elif self.LevelFour() == 'lose':
                    #add lose stuff/pics here
                    pass

                self.resetKeys()

            ## LEVEL FIVE (BOSS) LOOP ##
            while self.level == 5:

                self.LevelFiveDia()

                print("inside leve 5")
                #pygame.mixer.music.fadeout(1000)
                #pygame.mixer.music.load('music\Goku Mode.mp3')
                #pygame.mixer.music.play(-1)
                SIZE_X = 800
                SIZE_Y = 600
                TICKS_PER_BULLET = 5

                pygame.font.init()
                pygame.init()
                pygame.display.set_caption('pyBullethell')

                screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
                clock = pygame.time.Clock()

                bulletHell = BHGame(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
                bulletHell_exit = False
                while not bulletHell_exit:
                    print("game loop exit state: " + str(bulletHell_exit))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            bulletHell_exit = True
                    foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
                    foreground.fill(pygame.Color('black'))

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        bulletHell = BHGame(SIZE_X, SIZE_Y, TICKS_PER_BULLET)

                    bulletHell_exit = bulletHell.tick()
                    bulletHell.draw(foreground)

                    if bulletHell.win():
                        print("bullethell won and exited")
                        bulletHell_exit = True

                    screen.fill((60, 70, 90))
                    screen.blit(foreground, (0, 0))
                    pygame.display.flip()

                    clock.tick(60)
                self.clearScreen()
                #pygame.quit()### fix game ending

                ## end of game dialog ##
                self.EndGameDia()
                self.playing = False

            self.checkEvents()
            if self.BACK_KEY:
                self.playing= False

            self.display.fill(self.BLACK)
            self.drawText('outside of game loop', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))



            pygame.display.update()
            self.resetKeys()



    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.level = False, False, 0
                self.currMenu.runDisplay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False



    def wait(self, text="", fsize=7):
        a = True
        while a == True:
            self.clearScreen()
            h = 350
            textList = text.split("\n")
            if len(textList) > 1:
                for i in range(len(textList)):
                    h += 20
                    self.newDialogNoCls(textList[i], h)
            else:
                self.newDialog(textList[0])

            pygame.display.update()
            self.drawText("press enter to continue", fsize, self.DISPLAY_W/2, 450)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    print("enter pressed")
                    self.clearScreen()
                    a = False
            pygame.display.update()

    ##---------------------------##
    ## LEVEL ONE DIALOG FUNCTION ##
    ##---------------------------##
    def LevelOneDia(self):
        #pygame.mixer.music.fadeout(1000)
        #song = 'music\Comping.wav'
        #song = pygame.mixer.music.load(song)
        #pygame.mixer.music.play(-1)

        self.checkEvents()
        if self.START_KEY:
            self.level = 0
            self.playing = False

        self.clearScreen()
        #self.diaBox = pygame.image.load('Text Box.png') #working
        self.drawText('inside of game loop', 20, self.DISPLAY_W/2, 350)
        self.window.blit(self.display, (0,0))
        #self.window.blit(self.diaBox, (0,0)) #working

        self.wait("Cuck Cumber: Hey! How are you? It’s been a while")
        self.wait("Cuck Cumber: Have you heard about the new space invaders game?\n It’s all the rage")
        self.wait("Cuck Cumber: Here! I’ll teach you how to play!")
        print("done dia")


    ##-------------------------##
    ## LEVEL ONE GAME FUNCTION ##
    ##-------------------------##
    def LevelOne(self):
        #pygame.mixer.music.fadeout(1000)
        screen = self.window
        player_img = pygame.image.load("LevelOneAssets/spaceship.png")
        playerX, playerY = 336, 480
        playerX_change, playerY_change = 0, 0

        alien_img = []
        alienX = []
        alienY = []
        alienX_change = []
        alienY_change = []
        num_of_enemies = 7

        bullet_img = pygame.image.load("LevelOneAssets/bullet.png")
        bulletX, bulletY = 0, 480
        bulletX_change, bulletY_change = 0, 15
        bullet_state = "ready"

        background = pygame.image.load("LevelOneAssets/space_invaders_background3.png")
        game_end = pygame.image.load("LevelOneAssets/game_over(800x600).png")

        lives, livesX, livesY = 1, 10, 10
        score_value = 0
        font = pygame.font.Font("freesansbold.ttf", 32)
        textX, textY = 10, 40

        for i in range(num_of_enemies):
            alien_img.append(pygame.image.load("LevelOneAssets/alien.png"))
            alienX.append(random.randint(1, 735))
            alienY.append(random.randint(1, 350))
            alienX_change.append(2)
            alienY_change.append(40)

        def gameLoopDrawText(text, size, x, y, font='NixieOne.ttf', opacity=300):
            font = pygame.font.Font(font,size)
            screen = font.render(text, True, (255,255,0))
            screen.set_alpha(opacity)
            textRect = screen.get_rect()
            textRect.center = (x,y)
            screen.blit(screen,textRect)
        

        def game_over():
            if lives == 0:
                return "lose"
                screen.blit(game_end, (0, 0))

        def win_game():
            if score_value == 30:
                self.level += 1
                return "win"

        def pause():
            self.FPS = 0
            while self.paused:
                screen2 = screen
                screen2.set_alpha(150)
                tutfont = pygame.font.Font("fonts\Pixeboy-z8XGD.ttf", 30)
                tutMessage1 = tutfont.render("PAUSED", True, self.WHITE)
                screen2.blit(tutMessage1, (self.DISPLAY_W / 2 - 300 , self.DISPLAY_H /2))
                screen.blit(screen2, (0,0))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.FPS = 30
                    self.paused = False
                pygame.display.update()
            pygame.display.update()

        def showLevel(X, Y):
            lives_num = font.render("level -  " + str(self.level), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def health(X, Y):
            lives_num = font.render("Health -  " + str(lives), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def show_score(X, Y):
            score = font.render("Score - " + str(score_value) + " / 30", True, (132, 43, 215))
            screen.blit(score, (X, Y))

        def player(X, Y):
            screen.blit(player_img, (X, Y))


        def alien(X, Y, i):
            screen.blit(alien_img[i], (X, Y))

        def clearSreen2():
            self.display.fill((0, 0, 0, 0))

        def tutorial(score_value):
            while self.tutState:
                self.clearScreen()
                screen2 = screen
                screen2.set_alpha(150)
                tutfont = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 30)
                tutMessage1 = tutfont.render("Use left and right arrow keys to move and", True, self.WHITE)
                tutMessage2 = tutfont.render("press space to fire", True, self.WHITE)
                screen2.blit(tutMessage1, (self.DISPLAY_W / 2 - 300 , self.DISPLAY_H /2))
                screen2.blit(tutMessage2, (self.DISPLAY_W / 2 - 300 , self.DISPLAY_H /2 + 20))
                screen.blit(screen2, (0,0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        clearSreen2()
                        self.tutState = False
                pygame.display.update()

            """ PAUSE WIP
            while score_value == 15:
                self.clearScreen()
                screen2 = screen
                screen2.set_alpha(150)
                tutfont = pygame.font.Font("fonts\Pixeboy-z8XGD.ttf", 30)
                tutMessage1 = tutfont.render("Good job keep it up!", True, self.WHITE)
                screen2.blit(tutMessage1, (self.DISPLAY_W / 2 - 300 , self.DISPLAY_H /2))
                screen.blit(screen2, (0,0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        clearSreen2()
                        score_value += 1
                print("YAAAAAAAAAAA YEEEEAAAAATTTTTTEEEEE")
                pygame.display.update()
            """





        def bullet(X, Y):
            global bullet_state
            bullet_state = "fire"
            screen.blit(bullet_img, (X + 16, Y + 10))


        def is_collisison(alienX, alienY, bulletX, bulletY):
            distance = math.sqrt((alienX - bulletX) ** 2 + (alienY - bulletY) ** 2)
            if distance < 40:
                return True
            else:
                return False

        running1 = True
        while running1:

            self.clock.tick(self.FPS)

                # RGB
            screen.fill((132, 43, 215))

            screen.blit(background, (0, 0))


            if playerX > 735:
                playerX = 735
            elif playerX < 0:
                playerX = 0

            if playerY > 540:
                playerY = 540
            if playerY < 0:
                playerY = 0

            for i in range(num_of_enemies):
                alienX[i] += alienX_change[i]
                if alienX[i] > 735:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = -1
                elif alienX[i] < 0:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = 1

                collision = is_collisison(alienX[i], alienY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    alienX[i] = random.randint(1, 735)
                    alienY[i] = random.randint(1, 350)
                    #explosion_sound = mixer.Sound("LevelOneAssets/explosion.wav")
                    #explosion_sound.play()
                alien(alienX[i], alienY[i], i)
                if alienY[i] >= 475:
                    lives -= 1
                    alienY[i] = random.randint(1, 350)

                if lives == 0:
                    print("level 1 lose")
                    game_over()

                if score_value == 30:
                    print("level 1 win")
                    return win_game()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running1 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            playerX_change += 1
                        if event.key == pygame.K_LEFT:
                            playerX_change -= 1
                        if event.key == pygame.K_SPACE:
                            if bullet_state == "ready":
                                bullet(playerX, bulletY)
                                bulletX = playerX
                                #bullet_sound = mixer.Sound("LevelOneAssets\laser.wav")
                                #bullet_sound.play()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            playerX_change = 0
                        if event.key == pygame.K_LEFT:
                            playerX_change = 0
                        if event.key == pygame.K_SPACE:
                            bullet_state = "fire"


                playerY += playerY_change
                playerX += playerX_change
                player(playerX, playerY)

                if bulletY <= 0:
                    bullet_state = "ready"
                    bulletY = playerY

                if bullet_state == "fire":
                    bullet(bulletX, bulletY)
                    bulletY -= bulletY_change

                """
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            print("p pressed")
                            self.paused = True
                            pause()
                """

                alienY_change[i] = 40
                alienX[i] += alienX_change[i]

                showLevel(textX, textY - 25)
                show_score(textX, textY + 5 )
                health(textX, textY + 35)
                tutorial(score_value)

                pygame.display.update()

##---------------------------##
## LEVEL TWO DIALOG FUNCTION ##
##---------------------------##
    def LevelTwoDia(self):
        #pygame.mixer.music.fadeout(1000)
        #song = 'music\Comping.wav'
        #song = pygame.mixer.music.load(song)
        #pygame.mixer.music.play(-1)

        self.checkEvents()
        if self.START_KEY:
            self.level = 0
            self.playing = False

        self.clearScreen()
        #self.diaBox = pygame.image.load('Text Box.png') #working
        self.drawText('inside of game loop', 20, self.DISPLAY_W/2, 350)
        self.window.blit(self.display, (0,0))
        #self.window.blit(self.diaBox, (0,0)) #working

        self.wait("Damn. Guess you’re ELOs pretty high.\nYou’ll have to teach me your tactics sometime")
        self.wait("INSERT CONTEXT")
        self.wait("Tom Ato:\nHey you’re the new guy yeah?\nBro I’m looking for more fresh meat,\nI’m a god on the field and on the game. Prepare to get destroyed!!")
        print("done dia")



##-------------------------##
## LEVEL TWO GAME FUNCTION ##
##-------------------------##


    def LevelTwo(self):
        #pygame.mixer.music.fadeout(1000)
        screen = self.window
        player_img = pygame.image.load("LevelTwoAssets/spaceship.png")
        playerX, playerY = 336, 480
        playerX_change, playerY_change = 0, 0

        alien_img = []
        alienX = []
        alienY = []
        alienX_change = []
        alienY_change = []
        num_of_enemies = 8

        bullet_img = pygame.image.load("LevelTwoAssets/bullet.png")
        bulletX, bulletY = 0, 480
        bulletX_change, bulletY_change = 0, 15
        bullet_state = "ready"

        background = pygame.image.load("LevelTwoAssets/trees.png")
        game_end = pygame.image.load("LevelTwoAssets/game_over(800x600).png")

        lives, livesX, livesY = 1, 10, 10
        score_value = 0
        font = pygame.font.Font("freesansbold.ttf", 32)
        textX, textY = 10, 40

        for i in range(num_of_enemies):
            alien_img.append(pygame.image.load("LevelTwoAssets/alien.png"))
            alienX.append(random.randint(1, 735))
            alienY.append(random.randint(1, 350))
            alienX_change.append(2)
            alienY_change.append(40)

        def game_over():
            if lives == 0:
                return "lose"
                screen.blit(game_end, (0, 0))

        def win_game():
            if score_value == 45:
                self.level += 1
                return "win"

        def showLevel(X, Y):
            lives_num = font.render("level -  " + str(self.level), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def health(X, Y):
            lives_num = font.render("Health -  " + str(lives), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def show_score(X, Y):
            score = font.render("Score - " + str(score_value) + " / 45", True, (132, 43, 215))
            screen.blit(score, (X, Y))

        def player(X, Y):
            screen.blit(player_img, (X, Y))


        def alien(X, Y, i):
            screen.blit(alien_img[i], (X, Y))


        def bullet(X, Y):
            global bullet_state
            bullet_state = "fire"
            screen.blit(bullet_img, (X + 16, Y + 10))


        def is_collisison(alienX, alienY, bulletX, bulletY):
            distance = math.sqrt((alienX - bulletX) ** 2 + (alienY - bulletY) ** 2)
            if distance < 40:
                return True
            else:
                return False


        running1 = True
        while running1:

            self.clock.tick(self.FPS)

                # RGB
            screen.fill((132, 43, 215))

            screen.blit(background, (0, 0))

            if playerX > 735:
                playerX = 735
            elif playerX < 0:
                playerX = 0

            if playerY > 540:
                playerY = 540
            if playerY < 0:
                playerY = 0

            for i in range(num_of_enemies):
                alienX[i] += alienX_change[i]
                if alienX[i] > 735:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = -1
                elif alienX[i] < 0:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = 1

                collision = is_collisison(alienX[i], alienY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    alienX[i] = random.randint(1, 735)
                    alienY[i] = random.randint(1, 350)
                    #explosion_sound = mixer.Sound("LevelTwoAssets/explosion.wav")
                    #explosion_sound.play()
                alien(alienX[i], alienY[i], i)
                if alienY[i] >= 475:
                    lives -= 1
                    alienY[i] = random.randint(1, 350)

                if lives == 0:
                    print("level " + str(self.level) +" lose")
                    game_over()

                if score_value == 45:
                    print("level " + str(self.level) +" win")
                    return win_game()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running1 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            playerX_change += 1
                        if event.key == pygame.K_LEFT:
                            playerX_change -= 1
                        if event.key == pygame.K_SPACE:
                            if bullet_state == "ready":
                                bullet(playerX, bulletY)
                                bulletX = playerX
                                #bullet_sound = mixer.Sound("LevelTwoAssets\laser.wav")
                                #bullet_sound.play()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            playerX_change = 0
                        if event.key == pygame.K_LEFT:
                            playerX_change = 0
                        if event.key == pygame.K_SPACE:
                            bullet_state = "fire"


                playerY += playerY_change
                playerX += playerX_change
                player(playerX, playerY)
                

                if bulletY <= 0:
                    bullet_state = "ready"
                    bulletY = playerY

                if bullet_state == "fire":
                    bullet(bulletX, bulletY)
                    bulletY -= bulletY_change

                alienY_change[i] = 40
                alienX[i] += alienX_change[i]
                
                showLevel(textX, textY - 25)
                show_score(textX, textY + 5 )
                health(textX, textY + 35)

                pygame.display.update()


##---------------------------##
## LEVEL THREE DIALOG FUNCTION ##
##---------------------------##
    def LevelThreeDia(self):
        #pygame.mixer.music.fadeout(1000)
        #song = 'music\Comping.wav'
        #song = pygame.mixer.music.load(song)
        #pygame.mixer.music.play(-1)

        self.checkEvents()
        if self.START_KEY:
            self.level = 0
            self.playing = False

        self.clearScreen()
        #self.diaBox = pygame.image.load('Text Box.png') #working
        self.drawText('inside of game loop', 20, self.DISPLAY_W/2, 350)
        self.window.blit(self.display, (0,0))
        #self.window.blit(self.diaBox, (0,0)) #working

        self.wait("Tom Ato:\nWHAT YOU BEAT ME??! Damn,\nI guess you’re pretty good huh.\nWell I’ll see you later at the football game tonight yeah?")
        self.wait("INSERT CONTEXT")
        self.wait("Tan Gerine:\nCall this shit the Coltrane changes the way\nImma negative harmony and Cannonball\nyou’re ass right into the next phrase.\nAdderley that is!")
        print("done dia")



##-------------------------##
## LEVEL THREE GAME FUNCTION ##
##-------------------------##


    def LevelThree(self):
        #pygame.mixer.music.fadeout(1000)
        screen = self.window
        player_img = pygame.image.load("LevelThreeAssets/spaceship.png")
        playerX, playerY = 336, 480
        playerX_change, playerY_change = 0, 0

        alien_img = []
        alienX = []
        alienY = []
        alienX_change = []
        alienY_change = []
        num_of_enemies = 8

        bullet_img = pygame.image.load("LevelThreeAssets/bullet.png")
        bulletX, bulletY = 0, 480
        bulletX_change, bulletY_change = 0, 15
        bullet_state = "ready"

        background = pygame.image.load("LevelThreeAssets/blue mountain background.png")
        game_end = pygame.image.load("LevelThreeAssets/game_over(800x600).png")

        lives, livesX, livesY = 1, 10, 10
        score_value = 0
        font = pygame.font.Font("freesansbold.ttf", 32)
        textX, textY = 10, 40

        for i in range(num_of_enemies):
            alien_img.append(pygame.image.load("LevelThreeAssets/alien.png"))
            alienX.append(random.randint(1, 735))
            alienY.append(random.randint(1, 350))
            alienX_change.append(2)
            alienY_change.append(40)

        def game_over():
            if lives == 0:
                return "lose"
                screen.blit(game_end, (0, 0))

        def win_game():
            if score_value == 55:
                self.level += 1
                return "win"

        def showLevel(X, Y):
            lives_num = font.render("level -  " + str(self.level), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def health(X, Y):
            lives_num = font.render("Health -  " + str(lives), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def show_score(X, Y):
            score = font.render("Score - " + str(score_value) + " / 55", True, (132, 43, 215))
            screen.blit(score, (X, Y))

        def player(X, Y):
            screen.blit(player_img, (X, Y))


        def alien(X, Y, i):
            screen.blit(alien_img[i], (X, Y))


        def bullet(X, Y):
            global bullet_state
            bullet_state = "fire"
            screen.blit(bullet_img, (X + 16, Y + 10))


        def is_collisison(alienX, alienY, bulletX, bulletY):
            distance = math.sqrt((alienX - bulletX) ** 2 + (alienY - bulletY) ** 2)
            if distance < 40:
                return True
            else:
                return False


        running1 = True
        while running1:

            self.clock.tick(self.FPS)

                # RGB
            screen.fill((132, 43, 215))

            screen.blit(background, (0, 0))

            if playerX > 735:
                playerX = 735
            elif playerX < 0:
                playerX = 0

            if playerY > 540:
                playerY = 540
            if playerY < 0:
                playerY = 0

            for i in range(num_of_enemies):
                alienX[i] += alienX_change[i]
                if alienX[i] > 735:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = -1.5
                elif alienX[i] < 0:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = 1.5

                collision = is_collisison(alienX[i], alienY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    alienX[i] = random.randint(1, 735)
                    alienY[i] = random.randint(1, 350)
                    #explosion_sound = mixer.Sound("LevelThreeAssets\explosion.wav")
                    #explosion_sound.play()
                alien(alienX[i], alienY[i], i)
                if alienY[i] >= 475:
                    lives -= 1
                    alienY[i] = random.randint(1, 350)

                if lives == 0:
                    print("level " + str(self.level) +" lose")
                    game_over()

                if score_value == 55:
                    print("level " + str(self.level) +" win")
                    return win_game()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running1 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            playerX_change += 1
                        if event.key == pygame.K_LEFT:
                            playerX_change -= 1
                        if event.key == pygame.K_SPACE:
                            if bullet_state == "ready":
                                bullet(playerX, bulletY)
                                bulletX = playerX
                                #bullet_sound = mixer.Sound("LevelThreeAssets\laser.wav")
                                #bullet_sound.play()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            playerX_change = 0
                        if event.key == pygame.K_LEFT:
                            playerX_change = 0
                        if event.key == pygame.K_SPACE:
                            bullet_state = "fire"


                playerY += playerY_change
                playerX += playerX_change
                player(playerX, playerY)
                

                if bulletY <= 0:
                    bullet_state = "ready"
                    bulletY = playerY

                if bullet_state == "fire":
                    bullet(bulletX, bulletY)
                    bulletY -= bulletY_change

                alienY_change[i] = 40
                alienX[i] += alienX_change[i]
                
                showLevel(textX, textY - 25)
                show_score(textX, textY + 5 )
                health(textX, textY + 35)

                pygame.display.update()

##----------------------------##
## LEVEL FOUR DIALOG FUNCTION ##
##----------------------------##
    def LevelFourDia(self):
        #pygame.mixer.music.fadeout(1000)
        #song = 'music\Comping.wav'
        #song = pygame.mixer.music.load(song)
        #pygame.mixer.music.play(-1)

        self.checkEvents()
        if self.START_KEY:
            self.level = 0
            self.playing = False

        self.clearScreen()
        #self.diaBox = pygame.image.load('Text Box.png') #working
        self.drawText('inside of game loop', 20, self.DISPLAY_W/2, 350)
        self.window.blit(self.display, (0,0))
        #self.window.blit(self.diaBox, (0,0)) #working

        self.wait("Tom Ato:\nDamn, guess you’re a bit more fluent in fusion than I am.\n I’ve got to go practice 40 hours more then!")
        self.wait("INSERT CONTEXT")
        self.wait("MORE DIALOG")
        print("done dia")



##--------------------------##
## LEVEL FOUR GAME FUNCTION ##
##--------------------------##


    def LevelFour(self):
        #pygame.mixer.music.fadeout(1000)
        screen = self.window
        player_img = pygame.image.load("LevelFourAssets/spaceship.png")
        playerX, playerY = 336, 480
        playerX_change, playerY_change = 0, 0

        alien_img = []
        alienX = []
        alienY = []
        alienX_change = []
        alienY_change = []
        num_of_enemies = 9

        bullet_img = pygame.image.load("LevelFourAssets/bullet.png")
        bulletX, bulletY = 0, 480
        bulletX_change, bulletY_change = 0, 15
        bullet_state = "ready"

        background = pygame.image.load("LevelFourAssets/red desert background.png")
        game_end = pygame.image.load("LevelFourAssets/game_over(800x600).png")

        lives, livesX, livesY = 1, 10, 10
        score_value = 0
        font = pygame.font.Font("freesansbold.ttf", 32)
        textX, textY = 10, 40

        for i in range(num_of_enemies):
            alien_img.append(pygame.image.load("LevelFourAssets/alien.png"))
            alienX.append(random.randint(1, 735))
            alienY.append(random.randint(1, 350))
            alienX_change.append(2)
            alienY_change.append(40)

        def game_over():
            if lives == 0:
                return "lose"
                screen.blit(game_end, (0, 0))

        def win_game():
            if score_value == 60:
                self.level += 1
                return "win"

        def showLevel(X, Y):
            lives_num = font.render("level -  " + str(self.level), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def health(X, Y):
            lives_num = font.render("Health -  " + str(lives), True, (132, 43, 215))
            screen.blit(lives_num, (X, Y))

        def show_score(X, Y):
            score = font.render("Score - " + str(score_value) + " / 60", True, (132, 43, 215))
            screen.blit(score, (X, Y))

        def player(X, Y):
            screen.blit(player_img, (X, Y))


        def alien(X, Y, i):
            screen.blit(alien_img[i], (X, Y))


        def bullet(X, Y):
            global bullet_state
            bullet_state = "fire"
            screen.blit(bullet_img, (X + 16, Y + 10))


        def is_collisison(alienX, alienY, bulletX, bulletY):
            distance = math.sqrt((alienX - bulletX) ** 2 + (alienY - bulletY) ** 2)
            if distance < 40:
                return True
            else:
                return False


        running1 = True
        while running1:

            self.clock.tick(self.FPS)

                # RGB
            screen.fill((132, 43, 215))

            screen.blit(background, (0, 0))

            if playerX > 735:
                playerX = 735
            elif playerX < 0:
                playerX = 0

            if playerY > 540:
                playerY = 540
            if playerY < 0:
                playerY = 0

            for i in range(num_of_enemies):
                alienX[i] += alienX_change[i]
                if alienX[i] > 735:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = -1.5
                elif alienX[i] < 0:
                    alienY[i] += alienY_change[i]
                    alienX_change[i] = 1.5

                collision = is_collisison(alienX[i], alienY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    alienX[i] = random.randint(1, 735)
                    alienY[i] = random.randint(1, 350)
                    #explosion_sound = mixer.Sound("LevelFourAssets/explosion.wav")
                    #explosion_sound.play()
                alien(alienX[i], alienY[i], i)
                if alienY[i] >= 475:
                    lives -= 1
                    alienY[i] = random.randint(1, 350)

                if lives == 0:
                    print("level " + str(self.level) +" lose")
                    game_over()

                if score_value == 60:
                    print("level " + str(self.level) +" win")
                    return win_game()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running1 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            playerX_change += 1
                        if event.key == pygame.K_LEFT:
                            playerX_change -= 1
                        if event.key == pygame.K_SPACE:
                            if bullet_state == "ready":
                                bullet(playerX, bulletY)
                                bulletX = playerX
                                #bullet_sound = mixer.Sound("LevelFourAssets\laser.wav")
                                #bullet_sound.play()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            playerX_change = 0
                        if event.key == pygame.K_LEFT:
                            playerX_change = 0
                        if event.key == pygame.K_SPACE:
                            bullet_state = "fire"


                playerY += playerY_change
                playerX += playerX_change
                player(playerX, playerY)
                

                if bulletY <= 0:
                    bullet_state = "ready"
                    bulletY = playerY

                if bullet_state == "fire":
                    bullet(bulletX, bulletY)
                    bulletY -= bulletY_change

                alienY_change[i] = 40
                alienX[i] += alienX_change[i]
                
                showLevel(textX, textY - 25)
                show_score(textX, textY + 5 )
                health(textX, textY + 35)

                pygame.display.update()


##----------------------------##
## LEVEL FIVE DIALOG FUNCTION ##
##----------------------------##

    def LevelFiveDia(self):
        #pygame.mixer.music.fadeout(1000)
        #song = 'music\Comping.wav'
        #song = pygame.mixer.music.load(song)
        #pygame.mixer.music.play(-1)

        self.checkEvents()
        if self.START_KEY:
            self.level = 0
            self.playing = False

        self.clearScreen()
        #self.diaBox = pygame.image.load('Text Box.png') #working
        self.drawText('inside of game loop', 20, self.DISPLAY_W/2, 350)
        self.window.blit(self.display, (0,0))
        #self.window.blit(self.diaBox, (0,0)) #working

        self.wait("GOKU: sum sum idk add dialog here")
        self.wait("INSERT CONTEXT")
        self.wait("MORE DIALOG")
        print("done dia")
