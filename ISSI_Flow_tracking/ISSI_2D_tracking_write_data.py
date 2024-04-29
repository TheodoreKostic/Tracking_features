import numpy as np 
import matplotlib.pyplot as plt 
#import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr

# We need this to navigate through our data
import muram 

# Input/output
from astropy.io import fits

# We should import all tau_slices at Tau = 1 and see how flow tracking behaves for this data
# Initializing list of names of all the files
filenames = []

# Retreiving only numerical files
for file in sorted(os.listdir (os.getcwd())):
	if file.startswith("tau_slice"):
		#print (file)
		filenames.append(file)
print ("How many files are in directory: {}".format(len(filenames)))

# Setting the new array length as the number of tau slices
NT = len(filenames) # timeseries

iter = 50
level = 1.0
tempfile = muram.MuramTauSlice('', iter, level)
# Let's print the shape of our file(s):
print(np.shape(tempfile))

NP, NX, NY = np.shape(tempfile) # parameters, x, y
#T_series = np.zeros([NX, NY])
T_array = []
Bz_array = []
Vx_array = []
Vy_array = []
# To make sure we are using the temperature
#plt.imshow(tempfile[8].T, origin='lower',vmin=5500,vmax=8000)

# Looping through all the slices
test_range = len(filenames)
for iter in range(test_range): 
	test = filenames[iter]
	#print(test)
	data_full = np.fromfile(test, dtype="float32")
	data = data_full[4:].reshape(11, 1536, 1536)
	T = data[8,:,:]
	Bz = data[7,:,:]
	Vx = data[1,:,:]
	Vy = data[2,:,:]
	Vx_array.append(Vx)
	Vy_array.append(Vy)
	T_array.append(T)
	Bz_array.append(Bz)
	
	
# Kada se traze brzine, pre nego sto se trazi korelacija, nadjimo nacin da vizualizujemo ono sto dobijamo
# i vidimo da kakve su mape brzine, da li su granule ok itd.

# For easier further use we will write the data out in a fits file
# that shall be available to users

T_array = np.asarray(T_array)
Bz_array = np.asarray(Bz_array)
Vx_array = np.asarray(Vx_array)
Vy_array = np.asarray(Vy_array)

Temp = fits.PrimaryHDU(T_array)
Bz = fits.ImageHDU(Bz_array)
Vx = fits.ImageHDU(Vx_array)
Vy = fits.ImageHDU(Vy_array)
data_out = fits.HDUList([Temp, Bz, Vx, Vy])

# Write the fits file
data_out.writeto("ISSI_2D_Tau=1.0-" + str(test_range) + "slices.fits", overwrite = True)
