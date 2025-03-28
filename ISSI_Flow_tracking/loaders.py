import muram as muram
import numpy as np 
from tqdm import tqdm
from astropy.io import fits

def load_from_muram_slices(path, start, step, number, parameter, depth):

	for i in tqdm(range(number)):
		snapshot = start + i*step

		test = 0

		# For the intensity
		if (parameter == 'Ic'):
			test=muram.MuramIntensity(path, snapshot)

		# For Bz (or anything else, we have to approach it differently:)
		elif (parameter == 'Bz'):
			data = muram.read_slice(path, snapshot, 'tau', depth)
			test = np.copy(data[0][5,:,:] * np.sqrt(4 * np.pi))
			data = None
		elif (parameter == 'TB'):
			data = muram.read_slice(path, snapshot, 'tau', depth)
			T = np.copy(data[0][8,:,:])
			B = (np.exp(27409.0/T) - 1.0) ** (-1.0)
			test = np.copy(B)
			data = None
		else:
			print("Something wrong with the parameter choice")
		
		
		if (i==0):
			cube = test.reshape(1,1536,1536)
		else:
			cube = np.append(cube,test[None,:,:],axis=0)
			test = None 

	print("info::load_from_muram_slices::final cube size is: ", cube.shape)
	return cube

def load_from_lw_fits(path, start, step, number, wvl):

	for i in tqdm(range(number)):
		snapshot = start + i*step

		test = 0

		# For the intensity
		test = fits.open(path+str(snapshot)+'_lwsynth_100.0.fits')[0].data[:,:,0,wvl]

		qs = 1.0
		if (i==0):
			cube = test.reshape(1,1536,1536)
			qs = np.mean(cube)
			print("info::load_from_lw_fits::normalizing each image with:  ", qs)		
			cube /= qs

		else:
			cube = np.append(cube,test[None,:,:]/qs,axis=0)
			test = None 

	print("info::load_from_lw_fits::final cube size is: ", cube.shape)
	return cube

