import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def screenwrap(self):
    if(self.position.x > SCREEN_WIDTH):
        self.position.x = 0 + (self.position.x - SCREEN_WIDTH) 
    elif(self.position.x < 0):
        self.position.x = SCREEN_WIDTH + (SCREEN_WIDTH - self.position.x)

    if(self.position.y > SCREEN_HEIGHT):
        self.position.y = 0 + (self.position.y - SCREEN_HEIGHT) 
    elif(self.position.y < 0):
        self.position.y = SCREEN_HEIGHT + (SCREEN_HEIGHT - self.position.y)