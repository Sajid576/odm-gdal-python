import sys
import os
import shutil

tms_output_path = sys.argv[1]
xyz_output_path = tms_output_path+'/xyz'

shutil.copytree(tms_output_path, xyz_output_path)


def convert2xyz(filename, zoom):
    print('->', zoom)
    tms_y = int(filename.split('.')[0])
    temp = zoom.split('/')
    zoom_level = int(temp[len(temp)-1])
    y = (2 ** zoom_level) - tms_y - 1
    return str(y)+'.png'


zoomSubfolders = [f.path for f in os.scandir(xyz_output_path) if f.is_dir()]
for folder in zoomSubfolders:
    xSubfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
    for xfolder in xSubfolders:
        files = os.listdir(xfolder)
        for file in files:
            new_name = convert2xyz(file, folder)
            os.rename(xfolder+"/"+file, xfolder+"/" + new_name)
