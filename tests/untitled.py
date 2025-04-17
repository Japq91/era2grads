import xarray as xr
import os
ifile='borrar_superficie_1.nc'
ofile='l4_optimizado.nc'

d=xr.open_dataset(ifile)
if 'pressure_level' in list(d.variables): d=d.rename({'pressure_level':'level'})
if 'valid_time' in list(d.variables): d=d.rename({'valid_time':'time'})
d.to_netcdf('tmp_%s'%ifile)
os.system('cdo -f nc4c -z zip_2 copy tmp_%s %s'%(ifile,ofile))