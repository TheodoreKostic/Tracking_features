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




# Filtered velocities
from scipy.ndimage import gaussian_filter
# For velocities derived through FLCT
filter__x = []
filter__y = []
for j in range(0, len(Vel_x_Bz)):
    filtered_x = gaussian_filter(Vel_x_Bz[j].flatten(), sigma = 4, mode = 'wrap')
    filter__x.append(filtered_x)
    filtered_y = gaussian_filter(Vel_y_Bz[j].flatten(), sigma = 4, mode = 'wrap')
    filter__y.append(filtered_y)
# For velocities that come from simulation
filter__x_sim = []
filter__y_sim = []
for j in range(0, len(Vx_diff)):
    filterx = gaussian_filter(Vx_diff[j].flatten(), sigma = 4, mode = 'wrap')
    filter__x_sim.append(filterx)
    filtery = gaussian_filter(Vy_diff[j].flatten(), sigma = 4, mode = 'wrap')
    filter__y_sim.append(filtery)

print(len(filter__x))
print(len(filter__x_sim))
# Now to the correlation part
r_x = [] # for filtered x from FLCT
r_y = [] # for filtered y from FLCT
filter__x = np.asarray(filter__x)
filter__y = np.asarray(filter__y)
filter__x_sim = np.asarray(filter__x_sim)
filter__y_sim = np.asarray(filter__y_sim)
for j in range(0, len(filter__x)):
    valx = pearsonr(filter__x[j], filter__x_sim[j])
    r_x.append(valx)
    valy = pearsonr(filter__y[j], filter__y_sim[j])
    r_y.append(valy)

print(r_x)
print("--------------------------")
print(r_y)