import pygame
from Lava import Lava
from Exit import Exit
from Flag import Flag

class World():

	def __init__(self, data, tile_size, tile_sizex, tile_sizey):

		self.tile_list = []

		dirt = pygame.image.load('image/Environment/dirt.png')
		grass = pygame.image.load('image/Environment/grass.png')
		flag = pygame.image.load('image/Environment/flag.png')

		self.lava_group = pygame.sprite.Group()
		self.exit_group = pygame.sprite.Group()
		self.flag_group = pygame.sprite.Group()

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt, (tile_sizex, tile_sizey))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_sizex
					img_rect.y = row_count * tile_sizey
					tile = (img, img_rect)
					self.tile_list.append(tile)

				if tile == 2:
					img = pygame.transform.scale(grass, (tile_sizex, tile_sizey))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_sizex
					img_rect.y = row_count * tile_sizey
					tile = (img, img_rect)
					self.tile_list.append(tile)
				
				if tile == 3:
					lava = Lava(col_count * tile_sizex, row_count * tile_sizey, tile_sizex)
					self.lava_group.add(lava)
				
				if tile == 4:
					exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2), tile_size)
					self.exit_group.add(exit)

				if tile == 5:
					
					flag = Flag(col_count * tile_size, row_count * tile_size - (tile_size // 2.08), tile_size)
					self.flag_group.add(flag)

				col_count += 1
			row_count += 1


	def draw(self, screen):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])