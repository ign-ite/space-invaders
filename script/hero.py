import pygame

class Hero(object):
    def __init__(self):
        self.image = pygame.image.load('../assets/ship.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.x = 270
        self.y = 540

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        dist = 5
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= dist
        elif keys[pygame.K_RIGHT] and self.x < 525:
            self.x += dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))