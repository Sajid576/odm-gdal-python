## Prequisities

- Linux
- Python3
- Docker

## Project Guide

- Place your dataset folder in root project directory.
- In run.sh, pass the folder name of the dataset in the dataset_folder option, pass the desired resolution of the image dataset.dim option is not recommended to change.If you face memory related problem while running the ODM,then you can reduce the dimensions of the image dataset and tune the value by trial and error.

- 1. Generate OSM,DSM report and other results using the following command(ODM):

```
$ bash run.sh
```

- 2. Generate the TMS and XYZ tiles for OSM from the results according to the specified zoom levels:

```
$ bash generate_tiles.sh
```

- 3. Generate the TMS and XYZ tiles for DSM from the results according to the specified zoom levels:

```
$ bash generate_dsm_tiles.sh
```

## Screenshot

![alt text](https://github.com/Sajid576/odm-gdal-python/blob/master/Outcome_Screenshot.png)
From the screenshot, we can see the outcome folder named `results`(1) that is generated after 1st command, output folder(2) that is generated after 2nd command and output folder(3) that is generated after 3rd command.

For more information, [see here](https://github.com/OpenDroneMap/ODM)
