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
# DINO_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png")))
# S_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")))
# B_CACTUS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")))

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird01.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","bird02.png")))]
DINO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png"))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png")),(24,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png")),(24,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01Fixed.png")),(34,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02Fixed.png")),(34,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png")),(24,25))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDeath01.png")))]
CACTUS_IMGS = [pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")),(15,30) )), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")),(10,20) )), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","ManySmallCactus01.png")), (30,20) ))]
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
    VEL = 7
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

###__CREATES THE OBJECT DINOSAUR__###
class Dino:
    ##_CONSTANT VARIABLES USED_##
    IMGS = DINO_IMGS
    ANIMATION_TIME = 2

    #_ESTABLISHED THE ATRIBUTES OF THE OBJECT BIRD | CONSTRUCTOR_#
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
        self.isJumping = False
        self.isDucking = False

    #_FUNCTION THAT ESTABLISHES A JUMP_#
    def jump(self):
        self.vel = -10.5    # moves up the screen, on minus Y axis
        self.height = self.y
        if (self.isJumping == False):
            self.tick_count = 0
            self.isJumping = True
    
    #_FUNCTION THAT ESTABLISHES DUCKING_#
    def duck(self):
        self.height = self.y
        if (self.isDucking == False):
            self.tick_count = 0
            # if (self.img_count != 0):
            #     self.img_count = 0
            self.isDucking = True
    
    #_FUNCTION THAT IS MAKING THE DINOSAUR HAVE AN ARC AND MOVE_#
    def move(self):
        self.tick_count += 1

        if (self.isJumping == True):
            if (self.y > 95):
                self.isJumping = False

            else:
                if (self.y < 60):
                    d = self.vel*self.tick_count + 1.2*self.tick_count**2   # Physics formula for parabolic trayectory
                
                else:
                    d = self.vel*self.tick_count + 1.5*self.tick_count**2   # Physics formula for parabolic trayectory

                #establishes a limit of speed for the movement
                if d >= 16:
                    d = 16

                if d < 0:
                    d -= 2

                if (self.isDucking == True):
                    d = 20
                        
                self.y = self.y + d

        elif (self.isDucking == True):
            self.y = 95
            # self.isDucking = False
        
        elif (self.y > 95):
            self.y = 95
            self.vel = 0
    
    #_FUNCTION TO CREATE ANIMATION_#    
    def draw(self, win):
        self.img_count += 1

        if (self.isJumping):    #MAKES THE ANIMATION OF THE DINOISAUR JUMPING
            self.img = self.IMGS[5]
            self.img_count = 0
        elif (self.isDucking):  #MAKES THE ANIMATION OF THE DINOSAUR RUNNING WHILE DUCKING
            if self.img_count < self.ANIMATION_TIME:
                self.img = self.IMGS[3]
            elif self.img_count < self.ANIMATION_TIME*2:
                self.img = self.IMGS[4]
            elif self.img_count < self.ANIMATION_TIME*2+1:
                self.img = self.IMGS[3]
                self.img_count = 0
                self.isDucking = False
        else:   #MAKES THE ANIMATION OF THE DINOISAUR RUNNING
            """According to the "img_count" and waiting 5 "seconds" to display the next image of the bird eith different wing position"""
            if self.img_count < self.ANIMATION_TIME:
                self.img = self.IMGS[1]
            elif self.img_count < self.ANIMATION_TIME*2:
                self.img = self.IMGS[2]
            elif self.img_count < self.ANIMATION_TIME*2 + 1:
                self.img = self.IMGS[1]
                self.img_count = 0
        
        win.blit(self.img, (self.x,self.y))
    
    #_FUNCTION FOR COLISION_#
    """ Uses the mask to be more acurrate for the user in colision, and not use boxes """
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

###_CREATES THE OBJECT CACTUS_###
class Cactus:
    VEL = 7

    #_FUNCTION CREATES ATRIBUTES OF PIPE | CONSTRUCTOR_#
    def __init__(self, x):
        self.x = x
        self.height = 90

        cacltus_id = random.randint(0,1)

        if (cacltus_id == 0):
            self.height = 90
        else:
            self.height = 110

        self.img = CACTUS_IMGS[cacltus_id]

        self.passed = False #for colision purposes and AI
    
    #_FUNCTION TO MOVE THE PIPE IN X AXIS_#
    def move(self):
        self.x -= self.VEL  #Moves the pipe to the left
    
    #_FUCNTION TO DISPLAY PIPE_#
    def draw(self, win):
        win.blit(self.img, (self.x, self.height))
    
    #_COLITION USING MASK TO BE MORE ACCURATE WITH THE COLISION BOX_#
    """ There will be colision box, however inside the colision box there us a mask (shaped like the bird and the pipe, by checking if the background is transparent) 
    son that although the boxes touch themselves, but the mask dn't, then tere is no colision."""
    def collide(self, dino, win):
        dino_mask = dino.get_mask() #saves the positions of the dinosaur image
        cactus_mask = pygame.mask.from_surface(self.img)    #saves the obstacle position of the cactus

        #checks if the masks collide
        offset = (self.x - dino.x, self.height - round(dino.y))

        point = dino_mask.overlap(cactus_mask, offset)

        if (point):
            return True
         
        return False

#################
###___GAME____###
#################

###__GAME FUNCTIONS__###
#_FUNCTION THAT CREATES A SCREEEN_#
def draw_window(screen, ground, clouds, dino, cacti):
    screen.fill(WHITE)
    ground.draw(screen) #Displays ground
    
    for cloud in clouds:
        cloud.draw(screen)

    dino.draw(screen)   #Displays dinosaur
    
    for cactus in cacti:
        cactus.draw(screen)
    pygame.display.update() #refreshes

#_FUCNTION THAT PALYS THE GAME_#
def main():
    #_Creating Objects_#
    ground = Ground(125) #creates and sets the ground
    clouds = [Cloud(600)]
    dino = Dino(0,95)   #creates and setes the dinosaur
    #cactus = Cactus(550)   #creates a single cactus
    cacti = [Cactus(550)]

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #sets the window size
    screen.fill(WHITE)
    clock = pygame.time.Clock() #creates a control for frame rates

    prev_cactus = 600
    for i in range(2):
        prev_cactus += random.randint(300,600)
        cacti.append(Cactus(prev_cactus))

    run = True
    while run: #Plays game while you don't quit
        clock.tick(30)  #Sets the frame rate at 30

        for event in pygame.event.get():    #when something is clicked then:
            if event.type == pygame.QUIT:   #will quit the loop for the "X" button on the screen
                run = False
                #pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()
                # if event.key == pygame.K_DOWN:
                #     dino.duck()

        keys = pygame.key.get_pressed() #checks for a key of the keyboard is being pressed
        if keys[pygame.K_DOWN]: #if the key is the down arrow, then it will
            dino.duck() #makes dinosaur duck

        add_cactus = False  #establishes not to add a cactus
        rem_cactus = []    #for saving which cactus to delete
        for cactus in cacti:
            
            if (not cactus.passed and cactus.x < dino.x):   #until the dinosaur passes the cactus it will create another one
                cactus.passed = True
                add_cactus = True

            if cactus.collide(dino, screen):
                print('TOUCHED')
            
            if (cactus.x < -30):
                rem_cactus.append(cactus)
            
            cactus.move()
        
        
        if (add_cactus):
            prev_cactus = cacti[len(cacti)-1].x
            prev_cactus += random.randint(200,600)
            cacti.append(Cactus(prev_cactus))

        for re in rem_cactus:
            cacti.remove(re)
        
        
        add_cloud = False
        rem_cloud = []
        for cloud in clouds:
            if (cloud.x < -99):
                add_cloud = True
            
            if (cloud.x < -100):
                rem_cloud.append(cloud)
            
            cloud.move()

        if (add_cloud):
            clouds = [Cloud(600)]
            add_cloud = False
        
        for r in rem_cloud:
            clouds.remove(r)
        

        ground.move()   #Makes the ground move to give a perseption of running
        dino.move()     #Makes the dinosaur constantly run

        draw_window(screen, ground, clouds, dino, cacti) #calls the function "draw_window"


main()