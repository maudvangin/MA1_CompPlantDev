#!/bin/bash
#
#PBS -N unique_ids
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:15:00
#PBS -l vmem=4gb

python /scratch/gent/472/vsc47291/MA1_CompPlantDev/data/extract_AT_LJ.py