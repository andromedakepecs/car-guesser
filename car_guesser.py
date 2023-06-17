import os, random
from PIL import Image

CROP_WIDTH = 160

# Path to car directory
car_dir = os.getcwd() + "/car-pictures"

# Get random car file
car_f = random.choice([x for x in os.listdir(car_dir) if os.path.isfile(os.path.join(car_dir, x))])
print(car_f)

# Open the image in RGB mode
car_path = car_dir + "/" + car_f
car_img = Image.open(car_path)
car_img.show() # test

# Randomly crop the image
width, height = car_img.size
left = random.randint(0, width - CROP_WIDTH)
top = height / 4
right = left + CROP_WIDTH
bottom = 3 * height / 4

cropped_img = car_img.crop((left, top, right, bottom))
cropped_img.show()


