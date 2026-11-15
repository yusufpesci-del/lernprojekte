import os
import sys
from PIL import Image, ImageOps




if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()

if output_ext not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif input_ext != output_ext:
    sys.exit("Input and output have different extensions")


shirt = Image.open("shirt.png")

try:
    photo = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

photo = ImageOps.fit(photo, shirt.size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])





# erlaubt	.jpg, .jpeg, .png — mehr als eine
# Groß/Klein egal	.JPG muss genauso gelten wie .jpg
# beide gleich	rein .jpg und raus .png ist ein Fehler. Auch .jpg → .jpeg

