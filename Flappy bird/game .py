import random #For generating random numbers
import sys #For exiting the game.
import time
import pygame
import pygame.locals
#import * #Basic pygame imports


#Global variables for the game
from pygame import K_ESCAPE, KEYDOWN, QUIT, K_SPACE, K_UP, K_1, K_2, K_3, K_4, K_5

FPS = 40
SCREENWIDTH = 342
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.75
GAME_SPRITES = {}
GAME_SOUNDS = {}
BACKGROUND = 'gallery/background.png'
PIPE = 'gallery/pipe.png'
UPPER_LIMIT = ()

def welcomeScreen():
    """
    shows welcome images on the screen
    """
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game!
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if the user clicks space or up key, starts the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            else:
                SCREEN.blit(GAME_SPRITES['message'], (0, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    SCREEN.blit(GAME_SPRITES['instructions'], (0, 0))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    time.sleep(2)
    while True:
        for event in pygame.event.get():
            if event.key == K_1:
                GAME_SPRITES['player'] = GAME_SPRITES['player1']
                print("True!")
                return
            elif event.key == K_2:
                GAME_SPRITES['player'] = GAME_SPRITES['player2']
                return
            elif event.key == K_3:
                GAME_SPRITES['player'] = GAME_SPRITES['player3']
                return
            elif event.key == K_4:
                GAME_SPRITES['player'] = GAME_SPRITES['player4']
                return
            elif event.key == K_5:
                GAME_SPRITES['player'] = GAME_SPRITES['player5']
                return
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                SCREEN.blit(GAME_SPRITES['selection'], (0, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame2():
    score = 0
    playerx = 15
    playery = 236
    basex = 0

    newPipe1 = [{'x': SCREENWIDTH, 'y': random.randrange(285, 390, 20)},
                {'x': SCREENWIDTH+200, 'y': random.randrange(275, 390, 20)}]
    newRock1 = [{'x': SCREENWIDTH+45, 'y': random.randrange(80, 115, 5)},
                {'x': SCREENWIDTH+250, 'y': random.randrange(80, 115, 5)}]

    pipeVelX = -4
    playerVely = -9
    playerMaxVely = 10
    playerMinvely = -8
    playerAccVely = 1
    playerFlapAccv = -8  # velocity while flapping
    playerFlapped = False  # its true only while player is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.type == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVely = playerFlapAccv
                    playerFlapped = True
                    #GAME_SOUNDS['wing'].play()

        # this function will return if the player crashed
        isCollide(playerx, playery, newPipe1, newRock1)

        if playerVely < playerMaxVely and not playerFlapped:
            playerVely += playerAccVely

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVely, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerpipe in zip(newPipe1, newRock1):
            upperPipe['x'] += pipeVelX
            lowerpipe['x'] += pipeVelX

        # if pipe is out of the screen, remove it
        if newPipe1[0]['x'] < -GAME_SPRITES['pipe'].get_width():
            newPipe1.pop(0)
            newpipe = {'x': SCREENWIDTH, 'y': random.randrange(275, 390, 20)}
            newPipe1.append(newpipe)

        if newRock1[0]['x'] < -GAME_SPRITES['rock'].get_width():
            newRock1.pop(0)
            newrock = {'x': SCREENWIDTH - 5, 'y': random.randrange(80, 115, 5)}
            newRock1.append(newrock)

       #Lets blit our sprites now!
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(newPipe1, newRock1):
            SCREEN.blit(GAME_SPRITES['pipe'], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['rock'], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, newPipe1, newRock1):
    #GAME_SOUNDS['hit'].play()
    if playery >= 350 or playery <= 87:
        print("YOU HIT THE LIMIT!")
        pygame.quit()
        sys.exit()

    if playery+15 <= newRock1[0]['y']+105 and 70 >= newRock1[0]['x']+55 > 15:
        print("you hit the aestroid!")
        pygame.quit()
        sys.exit()

    if playery+75 >= newPipe1[0]['y']+10 and 75 >= newPipe1[0]['x']+25 > 15:
        print("you hit the cactus!")
        pygame.quit()
        sys.exit()

    else:
        return

if __name__ =="__main__":
    # This will be the main function from where our game will start
    pygame.init()  #Intialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy bird by NOOBPOOK")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/1.png').convert_alpha(),
        pygame.image.load('gallery/2.png').convert_alpha(),
        pygame.image.load('gallery/3.png').convert_alpha(),
        pygame.image.load('gallery/4.png').convert_alpha(),
        pygame.image.load('gallery/5.png').convert_alpha(),
        pygame.image.load('gallery/6.png').convert_alpha(),
        pygame.image.load('gallery/7.png').convert_alpha(),
        pygame.image.load('gallery/8.png').convert_alpha(),
        pygame.image.load('gallery/9.png').convert_alpha(),
        pygame.image.load('gallery/10.png').convert_alpha(),
    )


    GAME_SPRITES['message'] = pygame.image.load('gallery/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/base.png').convert_alpha()
    GAME_SPRITES['instructions'] = pygame.image.load('gallery/instructions.png').convert()
    GAME_SPRITES['pipe'] = pygame.image.load(PIPE).convert_alpha()
    GAME_SPRITES['rock'] = pygame.image.load('gallery/rock.png').convert_alpha()

    #pygame.mixer.init()
    #GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/Music/Bigexplosion.wav')
    #GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/Music/Cartoonboing.wav')
    #GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/Music/Instrumentstrum.wav')
    #GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/Music/Swoosh.wav')


    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['selection'] = pygame.image.load('gallery/selection.png')
    GAME_SPRITES['player1'] = pygame.image.load('gallery/Characters/angry_bird.png').convert_alpha()
    GAME_SPRITES['player2'] = pygame.image.load('gallery/Characters/astronaut.png').convert_alpha()
    GAME_SPRITES['player3'] = pygame.image.load('gallery/Characters/bird.png').convert_alpha()
    GAME_SPRITES['player4'] = pygame.image.load('gallery/Characters/doremon.png').convert_alpha()
    GAME_SPRITES['player5'] = pygame.image.load('gallery/Characters/shinchan.png').convert_alpha()

    while True:
        welcomeScreen()#Shows welcome screen to the user until he preses a button.
        print("Done!")
        mainGame()   #This is the main game function
        mainGame2()
