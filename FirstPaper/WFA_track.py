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
path = "/scratch/teodor_kostic/ISSI_2D_Slice"

for file in sorted(os.listdir (os.getcwd())):
	if file.startswith("loc_dyn_32_32_16_series"):
		#print (file)
		filenames.append(file)

print(len(filenames))

vel_x = [] #vx array
vel_y = [] #vy array
BZ = [] #Bz array

# FLCT settings
fwhm = 600.0 #km
delta_t = 10.0 * 3 #s
pixelsize = 32.0 #km because we compare to (768, 768)
sigma = fwhm/1.665/pixelsize # Gaussian
print("Sigma: {}".format(sigma))
cube = fits.open("loc_dyn_32_32_16_series_tumag_l2_wfa.fits")[0].data
for i in tqdm(range(1, len(cube))):
	B1 = np.copy(cube[i-1,:,:])
	B2 = np.copy(cube[i,:,:])
	vx, vy, vm = pyflct.flct(B1, B2, delta_t, pixelsize, sigma, quiet = True)
	vel_x.append(vx)
	vel_y.append(vy)
	#BZ.append(B)
	#BZ = np.asarray(BZ)
	#Bz = fits.PrimaryHDU(BZ)
	#data_out = fits.HDUList([Bz])
	#data_out.writeto("FeI_ME_Bz")


vel_x = np.asarray(vel_x)
vel_y = np.asarray(vel_y)
vxhdu = fits.PrimaryHDU(vel_x)
vyhdu = fits.ImageHDU(vel_y)
vxhdu.header['UNITS'] = 'km/s' # units that velocities are in 
vxhdu.header['TRACKED'] = 'FeI_Bz' # the parameter which was tracked
#vxhdu.header['WHEN_RUN'] = ts # timestamp of run
vxhdu.header['AUTHOR'] = 'Teodor'
vxhdu.header['FWHM'] = fwhm # in kilometres
vxhdu.header['PIXELS'] = pixelsize # in kilometres
vxhdu.header['SIGMA'] = sigma # FLCT window in kilometres 
vxhdu.header['DELTAT'] = delta_t # time interval between two frames in seconds
vxhdu.header['THRESH'] = 0 # FLCT is not applied to pixels below this
vxhdu.header['SIMSTEP'] = 150 # should match the filename
vxhdu.header['SIMTIME'] = 4500 # 1 hour
vxhdu.header['COMMENT'] = 'ME_Bz'
to_output = fits.HDUList([vxhdu, vyhdu])
to_output.writeto(sys.argv[1][:-5]+'_tracked.fits', overwrite=True)