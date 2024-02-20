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

# Initializing list of names of all the files
filenames = []

# Getting only .h5 files for that is our data
for file in sorted(os.listdir (os.getcwd())):
	if file.endswith(".h5"):
		#print (file)
		filenames.append(file)
print (len(filenames))

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
d_T = 22 # will mostly be using and changing this one and the one for Bz
d_Bz = 22

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

from scipy.stats import pearsonr

r12x = pearsonr(vel_x123.flatten(), vx12.flatten())
print(r12x)

r12y = pearsonr(vel_y123.flatten(), vy12.flatten())
print(r12y)