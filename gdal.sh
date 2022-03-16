#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $PWD
cd gdal/GDAL-3.4.1.data/scripts
echo $PWD
#gdalinfo $RUNPATH/results/odm_orthophoto/odm_orthophoto.original.tif
gdal2xyz.py -b 1 -b 2 -dstnodata 0 $RUNPATH/results/odm_orthophoto/odm_orthophoto.original.tif $RUNPATH/output.txt