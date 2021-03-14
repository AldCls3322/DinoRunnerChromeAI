import pygame
import os, random

#_IMAGES_#
BIRD_IMGS = [pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","bird01.png")),(23, 20) )), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","bird02.png")),(23,20) ))]

###__CREATES THE OBJECT BIRD__###
class Bird:
    ##_CONSTANT VARIABLES USED_##
    IMGS = BIRD_IMGS
    ANIMATION_TIME = 3
    VEL = 10

    #_ESTABLISHED THE ATRIBUTES OF THE OBJECT BIRD | CONSTRUCTOR_#
    def __init__(self, x):
        self.x = x
        self.y = random.randint(0,70)
        self.img_count = 0
        self.img = self.IMGS[0]
    
    #_FUNCTION TO MOVE THE BIRD IN X AXIS_#
    def move(self):
        self.x -= self.VEL  #Moves the bird to the left

    #_FUNCTION TO CREATE ANIMATION_#    
    def draw(self, win):
        self.img_count += 1

        #MAKES THE ANIMATION OF THE BIRD FLAPPING THE WINGS
        """According to the "img_count" and waiting 5 "seconds" to display the next image of the bird eith different wing position"""
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*2 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        
        win.blit(self.img, (self.x, self.y))
        
    #_COLITION USING MASK TO BE MORE ACCURATE WITH THE COLISION BOX_#
    """ There will be colision box, however inside the colision box there is a mask (shaped like the bird, by checking if the background is transparent) 
    so that although the boxes touch themselves, but the mask don't, then tere is no colision."""
    def collide(self, dino, win):
        dino_mask = dino.get_mask() #saves the positions of the dinosaur image
        bird_mask = pygame.mask.from_surface(self.img)    #saves the obstacle position of the bird

        #checks if the masks collide
        offset = (self.x - dino.x, self.y - round(dino.y))

        point = dino_mask.overlap(bird_mask, offset)

        if (point):
            return True
         
        return False