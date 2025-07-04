# Tracking_features
Various codes that are implementation of feature tracking; Data used comes from COBOL5D and MURAM simulations

> [!NOTE]
> Content will be added and/or updated on weakly (to daily) basis 😀

`29. 1. 2024.`

<p>Added the MURAM_exp.ipynb Jupyter notebook in initial stage of development.</p>

`30. 1. 2024.`

<p>Added the Tracking_h5.ipynb Jupyter notebook with purpose of checking the validity of data.</p>
<p>Updating MURAM_exp.ipynb with additional testing of polarisation and vertical component of magnetic field. Correlation checked.</p>
<p>Updated Tau.ipynb - added code regarding convolution of velocities and a gaussian; correlation between <b><i>filtered</i></b> velocities checked.</p>

`01. 2. 2024.`
<p>In Tau_ipynb added the visual representation of correlation between <b><i>filtered</i></b> velocities.</p>

`11. 2. 2024.`
<p>Tau_ipynb - fixed the convolution by using gaussian_filter function instead of convolve.</p>

`20. 2. 2024.`
<p>COBOL_TIME.ipynb added. Basic check up done. FLCT doesn't produce expected results...</p>
<p>COBOL_TIME.ipynb, eventhough crude needs to be run on SUPERAST.</p>

> [!IMPORTANT]
> Pearson's coefficient is very low at the moment. Advised to check alternative methods.

<p>
  Added extract.py and Extract_series.py as an expansion of functionality - a light python script that will be used in conjunction with 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/COBOL_TIME.ipynb">COBOL_TIME.ipynb</a>.
</p>

`23. 2. 2024.`
<p>
  Updated 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Extract_series.py">Extracted_series.py</a>
  with loop through all the files and determining correlation between FLCT velocities and velocities given in simulation.
</p>

`25. 2. 2024.`
<p>
  Extracted_series.py updated: added the <b>gaussian_filter</b> convolution before checking the value of Pearson's coefficient. <br>
  COBOL_TIME.ipynb updated: using the data stored in fits file (look  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/    Extract_series.py">Extracted_series.py</a>) determined that the correlation between the velocities from simulation and velocities that FLCT calculated is low.
  The depth is constant and the moments in time series which were used for comparison were arbitrarily chosen.<br>
  Depth or layer at which we are "looking at" can be changed in script and we will need to find the one with best results.
</p>

`27. 2. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Extract_basic.py">Extracted_basic.py</a>,
  a python script that writes T, B<sub>z</sub>, V<sub>x</sub>, V<sub>y</sub> V<sub>z</sub> to a fits file and then compares these V<sub>x</sub> and V<sub>y</sub> averaged between every
  two adjacent timestamps in our timeseries and V<sub>x</sub> and V<sub>y</sub> derived using FLCT on T (temperature) and B<sub>z</sub> (z-component of magnetic field).
  The result are two scatter plots that compare said velocities in order to visualise the correlation or lack thereof.
</p>

`07. 3. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Histogram.py">Histogram.py</a>,
  a python script that makes use of fits file and plots histograms of x component velocity of average velocity from simulation
  and velocities derived from the said simulation using FLCT on temperature and z component of magnetic field. Will be updated 
  to do the same using y components, as well as to study statistics more closely.
</p>

`15. 3. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Velocity_diff.py">Velocity_diff.py</a>,
  a python script that makes uses fits file to import V<sub>x</sub>, V<sub>y</sub>, T and B<sub>z</sub> values for the specific layer of Sun's photosphere in order
  to compare those simulation values with the FLCT-derived values for horizontal velocities and calculates the correlation
  between them.
  Also does the same type of comparison after filtering velocities using gaussian filter.
</p>

`21. 3. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Write_to_fits.py">Write_to_fits.py</a>, which
  writes T, V<sub>x</sub>, V<sub>y</sub>, V<sub>z</sub>, B<sub>z</sub> and bolometric magnitude into a fits file,
  <br>
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FLCT_calc.py">FLCT_calc.py</a> 
  which uses FLCT algorithm in conjuction with T, B<sub>z</sub> and bolometric magnitude to calculate velocities
  and <br>
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Corr_calculation.py">Corr_calculation.py</a>, which
  compares aforementioned velocities with the ones from simulation.
</p>

`9. 4. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/synth/Muram_to_goodform.py">Muram_to_goodform.py</a>, a script that 
  gives two fits files as result. One contains the MuRAM data reshaped into suitable shape for synth function defined in minimal_synth_muram.py, while 
  the other reduces the size of test atmosphere another project (due to large CPU usage) and
  <br>
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/synth/minimal_synth_muram.py">minimal_synth_muram.py</a>,
  which is supposed to synthesise the spectrum using given z, T, V<sub>z</sub> and P<sub>gas</sub> contained in fits file, thus 
  giving intensity of spectral line that should be compared to known value in order to determine how valid our code is.
</p>

`17. 4. 2024.`
<p>
  Added 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/synth/Muram_1D.py">Muram_1D.py</a> as a fix for previously uploaded
  Muram_to_goodform.py (might be removed) which didn't account for all values of temperature and pressure correctly, thus neglecting several 
  parts of Sun's atmosphere in physical sense.
</p>

`29. 4. 2024.`
<p>
  Added several python scripts and a jupyter notebook in which parts of their codes are shown.
  <ol>
    <li>
       <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/ISSI_2D_tracking_write_data.py">ISSI_2D_tracking_write_data.py</a>
      This code checks how many slices are in user's directorium and takes the data in form of numpy arrays for needed physical paramters that are then written to new
      fits file.
    </li>
    <li>
       <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/ISSI_2D_FALC_calc.py">ISSI_2D_FALC_calc.py</a>
      In here the application of FLCT based on temperature can be found. The calculated velocities are then written to separate fits files for easier later usage.
    </li>
    <li>
      <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/ISSI_2D_corr_calc.py">ISSI_2D_corr_calc.py</a>
      Calculating correlation between V<sub>x</sub>, V<sub>y</sub> from simulation and V<sub>x</sub>, V<sub>y</sub> that FLCT gives back.
    </li>
    <li>
      <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Low_number_check.ipynb">Low_number_check.ipynb</a>
      Jupyter notebook which contains example of how these codes are used.
    </li>
  </ol> 
</p>

`14. 5. 2024.`
<p>
  The previously added scripts and notebook have been updated to include continuum intensity at 500nm as a new "windowing parameter".
</p>

`15. 5. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Example.ipynb">Example.ipynb</a> jupyter notebook
  that uses pyFLCT with I<sub>continuum</sub> as windowing parameter using cadence of 30 s, and FWHM = 1200, 2400 km.
</p>

`16. 5. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Degraded_data_QS.ipynb">Degraded_data_QS.ipynb</a> jupyter notebook
  that uses pyFLCT with degraded (Convolved with Airy disk of 1m telescope at 500 nm) I<sub>continuum</sub> as windowing parameter for different combinations of cadences and FWHMs. <br>
  Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Degraded_data_QS_testign.ipynb">Degraded_data_QS_testing.ipynb</a> jupyter notebook that is reserved for further testing
  of this, with Brian's input and advices. So far, it is safe to say that FWHM = 200 km doesn't really track the flows from the simulaton.
</p>

`27. 5. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Two_frames_check.ipynb">Two_frames_check.ipynb</a> jupyter notebook
  that will be used to represent the influence of values assinged to cadence and FWHM on the tracking algorithm of FLCT. <br>
  Minor changes to 2D_tracking_FLCT_calc_mpi.py.
</p>

`29. 5. 2024.`
<p>
  Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Miniexample.ipynb">Miniexample.ipynb</a>, jupyter notebook used to
  debbug discrepancy between two method of loading data - numpy.fromfile and read_slice from muram script. Both are used to open binary files, but the latter one is well-documented, while the
  first one is user-dependent, as in user has to manually test each array to determine which parameter is in question.
</p>

`4. 6. 2024.`
<p>
  Updated Miniexample.ipynb to show (visualise) flow fields as derived using (py)FLCT on the whole timeseries of slices at optical delpth $\tau=0.1$, where continuum intensity at 500 nm was used as windowing parameter. Furthermore, flow field of V<sub>x</sub> derived from FLCT is compared to flow field averaged V<sub>x</sub> that is loaded from simulation. The results so far show that some parts are correctly tracked while others aren't correlated.
</p>

`6. 6. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/MEAN_VEL.py">MEAN_VEL.py</a> python script that 
 writes V<sub>x</sub> and V<sub>y</sub> into fits file, as well as computes mean values and writes them in separate fits file. <br>
  Miniexample.ipynb - added function for temporal averaging of series; added comparison between FLCT V<sub>x</sub>, V<sub>y</sub> and filtered
  simulation V<sub>x</sub>, V<sub>y</sub> (gaussian_filter). <br>
  <b>CONCLUSION</b> - V<sub>xflct</sub> has high correlation with transposed V<sub>ysimfiltered</sub> and vice versa.
</p>

`13. 6. 2024.`
<p>
  Minor updates to Miniexample.ipynb.
</p>

`19. 6. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Np_fromfile_vs_read.ipynb">Np_fromfile_vs_read.ipynb</a> notebook in which we deduce
  how to compare V<sub>x</sub> and V<sub>y</sub> from simulation with ones derived by FCLT. It shows what and how to transpose before comparison takes place, as well as 
  how can variables be introduced so that x can be compared with x, y compared with y.
</p>

`26. 6. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/Meeting_pres.ipynb">Meeting_pres.ipynb</a>, notebook focused on
  establishing differences between velocities FLCT calculated for cadence of 30s and FWHM = {100, 300, 600, 1200}km. The said velocities have been averaged, and filter
  was applied to the ones that come directly from simulation in order to see if there is good correlation between pyFLCT and simulation; i.e if tracking works correctly.
  Furthermore, we have tried to see how size of apodizing window affects tracking while also searching for best $\sigma$ to use for <i>gaussian_filter</i> in order to get the
  maximum possible correlation.
</p>

`27. 6. 2024.`
<p>
 Minor changes to plots in Meeting_pres.ipynb.
</p>

`12. 7. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Synth_master/Synth_data_test.ipynb">Synth_data_test.ipynb</a>. It is 
  a notebook in which we test how FLCT behaves on synthetised spectra, i.e. on different wavelenghts and how it correlates with the ones from simulation.
</p>

`14. 7. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Synth_master/Synth_TAU(0.1, 1).ipynb">Synth_TAU(0.1, 1).ipynb  </a>. This is 
  a notebook in which we tested the correlation between FLCT velocities and  synthetised spectra at different $\lambda$, specifically at those close 
  to the line centre. The goal is to find at what $\tau$ can we recover flow using spectral lines.
</p>

`16. 7. 2024.`
<p>
Synth_TAU(0.1, 1).ipynb - Added comparison of FLCT velocities derived from synthetised spectra and FLCT velocities derived from simulation using intensity (cont) as
  windowing parameter.
</p>

`27. 7. 2024.`
<p>
Synth_TAU(0.1, 1).ipynb - Further comparisons done. Looking into correlation between intensities used for tracking.
</p>

`14. 8. 2024.`
<p>
Synth_TAU(0.1, 1).ipynb - RMS contrast for synthetised spectra and convolved synthetised spectra compared. 
  Comparison yields valid results.
</p>

`21. 8. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Synth_master/Convolved.ipynb">Convolved.ipynb</a> and
   <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Synth_master/Spektralna_linija.ipynb">Spektralna_linija.ipynb</a>. First one
     shows various tests applied to convovled synthetised spectra, while the latter is focused on correlation between FLCT velocities derived
     from synthetised spectra and simulation velocities at different values of $\log{\tau}$.
</p>

`13. 10. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Paper.ipynb">Paper.ipynb</a> notebook in which we 
  compare how continuum intensity (I<sub>cont</sub>), temperature (T) and T<sup>4</sup> differ in behaviour when taken to be
  windowing parameter. After that, we compute correlation between velocities derived using said parameter and simulation velocities.
</p>

`18. 10. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Wvls.ipynb">Wvls.ipynb</a>, a notebook that will be
  used to compare velocities FLCT derived using continuum intensity at 500 nm and velocities FLCT derived from spectra Lightweaver synthetised
  using different wavelenghts (and spectral line).
</p>

`18. 10. 2024.`
<p>
 Wvls.ipynb updated, intensity at more wavelenghts analysed and compared to continuum intensity at 500 nm from simulation.
</p>

`23. 10. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Wvls600.ipynb">Wvls600.ipynb</a>, a notebook that will be
  used to compare velocities FLCT derived using continuum intensity at 500 nm and velocities FLCT derived from spectra Lightweaver synthetised
  using different wavelenghts, but using FWHM of 600 km (+ some plotting).
</p>

`25. 10. 2024.`
<p>
 Wvls600.ipynb updated, intensity at more wavelenghts analysed and compared to continuum intensity at 500 nm from simulation. Plotted I<sub>LW</sub>
  and I<sub>cont500</sub>, both used for tracking. Preliminary results show that intensity at most of $\lambda$-s can be used equally as the one 
  from simulation.
</p>

`5. 11. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/TimeAvg.ipynb">TimeAvg.ipynb</a>, where
  we shall store plots, calculation of correlation coefficients and test how time averaging impacts the correlation. 
</p>

`13. 11. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/100_fits_test.ipynb">100_fits_test.ipynb</a>. It features
  comparison of FLCT velocities that result from tracking on Lightweaver synthetised intensity at 500 nm, on MURaM simulated continuum intensity and 
  on MURaM simulated continuum intensity when timestep between two adjacent snapshots is increased. At the moment, it seems an error has occured during
  tracking on synthetised spectrum.
</p>

`03. 12. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Checkup_timeavg.ipynb">Checkup_timeavg.ipynb</a>. Analysis of how
  choice of cadence and later choice of FWHM for Gaussian with which we convolve temporaly averaged velocities impacts the correlation between velocities with cadence 10 s,
  and velocities with cadence {20, 30, 40, 50, 60}s for 3 cases - FWHM = {300, 600, 1200} km.
</p>

`12. 12. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Separate.ipynb">Separate.ipynb</a>. 
  Tracked first pair and fourth pair of LW series at 500 nm and compared them to first and fourth element of all velocities that
  result from tracking MURaM intensity using FWHM = 600 km and cadence = 30 s.
</p>

`20. 12. 2024.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Lightweaver_31steps.ipynb">Lightweaver_31steps.ipynb</a>. 
  Comparison of MURaM simulation velocities, FLCT velocities that result from tracking Lightweaver intensity at 500nm and FLCT velocities that
  result from tracking MURaM intensity at 500 nm. Tracking Lightweaver intensity proves to be difficult.
</p>

`28. 12. 2024.`
<p>
  Updated 31 steps notebook. Analysed the velocities tracked at 3 different wavelengths that correspond to Section 3.2.
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/I_min_map.py">I_min_map.py</a> and 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/I_minimum_tracking">I_minimum_tracking.py</a>. These
  scripts are meant to locate wavelength at which intensity reaches minimal value, take those intensity maps and write them to 
  new files on which tracking will be possible.
</p>

`05. 01. 2025.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/FixedWavelength.ipynb">FixedWavelenth.ipynb</a> that 
  makes use of results from previosly added python scripts for fixed wavelength tracking. Right now, only FWHM = 600 km have been obtained. FWHM = 300 km
  is work in progress.
</p>

`11. 01. 2025.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Temp_and_Bz_vs_SIM.ipynb">Temp_and_Bz_vs_SIM.ipynb</a> that 
  deals with comparison of FLCT FWHM = 600 km, cadence = 10 s results from B<sub>z</sub> and MURaM simulation velocities at $\log\tau = \{-1, -2, -3\}$. The files 
  that result from applying FLCT on Temperature at these $\tau$ values will be added later.
</p>

`12. 01. 2025.`
<p>
 Temp_and_Bz_vs_SIM.ipynb updated. <br> 
  Comparison of FLCT FWHM = 600 km, cadence = 10 s results from Temperature and MURaM simulation velocities at $\log\tau = \{-1, -2, -3\}$ added.
</p>

`14. 01. 2025.`
<p>
 Temp_and_Bz_vs_SIM.ipynb updated. <br> 
  Comparison of FLCT FWHM = 600 km, cadence = 10 s results from Temperature and MURaM simulation velocities at $\log\tau = 0$ added, as
  well as comparison of FLCT B<sub>z</sub> and MURaM simulation velocities at $\log\tau = -4$.
</p>

`15. 01. 2025.`
<p>
 Temp_and_Bz_vs_SIM.ipynb updated. <br> 
  Comparison of FLCT FWHM = 600 km, cadence = 10 s results from Temperature and Intensity at 500 nm, and MURaM velocities
  at $\log\tau = 0$ done. Conclusion is that intensity is better choice as tracking parameter due to artefacts that can
  be seen in temperature.
</p>

`24. 01. 2025.`
<p>
 TimeAvg.ipynb notebook updated with results for tracking B<sub>z</sub> at $\log\tau = 0$ for dt = 10 s.
</p>

`31. 01. 2025.`
<p>
 Added <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Planck_vs_Bz.ipynb">Planck_vs_Bz.ipynb</a> that 
  deals with comparison of FLCT FWHM = 600 km, cadence = 30 s results from B<sub>z</sub> and MURaM simulation velocities at $\log\tau = \{-1, -2, -3\}$. 
  Comparison of FLCT FWHM = 600 km, cadence = 30 s results from Planck's function and MURaM simulation velocities at $\log\tau = \{-1, -2, -3\}$ used instead
  of ones that result from tracking Temperature because B<sub>$\lambda$</sub> more closely resembles "Radiation Intensity" - what we would get by tracking
  intensity.
</p>

`18. 02. 2025.`
<p>
  Comparison of FLCT FWHM = {300, 600}km, cadence = 30 s results from B<sub>z</sub> and Temperature vs. MURaM simulation velocities at $\log\tau = \{-1, -2, -3. -4\}$.
  We conclude that B<sub>z</sub> is much better choice than temperature, because B<sub>z</sub> largely changes due to an advection process, while $T$ experinces strong 
  contributions due to radiative transport.
</p>

`27. 02. 2025.`
<p>
  Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Synth_snapi.ipynb">Synth_snapi.ipynb</a> in which
  testing and visualization of synthesized data (spectral lines) will be done.
</p>

`28. 02. 2025.`
<p>
 Synth_snapi updated with comparison of ME inversion B<sub>z</sub>-s for Fe I 525.0 nm and Mg I b2 517.2 nm with B<sub>z</sub>-s 
  at $\log\tau = \{0, -1, -2, -3\}$.
</p>

`06. 03. 2025.`
<p>
  Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/ISSI_Flow_tracking/FLCT_Thresh.ipynb">FLCT_Thresh.ipynb</a>.
  Here we test the effect threshold has on resulting horizontal velocities in FLCT when B<sub>z</sub> is tracking parameter. Two chosen values are 50 Gauss and 100 Gauss
  and correlation with MURaM V<sub>x</sub> and V<sub>y</sub> is given for both. Analysis suggests that inculding threshold (excluding pixels below threshold values in FLCT
  calculation) actually descreases correlation with original velocities. 
</p>

`11. 03. 2025.`
<p>
  Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/ME_Bz_track.py">ME_Bz_track.py</a>.
  This is a short script for tracking Bz inferred using ME inversion of Fe I and Mg I b2 spectral lines.
</p>

`12. 03. 2025.`
<p>
  Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/MilneEddington_Bz_tracking.ipynb">MilneEddington_Bz_tracking.ipynb</a>.
  Notebook in which we visualize tracking results (from Bz inferred using ME inversion of Fe I and Mg I b2 spectral lines).
</p>

`19. 03. 2025.`
<p>
  Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/WFA_MgIb2.ipynb">WFA_MgIb2.ipynb</a>.
  Notebook in which we visualize tracking results from Bz inferred in weak-field approximation applied to Mg I b2 spectral line.
</p>

`27. 03. 2025.`
<p>
  Various updates with goal of improving visual representation of results. Trying new statistic tests.
</p>

`02. 04. 2025.`
<p>
 Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Final_plot_table.ipynb">Final_plot_table.ipynb</a>.
  Notebook in which we visualize tracking results from Bz inferred in weak-field approximation applied to Mg I b2 spectral line and
  Bz inferred using ME inversion of Fe I, all at one place.
</p>

`06. 04. 2025.`
<p>
  A few updates regarding curl calculation in python. Also added .png-s.
</p>


`11. 04. 2025.`
<p>
  A lot of minor visual changes to plots, labels and their sizes in some notebooks for clarity. 
</p>

`16. 04. 2025.`
<p>
 Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Appendix.ipynb">Appendix.ipynb</a>,
  where all work related to LOS velocity will be stored.
</p>

`26. 05. 2025.`
<p>
  Final_plot_table notebook updated:
  <ul>
    <li>
      Added functions that determine divergence and vorticity of flows
    </li>
    <li>
      Calculated divergence and vorticity from tracked velocities and compared to simulations
    </li>
    <li>
      Plotted those fields
    </li>
    <li>
      Determined the power of vorticity and power of divergence - their difference is negative; what this implies remains to be determined 
    </li>
  </ul>
</p>

`19. 06. 2025.`
<p>
 Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/FirstPaper/Power_curl.ipynb">Power_curl.ipynb</a>,
  where sum(|div($v$)|<sup>2</sup>)/area and sum(|curl($v$)|<sup>2</sup>)/area are calculated. Correlation between div. of ground-truth flows (MURaM velocities) and 
  div. of FLCT-inferred is significantly better if FLCT velocity field is smoothed before computing its divergence.
</p>

`30. 06. 2025.`
<p>
 Uploaded <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/Video.ipynb">Video.ipynb</a>,
  where we use time-series of MURaM velocities and ME (or WFA) inversion $B_z$ from which FLCT infers velocities to
  create a short video (time-lapse).
</p>
