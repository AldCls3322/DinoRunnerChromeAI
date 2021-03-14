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