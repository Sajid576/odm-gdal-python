#!/usr/bin/python
from PIL import Image
import os
import sys

# parameters from bash script
run_path = sys.argv[1]
dim = sys.argv[2].split('=')[1]
# main script
width = int(dim.split(',')[0])
height = int(dim.split(',')[1])
path = run_path+"/images/"
output_path = run_path+"/datasets/project/images/"

dirs = os.listdir(path)
print(dim)


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            exif = im.info['exif']
            #f, e = os.path.splitext(path+item)
            imResize = im.resize((width, height), Image.ANTIALIAS)
            imResize.save(output_path+item + ' resized.jpg',
                          'JPEG', quality=90, exif=exif)


resize()
