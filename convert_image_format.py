from PIL import Image

im = Image.open(r"C:\Users\Muzammel\Documents\test_augment_convert\A00204.NEF")

im = im.convert("RGB")

im.save(r"C:\Users\Muzammel\Documents\test_augment_convert\A00204.jpg")