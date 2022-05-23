from PIL import Image
from PIL import ImageChops

'''
This function compares 2 images, returns true if identical
otherwise false
'''


def compare_images(path_one, path_two):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            return True
        else:
            return False
    except ValueError as e:
        return False
