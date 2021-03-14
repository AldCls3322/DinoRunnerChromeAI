import pygame
import os, random

#_IMAGES_#
CACTUS_IMGS = [pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","BigCactus01.png")),(15,30) )), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","SmallCactus01.png")),(10,20) )), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","ManySmallCactus01.png")), (30,20) ))]

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
    """ There will be colision box, however inside the colision box there is a mask (shaped like the cactus, by checking if the background is transparent) 
    so that although the boxes touch themselves, but the mask don't, then tere is no colision."""
    def collide(self, dino, win):
        dino_mask = dino.get_mask() #saves the positions of the dinosaur image
        cactus_mask = pygame.mask.from_surface(self.img)    #saves the obstacle position of the cactus

        #checks if the masks collide
        offset = (self.x - dino.x, self.height - round(dino.y))

        point = dino_mask.overlap(cactus_mask, offset)

        if (point):
            return True
         
        return False