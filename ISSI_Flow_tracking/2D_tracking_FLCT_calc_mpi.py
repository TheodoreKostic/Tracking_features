## Various imports some probably not needed:

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
import loaders as loaders

class tags(IntEnum):
    """ Class to define the state of a worker.
    It inherits from the IntEnum class """ # Makes sense to me, but not sure what is the IntEnum class 
    READY = 0
    DONE = 1
    EXIT = 2
    START = 3

def slice_tasks(fullcube, task_start, grain_size):
    
    task_end = min(task_start + grain_size, fullcube.shape[0])

    sl = slice(task_start, task_end) # this is a slice object, allowing us to access the specific thingy
    
    data = {}
    data['taskGrainSize'] = task_end - task_start

    data['images'] = fullcube[task_start:task_end+1,:,:]
    
    return data

def worker_work(rank):
    # Function to define the work that the workers will do

    while True:
        # Send the overseer the signal that the worker is ready
        comm.send(None, dest=0, tag=tags.READY)
        # Receive the data with the index of the task, the atmosphere parameters and/or the tag
        data_in = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
        tag = status.Get_tag()

        
        if tag == tags.START:
            # Recieve the chunk
            task_index = data_in['index'] # I think we need this? - for what though (to keep track of what succeeeded where)
            cube = data_in['images']
            delta_t = data_in['delta_t']
            pixelsize = data_in['pixelsize']
            sigma = data_in['sigma']
            task_size = data_in['taskGrainSize']
            vel_x = []
            vel_y = []
            vm= []

            for t in range(1,task_size+1): # Now, task size is not one, probably a good choice
                
                vx, vy, m = pyflct.flct(cube[t-1], cube[t], delta_t, pixelsize, sigma, quiet=True)
                vel_x.append(vx)
                vel_y.append(vy)
                vm.append(m)

            success = 1
            # Send the computed data
            data_out =  {'index': task_index, 'success': success, 'vel_x': vel_x, 'vel_y' : vel_y, 'mask' : vm}
            comm.send(data_out, dest=0, tag=tags.DONE)

        # If the tag is exit break the loop and kill the worker and send the EXIT tag to overseer
        elif tag == tags.EXIT:
            break

    comm.send(None, dest=0, tag=tags.EXIT)

def overseer_work(cube, delta_t, pixelsize, sigma, task_grain_size=1):
    """ Function to define the work to do by the overseer """

    # Index of the task to keep track of each job
    task_index = 0
    num_workers = size - 1
    closed_workers = 0

    data_size = 0 # Let's figure out what this is - total number of pixels?
    num_tasks = 0 # And this is data_size // 16? 
    file_idx_for_task = [] # does this have sth to do with reading from file?
    task_start_idx = [] # no idea
    task_writeback_range = [] # no idea
    
    cdf_size = cube.shape[0]-1
    print("info::overseer::cdf_size = ", cdf_size)

    num_cdf_tasks = int(np.ceil(cdf_size / task_grain_size)) # number of tasks = roundedup number of pixels / grain
    
    task_start_idx.extend(range(0, cdf_size, task_grain_size))
    
    task_writeback_range.extend([slice(data_size + i*task_grain_size, min(data_size + (i+1)*task_grain_size,
        data_size + cdf_size)) for i in range(num_cdf_tasks)])
    
    data_size = cdf_size
    num_tasks = num_cdf_tasks

    # Define the lists that will store the data of each feature-label pair - I hate lists, can I work with 
    # numpy array 
    vel_x = [None] * data_size
    vel_y = [None] * data_size
    
    success = True
    task_status = [0] * num_tasks

    with tqdm(total=num_tasks, ncols=110) as progress_bar:
        
        # While we don't have more closed workers than total workers keep looping
        while closed_workers < num_workers:
            
            data_in = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
            source = status.Get_source()
            tag = status.Get_tag()

            if tag == tags.READY:
                try:
                    task_index = task_status.index(0)
                    
                    # Slice out our task
                    data = slice_tasks(cube, task_start_idx[task_index], task_grain_size)
                    data['index'] = task_index
                    data['delta_t'] = delta_t
                    data['pixelsize'] = pixelsize
                    data['sigma'] = sigma

                    # send the data of the task and put the status to 1 (done)
                    comm.send(data, dest=source, tag=tags.START)
                    task_status[task_index] = 1

                # If error, or no work left, turn off the worker
                except:
                    comm.send(None, dest=source, tag=tags.EXIT)

            # If the tag is Done, receive the status, the index and all the data
            # and update the progress bar
            elif tag == tags.DONE:
                success = data_in['success']
                task_index = data_in['index']

                if not success:
                    task_status[task_index] = 0
                    print(f"Task: {task_index} failed")
                else:
                    task_writeback = task_writeback_range[task_index]
                    vel_x[task_writeback] = data_in['vel_x']
                    vel_y[task_writeback] = data_in['vel_y']
                    # We can also put mask somewhere - but we don't use it at the moment
                    progress_bar.update(1)

            # if the worker has the exit tag mark it as closed.
            elif tag == tags.EXIT:
                #print(" * Overseer : worker {0} exited.".format(source))
                closed_workers += 1

    # Once finished, dump all the data
    vel_x = np.asarray(vel_x)
    vxhdu = fits.PrimaryHDU(vel_x)
    vyhdu = fits.ImageHDU(vel_y)
    to_output = fits.HDUList([vxhdu, vyhdu])
    to_output.writeto(sys.argv[1][:-5]+'_tracked.fits', overwrite=True)


# -----------------------------------------------------------------------------------

if (__name__ == '__main__'):

    # Initializations and preliminaries
    comm = MPI.COMM_WORLD   # get MPI communicator object
    size = comm.size        # total number of processes
    rank = comm.rank        # rank of this process
    status = MPI.Status()   # get MPI status object

    #print(f"Node {rank}/{size} active", flush=True)

    if rank == 0:

        # --------------------------------------------------------------------
        #cube = fits.open(sys.argv[1])[0].data
        delta_t = 10.0 * 3
        pixelsize = 16.0
        sigma = 100.0 / 1.665 / pixelsize

        path = '/mnt/c/Users/ivanz/OneDrive/Documents/Muram_ISSI_2D'
        cube = loaders.load_from_muram_slices(path, 0,150,2, 'Bz', 1.0)

        print("info::overseer::input size is: ", cube.shape)
        print("info::overseer::sigma in pixels: ", sigma)

        overseer_work(cube, delta_t, pixelsize, sigma, task_grain_size = 1)
    else:
        worker_work(rank)
        pass

    
