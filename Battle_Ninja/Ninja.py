import pygame

#Put in whatever ninja image we are using
IMAGE = pygame.image.load()

class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect()

    def move_up(self, units):
        self.rect.y = self.rect.y - units

    def move_down(self, units):
        self.rect.y = self.rect.y + units

    def move_right(self, units):
        self.rect.x = self.rect.x + units

    def move_left(self, units):
        self.rect.x = self.rect.x - units     