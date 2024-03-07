import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import sys
import os
import pyflct
from scipy.stats import pearsonr
from astropy.io import fits

# kek.writeto("series_basic.fits", overwrite = True)

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

# Real V_x histogram	
# Let's introduce a temporary array consisting of 3 timestamps taken from timeseries
a = [Vx_mean[28], Vx_mean[29], Vx_mean[30]]
a = np.asarray(a)
hist1, hist1_edges = np.histogram(a, density = True)
plt.hist(hist1, bins = 'auto')
plt.title("Real Vx, 3")
plt.show()

b = [Vx_mean[27], Vx_mean[28], Vx_mean[29], Vx_mean[30], Vx_mean[31]]
b = np.asarray(b)
hist2, hist2_edges = np.histogram(b, density = True)
plt.hist(hist2, bins = 'auto')
plt.title("Real Vx, 5")
plt.show()

c = [Vx_mean[24], Vx_mean[25], Vx_mean[26], Vx_mean[27], Vx_mean[28], Vx_mean[29], Vx_mean[30], Vx_mean[31], Vx_mean[32], Vx_mean[33], Vx_mean[34]]
c = np.asarray(c)
hist3, hist3_edges = np.histogram(c, density = True)
plt.hist(hist3, bins = 'auto')
plt.title("Real Vx, 10")
plt.show()

# FLCT Bz histogram
aa = [Vel_x_Bz[28], Vel_x_Bz[29], Vel_x_Bz[30]]
aa = np.asarray(aa)
hist1Bz, hist1Bz_edges = np.histogram(aa, density = True)
plt.hist(hist1Bz, bins = 'auto')
plt.title("FLCT Bz Vx, 3")
plt.show()

bb = [Vel_x_Bz[27], Vel_x_Bz[28], Vel_x_Bz[29], Vel_x_Bz[30], Vel_x_Bz[31]]
bb = np.asarray(bb)
hist2Bz, hist2Bz_edges = np.histogram(bb, density = True)
plt.hist(hist2Bz, bins = 'auto')
plt.title("FLCT Bz Vx, 5")
plt.show()

cc = [Vel_x_Bz[24], Vel_x_Bz[25], Vel_x_Bz[26], Vel_x_Bz[27], Vel_x_Bz[28], Vel_x_Bz[29], Vel_x_Bz[30], Vel_x_Bz[31], Vel_x_Bz[32], Vel_x_Bz[33], Vel_x_Bz[34]]
cc = np.asarray(cc)
hist3Bz, hist3Bz_edges = np.histogram(cc, density = True) 
plt.hist(hist3Bz, bins = 'auto')
plt.title("FLCT Bz Vx, 10")
plt.show()
"""
# FLCT T histogram
aaa = [Vel_x_T[28], Vel_x_T[29], Vel_x_T[30]]
aaa = np.asarray(aaa)
hist1T, hist1T_edges = np.histogram(aaa, density = True)
plt.hist(hist1Bz, bins = 'auto')
plt.title("FLCT T Vx, 3")
plt.show()

bbb = [Vel_x_T[27], Vel_x_T[28], Vel_x_T[29], Vel_x_T[30], Vel_x_T[31]]
bbb = np.asarray(bbb)
hist2T, hist2T_edges = np.histogram(bbb, density = True)
plt.hist(hist2T, bins = 'auto')
plt.title("FLCT T Vx, 5")
plt.show()

ccc = [Vel_x_T[24], Vel_x_T[25], Vel_x_T[26], Vel_x_T[27], Vel_x_T[28], Vel_x_T[29], Vel_x_T[30], Vel_x_T[31], Vel_x_T[32], Vel_x_T[33], Vel_x_T[34]]
ccc = np.asarray(ccc)
hist3T, hist3T_edges = np.histogram(ccc, density = True) 
plt.hist(hist3T, bins = 'auto')
plt.title("FLCT T Vx, 10")
plt.show()
"""
# Histograms in general
histogram_vx, hedges = np.histogram(np.asarray(Vx_mean).flatten(), density = True)
plt.hist(histogram_vx, bins = 'auto')
plt.title("Real Vx")
plt.show()

histogram_vxT, hedgesT = np.histogram(np.asarray(Vel_x_T).flatten(), density = True)
plt.hist(histogram_vxT, bins = 'auto')
plt.title("FLCT T Vx")
plt.show()

histogram_vxB, hedgesB = np.histogram(np.asarray(Vel_x_Bz).flatten(), density = True)
plt.hist(histogram_vxB, bins = 'auto')
plt.title("FLCT Bz Vx")
plt.show()