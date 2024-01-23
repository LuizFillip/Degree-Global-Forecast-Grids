import xarray as xr
import pygrib

# Open the GRIB2 file

def levels_variables(grbs):
        
    levels = set()
    variables = set()
        
    for grb in grbs:
        levels.add(grb['level'])
        variables.add(grb['name'])
    
    all_levels = sorted(list(levels))
    all_variables = sorted(list(variables))
    
    return all_levels, all_variables



def save_wind_components_to_xarray(grib_file_path):
    # Open the GRIB2 file
    grbs = pygrib.open(grib_file_path)

    # Select messages for 'U component of wind' and 'V component of wind'
    u_component_messages = grbs.select(name='U component of wind')
    v_component_messages = grbs.select(name='V component of wind')

    # Create xarray dataset
    ds = xr.Dataset()

    # Extract levels
    levels, variables = levels_variables(grbs)

    # Add coordinates
    ds['latitude'] = (('lat', 'lon'), u_component_messages[0].latlons()[0])
    ds['longitude'] = (('lat', 'lon'), u_component_messages[0].latlons()[1])
    ds['level'] = ('level', levels)

    # Add data variables
    for level in levels:
        u_values = [grb.values for grb in
                    u_component_messages if grb['level'] == level]
        v_values = [grb.values for grb in 
                    v_component_messages if grb['level'] == level]
        if u_values:
            ds[f'u_{level}'] = (('lat', 'lon'), u_values[0])

        if v_values:
            ds[f'v_{level}'] = (('lat', 'lon'), v_values[0])


    grbs.close()

    return ds


grib_file_path =  'gfs.0p25.2023010100.f000.grib2'

ds = save_wind_components_to_xarray(grib_file_path)

ds.to_netcdf('wind_components_data.nc')
