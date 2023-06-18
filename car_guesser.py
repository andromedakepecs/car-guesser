import os, random, time
from PIL import Image

CROP_WIDTH = 160

brands_guessed_one_try = 0
brands_guessed_two_try = 0

models_guessed_one_try = 0
models_guessed_two_try = 0

years_guessed_one_try = 0
years_guessed_two_try = 0

while True:
	# Path to car directory
	car_dir = os.getcwd() + "/car-pictures"

	# Get random car file
	car_f = random.choice([x for x in os.listdir(car_dir) if os.path.isfile(os.path.join(car_dir, x))])

	# Open the image in RGB mode
	car_path = car_dir + "/" + car_f
	car_img = Image.open(car_path)

	# Randomly crop the image
	width, height = car_img.size
	left = random.randint(0, width - CROP_WIDTH)
	top = height / 4
	right = left + CROP_WIDTH
	bottom = 3 * height / 4

	cropped_img = car_img.crop((left, top, right, bottom))
	cropped_img.show() # TODO better image viewer

	# Guessing game
	car_info = car_f.split("_")
	print(car_info) # testing purposes TODO delete

	brand_guess = input("Guess the brand: ")
	if brand_guess.lower() == "exit":
		break
	elif brand_guess.lower() in car_info[0].lower():
		print("Correct!")
		brands_guessed_one_try += 1
	else:
		print("Incorrect :(")
		car_img.show()
		brand_guess = input("Guess again: ")
		if brand_guess.lower() in car_info[0].lower():
			print("Correct!")
			brands_guessed_two_try += 1
		else:
			print("Incorrect :( The correct answer is", car_f)
			continue

	model_guess = input("Guess the model: ")
	if model_guess.lower() in car_info[1].lower():
		print("Correct!")
		models_guessed_one_try += 1
	else:
		print("Incorrect :(")
		car_img.show()
		model_guess = input("Guess again: ")
		if model_guess.lower() in car_info[1].lower():
			print("Correct!")
			models_guessed_two_try += 1
		else:
			print("Incorrect :( The correct answer is", car_f)
			continue

	year_guess = input("Guess the year: ")
	if year_guess.lower() in car_info[2].lower():
		print("Correct!")
		years_guessed_one_try += 1
	else:
		print("Incorrect :(")
		car_img.show()
		year_guess = input("Guess again: ")
		if year_guess.lower() in car_info[2].lower():
			print("Correct!")
			years_guessed_two_try += 1
		else:
			print("Incorrect :( The correct answer is", car_f)
			continue
	print("Here's the full image:")
	car_img.show()
	time.sleep(2)
	print("Next car!")

print("You guessed", brands_guessed_one_try, "in one try!")
print("You guessed", brands_guessed_two_try, "in two tries!")
print("You guessed", models_guessed_one_try, "in one try!")
print("You guessed", models_guessed_two_try, "in two tries!")
print("You guessed", years_guessed_one_try, "in one try!")
print("You guessed", years_guessed_two_try, "in two tries!")


	# if answer == too difficult ask would you like to remove this image from the quiz set
	# if answer yes then os.remove()


