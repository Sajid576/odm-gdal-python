#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

gdalinfo $RUNPATH/datasets/project/results/odm_orthophoto/odm_orthophoto.original_tiled.tif