#!/usr/bin/python
from PIL import Image
import os
import sys

# parameters from bash script
run_path = sys.argv[1]
dim = sys.argv[2].split('=')[1]
dataset_folder_name = sys.argv[3].split('=')[1]
print(dataset_folder_name)


# main script
max_width = int(dim.split(',')[0])
max_height = int(dim.split(',')[1])
path = run_path+"/"+dataset_folder_name+"/"
output_path = run_path+"/datasets/project/images/"

dirs = os.listdir(path)
print(dim)


def isHighResolution():
    total_width = 0
    total_height = 0
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            width, height = im.size
            total_width += width
            total_height += height

    avg_width = total_width // len(dirs)
    avg_height = total_height // len(dirs)
    print(avg_width, avg_height)
    if(avg_width > max_width or avg_height > max_height):
        return True
    else:
        return False


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            exif = im.info['exif']
            #f, e = os.path.splitext(path+item)
            imResize = im.resize((max_width, max_height), Image.ANTIALIAS)
            imResize.save(output_path+item + ' resized.jpg',
                          'JPEG', quality=90, exif=exif)


if(isHighResolution() == True):
    print("Resizing")
    resize()
else:
    print("Not resizing")
