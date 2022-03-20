#!/usr/bin/python
from PIL import Image
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))+"/images/"
output_path = os.path.dirname(os.path.abspath(
    __file__))+"/datasets/project/images/"

dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            exif = im.info['exif']
            #f, e = os.path.splitext(path+item)
            imResize = im.resize((5000, 3000), Image.ANTIALIAS)
            imResize.save(output_path+item + ' resized.jpg',
                          'JPEG', quality=90, exif=exif)


resize()
