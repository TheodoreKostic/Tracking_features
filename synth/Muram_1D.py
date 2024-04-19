import matplotlib.pyplot as plt
import time
import numpy as np
import sys
import muram as mio
import os
from astropy.io import fits

iter = 63000
T = mio.MuramCube(os.getcwd(), iter, 'T')
#print(np.min(T))
pgas = mio.MuramCube(os.getcwd(), iter, 'P')
#z = np.linspace(0, 16000, 1587519)
vz = mio.MuramCube(os.getcwd(), iter, 'vx')
vturb = np.zeros(len(vz))

i_start = 0
i_end = 128
j_start = 0
j_end = 128

temp = T[360:480,i_start:i_end,j_start:j_end]
print("The shape of temperature due to focusing on photosphere:{} ".format(np.shape(temp)))
Pgas = pgas[360:480,i_start:i_end,j_start:j_end]
Vz = vz[360:480,i_start:i_end,j_start:j_end]

temp = np.copy(temp)

NZ, NY, NX = temp.shape
# Given that we are interested in photosphere, we are limiting the range of temperature

temp[np.where(temp<2100.)] = 2100.
temp[np.where(temp>20000.)] = 20000.
''' for i in range(NZ):
	for j in range(NY):
		for k in range(NX):
			if temp[i][j][k] < 2000:
				temp[i][j][k] = 2000
			elif temp[i][j][k] > 20000:
				temp[i][j][k] = 20000
			else:
				temp[i][j][k] = temp[i][j][k] '''

print("The amount of time it takes to complete for loop in seconds:{}".format(time.process_time()))
#z = np.linspace(0, 16000, num = 480, endpoint = True)
z = np.arange(temp.shape[0]) * 16.0

z = np.tile(z[:, np.newaxis, np.newaxis], (1, NY, NX))

print("The shape of height(z):{} ".format(np.shape(z)))

# Modified data should be saved in a separate file from
# which it should be read into minimal_synth_muram.py

# Now we went into slightly different direction -> We are going to use this file directly in the mpi wrapper:

atmoscube = np.concatenate((z[None,:,:,:], (temp[None,:,:,:]), (Pgas[None,:,:,:]), (Vz[None,:,:,:])), axis=0)

print("The the final shape is:{} ".format(np.shape(atmoscube)))

'''one = fits.PrimaryHDU(temp)
two = fits.ImageHDU(Pgas)
three = fits.ImageHDU(Vz)
four = fits.ImageHDU(z)
tot = fits.HDUList([one, two, three, four])'''
tot = fits.PrimaryHDU(atmoscube)
tot.writeto("muram_fixed.fits", overwrite = True)
print("Finished")