import sys

from osgeo import gdal
tiff_file_path = sys.argv[1]

ds = gdal.Open(tiff_file_path)
ret = gdal.Info(ds)

# print(type(ds))
# print(ret)
if (ret.find('Lower Left') != -1):
    ll_starting_indx = ret.find('Lower Left')
    lowerleft_val = ''
    i = ll_starting_indx+13
    while(ret[i] != ')'):
        if(ret[i] != ' '):
            lowerleft_val += ret[i]
        # print(ret[i], end='')
        i += 1

    llx = lowerleft_val.split(',')[0]
    lly = lowerleft_val.split(',')[1]
    # print(llx)
    # print(lly)

if (ret.find('Upper Right') != -1):
    ur_starting_indx = ret.find('Upper Right')
    upperright_val = ''
    i = ur_starting_indx+13
    while(ret[i] != ')'):
        if(ret[i] != ' '):
            upperright_val += ret[i]
        # print(ret[i], end='')
        i += 1

    urx = upperright_val.split(',')[0]
    ury = upperright_val.split(',')[1]
    # print(urx)
    # print(ury)

print(llx, lly, urx, ury)
sys.exit(1)
