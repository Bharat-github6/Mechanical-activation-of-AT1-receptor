# Membrane mediated mechanical stimuli produces distinct active states in the AT1 receptor

This data/instructions acompany the folowing manuscript: <br>

**Title**: Membrane mediated mechanical stimuli produces distinct active states in the AT1 receptor.<br>

**Authors**:Bharat Poudel, Rajitha Rajeshwar T., Juan Vanegas <br>

**pre-print**: https://www.researchsquare.com/article/rs-2106113/v1 <br>

**Data and scripts for figures in the main text:**

**Figure 1:** ```Acyl_chain_length/acyl_chain_length.py``` - comparison of three membranes of different acyl cahin length: DMPC, POPC and SOPC.<br> 

**Figure 2:** ```Surface_Tension/st.py``` - average distances over the last 200 nanoseconds for SOPC systems under tension ranging from 0 to 20 mN/m in intervals of 5mN/m.<br>

**Figure 3:** ```Surface_Tension/thickness.py``` - bilayer thickness for different systems.<br> 

**Figure 4:** ```SOPC_SOPE/sope_sopc.py``` - time evolution of distances for SOPC and SOPC:SOPE membranes.<br> 

**Figure 5:** ```agonist_nanobody/time_evolution_different_system.py``` time evolution of agonist and/or nanobody bound systems.<br> 

**Figure 6:** ```Surface_Tension/distinct_activation.py``` - change in intra-helical distances between active and inactive states.<br> 

**Figure 7:** ```FES/fes_4colv2_for_paper.py``` - free energy estimation of AT1 receptor under various conditions.<br> 

**Data and scripts for figures in the Supplementary Material:**

**Figure S1:** ```supplemantary_figures/NPxxY/NPxxY.py``` - distance between Y302(OH) and Y215(OH) for WT systems.<br> 

**Figure S2:** ```supplementary_figures/POPC_with_ST/popc_st.py``` - distances for POPC systems with surface tensions of 5 mN/m and 10 mN/m.<br> 

**Figure S3:** ```supplementary_figures/POPC_with_ST/popc_thickness.py``` - POPC bilayer thickness under surface tensions of 0, 5 mN/m, and 10 mN/m compared to that of SOPC under various surface tensions.<br> 

**Figure S4:** ```supplemantary_figures/H8_mutation/h8.py``` - stability of active state for double mutant F309P/F313P.<br> 

**Figure S5:** ```supplemantary_figures/H8_mutation/insertion_depth.py``` - insertion depth of H8 for WT and double mutant F309P/F313P for various membranes.<br>

**Figure S6:** ```supplemantary_figures/H8_mutation/npxxy_h8.py``` - distance between Y302(OH) and Y215(OH) for WT and double mutant F309P/F313P for various membranes.<br>

**Figure S7:** ```supplementay_figure/energy_convergence/rmsd_fes.py``` root-mean-squared-deviation as a function of total simulation time for the free energy surfaces in the main text.<br>

**Figure S8:** ```supplementary_figure/energy_convergence/fes_supp.py``` free energy estimation of AT1 receptor with both S1I8 and nanoboy bound, as well as AT1 receptor with nanobody bound.<br> 

**Example of free energy calculation using the Locally Distributed Tesion (LDT) collective variable**

**Compiling and installing the PLUMED-patched version of GROMACS** <br>

The source code for GROMACS can be downloaded from https://manual.gromacs.org/2019.6/download.html. PLUMED can be downloaded from https://www.plumed.org/download. The particular version of PLUMED used for this study can be found in the following git repository: https://github.com/vanegasj/plumed2.

Installation instruction for compiling and installing PLUMED can be found here:https://www.plumed.org/doc-v2.7/user-doc/html/_installation.html.  This page also contains instruction on how to patch GROMACS with PLUMED. Once the GROMACS code has been patched, you can proceed with the normal compilation and installation of GROMACS

**Free energy of AT1 receptor with partial agonist (S1I8)** <br>
The folder ```S1I8_example_fes``` contains contains the necessary files to reproduce the well-tempered metadynamics free energy calculation shown in Figure 7c of the manuscript. The file ```run_metad_sim.sh``` contains the GROMACS command to launch the WT-metadynamics run with the 8 walkers. The folder S1I8/reweight contains the combined colvar files and plumed input files to perform the re-weighting and produce the 2D FES data. The script ```S1I8_example_fes/reweight/calc_fes.sh``` will execute the combining procedure and perform the re-weighting using plumed.






