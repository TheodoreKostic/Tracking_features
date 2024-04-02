## Bare-bones 1.5D synthesis using lightweaver and MPI
## Also a chance for me to learn MPI in python 

import lightweaver as lw 

from lightweaver.fal import Falc82 # essentially not needed 

from lightweaver.rh_atoms import H_6_atom, C_atom, O_atom, Si_atom, Al_atom, \
CaII_atom, Fe_atom, He_9_atom, MgII_atom, N_atom, NaI_fine_atom, S_atom # Specific atomic models that cover most of 
                                                                        # of the spectral lines studied in solar physccs 

import matplotlib.pyplot as plt
import time
import numpy as np
import sys

### First a minimal synthesis function:

def synth(atmos, conserve, prd, stokes, wave, mu, actives):
    
    '''
    Synthesize a spectral region with given parameters:
    
    Parameters
    ----------
    atmos : lw.Atmosphere - The atmospheric model in which to synthesise the line.
    
    conserve : bool - Whether to start from LTE electron density and conserve charge, or simply use from the electron density present in the atmospheric model.

    prd: bool - whether to use prd or no, most of the time it's no 

    stokes: bool - whether to synth all 4 Stokes parameters or I only - for tracking we start with I only
    
    wave : np.ndarray Array of wavelengths over which to resynthesise the final line profile

    mu : mu angle, gonna use 1.0 most of the times 

    actives: list of active species to synthesize

    Returns
    -------
    ctx : lw.Context -The Context object that was used to compute the equilibrium populations -> Gonna not return this
    
    Iwave : np.ndarray - The intensity at given mu and wave    '''
    
    # Configure the atmospheric angular quadrature - only matters for NLTE. Gonna use 3 for faster calc
    atmos.quadrature(3)
    
    # Configure the set of atomic models to use. Contrary to SNAPI you have to explicitly specify all species
    # Annoying, but since you have all the atoms in the file - that is fine.
    aSet = lw.RadiativeSet([H_6_atom(), C_atom(), O_atom(), Si_atom(), Al_atom(), CaII_atom(), Fe_atom(), He_9_atom(), MgII_atom(), N_atom(), NaI_fine_atom(), S_atom()])
    
    # Set actives to the ones you have inputted.
    aSet.set_active(actives)
    
    # Compute the necessary wavelength dependent information (SpectrumConfiguration).
    spect = aSet.compute_wavelength_grid()

    # Calculate electron density in lte, we are never using the electron density from the model
    eqPops = aSet.iterate_lte_ne_eq_pops(atmos)

    # Configure the Context which holds the state of the simulation for the  backend, and provides 
    # the python interface to the backend.
    # Feel free to increase Nthreads to increase the number of threads the program will use.
    # I would always stick to Nthreads = 1 as we are looking to mpi this one
    
    ctx = lw.Context(atmos, spect, eqPops, conserveCharge=conserve, Nthreads=1)
    
    # Iterate the Context to convergence (using the iteration function now
 	# provided by Lightweaver). Go test this one in order to calculate stuff in LTE!
    
    lw.iterate_ctx_se(ctx, prd=prd)
    
    # Update the background populations based on the converged solution and
    # compute the final intensity for mu=1 on the provided wavelength grid.
    eqPops.update_lte_atoms_Hmin_pops(atmos)
    
    # Calculate the (stokes) spectru, at the provided wavegrid at the specified mu
    Iwave = ctx.compute_rays(wave, [mu], stokes=stokes) 

    # We will want to return some populations or so, at some point (Firtez pipeline)
    #return ctx, Iwave

    # For now we are only returning the intensity:
    if (stokes == False):
    	Iwave = Iwave.reshape(1,-1)
    
    return Iwave

# Actually test if this works:

# Here we test reading 1D atmosphere for a txt file:

atmos_in = np.loadtxt(sys.argv[1], unpack=True, skiprows=1)

z = atmos_in[1] / 1E2
T = atmos_in[2]
vz = np.zeros(len(z))
vturb = atmos_in[8] / 1E2
pgas = atmos_in[3] * 10.0

atmos= lw.Atmosphere.make_1d(lw.atmosphere.ScaleType.Geometric, np.copy(z), np.copy(T), np.copy(vz), np.copy(vturb), Pgas=pgas)

wave = np.linspace(588.8, 589.8, 1001)
I = synth(atmos, conserve=False, prd=False, stokes=False, wave=wave*1.000293, mu=1.0, actives='Na')
