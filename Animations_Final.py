import pygame

class SpriteSheet():
	def __init__(self, image, dimension):
		self.sheet = image
		#count how many individual sprite there are inside the sprite sheet
		self.width = self.sheet.get_width()
		self.total = self.width / dimension

	def get_image(self, frame, width, height, scale):
		image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))

		return image