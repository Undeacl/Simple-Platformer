import pygame
from Animations_Final import SpriteSheet

class Flag(pygame.sprite.Sprite):

    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
		
        self.animates = 0
        
        self.master_animation_list = []

        self.last_update = pygame.time.get_ticks()
	    
        self.frame = 0
				
		#creating the animation for the flag
		
        empty_list = []
			
        type = pygame.image.load(f'image/Environment/flag_animation.png').convert_alpha()

        sprite = SpriteSheet(type, 60)

		#iterate how many sprite is being added
        for image in range(int(sprite.total)):
            empty_list.append(sprite.get_image(image, 60, 60, 1.5))

        self.master_animation_list.append(empty_list)	
		
		#define the character
        self.image = self.master_animation_list[self.animates][self.frame]

        self.image = pygame.transform.scale(self.image, (tile_size * 1.5, tile_size * 1.5))
		
        self.width = self.image.get_width()

        self.height = self.image.get_height()

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

		#character's mask
        self.mask = pygame.mask.from_surface(self.image)
    
    #update the animation
    def update(self, screen, tile_size):

        COOLDOWN = 150
		
		#cycle through the frame/sprite
        if pygame.time.get_ticks() - self.last_update >= COOLDOWN:
            self.frame += 1
            self.last_update = pygame.time.get_ticks()

        if self.frame >= len(self.master_animation_list[self.animates]):
            self.frame = 0
            #check to see if the animation has run once
            self.animation_complete = True
		
        self.image = self.master_animation_list[self.animates][self.frame]
        self.image = pygame.transform.scale(self.image, (tile_size * 1.5, tile_size * 1.5))

        screen.blit(self.image, self.rect)