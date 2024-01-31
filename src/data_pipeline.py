import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd 
import base as b 
import os 

b.config_labels()


def loadData(file):
    
    ds = xr.open_dataset(file)
    
    ds['longitude'] = ds['longitude'] - 180
    
    xlim = [-34.66, -35.25]
    ylim = [-7.5, -6.916]
    
    return ds.sel(
        latitude= (
            (ds.latitude > ylim[0]) & 
            (ds.latitude < ylim[1])), 
        longitude = (
            (ds.longitude < xlim[0]) &
            (ds.longitude > xlim[1]))
                )
    
import numpy as np 


def plot_components(ax, df):
    
    time = pd.to_datetime(df['time'].values)
    
    u = [i.mean() for i in df['u'].values]
    v = [i.mean() for i in  df['v'].values]
    
    
    title = time.strftime('%d/%m/%Y %Hh%M UT')
    
    alts = df.isobaricInhPa
    ax.plot(u, alts, 
            label = 'u component')
    
    ax.plot(v, alts , 
            label = 'v component')
    
    ax.set(xlabel = 'Velocity (m/s)', 
           xlim = [-10, 10],
           ylim = [650, 1000], 
           xticks = np.arange(-10, 15, 5),
           title = title)
    
    plt.gca().invert_yaxis()
    
    



def plot(path, files):
    
    fig, ax = plt.subplots(
          figsize = (18, 12), 
          dpi = 300, 
          sharex =  True, 
          sharey= True,
          ncols = 3, 
          nrows = 2
          )
    
    plt.subplots_adjust(wspace = 0.1)
    
    for i, ax in enumerate(ax.flat):
    
        infile = os.path.join(
            path, files[i]
            )
        ds = loadData(infile)
        
        ax.axvline(0, linestyle = '--')
        
        plot_components(ax, ds)
        
        if i == 0:
            ax.legend(
                ncol = 2,
                loc = 'upper center',
                bbox_to_anchor = (2.3, 1.3)
                )
            
            ax.set(ylabel = 'Isobaric height (hPa)')
            
        
        
    fig.savefig('NCEP_GFS/img/all_profiles.png')
    
# infile = 'NCEP_GFS/data/gfs.0p25.2021092218.f000.nc'

path = 'NCEP_GFS/data/'

files = sorted(os.listdir(path))

plot(path, files)

# infile = os.path.join(
#     path, files[6]
#     )

# ds = loadData(infile)
# 
# fig, ax = plt.subplots()
# plot_components(ax, ds)

# infile= 'NCEP_GFS/gfs.0p25.2019062106.f000.nc'

# ds = xr.open_dataset(infile)

# ds, infile 