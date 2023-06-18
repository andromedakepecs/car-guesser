import pygame, os, random

CAPTION = "Car Guesser"
WHITE = (255, 255, 255)
FPS = 40

def window():
	pygame.init()
	display_info = pygame.display.Info()
	game_display = pygame.display.set_mode((display_info.current_w, display_info.current_h))
	pygame.display.set_caption(CAPTION)

	clock = pygame.time.Clock()
	quit = False

	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True

		game_display.fill(WHITE)
		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()

def main():
	window()

if __name__ == "__main__":
	main()

