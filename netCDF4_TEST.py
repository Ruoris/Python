import netCDF4
from netCDF4 import Dataset
#import iris
import numpy as np

# x=iris.fileformats.netcdf.load_cubes("sun_hadukgrid_uk_region_ann-20y_198101-200012.nc")

# print(x)
# y=iris.analysis.geometry.geometry_area_weights(x,'ukcp18-uk-land-country-united_kingdom-hires',normalize=False)

weatherfile= Dataset('sun_hadukgrid_uk_1km_mon-30y_196101-199012.nc')
print(weatherfile.variables.keys())


temp=weatherfile.variables['monthly_maxtemp']
# time=weatherfile.variables['time']
# time_bnds=weatherfile.variables['time_bnds']
# projy=weatherfile.variables['projection_y_coordinate']
# projy_bnd=weatherfile.variables['projection_y_coordinate_bnds']
# projx=weatherfile.variables['projection_x_coordinate']
# projx_bnd=weatherfile.variables['projection_x_coordinate_bnds']
# trans_merc=weatherfile.variables['transverse_mercator']
# lat=weatherfile.variables['lat']
# lon=weatherfile.variables['lon']
# meaning=weatherfile.variables['meaning_period']

# for d in weatherfile.dimensions.items():
#     print(d)

# temp_array=temp[:]
# time_array=time[:]
# time_bnds_array=time_bnds[:]
# projy_array=projy[:]
# projy_bnd_array=projy_bnd[:]
# projx_array=projx[:]
# projx_bnd_array=projx_bnd[:]
# trans_merc_array=trans_merc[:]
# lat_array=lat[:]
# lon_array=lon[:]
# meaning_array=meaning[:]

# print(temp_array)
# print(time_array)
# print(time_bnds_array)
# print(projy_array)
# print(projy_bnd_array)
# print(projx_array)
# print(projx_bnd_array)
# print(trans_merc_array)
# print(lat_array)
# print(lon_array)
# print(meaning_array)













# temp=weatherfile.variables['monthly_maxtemp']
# time=weatherfile.variables['time']
# time_bnds=weatherfile.variables['time_bnds']
# projy=weatherfile.variables['projection_y_coordinate']
# projy_bnd=weatherfile.variables['projection_y_coordinate_bnds']
# projx=weatherfile.variables['projection_x_coordinate']
# projx_bnd=weatherfile.variables['projection_x_coordinate_bnds']
# trans_merc=weatherfile.variables['transverse_mercator']
# lat=weatherfile.variables['lat']
# lon=weatherfile.variables['lon']
# meaning=weatherfile.variables['meaning_period']

# for d in weatherfile.dimensions.items():
#     print(d)

# temp_array=temp[:]
# time_array=time[:]
# time_bnds_array=time_bnds[:]
# projy_array=projy[:]
# projy_bnd_array=projy_bnd[:]
# projx_array=projx[:]
# projx_bnd_array=projx_bnd[:]
# trans_merc_array=trans_merc[:]
# lat_array=lat[:]
# lon_array=lon[:]
# meaning_array=meaning[:]

# print(temp_array)
# print(time_array)
# print(time_bnds_array)
# print(projy_array)
# print(projy_bnd_array)
# print(projx_array)
# print(projx_bnd_array)
# print(trans_merc_array)
# print(lat_array)
# print(lon_array)
# print(meaning_array)
