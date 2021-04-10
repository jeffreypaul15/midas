import os
import cv2
import imgaug
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

def create_images(repetitions = 1, path = None, rgb = False, resize=(512,256)):
    images = []
    for i in os.listdir(path):
        image = cv2.imread(f"{path}/{i}", 1*rgb)
        image = cv2.resize(image, resize,
               interpolation = cv2.INTER_NEAREST)
        images.append(image)
    asd = np.asarray(images)
    return asd

def augment(images=None, save=False, save_original=False, path=None):
    ia.seed(1)
    seq = iaa.Sequential([
        iaa.Fliplr(0.7), # horizontal flips changed from 0.5
        iaa.Crop(percent=(0, 0.02)), # random crops
        # Small gaussian blur with random sigma between 0 and 0.5.
        # But we only blur about 50% of all images.
        iaa.Sometimes(
            0.5,
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        # Strengthen or weaken the contrast in each image.
        iaa.LinearContrast((0.75, 1.5)),
        # Add gaussian noise.
        # For 50% of all images, we sample the noise once per pixel.
        # For the other 50% of all images, we sample the noise per pixel AND
        # channel. This can change the color (not only brightness) of the
        # pixels.
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        # Make some images brighter and some darker.
        # In 20% of all cases, we sample the multiplier once per channel,
        # which can end up changing the color of the images.
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        # Apply affine transformations to each image.
        # Scale/zoom them, translate/move them, rotate them and shear them.
        iaa.Affine(
            rotate=(-10, 10),
            shear=(-3, 3)
        )
    ], random_order=True) # apply augmenters in random order

    images_aug = seq(images=images)
    
    names = 0
    if save:
        for i in images_aug:
            cv2.imwrite(f"{path}/{names}.jpg", i)
            names += 1
    if save_original:
        for i in images:
            cv2.imwrite(f"{path}/{names}.jpg", i)
            names += 1
    return images_aug