import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr
from astropy.io import fits

Temp = fits.open("series_all.fits")[0].data
Bz = fits.open("series_all.fits")[1].data
Vx = fits.open("series_all.fits")[2].data
Vy = fits.open("series_all.fits")[3].data
M_b = fits.open("series_all.fits")[5].data

# Let's do basic comparison of "real" velocities and the ones that FLCT gives
# between every 2 adjacent files 

Vx_mean = []
Vy_mean = []
for j in range(1, len(Vx)):
    vx = (Vx[j-1] + Vx[j])/2/1e5
    Vx_mean.append(vx)
    vy = (Vy[j-1] + Vy[j])/2/1e5
    Vy_mean.append(vy)

# Now, we implement FLCT on our Temp array
Vel_x_T = []
Vel_y_T = []
Vm_T = []
for j in range(1, len(Temp)):
    vel_x, vel_y, vm = pyflct.flct(Temp[j-1], Temp[j], 1*30, 1*48, 5.0)
    Vel_x_T.append(vel_x)
    Vel_y_T.append(vel_y)
    Vm_T.append(vm)

print("Length of Vel_x_T: {}".format(len(Vel_x_T)))

#Now for Bz array
Vel_x_Bz = []
Vel_y_Bz = []
Vm_Bz = []
for j in range(1, len(Bz)):
    vel_x, vel_y, vm = pyflct.flct(Bz[j-1], Bz[j], 1*30, 1*48, 5.0)
    Vel_x_Bz.append(vel_x)
    Vel_y_Bz.append(vel_y)
    Vm_Bz.append(vm)

print("Length of Vel_x_Bz: {}".format(len(Vel_x_Bz)))

# Now for bolometric magnitude
Vel_x_Mb = []
Vel_y_Mb = []
Vm_Mb = []
for j in range(1, len(M_b)):
    vel_x, vel_y, vm = pyflct.flct(M_b[j-1], M_b[j], 1*30, 1*48, 5.0)
    Vel_x_Mb.append(vel_x)
    Vel_y_Mb.append(vel_y)
    Vm_Mb.append(vm)
print("Length of Vel_x_Mb: {}".format(len(Vel_x_Mb)))

# And we can finally write them each to separate fits files
Vel_x_T = np.asarray(Vel_x_T)
Vel_y_T = np.asarray(Vel_y_T)
Vm_T = np.asarray(Vm_T)

Vel_x_Bz = np.asarray(Vel_x_Bz)
Vel_y_Bz = np.asarray(Vel_y_Bz)
Vm_Bz = np.asarray(Vm_Bz)

Vel_x_Mb = np.asarray(Vel_x_Mb)
Vel_y_Mb = np.asarray(Vel_y_Mb)
Vm_Mb = np.asarray(Vm_Mb)

T_x = fits.PrimaryHDU(Vel_x_T)
T_y = fits.ImageHDU(Vel_y_T)
T_v = fits.ImageHDU(Vm_T)
T_flct = fits.HDUList([T_x, T_y, T_v])
T_flct.writeto("FLCT_temperature.fits", overwrite = True)

Bz_x = fits.PrimaryHDU(Vel_x_Bz)
Bz_y = fits.ImageHDU(Vel_y_Bz)
Bz_v = fits.ImageHDU(Vm_Bz)
Bz_flct = fits.HDUList([Bz_x, Bz_y, Bz_v])
Bz_flct.writeto("FLCT_magnetic.fits", overwrite = True)

Mb_x = fits.PrimaryHDU(Vel_x_Mb)
Mb_y = fits.ImageHDU(Vel_y_Mb)
Mb_v = fits.ImageHDU(Vm_Mb)
Mb_flct = fits.HDUList([Mb_x, Mb_y, Mb_v])
Mb_flct.writeto("FLCT_bolometric.fits", overwrite = True)
