# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr

# Initializing list of names of all the files
filenames = []

# Getting only .h5 files for that is our data
for file in sorted(os.listdir (os.getcwd())):
	if file.endswith(".h5"):
		#print (file)
		filenames.append(file)
print ("How many files are in directory: {}".format(len(filenames)))

# Setting the new array length as the number of h5 files
NT = len(filenames)

tempfile = h5py.File(filenames[0])

# Getting the dimensions of our datasets
NZ,NY,NX = tempfile['T'].shape

# Arrays that will contain the data we want separated
T_series = np.zeros([NT, NX, NY])
Bz_series = np.zeros([NT, NX, NY])
Vx_series = np.zeros([NT, NX, NY])
Vy_series = np.zeros([NT, NX, NY])
Vz_series = np.zeros([NT, NX, NY])

# The depth we are "looking at"
d_T = input("Please enter a number in range (0, 40): ")
d_T = int(d_T) # will mostly be using and changing this one and the one for Bz
d_Bz = input("Please enter a number in range (0, 40): ")
d_Bz = int(d_Bz)
T_series[0] = np.copy(tempfile['T'][d_T].T)
Bz_series[0] = np.copy(tempfile['bz'][d_Bz].T)
Vx_series[0] = np.copy(tempfile['vx'][d_T].T)
Vy_series[0] = np.copy(tempfile['vy'][d_T].T)
Vz_series[0] = np.copy(tempfile['vz'][d_T].T)

del(tempfile)
# Input data in arrays
for t in range(1,NT):
    tempfile = h5py.File(filenames[t], 'r')
    T_series[t] = np.copy(tempfile['T'][d_T].T)
    Bz_series[t] = np.copy(tempfile['bz'][d_T].T)
    Vx_series[t] = np.copy(tempfile['vx'][d_T].T)
    Vy_series[t] = np.copy(tempfile['vy'][d_T].T)
    Vz_series[t] = np.copy(tempfile['vz'][d_T].T)
    del(tempfile)

from astropy.io import fits 
# Print the data into fresh .fits file
kek1 = fits.PrimaryHDU(T_series)
kek2 = fits.ImageHDU(Bz_series)
kek3 = fits.ImageHDU(Vx_series)
kek4 = fits.ImageHDU(Vy_series)
kek5 = fits.ImageHDU(Vz_series)
kek = fits.HDUList([kek1, kek2, kek3, kek4, kek5])

kek.writeto("series.fits", overwrite = True)

# Let's actually use pyflct to determine vel_x and vel_y for current working depth

Bz_1 = Bz_series[1].reshape(240, 2, 240, 2)
Bz_2 = Bz_series[2].reshape(240, 2, 240, 2)
Bz_3 = Bz_series[3].reshape(240, 2, 240, 2)
Bz12 = (Bz_1 + Bz_2).mean(axis = 3).mean(axis = 1)
Bz23 = (Bz_2 + Bz_3).mean(axis = 3).mean(axis = 1)
vel_x123, vel_y123, vm123 = pyflct.flct(Bz12, Bz23, 1*30, 1*50, 5.0) 

# Let's average the velocities from v series for comparison

vx1 = Vx_series[1].reshape(240, 2, 240, 2)
vy1 = Vy_series[1].reshape(240, 2, 240, 2)

vx2 = Vx_series[2].reshape(240, 2, 240, 2)
vy2 = Vy_series[2].reshape(240, 2, 240, 2)

vx12 = (vx1 + vx2).mean(axis = 3).mean(axis = 1)/1e5
vy12 = (vy1 + vy2).mean(axis = 3).mean(axis = 1)/1e5



r12x = pearsonr(vel_x123.flatten(), vx12.flatten())
print(r12x)

r12y = pearsonr(vel_y123.flatten(), vy12.flatten())
print(r12y)

# Recreate former code for all values of Bz_series
Vel_x = []
Vel_y = []
Vm = []
Bz_bin = []

for j in range(0, NT):
    Bz = Bz_series[j].reshape(240, 2, 240, 2)
    Bz_bin.append(Bz)
    #Bz_beam = (Bz_series[j] + Bz_series[j+1]).mean(axis = 3).mean(axis = 1)
    #print(Bz_beam)
    #Vel_x[j], Vel_y[j], Vm[j] = pyflct.flct(Bz_beam[j], Bz_beam[j+1], 1*30, 1*50, 5.0)
Bz_bin = np.array(Bz_bin)
Bz_mean = []
for j in range(1, NT):
    Bz_mean_ = (Bz_bin[j-1] + Bz_bin[j]).mean(axis = 3).mean(axis = 1)
    Bz_mean.append(Bz_mean_)
    
for j in range(1, len(Bz_mean)):
    vel_x, vel_y, vm = pyflct.flct(Bz_mean[j-1], Bz_mean[j], 1*30, 1*50, 5.0)
    Vel_x.append(vel_x)
    Vel_y.append(vel_y)
    Vm.append(vm)

Vx = []
Vy = []
for j in range(0, NT):
    vx = Vx_series[j].reshape(240, 2, 240, 2)
    Vx.append(vx)
    vy = Vy_series[j].reshape(240, 2, 240, 2)
    Vy.append(vy)
Vx_mean = []
Vy_mean = []
for j in range(1, len(Vx)):
    vx_mean = (Vx[j-1] + Vx[j]).mean(axis = 3).mean(axis = 1)/1e5
    vy_mean = (Vy[j-1] + Vy[j]).mean(axis = 3).mean(axis = 1)/1e5
    Vx_mean.append(vx_mean)
    Vy_mean.append(vy_mean)

Pearson__x = []
Pearson__y = []
for j in range(1, len(Vel_x)):
    p_x = pearsonr(Vx_mean[j-1].flatten(), Vel_x[j-1].flatten())
    Pearson__x.append(p_x)
    p_y = pearsonr(Vy_mean[j-1].flatten(), Vel_y[j-1].flatten())
    Pearson__y.append(p_y)
    print("Pearson for x:{}".format(p_x))
    print("Pearson for y:{}".format(p_y))

# Find the maximum pearson's coefficient and corresponding index
"""
Max__x__p = pearsonr(0, 0)
index_for_x = 0
for j in range(len(Pearson__x)):
    if Pearson__x[j].statistic > Max__x__p:
        Max__x__p = Pearson__x[j].statistic
        index_for_x = Pearson__x.index(max)


Max__y__p = pearsonr(0, 0)
index_for_y = 0
for j in range(len(Pearson__y)):
    if Pearson__y[j].statistic > Max__y__p:
        Max__y__p = Pearson__y[j].statistic
        index_for_y = Pearson__y.index(max)

print("Maximum Pearson coefficient {} is found for layer {} regarding x component of velocity".format(Max__x__p, index_for_x))
print("Maximum Pearson coefficient {} is found for layer {} regarding y component of velocity".format(Max__y__p, index_for_y))
"""
# Next, we would like to try to use gaussian_filter to convolve or "filter" our velocities 
# before we search for correlation 
from scipy.ndimage import gaussian_filter
# For velocities derived through FLCT
filter__x = []
filter__y = []
for j in range(0, len(Vel_x)):
    filtered_x = gaussian_filter(Vel_x[j].flatten(), sigma = 4, mode = 'wrap')
    filter__x.append(filtered_x)
    filtered_y = gaussian_filter(Vel_y[j].flatten(), sigma = 4, mode = 'wrap')
    filter__y.append(filtered_y)
# For velocities that come from simulation
filter__x_sim = []
filter__y_sim = []
for j in range(0, len(Vx_mean)):
    filterx = gaussian_filter(Vx_mean[j].flatten(), sigma = 4, mode = 'wrap')
    filter__x_sim.append(filterx)
    filtery = gaussian_filter(Vy_mean[j].flatten(), sigma = 4, mode = 'wrap')
    filter__y_sim.append(filtery)

print(len(filter__x))
print(len(filter__x_sim))
# Now to the correlation part
r_x = [] # for filtered x from FLCT
r_y = [] # for filtered y from FLCT
for j in range(0, len(filter__x)):
    valx = pearsonr(filter__x[j], filter__x_sim[j])
    r_x.append(valx)
    valy = pearsonr(filter__y[j], filter__y_sim[j])
    r_y.append(valy)