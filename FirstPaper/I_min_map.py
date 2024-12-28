from threadpoolctl import threadpool_limits

import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
threadpool_limits(1)
import pickle
from enum import IntEnum

import numpy as np
from mpi4py import MPI
from tqdm import tqdm
import sys
threadpool_limits(1)
from astropy.io import fits
import pyflct
import time
#import loaders as loaders
#import loadersBz as loaders
#import loadersT as loaders

filenames = []
path = "/scratch/teodor_kostic/ISSI_2D_Slices/New_synth"
# Retreiving only numerical files
for file in sorted(os.listdir (os.getcwd())):
	if file.endswith("_100.0.fits"):
		#print (file)
		filenames.append(file)

print(len(filenames))

def find_minimum_intensity(spec):

    imin = np.argmin(spec[30:60])+30
    x = np.arange(5) + imin - 2
    y = spec[x]
    a,b,c = np.polyfit(x,y,2)
    x_min = -b / 2 / a
    y_min = a * x_min **2.0 + b * x_min + c
    return x_min, y_min

v = np.zeros([1536,1536])
I_min = np.zeros([1536,1536])

for file in range(0, len(filenames)):
	cube = fits.open(filenames[file])[0].data
	cube = cube[:,:,:,21:]
	for i in tqdm(range(0, 1536)):
		for j in range(0, 1536):
			speed, intes = find_minimum_intensity(cube[i,j,0]) 
			v[i, j] = speed
			v = np.asarray(v)
			I_min[i, j] = intes
			I_min = np.asarray(I_min)
	Imi_hdu = fits.PrimaryHDU(I_min)
	v_hdu = fits.ImageHDU(v)
	to_output = fits.HDUList([Imi_hdu, v_hdu])
	to_output.writeto(filenames[file][:-5]+'_tracked.fits', overwrite=True)

