## Prequisities

- Docker

## Project Installation

- Generate orthophoto and other results using the following command:

```
$ bash run.sh
```

- Scale the input orthophoto using GDAL_translate

```
$ bash translate.sh
```

- Generate the tiles from the results according to the specified zoom levels:

```
$ bash generate_tiles.sh
```

For more information, [see here](https://github.com/OpenDroneMap/ODM)
