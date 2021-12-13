import time,pygame,sys,random

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
won = font.render("You Win", True, BLACK)

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
        self.image = pygame.transform.scale(self.image, (75,50))
        self.rect = self.image.get_rect()
        self.rect.center = (520, 200)

    def move(self):
        global player_pos
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            if self.rect.center[1] - 45 > 0:
                self.rect.move_ip(0,-5)
            else:
                pass
        if pressed_keys[K_DOWN]:
            if self.rect.center[1] + 50 < SCREEN_HEIGHT:
                self.rect.move_ip(0,5)
            else:
                pass
        if self.rect.left > 100:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-4,0)
        if self.rect.right < SCREEN_WIDTH-25:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(3,0)
        player_pos = self.rect[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)     

class Enemy(pygame.sprite.Sprite):
    pass


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
        pygame.mixer.Sound('pssst-1 (1).wav').play()

    def move(self):
        global bullet_pos
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT+SPEED):
            self.rect.top = 0
            self.rect.center = (shooter_pos,random.randint(0,40))
        bullet_pos = self.rect[1]

class Bullet_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
        pygame.mixer.Sound('pssst-1 (1).wav').play()

    def move(self):
        global bullet_pos2
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT+SPEED):
            self.rect.top = 0
            self.rect.center = (beamer_pos,random.randint(0,40))
        bullet_pos2 = self.rect[1]

class Bullet3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
        pygame.mixer.Sound('pssst-1 (1).wav').play()

    def move(self):
        global bullet_pos3
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT+SPEED):
            self.rect.top = 0
            self.rect.center = (beamer_pos,random.randint(0,40))
        bullet_pos3 = self.rect[1]


class Beamer(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("alien_spaceship2.png")
        self.image = pygame.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-100),0)

    def move(self):
        global beamer_pos
        move = random.randint(1,2)
        if self.rect.left > 0:
            if move == 1:
                for x in range(2):
                    self.rect.move_ip(-3,0)
        if self.rect.right < SCREEN_WIDTH-20:
            if move == 2:
                for x in range(2):
                    self.rect.move_ip(3,0)
        beamer_pos = self.rect[0] + 75

class Shooter(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shooter.png")
        self.image = pygame.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-100),0)
    
    def move(self):
        global shooter_pos
        move = random.randint(1,2)
        if self.rect.left > 0:
            if move == 1:
                for x in range(3):
                    self.rect.move_ip(-3,0)
        if self.rect.right < SCREEN_WIDTH-20:
            if move == 2:
                for x in range(3):
                    self.rect.move_ip(3,0)
        shooter_pos = self.rect[0] + 75

class Shooter2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shooter.png")
        self.image = pygame.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-100),0)
    
    def move(self):
        global shooter_pos2
        move = random.randint(1,2)
        if self.rect.left > 0:
            if move == 1:
                for x in range(3):
                    self.rect.move_ip(-3,0)
        if self.rect.right < SCREEN_WIDTH-20:
            if move == 2:
                for x in range(3):
                    self.rect.move_ip(3,0)
        shooter_pos2 = self.rect[0] + 75

class power_up(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,SCREEN_WIDTH), random.randint(100,SCREEN_HEIGHT))
    
    def move(self):
        self.rect.move_ip(0,0)

shooter_pos = 0
shooter_pos2 = 0
beamer_pos = 0
player_pos = 0
bullet_pos = 0
bullet_pos2 = 0
bullet_pos3 = 0
number = 5
power_time = False
power = []
start_time = 0
max_time = 10
power.append(random.randint(10,33))
power.append(random.randint(33,66))
power.append(random.randint(66,100))

P1 = Player()
E1 = Shooter()
E3 = Shooter2()
E2 = Beamer()
B1 = Bullet()
B2 = Bullet_2()
B3 = Bullet3()
PU1 = power_up()

enemies = pygame.sprite.Group()
enemies.add(B1)
enemies.add(B2)
enemies.add(E1)
enemies.add(E2)

power_ups = pygame.sprite.Group()
power_ups.add(PU1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(B1)
all_sprites.add(B2)
all_sprites.add(E1)
all_sprites.add(E2)

while True:
    pygame.mixer.Sound('ChillingMusic.wav').play()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    DISPLAYSURF.blit(background,(0,0))
    scores = font_small.render(str(score),True,WHITE)
    DISPLAYSURF.blit(scores,(10,10))
    
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image,entity.rect)
        
        entity.move()
        print(time.time() - start_time)
        if (time.time() - start_time) < max_time:
            DISPLAYSURF.blit(PU1.image,PU1.rect)
        else:
            power_time = False

    for amount in power:
        if amount == score:
            DISPLAYSURF.blit(PU1.image,PU1.rect)
            
    if bullet_pos > SCREEN_HEIGHT:
        score += 1
    if bullet_pos2 > SCREEN_HEIGHT:
        score += 1
    if bullet_pos3 > SCREEN_HEIGHT:
        score += 1
    
    if score > number:
        SPEED += 1
        number = number + 5

    if score == 50:
        enemies.add(E3)
        all_sprites.add(E3)
        enemies.add(B3)
        all_sprites.add(B3)

    if pygame.sprite.spritecollideany(P1,enemies) and power_time == False:
        pygame.mixer.Sound('crash.wav').play()
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over,(150,150))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit
        sys.exit()

    if pygame.sprite.spritecollideany(P1,power_ups):
        power_time = True
        for entity in power_ups:
            start_time = time.time()

    if score == 100:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(won,(160,150))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit
        sys.exit()
         
    pygame.display.update()
    Frame_Per_Sec.tick(FPS)