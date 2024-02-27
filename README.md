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

`1. 2. 2024.`
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
  a python script that writes T, B_z, V_x, V_y, V_z to a fits file and then compares these V_x and V_y averaged between every
  two adjacent timestamps in our timeseries and V_x and V_y derived using FLCT on T (temperature) and B_z (z-component of magnetic field).
  The result are two scatter plots that compare said velocities in order to visualise the correlation or lack thereof.
</p>
