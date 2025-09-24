import pygame

class Lava(pygame.sprite.Sprite):

    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        lava = pygame.image.load('image/Environment/lava.png')
        self.image = pygame.transform.scale(lava, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + (tile_size/2)
        