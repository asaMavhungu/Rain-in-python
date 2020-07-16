# Import and init
import pygame
pygame.init()
pygame.mixer.init()
# define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Rain coordinates
x = 0
y = 5
# open new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Real True Work of art")

carryOn = True
clock = pygame.time.Clock()

if 1 ==1:
	pass
# Main loop
while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False

	# Game logic
	if 1==2:
		pass
	# make screen black

	screen.fill(black)
	pygame.draw.line(screen, white, (349, x), (349, y), 5)
	x += 1
	y += 1

	pygame.display.flip()

pygame.quit()
