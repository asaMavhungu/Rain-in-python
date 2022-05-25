# Author: Asakundwi Mavhungu
# Date: 25 May 2022

# Dependencies: Pygame
# install with the cli command "pip install pygame" 

import pygame
import random

FPS = 75

WIDTH = 640
HEIGHT = 360
resolution = (WIDTH, HEIGHT)

WINDOW = pygame.display.set_mode(resolution)
pygame.display.set_caption("Rain in Pygame by Asakundwi Mavhungu")

BLUE = (102, 204, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Drop(object):
	"""
	A drop object
	A rectangle of certain color and dimensions
	"""
	def __init__(self):
		self.x = random.randint(0, WIDTH)
		self.y = random.randint(-200, -100)
		self.yspeed = random.randint(15, 25)
		self.width = 1
		self.height = 18

	def fall(self):
		"""
		Increase the y-value of a drop object
		"""
		self.y += self.yspeed
		self.yspeed += 0.15

		if self.y > HEIGHT:
			self.y = random.randint(-200, -100)
			self.x = random.randint(0, WIDTH)
			self.yspeed = random.randint(5, 12)

	def show(self):
		"""
		Draw a drop object to the display
		"""
		pygame.draw.rect(WINDOW, WHITE, [self.x, self.y, self.width, self.height])

def main():

	# Create 225 drops
	drops = [Drop() for _ in range(0, 225)]
	clock = pygame.time.Clock()

	running = True
	while running:

		clock.tick(FPS)

		# close window event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Fill the background with black
		WINDOW.fill(BLACK)

		# Let the drops fall and update the window
		for x in drops:
			x.fall()
			x.show()

		# refresh the display
		pygame.display.flip()

if __name__ == '__main__':
	main()