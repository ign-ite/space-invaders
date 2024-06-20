import pygame
from pygame import *
from hero import Hero

pygame.init()
screen = display.set_mode((600, 600))
clock = time.Clock()
FPS = 40
run = True
hero = Hero()


while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    hero.handle_keys()

    screen.fill('black')
    hero.draw(screen)
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()
