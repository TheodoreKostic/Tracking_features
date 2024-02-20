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
> Pearson's coefficient is very low at the moment. Advised to check alternative metods.

<p>
  Added extract.py and Extract_series.py as an expansion of functionality - a light python script that will be used in conjunction with 
  <a href = "https://github.com/TheodoreKostic/Tracking_features/blob/main/COBOL_TIME.ipynb">COBOL_TIME.ipynb</a>.
</p>
