#############
### INDEX ###
#############
"""
1.      LIBRARIES AND OBJECTS USED
2.      GLOBAL VARIABLES AND IMAGES
3.      OBJECTS
    3.1 GROUND OBJECT
    3.2 CLOUD OBJECT
4.      GAME
    4.1 WINDOW REFRESH AND DISPLAY
    4.2 GAME STARTS TO PLAY
    4.3 RUNNING THE NEURAL NETWORK OF NEAT
    4.4 SETS UP THE NEURAL NETWORK SPECIFICS AND RUNS THE WHOLE PROGRAM / GAME
"""

###__IMPORTING LIBRARIES AND OBJECTS__###
import pygame
import neat
import time, os, random

from Bird import Bird #import the class / object Bird from the "Bird.py" file
from Cactus import Cactus #import the class / object Bird from the "Cactus.py" file
from Dino import Dino #import the class / object Bird from the "Dino.py" fileg

pygame.font.init()  # start the pygame library

###__CONSTANT VARIABLES__###

#_SCREEN SIZES_#
WIN_WIDTH = 600
WIN_HEIGHT = 150
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))   #creates the screen
pygame.display.set_caption("Google Dinosaur Runner Clone with AI")  #sets the name of the screen

#_COLORS_#
WHITE = (255,255,255)
BLACK = (0,0,0)

#_FONTS_#
SCORE_FONT = pygame.font.SysFont("Rockwell", 24)    #"Speak Pro" "Source Sans Pro"

#_BACKGROUND IMAGES_#
GROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","ground.png")))
CLOUD_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","cloud.png")))

gen = 1 # the counter to display how many generations there had been

###__Creates/Defines an object Base__###
class Ground:
    VEL = 7 # speed at which the ground is going to move
    WIDTH = GROUND_IMG.get_width()
    IMG = GROUND_IMG

    #_FUNCTION CREATES ATRIBUTES OF PIPE | CONSTRUCTOR_#
    def __init__(self, y):
        self.y = y
        self.x1 = 0             #base number 1
        self.x2 = self.WIDTH    #base number 2
    
    #_FUNCTION TO MOVE THE BASE IN X AXIS_#
    def move(self): # Creates 2 images to be rotating and cycling giving the preseption of infinite background
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
    VEL = 4 # moves slower that the ground to give a better persepction
    IMG = CLOUD_IMG

    def __init__(self, x):
        self.y = random.randint(0,80)
        self.x = x
    
    #_FUNCTION TO MOVE THE BASE IN X AXIS_#
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
def draw_window(screen, ground, clouds, dinosaurs, cacti, score, gen):

    screen.fill(WHITE)
    ground.draw(screen) # Displays ground
    
    for cloud in clouds:
        cloud.draw(screen)  # Displays the clouds

    for dinosaur in dinosaurs:
        dinosaur.draw(screen)   # Displays dinosaur
    
    for cactus in cacti:
        cactus.draw(screen) # Displays cactus

    #Score Text Dispay#
    score_label = SCORE_FONT.render("Points: " + str(score),1,BLACK)
    screen.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15,5))

    #Generation Text Display#
    generation_label = SCORE_FONT.render("Gen: " + str(gen-1),1,BLACK)
    screen.blit(generation_label, (WIN_WIDTH/2 - generation_label.get_width()/2, 5))

    #Dinosaurs Still Alive Text Dispay#
    alive_dinos_label = SCORE_FONT.render("Alive: " + str(len(dinosaurs)),1,BLACK)
    screen.blit(alive_dinos_label, (5, 5))

    pygame.display.update() #refreshes

#_FUCNTION THAT PLAYS THE GAME_#
def eval_genomes(genomes, config):
    # Gets the variables used
    global screen, gen
    screen = WINDOW
    gen += 1

    #_Creating Objects_#
    nets = []   # list of the neural network used and that are playing assosiationg it with the genome of each dinosaur
    dinosaurs = []  # creates the list of the dinosaurs displayed in the screen
    ge = []     # list of genomes of each dinosaur

    for genome_id, genome in genomes: # gets the genome info of each dinosaur
        genome.fitness = 0  # start with fitness level of 0 / fitness will be use to determine the performance of the dinosaur
        net = neat.nn.FeedForwardNetwork.create(genome, config) # according to the config txt file it generates the neural network and adds the info to the list
        nets.append(net)
        dinosaurs.append(Dino(0,95))    # sets the dinosaur on x=0 and y=95
        ge.append(genome)
    
    ground = Ground(125) #creates and sets the ground
    clouds = [Cloud(600)]   # creates a list for the clouds
    cacti = [Cactus(550)]   # creates a list for multiple cactus to appear on screeen

    #_Makes the obstacle of continious and with random distance between them_#
    prev_cactus = 600   # defines that the first cactus was set on x = 600
    for i in range(2):  # creates 2 different cactuses with random distance between them and adds them to the previous created list
        prev_cactus += random.randint(300,600)
        cacti.append(Cactus(prev_cactus))

    #_Defines the Time rate_#
    clock = pygame.time.Clock() #creates a control for frame rates

    score = 0   # Establishes tha start for scoring

    run = True  # SETS START TO THE GAME

    while run: # Plays game while you don't quit
        clock.tick(30)  #Sets the frame rate at 30

        for event in pygame.event.get():    # when something is clicked then:
            if event.type == pygame.QUIT:   # will quit the loop for the "X" button on the screen
                run = False
                #pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    # will quit if you click "ESC"
                    run = False
                    quit()
        
        cactus_ind = 0  # makes sure the cactus scoring is the next one of the level
        if (len(dinosaurs) > 0):  # checks if there are dinosaurs still alive
            if (len(cacti) > 1 and dinosaurs[0].x > cacti[0].x ):  # if the dinosaurs passed the cactus then change the cactus you're looking at to the next one
                cactus_ind = 1    # cactus on the screen for neural network input
        else:
            run = False
            break

        for x, dinosaur in enumerate(dinosaurs):  # give each dinosaur a fitness of 0.1 for each frame it stays alive
            ge[x].fitness += 0.1
            dinosaur.move()

            # send dinosaur location and cactus location and determine from network whether to jump or not
            output = nets[dinosaurs.index(dinosaur)].activate((dinosaur.y, abs(dinosaur.y - cacti[cactus_ind].height), abs(dinosaur.x - cacti[cactus_ind].x)))

            if (output[0] > 0.5):  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                dinosaur.jump()

        add_cactus = False  #establishes not to add a cactus
        rem_cactus = []    #for saving which cactus to delete
        for cactus in cacti:
            # checks of the Dinosaur touched a Cactus
            for dinosaur in dinosaurs:
                if (cactus.collide(dinosaur, screen)):    # will remove the Dinosaur that touched the Cactus
                    ge[dinosaurs.index(dinosaur)].fitness -= 1  # if it touches the obstacle it will loose points of fitness
                    nets.pop(dinosaurs.index(dinosaur))
                    ge.pop(dinosaurs.index(dinosaur))
                    dinosaurs.pop(dinosaurs.index(dinosaur))
            
            if (not cactus.passed and cactus.x < dinosaur.x):   #until the dinosaur passes the cactus it will create another one
                cactus.passed = True
                add_cactus = True
            
            if (cactus.x < -30):    # after the cactus passes the screen it will be deleted, so we save it on a list that will later remove that cactus
                rem_cactus.append(cactus)
            
            cactus.move()   # sets motion to tha cactuses
        
        
        if (add_cactus):    # if the dinosaur passed a cactus it will generate new ones with same method as done previously
            score += 1

            # to add more rewards / fitness points to the dinosaurs that jumped the Cactus:
            for genome in ge:
                genome.fitness += 5

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

        ground.move()   #Makes the ground move to give a perseption of running

        draw_window(screen, ground, clouds, dinosaurs, cacti, score, gen) #calls the function "draw_window"

#_RUNS THE NEAT NEURAL NETWORK_#
def run(config_path):
    # After getting the location of config file

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config) # saves the number of dinosaurs there will be based on the txt file that it read form the previous line

    # Shows progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))   # gives output information
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 50)    # Run the game up to 50 generations.

    print('\nBest genome:\n{!s}'.format(winner))    # show final stats on terminal

###__MAIN__###
###___RUNS PROGRAM IF IT IS RAN DIRECTLY FROM FILE___###
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__) # It will get the path from the current working directory.
    config_path = os.path.join(local_dir, 'config-feedforward.txt') # Determine path to configuration file. 
    run(config_path)    # sets the neural network and runs the game.