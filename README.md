# Membrane mediated mechanical stimuli produces distinct active states in the AT1 receptor

These data/instructions acompany the folowing manuscript: <br>

**Title**: Membrane mediated mechanical stimuli produces distinct active-like states in the AT1 receptor.<br>

**Authors**:Bharat Poudel (University of Vermont), Rajitha Rajeshwar T. (University of Vermont), Juan Vanegas (Oregon State University)<br>

**Pre-print**: https://www.researchsquare.com/article/rs-2106113/v1 <br>

## Data and plotting scripts for figures in the main text and supplementary information

Each folder contains the input data generated from the MD simulations, the python script used to generate the corresponding plot, and the final png image. Each data file has a header that describes each column in the file. 

Statistical analyses including mean, standard deviation, quartiles, etc. calculated within the python scripts based on the input data files.

## Initial and final configurations of MD simulations

The folder `MD_configurations` contains the initial and final configurations for all the simulations presented in the study. The files are organized into folders labeled System_\#. The system description is shown in the table below and also inside a README.md file in each folder.

| System                           | Total Nr. of Atoms | Box dimensions (nm) | Nr. of Lipids | Nr. of Waters | Cl- | Na+ |
|----------------------------------|--------------------|---------------------|---------------|---------------|-----|-----|
| (1) DMPC + AT1R                  | 99,132             | 10x10x11.8          | 300           | 27,388        | 13  |  0  |
| (2) POPC + AT1R                  | 112,330            | 10.4x0.4x13.5       | 304           | 31,068        | 13  |  0  |
| (3) SOPC + AT1R                  | 106,560            | 10.4x10.4x13.5      | 298           | 29,050        | 13  |  0  |
| (4) SOPC:SOPE + AT1R             | 90,885             | 9.5x9.5x13          | 300           | 23,789        | 13  |  0  |
| (5) SOPC + AT1R + AngII          | 106,662            | 10.4x10.4x13.5      | 298           | 29,050        | 13  |  0  |
| (6) SOPC + AT1R + S1I8           | 106,651            | 10.4x10.4x13.5      | 298           | 29,050        | 14  |  0  |
| (7) SOPC + AT1R + S1I8 +Nb       | 107,821            | 10.4x10.4x13.5      | 298           | 29,056        | 8   |  0  |
| (8) SOPC + AT1R + Nb             | 107,912            | 10.4x10.4x13.5      | 298           | 29,056        | 7   |  0  |
| (9) POPC + F309P/313P AT1R       | 82,319             | 10.4x10.4x10        | 304           | 21,071        | 13  |  0  |
| (10) SOPC + F309P/313P AT1R      | 83,329             | 10.5x10.5x11        | 298           | 21,313        | 13  |  0  |
| (11) SOPC:SOPE + F309P/313P AT1R | 72,427             | 9.5x9.5x10          | 300           | 17,643        | 13  |  0  |
| (12) POPC + AT1R                 | 49,146             | 6.4x6.4x11.6        | 100           | 10,154        | 39  |  26 |
| (13) SOPC + AT1R                 | 52,021             | 6.4x6.4x12.5        | 100           | 10,911        | 41  |  28 |
| (14) SOPC + AT1R + AngII         | 48,274             | 6.7x6.7x11.5        | 100           | 9,616         | 37  |  24 |

## Example of free energy calculation using the Locally Distributed Tesion (LDT) collective variable

**Compiling and installing the PLUMED-patched version of GROMACS** <br>

The source code for GROMACS can be downloaded from https://manual.gromacs.org/2019.6/download.html. PLUMED can be downloaded from https://www.plumed.org/download. The particular version of PLUMED used for this study can be found in the following git repository: https://github.com/vanegasj/plumed2.

Installation instructions for compiling and installing PLUMED can be found here: https://www.plumed.org/doc-v2.7/user-doc/html/_installation.html.  This page also contains instruction on how to patch GROMACS with PLUMED. Once the GROMACS code has been patched, you can proceed with the normal compilation and installation of GROMACS

**Free energy of AT1 receptor with partial agonist (S1I8)** <br>

The folder ```S1I8_example_fes``` contains contains the necessary files to reproduce the well-tempered metadynamics free energy calculation shown in Figure 7c of the manuscript. The file ```run_metad_sim.sh``` contains the GROMACS command to launch the WT-metadynamics run with the 8 walkers. The folder S1I8/reweight contains the combined colvar files and plumed input files to perform the re-weighting and produce the 2D FES data. The script ```S1I8_example_fes/reweight/calc_fes.sh``` will execute the combining procedure and perform the re-weighting using plumed.
