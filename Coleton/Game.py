import pygame
pygame.init()

class hero(object):
    def __init__(self,armor,speed,punch,ABmod,Bmod,Mmod,AMmod,spell,resist):
        self.armor = armor
        self.speed = speed
        self.punch = punch
        self.ARmod = ARmod
        self.Rmod = Rmod
        self.AMmod = Mmod
        self.Mmod = Mmod
        self.resist = resist
"""ARmod = alien ranged mod, Rmod = Ranged mod, AMmod = alien melee mod, Mmod = melee mod,
spell is if they can cast spells or not resist = spell resistance,"""
#this is an idea I have on a character class
