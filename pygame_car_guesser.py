import pygame, os, random

CAPTION = "Car Guesser"
WHITE = (255, 255, 255)
FPS = 40

# def get_input(display, event):
# 	"""
# 	Gets user input in pygame window and displays
# 	Param event
# 	Return input
# 	TODO change magic numbers to screen-size related
# 	"""
# 	# Font
# 	font = pygame.font.Font(None, 32)
# 	user_text = ""
# 	input_rect = pygame.Rect(200, 200, 140, 32)
	
# 	color = pygame.Color('lightskyblue3')

# 	if event.key == pygame.K_BACKSPACE:
# 		user_text = user_text[:-1]
# 	else:
# 		user_text += event.unicode

# 	pygame.draw.rect(display, color, input_rect)

# 	text_surface = font.render(user_text, True, WHITE)
# 	display.blit(text_surface, (input_rect.x+5, input_rect.y+5))

# 	input_rect.w = max(100, text_surface.get_width()+10)
# 	pygame.display.flip()

# 	if event.key == pygame.K_RETURN:
# 		return user_text

def get_random_image_file():
	"""
	Gets random image from car-pictures directory
	Return String file name of random image
	"""
	car_dir = os.getcwd() + "/car-pictures"

	# Get random car file
	car_f = random.choice([x for x in os.listdir(car_dir) if os.path.isfile(os.path.join(car_dir, x))])
	return car_dir + "/" + car_f

def crop(img):
	"""
	Randomly crop the image
	Param img original image
	Return Surface cropped image
	"""
	# x and y coordinates in relation to the surface (regardless of surface location on screen)
	x = random.randint(0, int(img.get_width() / 2))
	y = random.randint(0, int(img.get_height() / 2))
	width = img.get_width() / 2
	height = img.get_height() / 2

	cropped_region = (x, y, width, height)
	return img.subsurface(cropped_region)

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

	turn = 0 # TODO use turns to determine if quizzing brand model year?
	user_input = ""
	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True
			# TODO if statements
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					user_input += user_input[:-1]
				elif event.key == pygame.K_RETURN:
					pass # TODO check input as guess
				elif event.key == pygame.K_UP:
					pass # TODO up arrow key zoom in
					#IMAGE_BIG = pygame.transform.rotozoom(cropped_img, 0, 5)
				elif event.key == pygame.K_DOWN:
					pass # TODO down arrow key zoom out
				else:
					user_input += event.unicode

		game_display.fill(WHITE)

		# Load image and get info
		img_path = get_random_image_file()
		img = pygame.image.load(img_path).convert()
		img_x = width / 2 - img.get_width() / 2
		img_y = height / 2 - img.get_height()

		# Crop image
		cropped_img = crop(img)

		# Display cropped image
		cropped_img_coord = ((width / 2 - cropped_img.get_width() / 2), height / 2 - cropped_img.get_height())
		game_display.blit(cropped_img, cropped_img_coord)
		pygame.display.flip()

		# # Display original image
		# game_display.blit(img, (img_x, img_y))
		# pygame.display.flip()

		# pygame.display.update()
		clock.tick(FPS)

	pygame.quit()

def main():
	"""
	Main method
	"""
	run_game()

if __name__ == "__main__":
	main()

