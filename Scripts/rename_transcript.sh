#!/bin/bash
#
#PBS -N confint
#PBS -l nodes=1:ppn=1
#PBS -l walltime=01:00:00
#PBS -l vmem=6gb

for f in *fa ; do python "/scratch/gent/472/vsc47291/MA1_CompPlantDev/OrthoFinder/tools/primary_transcript.py" "/scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes" ; done

