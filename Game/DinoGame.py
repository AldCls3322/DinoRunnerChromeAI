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
# DINO_RUN_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png")))]
# DINO_DUCK_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02.png")))]
# DINO_JUMP_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png")))
DINO_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png")))
# S_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")))
# B_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")))

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird02.png")))]
DINO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDeath01.png")))]
CACTUS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","ManySmallCactus01.png")))]
GROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","ground.png")))
CLOUD_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","cloud.png")))

###__CREATES THE OBJECT BIRD__###
class Bird:
    ##_CONSTANT VARIABLES USED_##
    IMGS = BIRD_IMGS
    ANIMATION_TIME = 5

    #_ESTABLISHED THE ATRIBUTES OF THE OBJECT BIRD | CONSTRUCTOR_#
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    #_FUNCTION TO CREATE ANIMATION_#    
    def draw(self, win):
        self.img_count += 1

        #MAKES THE ANIMATION OF THE BIRD FLAPPING THE WINGS
        """According to the "img_count" and waiting 5 "seconds" to display the next image of the bird eith different wing position"""
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        
    #_FUNCTION FOR COLISION_#
    """ Uses the mask to be more acurrate for the user in colision, and not use boxes """
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

###__Creates/Defines an object Base__###
class Ground:
    VEL = 5
    WIDTH = GROUND_IMG.get_width()
    IMG = GROUND_IMG

    #_FUNCTION CREATES ATRIBUTES OF PIPE | CONSTRUCTOR_#
    def __init__(self, y):
        self.y = y
        self.x1 = 0             #base number 1
        self.x2 = self.WIDTH    #base number 2
    
    #_FUNCTION TO MOVE THE BASE IN X AXIS_#
    """ Creates 2 images to be rotating and cycling giving the preseption of infinite movement """
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    #_FUCNTION TO DISPLAY THE GROUND_#   
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

#################
###___GAME____###
#################

###__GAME FUNCTIONS__###
#_FUNCTION THAT CREATES A SCREEEN_#
def draw_window(screen, ground):
    ground.draw(screen) #Displays ground
    screen.blit(DINO_IMG, (0,95)) #blit function is like draw
    pygame.display.update() #refreshes

#_FUCNTION THAT PALYS THE GAME_#
def main():
    #_Creating Objects_#
    ground = Ground(125) #creates and sets the ground
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
        
        ground.move()   #Makes the ground move to give a perseption of running

        draw_window(screen, ground) #calls the function "draw_window"


main()