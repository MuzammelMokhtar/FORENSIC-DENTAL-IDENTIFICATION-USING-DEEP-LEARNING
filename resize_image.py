from PIL import Image
import os

images = [file for file in os.listdir() if file.endswith(('jpg'))]
for image in images:
    img = Image.open(image)
    img.thumbnail((416,416))
    img.save("rs_"+image, optimize=True, quality=95)


