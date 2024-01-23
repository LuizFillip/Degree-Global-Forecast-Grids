import xarray as xr

import matplotlib.pyplot as plt
import numpy as np


infile = 'NCEP_GFS/data/wind_components_data.nc'
ds = xr.open_dataset(infile)
level = 2
ds = ds.sel(level = level)


u_component_values = ds[f'u_component_level_{level}'].values


latitude = np.linspace(-90, 90, 721)
longitude = np.linspace(0, 360, 1440)

lon, lat = np.meshgrid(longitude, latitude)

fig, ax = plt.subplots(figsize = (10, 5))

img = ax.contourf(lon, lat, u_component_values, cmap='viridis', levels=20)
plt.colorbar(img, label='U Component of Wind (m/s)')
ax.set(title = f'U Component of Wind at Level {level}',
       xlabel = 'Longitude', ylabel = 'Latitude')


fig.savefig(f'NCEP_GFS/img/{level}_u_component')