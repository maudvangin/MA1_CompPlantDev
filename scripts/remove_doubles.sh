#!/bin/bash
#
#PBS -N unique_ids
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:15:00
#PBS -l vmem=4gb

for f in /scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes/*.fa; do python /scratch/gent/472/vsc47291/MA1_CompPlantDev/OrthoFinder/tools/primary_transcript.py $f ; done
