## Prequisities

- Python3
- Docker

## Project Installation

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
