import pygame,sys,pyautogui,keyboard,random,time

from pygame import *
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

background = pygame.image.load("background1.jpg")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Space Crash')

SPEED = 5
score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.xcf")
        self.image = pygame.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.rect.center = (520, 200)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
        if self.rect.right > 0:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)     

class Enemy(pygame.sprite.Sprite):
    pass


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bullet.xcf")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        while self.rect.center[1] != 400:
            self.rect.move_ip(0,10)


class Shooter(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("alien_spaceship2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

class Beamer(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shooter.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

class Boss(Enemy):
    pass



P1 = Player()
E1 = Shooter()
E2 = Beamer()
B1 = Bullet()

enemies = pygame.sprite.Group()
enemies.add(B1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(B1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    DISPLAYSURF.blit(background,(0,0))
    scores = font_small.render(str(score),True,BLACK)
    DISPLAYSURF.blit(scores,(10,10))
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image,entity.rect)
        entity.move()

    '''if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over,(30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit
        sys.exit()'''
         
    pygame.display.update()
    Frame_Per_Sec.tick(FPS)