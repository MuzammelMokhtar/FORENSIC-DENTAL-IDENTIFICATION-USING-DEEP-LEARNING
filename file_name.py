import os

directory = r'C:\Users\Muzammel\Desktop\YOLOv4\test_images'

for filename in os.listdir(directory):
    if filename:
        print(filename)
        continue
    else:
        continue