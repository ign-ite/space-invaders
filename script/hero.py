import pygame
from shoot import Bullet



    def handle_keys(self, surface):
        keys = pygame.key.get_pressed()
        dist = 5
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= dist
        elif keys[pygame.K_RIGHT] and self.x < 525:
            self.x += dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))