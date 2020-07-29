import pygame 
import random 

class Asteroid(pygame.sprite.Sprite):
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load('asteroid.png')
    self.image = pygame.transform.smoothscale(self.image, (80,80))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(0,800), random.randint(0,600))
