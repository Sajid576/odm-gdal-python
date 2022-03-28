#!/bin/bash


#sudo chmod 777 -R $PWD/gdal/GDAL-3.4.1.data/scripts
RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $PWD
cd gdal/osgeo_utils
echo $PWD

TIME=$(date +'%d_%m_%Y_%H:%M:%S')
OUTPUTFOLDER=output_folder_dsm_$TIME
echo $OUTPUTFOLDER


val=$(python3 my_gdal_info.py $RUNPATH/results/odm_dem/dsm.tif 2>&1)  

IFS=' ' read llx lly urx ury<<< $val
echo $llx $lly $urx $ury

gdal_translate -a_nodata 0 -of GTiff -a_srs EPSG:32647 -a_ullr $llx $ury $urx $lly $RUNPATH/results/opensfm/stats/dsm.png  $RUNPATH/results/odm_dem/generated_dsm.tiff

# gdalinfo dsm.tiff
# gdal_translate -a_nodata 0 -of GTiff -a_srs EPSG:32647 -a_ullr 809911.652 347758.832 810137.102 347608.132  dsm.png  dsm.tiff


gdal2tiles.py --zoom=16-21  $RUNPATH/results/odm_dem/generated_dsm.tiff  $RUNPATH/$OUTPUTFOLDER
python3 tms2xyz.py $RUNPATH/$OUTPUTFOLDER