#!/bin/bash

#SBATCH --time=4:00:00
#SBATCH --mem=10g
#SBATCH --tmp=10g
#SBATCH --mail-type=ALL
#SBATCH --mail-user=menar060@umn.edu

###cloned from: https://github.com/VistaSohrab/TEfinder/tree/master
cd /home/hirschc1/menar060/programs/TEfinder/TEfinder/
module load conda
conda create -y -n TEfinder

source activate TEfinder
conda activate TEfinder
conda install -y -c bioconda picard=2.0.1
conda install -y -c bioconda bedtools=2.28.0
conda install -y -c bioconda samtools=1.3
