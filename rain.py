import pygame
import random

resolution = (640, 360)

WINDOW = pygame.display.set_mode(resolution)

BLUE = (102, 153, 255)
BLUE_DARK = (0, 0, 153)

class Drop(object):
	def __init__(self, num):
		self.x = random.randrange(0, 640)
		self.y = random.randrange(-200, -100)
		self.speed = random.randrange(100, 250)
		self.yspeed = self.speed/350

	def fall(self):
		self.y += self.yspeed

		if self.y > 360:
			self.y = random.randrange(-200, -100)

	def show(self):
		self.y = self.y
		pygame.draw.rect(WINDOW, BLUE_DARK, [self.x, self.y, 2, 9])








def main():



	drops = [Drop(i) for i in range(0, 100)]

	running = True
	while running:

		# Did the user click the window close button?
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Fill the background with white
		WINDOW.fill(BLUE)

		for x in drops:
			x.fall()
			x.show()

	    # Flip the display
		pygame.display.flip()

main()