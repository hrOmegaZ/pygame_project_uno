import pygame,sys,pyautogui,keyboard,random

from pygame.locals import *

pygame.init()

FPS = 30
Frame_Per_Sec = pygame.time.Clock()


BLACK = (0, 0, 0)

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
GREY = (128,128,128)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

score = 0

class Player():
    pass

class Enemy():
    pass

class Bullet():
    pass