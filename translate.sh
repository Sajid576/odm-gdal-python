#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

gdal_translate -of GTiff -co "TILED=YES" $RUNPATH/datasets/project/results/odm_orthophoto/odm_orthophoto.original.tif $RUNPATH/datasets/project/results/odm_orthophoto/odm_orthophoto.original_tiled.tif -a_ullr ulx uly lrx lry