import pygame
from pygame.locals import *
from enemy import Enemy
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ROW = 3
COL = 5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')
bg = pygame.image.load('../assets/background.png')


def draw_bg():
    screen.blit(bg, (0, 0))


class Hero_ship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/ship.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        speed = 8
        cooldown = 200

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        elif key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += speed
        time_now = pygame.time.get_ticks()
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        #draw health bar
        pygame.draw.rect(screen, 'red', (self.rect.x, (self.rect.bottom - 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, 'green', (
                self.rect.x, (self.rect.bottom - 10),
                int(self.rect.width * (self.health_remaining / self.health_start)),
                15))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/bullet2.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > 0:
            self.kill()

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


hero_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

def create_aliens():
    for row in range(ROW):
        for item in range(COL):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)


create_aliens()
hero_ship = Hero_ship(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT - 70), 3)
hero_group.add(hero_ship)

clock = pygame.time.Clock()
FPS = 40
run = True

enemy_locations = [(5, 10), (65, 10), (125, 10), (185, 10), (245, 10), (305, 10), (365, 10), (425, 10), (485, 10),
                   (545, 10),
                   (5, 70), (65, 70), (125, 70), (185, 70), (245, 70), (305, 70), (365, 70), (425, 70), (485, 70),
                   (545, 70),
                   (5, 130), (65, 130), (125, 130), (185, 130), (245, 130), (305, 130), (365, 130), (425, 130),
                   (485, 130), (545, 130)]
ENEMIES = []
for pos in enemy_locations:
    enemy = Enemy(pos)
    ENEMIES.append(enemy)
while run:
    clock.tick(FPS)
    draw_bg()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    hero_ship.update()
    bullet_group.update()
    alien_group.update()
    alien_bullet_group.update()


    #update sprite groups
    hero_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)

    pygame.display.update()
pygame.quit()
