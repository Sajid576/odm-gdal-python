#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $RUNPATH
sudo docker run -ti --rm -v $RUNPATH/datasets:/datasets opendronemap/odm --project-path /datasets project --dsm --orthophoto-resolution 2

# unlock all result folders
sudo chmod 777 -R $RUNPATH/datasets/project
cd $RUNPATH/datasets/project

#clear previous results
rm -r results/*

# move results
shopt -s extglob
mkdir results
mv -vt results/ $PWD/!(images)
# move results to the root directory
mv -vt $RUNPATH results