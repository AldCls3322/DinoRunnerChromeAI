import pygame
import neat
import time, os, random
pygame.font.init()

###__CONSTANT VARIABLES__###

#_SCREEN SIZES_#
WIN_WIDTH = 600
WIN_HEIGHT = 150

#_COLORS_#
WHITE = (255,255,255)
BLACK = (0,0,0)

#_IMAGES_#
DINO_RUN_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png")))]
DINO_DUCK_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02.png")))]
DINO_JUMP_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png")))

DINO_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png")))

S_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")))
B_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")))

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird02.png")))]
DINO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDeath01.png")))]
CACTUS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","ManySmallCactus01.png")))]

#################
###___GAME____###
#################

###__GAME FUNCTIONS__###
#_FUNCTION THAT CREATES A SCREEEN_#
def draw_window(screen):
    screen.blit(DINO_IMG, (0,95)) #blit function is like draw
    pygame.display.update() #refreshes

#_FUCNTION THAT PALYS THE GAME_#
def main():
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #sets the window size
    screen.fill(WHITE)
    clock = pygame.time.Clock() #creates a control for frame rates

    run = True
    while run: #Plays game while you don't quit
        clock.tick(30)  #Sets the frame rate at 30

        for event in pygame.event.get():    #when something is clicked then:
            if event.type == pygame.QUIT:   #will quit the loop for the "X" button on the screen
                run = False
                #pygame.quit()
                quit()
        

        draw_window(screen) #calls the function "draw_window"

main()