#!/bin/bash
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --account=uvm112
#SBATCH --export=ALL
#SBATCH --no-requeue
#SBATCH -t 10:00:00



module purge
module load slurm



#module load gromacs/2021-plumed-gpu
module load plumed/2.8

#sh cp.sh 
#for i in `seq 0 7`;
#do

#plumed driver --ixtc ../M00$i/topol.xtc --plumed plumed$i.dat --trajectory-stride 5
#done

sh combine_files.sh
sh combine_colvar.sh


cp ../M000/HILLS .
plumed --no-mpi driver --noatoms --plumed plumed_reweight.dat
