import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr
from astropy.io import fits

# kek.writeto("series_basic.fits", overwrite = True)

Temp = fits.open("series_basic.fits")[0].data
Bz = fits.open("series_basic.fits")[1].data
Vx = fits.open("series_basic.fits")[2].data
Vy = fits.open("series_basic.fits")[3].data

# Let's do basic comparison of "real" velocities and the ones that FLCT gives
# between every 2 adjacent files 

Vx_diff = []
Vy_diff = []
for j in range(1, len(Vx)):
    vx = (Vx[j] - Vx[j-1])/1e5
    Vx_diff.append(vx)
    vy = (Vy[j] - Vy[j-1])/1e5
    Vy_diff.append(vy)

# Now, we implement FLCT on our Temp array
Vel_x_T = []
Vel_y_T = []
Vm_T = []
for j in range(1, len(Temp)):
    vel_x, vel_y, vm = pyflct.flct(Temp[j-1], Temp[j], 1*30, 1*50, 5.0)
    Vel_x_T.append(vel_x)
    Vel_y_T.append(vel_y)
    Vm_T.append(vm)

print("Length of Vel_x_T: {}".format(len(Vel_x_T)))

#Now for Bz array
Vel_x_Bz = []
Vel_y_Bz = []
Vm_Bz = []
for j in range(1, len(Bz)):
    vel_x, vel_y, vm = pyflct.flct(Bz[j-1], Bz[j], 1*30, 1*50, 5.0)
    Vel_x_Bz.append(vel_x)
    Vel_y_Bz.append(vel_y)
    Vm_Bz.append(vm)

print("Length of Vel_x_Bz: {}".format(len(Vel_x_Bz)))
Pearson__xT = []
Pearson__yT = []
for j in range(1, len(Vel_x_T)):
    p_x = pearsonr(Vx_diff[j-1].flatten(), Vel_x_T[j-1].flatten())
    Pearson__xT.append(p_x)
    p_y = pearsonr(Vy_diff[j-1].flatten(), Vel_y_T[j-1].flatten())
    Pearson__yT.append(p_y)
    print("Pearson for x:{}".format(p_x))
    print("Pearson for y:{}".format(p_y))

print("----------------------------------------")
Pearson__xBz = []
Pearson__yBz = []
for j in range(1, len(Vel_x_Bz)):
    p_x = pearsonr(Vx_diff[j-1].flatten(), Vel_x_Bz[j-1].flatten())
    Pearson__xBz.append(p_x)
    p_y = pearsonr(Vy_diff[j-1].flatten(), Vel_y_Bz[j-1].flatten())
    Pearson__yBz.append(p_y)
    print("Pearson for x:{}".format(p_x))
    print("Pearson for y:{}".format(p_y))