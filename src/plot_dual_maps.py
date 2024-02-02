import GEO as gg 
import numpy as np
import base as b 
import cartopy.crs as ccrs
import matplotlib.pyplot as plt 
import xarray as xr

def mapping(lon_min, lon_max, lat_min, lat_max):
    
    
    fig, ax = plt.subplots(
         figsize = (17, 12), 
         dpi = 300, 
         ncols = 2,
         subplot_kw = 
         {'projection': ccrs.PlateCarree()}
         )
    
    
    lat_lims = dict(min = lat_min, max = lat_max, stp = 10)
    lon_lims = dict(min = lon_min, max = lon_max, stp = 10) 
    
    for i in range(2):
        
        gg.map_attrs(
            ax[i], 
            lat_lims = lat_lims, 
            lon_lims = lon_lims,
            year = 2022, grid = False
            )
        xlim = [-34.66, -35.25]
        ylim = [-7.5, -6.916]
        
        gg.plot_square_area(
                ax[i], 
                lat_min = ylim[0], 
                lon_min = xlim[0],
                lat_max = ylim[1], 
                lon_max = xlim[1]
                )

    
    return fig, ax 

def plot_maps_contour(
        df, 
        lat_min, lat_max,
        lon_min, lon_max
        ):

    fig, ax = mapping(
        lon_min, lon_max, 
        lat_min, lat_max
        )
    
    vmax = round(df['u'].max().item())
    
    level = np.linspace(-vmax, vmax, 50)
    
    for i, wind in enumerate(['u', 'v']):
        # name = df[wind].attrs['GRIB_name']
        
        ax[i].contourf(
            df.longitudes, 
            df.latitudes, 
            df[wind].values, 
            levels = level,
            cmap = 'jet'
            )
        
        ax[i].set(title = wind + ' component')
    
    
    
    b.plot_colorbar(
            fig,
            vmin = level.min(), 
            vmax = level.max(), 
            rainbow = "jet",
            fontsize = 25,
            step = 10,
            label = r'Velocity (m/s)'
            )
    
file = 'NCEP_GFS/data/gfs.0p25.2017071018.f000.nc'

ds = xr.open_dataset(file)

ds = ds.sel(level = 900)
ds['longitudes'] = ds['longitudes'] - 180


lon_min, lon_max = -70, -30
lat_min, lat_max = -40, 10

plot_maps_contour(
        ds, 
        lat_min, lat_max,
        lon_min, lon_max
        )