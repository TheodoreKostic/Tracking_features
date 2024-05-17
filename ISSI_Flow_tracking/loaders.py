import muram as muram
import numpy as np 
from tqdm import tqdm

def load_from_muram_slices(path, start, step, number, parameter, depth):

	for i in tqdm(range(number)):
		snapshot = start + i*step

		# For the intensity
		#test=muram.MuramIntensity(path, snapshot)

		# For Bz (or anything else, we have to approach it differently:)
		data = muram.read_slice(path, snapshot, 'tau', '0.100')
		test = np.copy(data[0][5,:,:] * np.sqrt(4 * np.pi))
		data = None

		if (i==0):
			cube = test.reshape(1,1536,1536)
		else:
			cube = np.append(cube,test[None,:,:],axis=0)
			test = None 

	print("info::load_from_muram_slices::final cube size is: ", cube.shape)
	return cube

