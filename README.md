# Membrane mediated mechanical stimuli produces distinct active states in the AT1 receptor

This data/instructions acompany the folowing manuscript: <br>

**Title**: Membrane mediated mechanical stimuli produces distinct active states in the AT1 receptor.<br>

**Authors**:Bharat Poudel, Rajitha Rajeshwar T., Juan Vanegas <br>

**pre-print**: https://www.researchsquare.com/article/rs-2106113/v1 <br>

**Datas and script for the figure:**

``` Acyl_chain_length/acyl_chain_length.py ```  has the script for comparing three  membrane of different acyl length, DMPC, POPC and SOPC. It corresponds to the Fig 1. <br> 


```Surface_Tension/st.py ``` has the script for plotting the average distance of descriptor of last 200 nanoseconds. We have used the system with SOPC ranging from 0 to 20 mN/m in the interval of 5mN/m. It corresponds to the Fig 2. <br>


```SOPC_SOPE/sope_sopc.py ```  has script for plotting the time evolution of different descriptor of pure SOPC membrane and SOPC:SOPE membrane and it corresponds to teh Fig 3. <br> 


```Surface_Tension/thickness.py ``` has the scripts for plotting bilayer thickness for different systems. It corresponds to the Fig 4. <br> 


```agonist_nanobody/time_evolution_different_system.py ``` has the script for plotting the time evolution of different systems, AT1 receptor with S1I8, AT1 receptor with AngII, AT1 receptor with Nanobody bound and AT1 receptor with S1I8 and Nanobody bound. It corresponds to the Fig 5. <br> 




```Surface_Tension/distinct_activation.py  ``` has the script for plotting change in inter-helical distances between active and inactive states. It corresponds to the FIGURE 6. <br> 




``` FES/fes_4colv2_for_paper.py ``` has the script for plotting free energy estimation of AT1 receptor under various condition. It corresponds to the Fig 7. <br> 






```supplemantary_figure/NPxxY/NPxxY.py``` -contains script of analyzing the interaction of Y302 (OH) to Y215 (OH) for all the system simulated. It corresponds to the Fig S1 on supplementary section. <br> 




```supplemantary_figure/H8_mutation/h8.py ``` has the script for plotting the effect of F309P and F313P on mechanical activation/inactivation. It corresponds to the Fig S2 on supplementary section. <br> 

```supplementary_figure/POPC_with_ST/popc_thickness.py ``` -contains the script for analyzing the POPC bilayer thickness under surface tension of 0, 5mN/m and 10mN/m compared with SOPC membrane with various surface tension. It corresponds to the Fig S3 on on supplememtary section. <br> 


```supplementary_figure/POPC_with_ST/popc_st.py``` -contains the script for analyzing the system with POPC with Surface tension 5mN/m and 10mN/m. It corresponds to the Fig S4 on supplementary section. <br> 


```supplementay_figure/energy_convergence/rmsd_fes.py``` has the script for checking the convergence of free energy simulation. It corresponds to the Fig S5 on supplementary sections. <br> 

```supplementary_figure/energy_convergence/fes_supp.py ``` has the script for plotting free energy estimation of AT1 receptor with nanoboy and S1I8 bound and AT1 receptor with nanobody bound. It corresponds to the Fig S6 on supplementary sections. <br> 


**Example of free energy calculation using the Locally Distributed Tesion (LDT) collective variable**

**Compiling and installing the PLUMED-patched version of GROMACS** <br>

The source code for GROMACS can be downloaded from https://manual.gromacs.org/2019.6/download.html. PLUMED can be downloaded from https://www.plumed.org/download. The particular version of PLUMED used for this study can be found in the following git repository: https://github.com/vanegasj/plumed2.

Installation instruction for compiling and installing PLUMED can be found here:https://www.plumed.org/doc-v2.7/user-doc/html/_installation.html.  This page also contains instruction on how to patch GROMACS with PLUMED. Once the GROMACS code has been patched, you can proceed with the normal compilation and installation of GROMACS

**Free energy of AT1 receptor with partial agonist (S1I8)** <br>
The folder S1I8 contains contains the necessary files to reproduce the well-tempered metadynamics free energy calculation shown in FIGURE 7c of the manuscript. The file run_metad_sim.sh contains the GROMACS command to launch the WT-metadynamics run with the 8 walkers. The folder S1I8/reweight contains the combined colvar files and plumed input files to perform the re-weighting and produce the 2D FES data. The script S1I8/reweight/calc_fes.sh will execute the combining procedure and perform the re-weighting using plumed.






