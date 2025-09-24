import pygame

class Exit(pygame.sprite.Sprite):

    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        lava = pygame.image.load('image/Environment/portal.png')
        self.image = pygame.transform.scale(lava, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        