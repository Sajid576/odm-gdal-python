#!/bin/bash


#sudo chmod 777 -R $PWD/gdal/GDAL-3.4.1.data/scripts
RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $PWD
cd gdal/osgeo_utils
echo $PWD
# install faker for random color code generating
pip install faker
mkdir $RUNPATH/output_dsm_color_info/
python3 my_raster_classifier.py $RUNPATH/results/odm_dem/dsm.tif  $RUNPATH/output_dsm_color_info/
# val=$(python3 my_raster2array.py $RUNPATH/results/odm_dem/dsm.tif 2>&1) 
# echo $val