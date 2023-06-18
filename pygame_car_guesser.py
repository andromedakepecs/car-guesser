import pygame, os, random

CAPTION = "Car Guesser"
CROP_WIDTH = 160
WHITE = (255, 255, 255)
FPS = 40

def get_input():
	"""
	Gets user input in pygame window
	"""
	pass

def get_random_image_file():
	"""
	Gets random image from car-pictures directory
	Return String file name of random image
	"""
	car_dir = os.getcwd() + "/car-pictures"

	# Get random car file
	car_f = random.choice([x for x in os.listdir(car_dir) if os.path.isfile(os.path.join(car_dir, x))])
	return car_dir + "/" + car_f

def crop_image(img, orig_x, orig_y):
	"""
	Randomly crop the image
	Param orig_x, x coord of original image
	Param orig_y, y coord of original image
	Return cropped image
	"""
	# left = random.randint(0, img.get_width() - CROP_WIDTH)
	# top = img.get_height() / 4
	# right = left + CROP_WIDTH
	# bottom = 3 * img.get_height() / 4
	# cropped_img = img.crop((left, top, right, bottom))
	# return pygame.image.load(cropped_img).convert()

	x = random.randint(orig_x, orig_x + img.get_width() - CROP_WIDTH)
	y = (orig_y + img.get_height()) / 4
	width = x + CROP_WIDTH
	height = 3 * y
	return img.subsurface((x, y, width, height))


def display_image(img, game_display, img_x, img_y):
	"""
	Displays image
	Parameter img image
	"""
	game_display.blit(img, (img_x, img_y))
	pygame.display.flip()

def run_game():
	"""
	Runs the game
	"""
	# Open window and get display info
	pygame.init()
	display_info = pygame.display.Info()
	width = display_info.current_w
	height = display_info.current_h
	game_display = pygame.display.set_mode((width, height))
	pygame.display.set_caption(CAPTION)

	clock = pygame.time.Clock()
	quit = False

	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True

		game_display.fill(WHITE)

		# Display image
		img_path = get_random_image_file()
		img = pygame.image.load(img_path).convert()
		img_x = width / 2 - img.get_width() / 2
		img_y = height / 2 - img.get_height()

		cropped_img = crop_image(img, img_x, img_y)
		display_image(img, game_display, img_x, img_y)

		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()

def main():
	"""
	Main method
	"""
	run_game()

if __name__ == "__main__":
	main()

