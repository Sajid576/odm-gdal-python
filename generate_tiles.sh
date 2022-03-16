#!/bin/bash


#sudo chmod 777 -R $PWD/gdal/GDAL-3.4.1.data/scripts
RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $PWD
cd gdal/osgeo_utils
echo $PWD

time=$(date +'%d_%m_%Y_%H:%M:%S')
# echo $time
gdal2tiles.py --zoom=16-21 --xyz $RUNPATH/results/odm_orthophoto/odm_orthophoto.original.tif $RUNPATH/output_folder_$time 