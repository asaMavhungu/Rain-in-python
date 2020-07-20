import pygame

resolution = (640, 360)

WINDOW = pygame.display.set_mode(resolution)

BLUE = (102, 153, 255)
BLUE_DARK = (0, 0, 153)

class Drop(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.yspeed = 0.05

	def fall(self):
		self.y += self.yspeed

	def show(self):
		self.y = self.y
		pygame.draw.rect(WINDOW, BLUE_DARK, [self.x, self.y, 2, 9])








def main():

	d = Drop(640/2 , 360/2)

	drops = [Drop(i, 10) for i in range(0, 640, 10)]

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