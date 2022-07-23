from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage import io
from PIL import Image
import numpy as np
import cv2
import os

a = '136_'
p = 1

# Selfie
image_directory = r'C:\Users\Muzammel\Desktop\YOLOv4\Images3\Respondent_136/'
save_to_dir = r'C:\Users\Muzammel\Desktop\YOLOv4\Images3\Respondent_136'
im = cv2.imread('C:/Users/Muzammel/Desktop/YOLOv4/Images3/Respondent_136/rs_A13603X1.jpg')
WIDTH = im.shape[1]
HEIGHT = im.shape[0]


# Teeth
image_directory_2 = r'C:\Users\Muzammel\Desktop\YOLOv4\Images3_teeth\Respondent_136/'
save_to_dir_2 = r'C:\Users\Muzammel\Desktop\YOLOv4\Images3_teeth\Respondent_136'
#IM2 = cv2.imread('C:/Users/Muzammel/Desktop/YOLOv4/Images3_teeth/Respondent_3/rs_A00204.jpg')
#WIDTH2 = IM2.shape[1]
#HEIGHT2 = IM2.shape[0]
WIDTH2 = 416
HEIGHT2 = 277



################################################################################################## 0


datagen = ImageDataGenerator(
	rotation_range=30,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a + str(p),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break



################################################################################################################### 1

datagen = ImageDataGenerator(
	rotation_range=60,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a + str(p+1),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


#################################################################################################################### 2

datagen = ImageDataGenerator(
	rotation_range=90,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a + str(p+2),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break





#################################################################################################################### 3

datagen = ImageDataGenerator(
	rotation_range=120,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")


dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a + str(p+3),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break




#################################################################################################################### 4


datagen = ImageDataGenerator(
	rotation_range=150,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a +  str(p+4),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


#################################################################################################################### 5


datagen = ImageDataGenerator(
	rotation_range=180,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH,HEIGHT))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir,
                          save_prefix= a + str(p+5),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 6


datagen = ImageDataGenerator(
	rotation_range=30,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+6),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 7


datagen = ImageDataGenerator(
	rotation_range=60,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+7),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 8


datagen = ImageDataGenerator(
	rotation_range=90,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+8),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 9


datagen = ImageDataGenerator(
	rotation_range=120,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+9),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 10


datagen = ImageDataGenerator(
	rotation_range=150,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+10),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break


################################################################################################## 11


datagen = ImageDataGenerator(
	rotation_range=180,
	#zoom_range=None,
	#width_shift_range=0.2,
	#height_shift_range=0.2,
	#shear_range=None,
	#horizontal_flip=True,
    #vertical_flip=True,
	fill_mode="nearest")

dataset = []

my_images = os.listdir(image_directory_2)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory_2 + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((WIDTH2,HEIGHT2))
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0


for batch in datagen.flow(x, batch_size=16,
                          save_to_dir= save_to_dir_2,
                          save_prefix= a + str(p+11),
                          save_format='jpg'):
    i += 1
    if i > 0:
        break