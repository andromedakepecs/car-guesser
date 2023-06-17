import os, random
from PIL import Image

# Path to car directory
car_dir = os.getcwd() + "/car-pictures"

# Get random car file
car_f = random.choice([x for x in os.listdir(car_dir) if os.path.isfile(os.path.join(car_dir, x))])

# Open the image in RGB mode
car_path = car_dir + "/" + car_f
car_img = Image.open(car_path)


