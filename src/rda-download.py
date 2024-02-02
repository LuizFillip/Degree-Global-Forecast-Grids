#!/usr/bin/env python
""" 
Python script to download selected files from rda.ucar.edu.
After you save the file, don't forget to make it executable
i.e. - "chmod 755 <name_of_script>"
"""
import sys, os
from urllib.request import build_opener
import datetime as dt 


opener = build_opener()
root = 'https://data.rda.ucar.edu/ds084.1/'

def download(filelist):
    for file in filelist:
        ofile = os.path.basename(file)
        sys.stdout.write("downloading " + ofile + " ... ")
        sys.stdout.flush()
        infile = opener.open(file)
        outfile = open(ofile, "wb")
        outfile.write(infile.read())
        outfile.close()
        sys.stdout.write("done\n")
        

dn = dt.datetime(2021, 9, 22, 12 + 3)

def URL(dn):
    
    folder = dn.strftime('%Y/%Y%m%d/')
    
    filename = dn.strftime('gfs.0p25.%Y%m%d%H.f000.grib2')
    
    return root + folder + filename

#04/07/2019 (07:01h local) e 21/06/2019 (02:25h local)

#29/11/2018 - 11:00h local
#21/08/2017 (20:05h local), 10/07/2017 (17:00h local), 03/05/2017 (01:06h local)



# 2022 - 16/07/2022 - 17:00h local   ------ 20 UT
# 2021 - 22/09/2021 - 12:00h local            15 UT

# 2020 - Não houve registros

# 2019 - 04/07/2019 (07:01h local)  10 UT 
# 21/06/2019 (02:25h local)     6 UT ou 7 UT

# 2018 - 29/11/2018 - 11:00h local     ---  14 UT

# 2017 - 21/08/2017 (20:05h local), 23 UT
# 10/07/2017 (17:00h local),    20 UT
# 03/05/2017 (01:06h local)     4 UT





    
dates = [dt.datetime(2022, 7, 16, 20), 
         dt.datetime(2021, 9, 22, 15), 
         dt.datetime(2019, 7, 4, 10),
         dt.datetime(2019, 6, 21, 6),
         dt.datetime(2018, 11, 29, 14), 
         dt.datetime(2017, 8, 21, 23),
         dt.datetime(2017, 7, 10, 20),
         dt.datetime(2017, 5, 3, 4)]


dates = [dt.datetime(2022, 7, 17, 0), 
         dt.datetime(2022, 7, 16, 18),
         dt.datetime(2021, 9, 22, 12), 
         dt.datetime(2021, 9, 22, 18),
         dt.datetime(2019, 7, 4, 12),
         dt.datetime(2019, 6, 21, 6),
         dt.datetime(2018, 11, 29, 12), 
         dt.datetime(2017, 8, 22, 0),
         dt.datetime(2017, 7, 10, 18),
         dt.datetime(2017, 7, 11, 0),
         dt.datetime(2017, 5, 3, 6)]


dates = [URL(dn) for dn in dates]

# download([URL(dt.datetime(2018, 11, 29, 16))])