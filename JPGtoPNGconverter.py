
import  os
from PIL import Image
name = list(map(str,input().split()))
image_folder =name[0]
output_folder = name[1]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    new_name = list(filename.split('.'))[0]
    img.save(f"{output_folder}{new_name}{'.png'}",'png')
    print('done')


