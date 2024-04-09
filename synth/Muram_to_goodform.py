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
z = np.linspace(0, 16000, 1587519)
vz = mio.MuramCube(os.getcwd(), iter, 'vx')
vturb = np.zeros(len(vz))

temp = T[:,:128,:128]
pgas = pgas[:,:128,:128]
vz = vz[:,:128,:128]
temp = temp[temp[:,:,:] > 2000]
temp = temp[temp < 9000]
pgas = temp[temp > 2000]
pgas = temp[temp < 9000]
vz = temp[temp > 2000]
vz = temp[temp < 9000]
print("The shape of temperature")
print(np.shape(temp))
print("------------------")
print("The minimum of temperature:{}".format(np.min(temp)))
print("The maximum of temperature:{}".format(np.max(temp)))
print("------------------")

print("The shape of z")
print(np.shape(z))
print(time.process_time())

temp = temp.flatten()
print("The shape of flattened temperature")
print(np.shape(temp))
print("The minimum of flattened temperature:{}".format(np.min(temp)))
pgas = pgas.flatten()
vz = vz.flatten()

# Falc fits instead of falc dat
one = fits.PrimaryHDU(temp)
two = fits.ImageHDU(pgas)
three = fits.ImageHDU(z)
four = fits.ImageHDU(vz)
tot = fits.HDUList([one, two, three, four])
tot.writeto("muram_in.fits", overwrite = True)

# Reducing the size of fits file

original = fits.open("i_am_test.fits")[0].data
print(original.shape)

cropped = original[:,:,0:24,0:24]
kek1 = fits.PrimaryHDU(cropped)
kek = fits.HDUList([kek1])
kek.writeto("i_am_test_cropped.fits", overwrite = True)