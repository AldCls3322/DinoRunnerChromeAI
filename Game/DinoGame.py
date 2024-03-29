##__LIBRARIES USED__##
import pygame
import neat
import time, os, random
pygame.font.init()

from Bird import Bird #import the class / object Bird from the "Bird.py" file
from Cactus import Cactus #import the class / object Bird from the "Cactus.py" file
from Dino import Dino #import the class / object Bird from the "Dino.py" fileg

###__CONSTANT VARIABLES__###

#_SCREEN SIZES_#
WIN_WIDTH = 600
WIN_HEIGHT = 150

#_COLORS_#
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)

#_FONTS_#
SCORE_FONT = pygame.font.SysFont("Rockwell", 24)    #"Speak Pro" "Source Sans Pro"
ENDING_FONT = pygame.font.SysFont("Speak Pro", 30)

#_IMAGES_#
# DINO_RUN_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png")))]
# DINO_DUCK_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02.png")))]
# DINO_JUMP_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png")))
# DINO_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png")))
# S_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")))
# B_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")))

GROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","ground.png")))
CLOUD_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","cloud.png")))


###__Creates/Defines an object Base__###
class Ground:
    VEL = 7
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
        win.blit(self.IMG, (self.x1, self.y))   #blit function is like draw
        win.blit(self.IMG, (self.x2, self.y))

###__Creates/Defines an object Cloud__###
class Cloud:
    VEL = 4
    IMG = CLOUD_IMG

    def __init__(self, x):
        self.y = random.randint(0,80)
        self.x = x
    
    #_FUNCTION TO MOVE THE BASE IN X AXIS_#
    """ Creates 2 images to be rotating and cycling giving the preseption of infinite movement """
    def move(self):
        self.x -= self.VEL

    #_FUCNTION TO DISPLAY THE GROUND_#   
    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))   #blit function is like draw

#################
###___GAME____###
#################

###__GAME FUNCTIONS__###
#_FUNCTION THAT CREATES A SCREEEN_#
def draw_window(screen, ground, clouds, dino, birds, cacti, score, alive):
    screen.fill(WHITE)
    ground.draw(screen) #Displays ground
    
    for cloud in clouds:
        cloud.draw(screen)

    dino.draw(screen)   #Displays dinosaur

    for bird in birds:
        bird.draw(screen)   #Displays bird
    
    for cactus in cacti:
        cactus.draw(screen)

    #Score Dispay#
    score_label = SCORE_FONT.render("Score: " + str(score),1,BLACK)
    screen.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15,5))

    #Ending Text Display#
    if (alive == False):
        ending_label = ENDING_FONT.render("Press 'BACKSPACE' to restart",1,GREY)
        screen.blit(ending_label, (WIN_WIDTH/2 - ending_label.get_width()/2, WIN_HEIGHT/2))

    pygame.display.update() #refreshes

#_FUNCTION TO RESTART/START_#
def restart():
    #_Creating Objects_#
    ground = Ground(125) #creates and sets the ground
    clouds = [Cloud(600)]   # creates a list for the clouds
    dino = Dino(0,95)   #creates and setes the dinosaur
    #cactus = Cactus(550)   #creates a single cactus
    birds = [Bird(900)]     # creates a single bird
    cacti = [Cactus(550)]   # creates a list for multiple cactus to appear on screeen

    #_Making the Screen and defining a Time_#
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #sets the window size
    pygame.display.set_caption("Google Dinosaur Runner Clone") # sets the window name
    screen.fill(WHITE)  # makes the background WHITE
    clock = pygame.time.Clock() #creates a control for frame rates

    score = 0   # Establishes tha start for scoring

    #_Makes the obstacle of continious and with random distance between them_#
    prev_cactus = 600   # defines that the first cactus was set on x = 600
    for i in range(2):  # creates 2 different cactuses with random distance between them and adds them to the previous created list
        prev_cactus += random.randint(300,600)
        cacti.append(Cactus(prev_cactus))

    run = True  # SETS START TO THE GAME
    alive = True

    return ground, clouds, dino, birds, cacti, screen, clock, score, prev_cactus, run, alive

#_FUCNTION THAT PALYS THE GAME_#
def main():
    
    ground, clouds, dino, birds, cacti, screen, clock, score, prev_cactus, run, alive = restart()

    while run: #Plays game while you don't quit
        clock.tick(30)  #Sets the frame rate at 30

        for event in pygame.event.get():    #when something is clicked then:
            if event.type == pygame.QUIT:   #will quit the loop for the "X" button on the screen
                run = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()
                if event.key == pygame.K_BACKSPACE:
                    print("RESTART")
                    ground, clouds, dino, birds, cacti, screen, clock, score, prev_cactus, run, alive = restart()
                if event.key == pygame.K_ESCAPE:
                    run = False
                    quit()
        
        if (alive):

            keys = pygame.key.get_pressed() #checks for a key of the keyboard is being pressed
            if keys[pygame.K_DOWN]: #if the key is the down arrow, then it will
                dino.duck() #makes dinosaur duck

            add_cactus = False  #establishes not to add a cactus
            rem_cactus = []    #for saving which cactus to delete
            for cactus in cacti:
                
                if (not cactus.passed and cactus.x < dino.x):   #until the dinosaur passes the cactus it will create another one
                    cactus.passed = True
                    add_cactus = True

                if cactus.collide(dino, screen):    # checks of the Dinosaur touched a Cactus
                    print('TOUCHED')
                    alive = False
                
                if (cactus.x < -30):    # after the cactus passes the screen it will be deleted, so we save it on a list that will later remove that cactus
                    rem_cactus.append(cactus)
                
                cactus.move()   # sets motion to tha cactuses
            
            
            if (add_cactus):    # if the dinosaur passed a cactus it will generate new ones with same method as done previously
                score += 1

                prev_cactus = cacti[len(cacti)-1].x
                prev_cactus += random.randint(200,600)
                cacti.append(Cactus(prev_cactus))

            for re in rem_cactus:   # deletes the cactus that was already jumped
                cacti.remove(re)
            
            
            add_cloud = False   # establishes not to add a cloud yet
            rem_cloud = []      # a list to save the clouds that need to be removed
            for cloud in clouds:    # will establish what happens to the clouds
                if (cloud.x < -99): # after the cloud passes through the screen it will create a new one.
                    add_cloud = True
                
                if (cloud.x < -100):    # after the cloud passes the screen it saves it to the list that will delete tha passed clouds
                    rem_cloud.append(cloud)
                
                cloud.move()    # sets motion to the clouds

            if (add_cloud): # if it must create a new cloud it will create a new one in the right side.
                clouds = [Cloud(600)]
                add_cloud = False
            
            for r in rem_cloud: # deletes the passed cloud
                clouds.remove(r)
            
            add_bird = False
            rem_bird = []
            for bird in birds:
                if (bird.x < -23):
                    add_bird = True
                    rem_bird.append(bird)
                
                if bird.collide(dino, screen):    # checks of the Dinosaur touched a Bird
                    print('TOUCHED')
                    alive = False
                
                bird.move() #Makes the bird move
            
            if (add_bird):  # after one passes the screen it creates a new one 
                score += 1
                
                birds.append(Bird(1800))
                add_bird = False
            
            for r in rem_bird:  # deletes the passed bird
                birds.remove(r)

            ground.move()   #Makes the ground move to give a perseption of running
            dino.move()     #Makes the dinosaur constantly run

        draw_window(screen, ground, clouds, dino, birds, cacti, score, alive) #calls the function "draw_window"


main()