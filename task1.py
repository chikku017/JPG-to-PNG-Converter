from PIL import Image,ImageFilter
img = Image.open("beach.jpg")
new_image = img.crop((100, 100, 250, 250))
new_image.show()