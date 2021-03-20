import pygame
import os, random

#_IMAGES_#
DINO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dino01.png"))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoRun01.png")),(24,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoRun02.png")),(24,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoDuck01Fixed.png")),(34,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoDuck02Fixed.png")),(34,28))), pygame.transform.scale2x(pygame.transform.scale(pygame.image.load(os.path.join("Game/IMGS","dinoJump01.png")),(24,25))), pygame.transform.scale2x(pygame.image.load(os.path.join("Game/IMGS","dinoDeath01.png")))]

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
                self.y = 95

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

