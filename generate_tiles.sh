#!/bin/bash


#sudo chmod 777 -R $PWD/gdal/GDAL-3.4.1.data/scripts
RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $PWD
cd gdal/osgeo_utils
echo $PWD

TIME=$(date +'%d_%m_%Y_%H:%M:%S')
OUTPUTFOLDER=output_folder_$TIME
echo $OUTPUTFOLDER
# echo $time
gdal2tiles.py --zoom=16-21  $RUNPATH/results/odm_orthophoto/odm_orthophoto.original.tif  $RUNPATH/$OUTPUTFOLDER
python3 tms2xyz.py $RUNPATH/$OUTPUTFOLDER