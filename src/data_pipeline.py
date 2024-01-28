import xarray as xr

ds = xr.open_dataset('NCEP_GFS/data/gfs.0p25.2022071618.f000.nc')

ds['longitude'] = ds['longitude'] - 180

#%%%%
import cartopy.crs as ccrs
import datetime as dt
import matplotlib.pyplot as plt
import GEO as gg 

fig, ax = plt.subplots(
     figsize = (17, 12), 
     dpi = 300, 
     subplot_kw = 
     {'projection': ccrs.PlateCarree()}
     )


lat_lims = dict(min = -9, max = -6, stp = 1)
lon_lims = dict(min = -37, max = -34, stp = 1) 


gg.map_attrs(
    ax, 
    lat_lims = lat_lims, 
    lon_lims = lon_lims,
    year = 2022, grid = False
    )



lon_min, lon_max = -40,  -34
lat_min, lat_max = -10, -5

df = ds.sel(isobaricInhPa = 900,
            latitude= (
                (ds.latitude > lat_min) & 
                (ds.latitude < lat_max)), 
            longitude = (
                (ds.longitude < lon_max) &
                (ds.longitude > lon_min))
            )

xlim = [-34.66, -35.25]
ylim = [-7.5, -6.916]
gg.plot_square_area(
        ax, 
        lat_min = ylim[0], 
        lon_min = xlim[0],
        lat_max = ylim[1], 
        lon_max = xlim[1]
        )


# df1= df.sel(longitude = (ds.longitude < -30))


df['u'].plot(ax = ax)

# df