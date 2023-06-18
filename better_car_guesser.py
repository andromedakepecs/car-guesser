import os, random, time
from PIL import Image

"""
Car Guessing Game in Console with Primitive Image Show
@author Andromeda Kepecs
"""

def crop_image(img):
	"""
	Crop an image
	@param Image original image
	@return Image cropped image
	"""
	w, h = img.size
	left = random.randint(0, w / 2)
	top = h / 4
	right = left + w / 2
	bottom = 3 * h / 4
	return img.crop((left, top, right, bottom))

def make_guess(inp, img, car_file, loc, game_info, car_info):
	"""
	Let user guess twice, showing full image on second guess
	@param inp String initial user input
	@param img Image original image
	@param car_file String full path to car image file
	@param loc int location of info ie brand model year in car info
	@param game_info list of score etc.
	@param car_info list of car info
	@return String state to indicate removal of file
	"""
	if inp.lower() == car_info[loc].lower():
		print("Correct!")
		game_info[2 * loc] += 1
	else:
		print("Incorrect :( Try again with the full picture:")
		img.show()
		inp = input("Guess again: ")
		if inp.lower() == car_info[loc].lower():
			print("Correct!")
			game_info[2 * loc + 1] += 1
		else:
			print("Incorrect :( The correct answer is", car_info[loc])
			return "remove"

def remove_file(file):
	"""
	Remove a file from the quiz set
	@param File file
	@return boolean if file is removed
	"""
	inp = input("Would you like to remove this car from the quiz set? ")
	if inp.lower() == "yes":
		inp = input("Are you sure? Type REMOVE to confirm: ")
		if inp == "REMOVE":
			os.remove(file)
			return True

def fun_facts(car_info):
	"""
	Print car fun facts
	"""
	msrp = car_info[3]
	front_wheel_size = car_info[4]
	horsepower = car_info[5]
	width = car_info[8]
	height = car_info[9]
	length = car_info[10]
	gas_mileage = car_info[11]
	print("(Disclaimer: these facts may be inaccurate)")
	print("Did you know the", car_info[2], car_info[0], car_info[1], "has...")
	print("\tan approximate MSRP of $" + msrp + "k")
	print("\ta front wheel size of", front_wheel_size)
	print("\tapproximately", horsepower, "horsepower")
	print("\ta maximum width of", width, "inches")
	print("\tan overall height of", height, "inches")
	print("\tan overall length of", length, "inches")
	print("\tand a gas mileage of approximately", gas_mileage, "mpg")


def play_game():
	"""
	Play the car guessing game
	@return list of game info 
	"""

	# brandguess1, brandguess2, modelguess1, modelguess2, yearguess1, yearguess2, total
	game_info = [0, 0, 0, 0, 0, 0, 0]
	
	while True:
		fp = os.getcwd() + "/car-pictures"
		rand_file = random.choice([x for x in os.listdir(fp) if os.path.isfile(os.path.join(fp, x))])

		full_path = fp + "/" + rand_file
		img = Image.open(full_path)
		cropped_img = crop_image(img)

		cropped_img.show()

		car_info = rand_file.split("_")

		# User guesses
		cat_num = 0
		while cat_num <= 2:
			category = ""
			if cat_num == 0:
				category = "brand"
			elif cat_num == 1:
				category = "model"
			else:
				category = "year"

			inp = input("Guess the " + category + ": ")
			state = make_guess(inp, img, full_path, cat_num, game_info, car_info)
			if state == "remove":
				if remove_file(full_path):
					break
			cat_num += 1

		game_info[6] += 1

		inp = input("Want to know some fun facts about this car? ")
		if "yes" in inp.lower():
			fun_facts(car_info)

		inp = input("Play again? ")
		if "no" in inp.lower():
			return game_info

def print_result(one, two, total, category):
	"""
	Print result
	@param int one num guessed in one try
	@param int two num guessed in two tries
	@param int total number of cars guessed
	@param String category ie brand model year
	"""
	print("You guessed", one, category, "in one try!")
	print("You guessed", two, category, "in two tries!")
	percent_correct = int((one+two)/total * 100)
	if percent_correct > 50:
		print("You got " + str(percent_correct) + "% correct! Great job!")
	else:
		print("You got " + str(percent_correct) + "% correct! You can do better...")

	print()

def print_results(game_info):
	"""
	Print game results
	@param list of game info
	"""
	bg1, bg2, mg1, mg2, yg1, yg2, t = game_info

	print_result(bg1, bg2, t, "brands")
	print_result(mg1, mg2, t, "models")
	print_result(yg1, yg2, t, "years")

def main():
	print("Welcome to console-based Car Guessing Game!")
	game_info = play_game()
	print_results(game_info)

if __name__ == "__main__":
	main()