import numpy as np 
import matplotlib.pyplot as plt 
#import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr
from astropy.io import fits

test_range = 361 # number of slices
# Real Vx and Vy
Vx = fits.open("ISSI_2D_Tau=1.0-" + str(test_range) + "slices.fits")[2].data
Vy = fits.open("ISSI_2D_Tau=1.0-" + str(test_range) + "slices.fits")[3].data

# FLTC-derived velocities based on temperature
Vel_x_T = fits.open("ISSI_FLCT_temperature.fits")[0].data
Vel_y_T = fits.open("ISSI_FLCT_temperature.fits")[1].data
Vm_T = fits.open("ISSI_FLCT_temperature.fits")[2].data

# FLTC-derived velocities based on magnetic field
Vel_x_Bz = fits.open("ISSI_FLCT_magnetic.fits")[0].data
Vel_y_Bz = fits.open("ISSI_FLCT_magnetic.fits")[1].data
Vm_Bz = fits.open("ISSI_FLCT_magnetic.fits")[2].data

# Averaged, i.e mean Vx and Vy
Vx_mean = []
Vy_mean = []
for j in range(1, len(Vx)):
    vx = (Vx[j-1] + Vx[j])/2/1e5
    Vx_mean.append(vx)
    vy = (Vy[j-1] + Vy[j])/2/1e5
    Vy_mean.append(vy)

Vx_mean = np.asarray(Vx_mean)
Vy_mean = np.asarray(Vy_mean)

# Pearson's correlation coefficients
px_1 = []
py_1 = []

# This is for show only
# It will be updated to run more smoothly

for j in range(1, len(Vel_x_Mb)):
    p_x = pearsonr(Vx_mean[j-1].flatten(), Vel_x_T[j-1].flatten())
    px_1.append(p_x)
    p_y = pearsonr(Vy_mean[j-1].flatten(), Vel_y_T[j-1].flatten())
    py_1.append(p_y)
    print("Pearson for x:{}".format(p_x))
    print("Pearson for y:{}".format(p_y))