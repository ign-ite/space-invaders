import pygame


class Enemy(object):
    def __init__(self, pos):
        self.image = pygame.image.load('../assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def drop(self, screen):
        self.pos = (self.pos[0] - self.pos[1])
        self.draw(screen)