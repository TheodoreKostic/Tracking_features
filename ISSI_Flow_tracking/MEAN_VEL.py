import numpy as np 
import matplotlib.pyplot as plt 
#import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr
from tqdm import tqdm
import time
# We need this to navigate through our data
#import muram as muram

# Input/output
from astropy.io import fits

filenames = []
path = "/home/teodor_kostic/ISSI_2D_Slices/TAU_0_100"
# Retreiving only numerical files
for file in sorted(os.listdir (os.getcwd())):
	if file.startswith("tau_slice_0.100"):
		#print (file)
		filenames.append(file)

print(len(filenames))
vxr = []
vyr = []

test_range = 361
for iter in range(test_range):
    test = filenames[iter]
    #print(iter)
    data_full = np.fromfile(test, dtype="float32")
    data = data_full[4:].reshape(11, 1536, 1536)
    Vx = np.copy(data[2,:,:])
    Vy = np.copy(data[3,:,:])
    vxr.append(Vx)
    vyr.append(Vy)

Vx = np.asarray(vxr)
Vy = np.asarray(vyr)





VX = fits.PrimaryHDU(Vx)
VY = fits.ImageHDU(Vy)

data_out = fits.HDUList([VX, VY])

# Write the fits file
data_out.writeto("Velocities.fits", overwrite = True)




Vx_ = fits.open("Velocities.fits")[0].data
Vy_ = fits.open("Velocities.fits")[1].data

# Average
Vx_mean = []
Vy_mean = []
for j in range(1, len(Vx_)):
    vx = (Vx_[j-1] + Vx_[j])/2/1e5
    vx__ = np.copy(vx)
    del(vx)
    Vx_mean.append(vx__)
    vy = (Vy_[j-1] + Vy_[j])/2/1e5
    vy__ = np.copy(vy)
    del(vy)
    Vy_mean.append(vy__)
    #print(j)

Vx_mean = np.asarray(Vx_mean)
Vy_mean = np.asarray(Vy_mean)

out1 = fits.PrimaryHDU(Vx_mean)
out2 = fits.ImageHDU(Vy_mean)
out = fits.HDUList([out1, out2])
out.writeto("Mean_velocities.fits", overwrite = True)