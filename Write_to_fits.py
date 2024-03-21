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
MB_series = np.zeros([NT, NX, NY])
# The depth we are "looking at"
#d_T = input("Please enter a number in range (0, 40): ")
#d_T = int(d_T) # will mostly be using and changing this one and the one for Bz
#d_Bz = input("Please enter a number in range (0, 40): ")
#d_Bz = int(d_Bz)
d = input("Please enter a number in range (0, 40): ")
d = int(d)
T_series[0] = np.copy(tempfile['T'][d].T)
Bz_series[0] = np.copy(tempfile['bz'][d].T)
Vx_series[0] = np.copy(tempfile['vx'][d].T)
Vy_series[0] = np.copy(tempfile['vy'][d].T)
Vz_series[0] = np.copy(tempfile['vz'][d].T)
MB_series[0] = np.copy(tempfile['bolometric'][d].T)
del(tempfile)
# Input data in arrays
for t in range(1,NT):
    tempfile = h5py.File(filenames[t], 'r')
    T_series[t] = np.copy(tempfile['T'][d].T)
    Bz_series[t] = np.copy(tempfile['bz'][d].T)
    Vx_series[t] = np.copy(tempfile['vx'][d].T)
    Vy_series[t] = np.copy(tempfile['vy'][d].T)
    Vz_series[t] = np.copy(tempfile['vz'][d].T)
    MB_series[t] = np.copy(tempfile['bolometric'][d].T)
    del(tempfile)

from astropy.io import fits 
# Print the data into fresh .fits file
kek1 = fits.PrimaryHDU(T_series)
kek2 = fits.ImageHDU(Bz_series)
kek3 = fits.ImageHDU(Vx_series)
kek4 = fits.ImageHDU(Vy_series)
kek5 = fits.ImageHDU(Vz_series)
kek6 = fits.ImageHDU(MB_series)
kek = fits.HDUList([kek1, kek2, kek3, kek4, kek5, kek6])

kek.writeto("series_all.fits", overwrite = True)