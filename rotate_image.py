from PIL import Image, ImageFilter
import os
import glob


rotate_angle = 45
if os.path.isdir("Rotate_Images") == False:
	os.mkdir("Rotate_Images")

for filename in glob.glob('Images/*.*'):
    
    print(filename)
    image = Image.open(filename)

    blur_image = image.rotate(rotate_angle)
    
    blur_image = blur_image.save("Rotate_Images/"+filename.split('/')[1]  + "_blur.jpg")
