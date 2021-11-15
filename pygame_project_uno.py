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

font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont('Verdana',20)
game_over = font.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('pygame thingy')

SPEED = 5
score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("alien_shaceship2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

P1 = Player()
E1 = Enemy()
E2 = Bullet()