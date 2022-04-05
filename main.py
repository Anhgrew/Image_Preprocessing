import imageio
import imgaug as ia
import numpy as np
import glob
from imgaug import augmenters as iaa
import os

ia.seed(10)

#rotate = iaa.Affine(rotate=(-25, 25))
seq = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2)),
    iaa.GaussianBlur(sigma=(0.0, 10.0)),
    iaa.AverageBlur(k=(2, 15)),
    iaa.MultiplyAndAddToBrightness(mul=(0.5, 1.5), add=(-30, 30)),
    iaa.Flipud(0.5),
    iaa.Resize((0.8, 1.0)),
    iaa.AdditiveGaussianNoise(scale=(0, 0.2*255))
])

generating_image_folder = '/GernerateImages/'
for filename in glob.glob('Images/*.*'):

    image = imageio.imread(filename)

    image_testing_folder_name = filename.split('/')[1].split('.')[0]

    if os.path.isdir(os.path.join(os.getcwd() + generating_image_folder, image_testing_folder_name)) == False:
        os.makedirs(os.path.join(
            os.getcwd() + generating_image_folder, image_testing_folder_name))

    images_aug = [imageio.imwrite(os.path.join(os.getcwd() + generating_image_folder + '/' +
                                  image_testing_folder_name, str(i) + '.jpg'), seq(image=image)) for i in range(100)]
