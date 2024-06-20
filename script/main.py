import pygame
from pygame import *
from hero import Hero
from enemy import Enemy
from random import randint

pygame.init()
screen = display.set_mode((600, 600))
clock = time.Clock()
FPS = 40
run = True
hero = Hero()
enemy_locations = [(5, 10),(65, 10), (125, 10), (185, 10), (245, 10), (305, 10), (365, 10), (425, 10), (485, 10), (545, 10),
                   (5, 70),(65, 70), (125, 70), (185, 70), (245, 70), (305, 70), (365, 70), (425, 70), (485, 70), (545, 70),
                   (5, 130),(65, 130), (125, 130), (185, 130), (245, 130), (305, 130), (365, 130), (425, 130), (485, 130), (545, 130)]
ENEMIES = []
for pos in enemy_locations:
    enemy = Enemy(pos)
    ENEMIES.append(enemy)
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    hero.handle_keys(screen)

    screen.fill('black')
    hero.draw(screen)
    ENEMIES[randint(0, len(ENEMIES) - 1)].drop(screen)



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
