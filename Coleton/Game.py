import pygame
pygame.init()

class Enemy(object):
    def __init__(self,armor,speed,resist):
        self.armor = armor
        self.speed = speed
        self.resist = resist
# resist = spell resist
