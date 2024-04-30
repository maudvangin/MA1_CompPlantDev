#!/bin/bash
#
#PBS -N orthofinder
#PBS -l nodes=1:ppn=4
#PBS -l walltime=16:00:00
#PBS -l vmem=8gb

module load OrthoFinder/2.5.5-foss-2023a 

orthofinder -f /scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes/primary_transcripts
