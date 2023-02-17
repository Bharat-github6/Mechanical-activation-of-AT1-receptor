#!/bin/bash
#SBATCH --job-name="AT1R/-/Ag"
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --gpus=4
#SBATCH --mem=48G
#SBATCH --no-requeue
#SBATCH --account=uvm112
#SBATCH --export=ALL
#SBATCH -t 48:00:00



module load gromacs/2021-plumed-gpu



dirs=''
for i in `seq 0 7`;
do
dirs="$dirs"M`printf "%03d" $i`" "
done
mpiexec -n 8 -npernode 8 mdrun_mpi_PL -deffnm topol -cpi  -plumed plumed.dat -multidir $dirs
