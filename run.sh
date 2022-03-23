#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $RUNPATH
sudo docker run -ti --rm -v $RUNPATH/datasets:/datasets opendronemap/odm --project-path /datasets project --dsm --orthophoto-resolution 4 --auto-boundary

# unlock all result folders
sudo chmod 777 -R $RUNPATH/datasets/project
# cd $RUNPATH/datasets/project

# #clear previous results
rm -r $RUNPATH/results/*

# move results
shopt -s extglob
mkdir $RUNPATH/datasets/project/results/
mv -vt $RUNPATH/datasets/project/results/ $RUNPATH/datasets/project/!(images)
# move results to the root directory
mv -vt $RUNPATH $RUNPATH/datasets/project/results/