## Prequisities

- Python3
- Docker

## Project Installation

- Place your dataset folder in root project directory.
- In run.sh, pass the folder name of the dataset in the dataset_folder option, pass the desired resolution of the image dataset.dim option is not recommended to change.If you face memory related problem while running the ODM,then you can reduce the dimensions of the image dataset and tune the value by trial and error.

- Generate OSM,DSM report and other results using the following command(ODM):

```
$ bash run.sh
```

- Generate the TMS and XYZ tiles for OSM from the results according to the specified zoom levels:

```
$ bash generate_tiles.sh
```

- Generate the TMS and XYZ tiles for DSM from the results according to the specified zoom levels:

```
$ bash generate_dsm_tiles.sh
```

For more information, [see here](https://github.com/OpenDroneMap/ODM)
