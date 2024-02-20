import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import sys
import os

filenames = []

for file in sorted(os.listdir (".")):
	if file.endswith(".h5"):
		#print (file)
		filenames.append(file)
print (len(filenames))

NT = len(filenames)

tempfile = h5py.File(filenames[0])

NZ,NY,NX = tempfile['T'].shape

T_series = np.zeros([NT, NX, NY])
Bz_series = np.zeros([NT, NX, NY])

d_T = 20
d_Bz = 22

T_series[0] = np.copy(tempfile['T'][d_T].T)
Bz_series[0] = np.copy(tempfile['bz'][d_Bz].T)

del(tempfile)

for t in range(1,NT):

	tempfile = h5py.File(filenames[t], 'r')

	T_series[t] = np.copy(tempfile['T'][d_T].T)
	Bz_series[t] = np.copy(tempfile['bz'][d_Bz].T)

	del(tempfile)

from astropy.io import fits 

kek1 = fits.PrimaryHDU(T_series)
kek2 = fits.ImageHDU(Bz_series)

kek = fits.HDUList([kek1,kek2])

kek.writeto("series.fits",overwrite=True)


