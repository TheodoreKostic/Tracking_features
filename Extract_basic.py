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

# The depth we are "looking at"
d_T = input("Please enter a number in range (0, 40): ")
d_T = int(d_T) # will mostly be using and changing this one and the one for Bz
d_Bz = input("Please enter a number in range (0, 40): ")
d_Bz = int(d_Bz)
T_series[0] = np.copy(tempfile['T'][d_T].T)
Bz_series[0] = np.copy(tempfile['bz'][d_Bz].T)
Vx_series[0] = np.copy(tempfile['vx'][d_T].T)
Vy_series[0] = np.copy(tempfile['vy'][d_T].T)
Vz_series[0] = np.copy(tempfile['vz'][d_T].T)

del(tempfile)
# Input data in arrays
for t in range(1,NT):
    tempfile = h5py.File(filenames[t], 'r')
    T_series[t] = np.copy(tempfile['T'][d_T].T)
    Bz_series[t] = np.copy(tempfile['bz'][d_Bz].T)
    Vx_series[t] = np.copy(tempfile['vx'][d_T].T)
    Vy_series[t] = np.copy(tempfile['vy'][d_T].T)
    Vz_series[t] = np.copy(tempfile['vz'][d_T].T)
    del(tempfile)

from astropy.io import fits 
# Print the data into fresh .fits file
kek1 = fits.PrimaryHDU(T_series)
kek2 = fits.ImageHDU(Bz_series)
kek3 = fits.ImageHDU(Vx_series)
kek4 = fits.ImageHDU(Vy_series)
kek5 = fits.ImageHDU(Vz_series)
kek = fits.HDUList([kek1, kek2, kek3, kek4, kek5])

kek.writeto("series_basic.fits", overwrite = True)

Temp = fits.open("series_basic.fits")[0].data
Bz = fits.open("series_basic.fits")[1].data
Vx = fits.open("series_basic.fits")[2].data
Vy = fits.open("series_basic.fits")[3].data

# Let's do basic comparison of "real" velocities and the ones that FLCT gives
# between every 2 adjacent files 

Vx_mean = []
Vy_mean = []
for j in range(1, len(Vx)):
    vx = (Vx[j-1] + Vx[j])/2/1e5
    Vx_mean.append(vx)
    vy = (Vy[j-1] + Vy[j])/2/1e5
    Vy_mean.append(vy)

# Now, we implement FLCT on our Temp array
Vel_x_T = []
Vel_y_T = []
Vm_T = []
for j in range(1, len(Temp)):
    vel_x, vel_y, vm = pyflct.flct(Temp[j-1], Temp[j], 1*30, 1*50, 5.0)
    Vel_x_T.append(vel_x)
    Vel_y_T.append(vel_y)
    Vm_T.append(vm)

print("Length of Vel_x_T: {}".format(len(Vel_x_T)))

#Now for Bz array
Vel_x_Bz = []
Vel_y_Bz = []
Vm_Bz = []
for j in range(1, len(Bz)):
    vel_x, vel_y, vm = pyflct.flct(Bz[j-1], Bz[j], 1*30, 1*50, 5.0)
    Vel_x_Bz.append(vel_x)
    Vel_y_Bz.append(vel_y)
    Vm_Bz.append(vm)

print("Length of Vel_x_Bz: {}".format(len(Vel_x_Bz)))
#cube_T = 
# We should check two cases:
# 1. Real vs. FLCT on T
# 2. Real vs. FCLT on B
# and plot both results
# 1.

fig, ax = plt.subplots()
ax.scatter(np.asarray(Vel_x_T), np.asarray(Vel_x_T)-np.asarray(Vx_mean), s=25, zorder=10)
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

# now plot both limits against eachother
ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_title("FLCT T vs. 'Real' x velocity")
plt.savefig("T_vs_realdiff.png", dpi = 300)
plt.show()

# 2.
fig, ax = plt.subplots()
ax.scatter(np.asarray(Vel_x_Bz), np.asarray(Vel_x_Bz)-np.asarray(Vx_mean), s=25, zorder=10)
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

# now plot both limits against eachother
ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_title("FLCT B vs. 'Real' x velocity")
plt.savefig("Bz_vs_realdiff.png", dpi = 300)
plt.show()
