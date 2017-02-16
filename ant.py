import random

class Ant(object):
    def __init__(self,color,size):
        self.x = random.randint(10,size[0])
        self.y = random.randint(10,size[1])
        self.direction = random.randint(0,4)
        self.color = color
