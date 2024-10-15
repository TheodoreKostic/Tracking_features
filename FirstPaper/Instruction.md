Kod 2D_tracking_FLCT_calc_mpi.py je namesten tako da je napisano:

`import loadersT as loaders`

tako da loadersT uzima Temp na nacin na koji si ti napravio za B<sub>z</sub>. Pokrenuo sam naredbom  `mpirun -n 10 python 2D_tracking_FLCT_calc_mpi.py pyFLCT_fwhm_1200_dt_30_T.fits`,
nakon cega sam u loadersT promenio test da koristi 4. stepen temperature, `test = np.copy(data[0][8,:,:]**4)`. I opet pokrenuo `mpirun -n 10 python 2D_tracking_FLCT_calc_mpi.py pyFLCT_fwhm_1200_dt_30_TTTT.fits`, 
da bih sacuvao u dva zasebna fajla.
