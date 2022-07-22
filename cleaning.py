import csv
from numpy import delete
import pandas as pd

data=pd.read_csv("final.csv")
print(data.shape)

del data["hyperlink"]
del data["temp_planet_mass"]
del data["temp_planet_date"]
del data["pl_letter"]
del data["pl_name"]
del data["pl_controvflag"]
del data["pl_pnum"]
del data["pl_orbper"]
del data["pl_orbpererr1"]
del data["pl_orbpererr2"]
del data["pl_orbperlim"]
del data["pl_orbsmax"]
del data["pl_orbsmaxerr1"]
del data["pl_orbsmaxerr2"]
del data["pl_orbsmaxlim"]
del data["pl_orbeccen"]
del data["pl_orbeccenerr1"]
del data["pl_orbeccenerr2"]
del data["pl_orbeccenlim"]
del data["pl_orbincl"]
del data["pl_orbinclerr1"]
del data["pl_orbinclerr2"]
del data["pl_orbincllim"]
del data["pl_bmassj"]
del data["pl_bmassjerr1"]
del data["pl_bmassjerr2"]
del data["pl_bmassjlim"]
del data["pl_bmassprov"]
del data["pl_radj"]
del data["pl_radjerr1"]
del data["pl_radjerr2"]
del data["pl_radjlim"]
del data["pl_denserr1"]
del data["pl_denserr2"]
del data["pl_denslim"]
del data["pl_ttvflag"]
del data["pl_kepflag"]
del data["pl_k2flag"]
del data["pl_nnotes"]
del data["ra"]
del data["dec"]
del data["st_dist"]
del data["st_disterr1"]
del data["st_disterr2"]
del data["st_distlim"]
del data["gaia_dist"]
del data["gaia_disterr1"]
del data["gaia_disterr2"]
del data["gaia_distlim"]
del data["st_optmag"]
del data["st_optmagerr"]
del data["st_optmaglim"]
del data["st_optband"]
del data["gaia_gmag"]
del data["gaia_gmagerr"]
del data["gaia_gmaglim"]
del data["st_tefferr1"]
del data["st_tefferr2"]
del data["st_tefflim"]
del data["st_masserr1"]
del data["st_masserr2"]
del data["st_masslim"]
del data["st_raderr1"]
del data["st_raderr2"]
del data["st_radlim"]
del data["rowupdate"]
del data["pl_facility"]
print(data.shape)
print(list(data))
data=data.rename({
    "pl_hostname":"solar_system_name",
    "pl_discmethod":"planet_discovery_method",
    'pl_dens':"planetdensity",
    "ra_str":"rightascension",
    "dec_str":"declination",
    "st_teff":"host_star_temperature",
    "st_mass":"host mass",
    "st_rad":"star_radius"
},axis="columns")
print(list(data))
#with open("final1.csv","w",newline='') as a:
data.to_csv("final1.csv")