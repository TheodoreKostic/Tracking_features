Kod 2D_tracking_FLCT_calc_mpi.py je napisan tako da uzima novu verziju loaders koja izdvaja temperaturu:

`import loadersT as loaders`

tako da loadersT uzima T na nacin na koji si ti napravio za B<sub>z</sub>. Pokrenuo sam naredbom  `mpirun -n 10 python 2D_tracking_FLCT_calc_mpi.py pyFLCT_fwhm_1200_dt_30_T.fits`,
nakon cega sam u loadersT promenio test da koristi 4. stepen temperature, `test = np.copy(data[0][8,:,:]**4)`, pa pokrenuo `mpirun -n 10 python 2D_tracking_FLCT_calc_mpi.py pyFLCT_fwhm_1200_dt_30_TTTT.fits`, 
da bih sacuvao u dva zasebna fajla. U principu, kao sto smo radili i pre, nisam menjao formulu. Naravno -n 10 se moze zameniti vecim brojem. 
