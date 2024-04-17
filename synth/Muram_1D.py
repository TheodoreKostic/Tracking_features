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

temp = T[360:480,:,:]
print("The shape of temperature due to focusing on photosphere:{} ".format(np.shape(temp)))
Pgas = pgas[360:480,:,:]
Vz = vz[360:480,:,:]
Vturb = np.zeros(len(Vz))
temp = np.copy(temp)
# Given that we are interested in photosphere, we are limiting the range of temperature
for i in range(len(temp)):
	for j in range(1536):
		for k in range(1536):
			if temp[i][j][k] < 2000:
				temp[i][j][k] = 2000
			elif temp[i][j][k] > 20000:
				temp[i][j][k] = 20000
			else:
				temp[i][j][k] = temp[i][j][k]

print("The amount of time it takes to complete for loop in seconds:{}".format(time.process_time()))
z = np.linspace(0, 16000, num = 480, endpoint = True)
print("The shape of height(z):{} ".format(np.shape(z)))

# Modified data should be saved in a separate file from
# which it should be read into minimal_synth_muram.py


one = fits.PrimaryHDU(temp)
two = fits.ImageHDU(Pgas)
three = fits.ImageHDU(z)
four = fits.ImageHDU(Vz)
tot = fits.HDUList([one, two, three, four])
tot.writeto("muram_fixed.fits", overwrite = True)
print("Finished")