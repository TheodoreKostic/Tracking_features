import numpy as np
import matplotlib.pyplot as plt
import pyflct
from astropy.io import fits
import sys
import os

filenames = []
path = "/scratch/teodor_kostic/ISSI_2D_Slices/New_synth"
# Retreiving only numerical files
for file in sorted(os.listdir (os.getcwd())):
	if file.endswith("_100.0.fits"):
		#print (file)
		filenames.append(file)

print(len(filenames))


delta_t = 10.0 * 3
pixelsize = 16
sigma = 600.0 / 1.665 / pixelsize

# Lists in which velocities will be stored
vel_x = []
vel_y = []
vm = []

for j in range(1, len(filenames)):
	cube1 = fits.open(filenames[j-1])[0].data
	cube2 = fits.open(filenames[j])[0].data
	image1 = cube1[:,:,0,4]
	image2 = cube2[:,:,0,4]
	#image1 = np.min(image1, axis = 2)
	#image2 = np.min(image2, axis = 2)
	vx, vy, m = pyflct.flct(image1, image2, delta_t, pixelsize, sigma, quiet = True)
	vel_x.append(vx)
	vel_y.append(vy)
	vm.append(m)
	print("Done")

vel_x = np.asarray(vel_x)
vel_y = np.asarray(vel_y)
vxhdu = fits.PrimaryHDU(vel_x)
vyhdu = fits.ImageHDU(vel_y)
vxhdu.header['UNITS'] = 'km/s' # units that velocities are in 
vxhdu.header['TRACKED'] = 'LW Intensity' # the parameter which was tracked
#vxhdu.header['WHEN_RUN'] = ts # timestamp of run
vxhdu.header['AUTHOR'] = 'Teodor'
vxhdu.header['FWHM'] = fwhm # in kilometres
vxhdu.header['PIXELS'] = pixelsize # in kilometres
vxhdu.header['SIGMA'] = sigma # FLCT window in kilometres 
vxhdu.header['DELTAT'] = delta_t # time interval between two frames in seconds
vxhdu.header['THRESH'] = 0 # FLCT is not applied to pixels below this
vxhdu.header['SIMSTEP'] = 0.2 # should match the filename
vxhdu.header['SIMTIME'] = 900 # 1 hour
vxhdu.header['COMMENT'] = ''
to_output = fits.HDUList([vxhdu, vyhdu])
to_output.writeto(sys.argv[1][:-5]+'_tracked.fits', overwrite=True)
