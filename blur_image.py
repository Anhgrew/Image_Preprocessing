from PIL import Image, ImageFilter
import os

import glob
blur_level = 2
if os.path.isdir("Blur_Images") == False:
	os.mkdir("Blur_Images")

for filename in glob.glob('Images/*.*'):
    
    print(filename)
    image = Image.open(filename)

    blur_image = image.filter(ImageFilter.GaussianBlur(blur_level))
    
    blur_image = blur_image.save("Blur_Images/"+filename.split('/')[1]  + "_blur.jpg")
