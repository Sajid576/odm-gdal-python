import sys

from faker import Factory
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as colors
# %matplotlib inline
from osgeo import gdal
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')


def getRandomHexColor():
    fake = Factory.create()
    hex_num = fake.hex_color()
    return hex_num.upper()


def getStartingPoint(val):
    rem = val % 10
    res = val-rem
    return res


def getEndingPoint(val):
    rem = val % 10
    res = val + (10-rem)
    return res


def getHeightRangeList(start, end):
    interval = 10
    height_list = []
    for i in range(start, end, interval):
        height_list.append((i, i+10))
    return height_list


def generateColorList(total_class):
    red = '#FF3333'
    green = '#12F0D2'
    color_list = []
    color_list.append(red)
    for i in range(total_class-2):
        color_list.append(getRandomHexColor())
    color_list.append(green)
    return color_list


# driver code
tif_file_path = sys.argv[1]
output_path = sys.argv[2]
chm_dataset = gdal.Open(tif_file_path)
data = {}
list_data = {}


cols = chm_dataset.RasterXSize
rows = chm_dataset.RasterYSize
chm_mapinfo = chm_dataset.GetGeoTransform()

xMin = chm_mapinfo[0]
yMax = chm_mapinfo[3]
xMax = xMin + chm_dataset.RasterXSize/chm_mapinfo[1]  # divide by pixel width
# divide by pixel height (note sign +/-)
yMin = yMax + chm_dataset.RasterYSize/chm_mapinfo[5]
chm_ext = (xMin, xMax, yMin, yMax)
print('chm raster extent:', chm_ext)


chm_raster = chm_dataset.GetRasterBand(1)
noDataVal = chm_raster.GetNoDataValue()
print('no data value:', noDataVal)
scaleFactor = chm_raster.GetScale()
print('scale factor:', scaleFactor)
chm_stats = chm_raster.GetStatistics(True, True)
print('SERC CHM Statistics: Minimum=%.2f, Maximum=%.2f, Mean=%.3f, StDev=%.3f' %
      (chm_stats[0], chm_stats[1], chm_stats[2], chm_stats[3]))


data['total_columns'] = cols  # the dataset dimensions
data['total_rows'] = rows
data['total_bands'] = chm_dataset.RasterCount       # number of bands
data['driver'] = chm_dataset.GetDriver().LongName   # driver
data['raster_extent'] = chm_ext
data['scale_factor'] = scaleFactor
data['stat'] = {
    'min': chm_stats[0],
    'max': chm_stats[1],
    'mean': chm_stats[2],
    'std_dev': chm_stats[3]
}


chm_array = chm_dataset.GetRasterBand(
    1).ReadAsArray(0, 0, cols, rows).astype(np.float)
# Assign CHM No Data Values to NaN
chm_array[chm_array == int(noDataVal)] = np.nan
chm_array = chm_array/scaleFactor
print('SERC CHM Array:\n', chm_array)  # display array values


height_list = getHeightRangeList(getStartingPoint(
    int(chm_stats[0])), getEndingPoint(int(chm_stats[1])))
print(height_list)
color_list = generateColorList(len(height_list))
print(color_list)

color_height_map = []
for i in range(len(height_list)):
    temp = {}
    temp[color_list[i]] = [height_list[i][0], height_list[i][1]]
    color_height_map.append(temp)
data['color_height'] = color_height_map
print(data)

# Serializing json
with open(output_path+"data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)


chm_reclass = copy.copy(chm_array)
for i in range(len(height_list)):
    chm_reclass[np.where((chm_array > height_list[i][0]) &
                         (chm_array <= height_list[i][1]))] = i+1

# for x in chm_reclass:
#   for y in x:
#     print(y,end=' ')
#   print()
list_data['array'] = chm_reclass.tolist()

with open(output_path+"list_data.json", "w") as outfile:
    json.dump(list_data, outfile, indent=4)

# print('Min:',np.nanmin(chm_reclass))
# print('Max:',np.nanmax(chm_reclass))
# print('Mean:',round(np.nanmean(chm_reclass),2))

plt.figure()  # ax = plt.subplots()
cmapCHM = colors.ListedColormap(color_list)
plt.imshow(chm_reclass, extent=chm_ext, cmap=cmapCHM)
plt.title('SERC CHM Classification')
ax = plt.gca()
# do not use scientific notation
ax.ticklabel_format(useOffset=False, style='plain')
# rotate x tick labels 90 degrees
rotatexlabels = plt.setp(ax.get_xticklabels(), rotation=90)
# forceAspect(ax,aspect=1)
ax.set_aspect('auto')


# Create custom legend to label the  canopy height classes:
class_box = []
for i in range(len(height_list)):
    label = str(height_list[i][0])+' < height < '+str(height_list[i][1])
    class_box.append(mpatches.Patch(color=color_list[i], label=label))

ax.legend(handles=class_box, handlelength=0.7, bbox_to_anchor=(
    1.05, 0.4), loc='lower left', borderaxespad=0.)
plt.savefig(output_path+'dsm.png', bbox_inches='tight')
