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
 writes V<sub>x</sub> and V<sub>y</sub> into fits file, as well as computes mean values and writes them in separate fits file.
</p>
