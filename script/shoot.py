import pygame

class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('../assets/bullet2.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

    def move(self, surface):
        while self.y < 590:
            self.y += 5
            surface.blit(self.image, (self.x, self.y))