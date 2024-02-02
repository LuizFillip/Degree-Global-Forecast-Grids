import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd 
import base as b 
import os 
import numpy as np 
import datetime as dt 

b.config_labels()


def loadData(file):
    
    ds = xr.open_dataset(file)
    
    ds['longitudes'] = ds['longitudes'] - 180
    
    xlim = [-34.66, -35.25]
    ylim = [-7.5, -6.916]
    
    return ds.sel(
        latitudes= (
            (ds.latitudes > ylim[0]) & 
            (ds.latitudes < ylim[1])), 
        longitudes = (
            (ds.longitudes < xlim[0]) &
            (ds.longitudes > xlim[1]))
                )
    

def get_year(fn): return int(fn.split('.')[2][:4])


def plot_components(ax, df, time):
        
    u = [i.mean() for i in df['u'].values]
    v = [i.mean() for i in df['v'].values]
    
    
    title = time.strftime('%d/%m/%Y %Hh%M UT')
    
    alts = df.level
    ax.plot(u, alts, label = 'u component')
    
    ax.plot(v, alts , label = 'v component')
    
    ax.set(xlabel = 'Velocity (m/s)', 
           xlim = [-5, 5],
           ylim = [650, 1000], 
           xticks = np.arange(-5, 6, 1),
           title = title,
           ylabel = 'Isobaric height (hPa)')
    
    ax.axvline(0, linestyle = '--')
    plt.gca().invert_yaxis()
    
    ax.legend(
        loc = 'upper right',
        )
    
    
    
def plot(path, date_list):
    cols = len(date_list)
    fig, ax = plt.subplots(
          figsize = (18, 10), 
          dpi = 300, 
          sharex =  True, 
          sharey = True,
          ncols = cols
          )
    
    plt.subplots_adjust(wspace = 0.1)
    files = get_filenames(date_list)
    
    for i, time in enumerate(date_list):

        infile = os.path.join(
            path, files[i]
            )
        ds = loadData(infile)
        
        
        if cols == 1:
            plot_components(ax, ds, time)
        else:
            plot_components(ax[i], ds, time)

    return fig 
    
    

path = 'NCEP_GFS/data/'


dates = [[dt.datetime(2022, 7, 17, 0), 
         dt.datetime(2022, 7, 16, 18)],
         [dt.datetime(2021, 9, 22, 12), 
         dt.datetime(2021, 9, 22, 18)],
         [dt.datetime(2019, 7, 4, 12),
         dt.datetime(2019, 6, 21, 6)],
         [dt.datetime(2018, 11, 29, 12)], 
         [dt.datetime(2017, 8, 22, 0),
         dt.datetime(2017, 7, 10, 18),
         dt.datetime(2017, 7, 11, 0),
         dt.datetime(2017, 5, 3, 6)]]

def get_filenames(dates):
    fmt ='gfs.0p25.%Y%m%d%H.f000.nc'
    return [dn.strftime(fmt) for dn in dates]

def main():
    for date_list in dates:
        date_list = dates[-1] 
        fig = plot(path, date_list)
        name = date_list[0].year
        print('processing...', name)
        fig.savefig(f'NCEP_GFS/img/{name}.png')