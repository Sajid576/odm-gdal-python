#!/bin/bash


#sudo chmod 777 -R $PWD/gdal/GDAL-3.4.1.data/scripts
RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ls  $RUNPATH/datasets/project/odm_orthophoto/
echo $PWD
cd gdal/GDAL-3.4.1.data/scripts
echo $PWD

time=$(date +'%d_%m_%Y_%H:%M:%S')
# echo $time
gdal2tiles.py --zoom=16-21 $RUNPATH/datasets/project/results/odm_orthophoto/odm_orthophoto.original_tiled.tif $RUNPATH/output_folder_$time