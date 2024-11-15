#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=250gb
#SBATCH -t 96:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=menar060@umn.edu
#SBATCH -o M_xaa_index.out
#SBATCH -e M_xaa_index.err
#SBATCH --tmp=100gb


cd /home/hirschc1/menar060/programs/mcclintock/mcclintock/
CONDA_BASE=$(conda info --base)
source ${CONDA_BASE}/etc/profile.d/conda.sh
conda activate mcclintock
#source activate mcclintock

python3 mcclintock.py \
    -r maize/B73Oh43/B73_chrs.fa \
    -c maize/B73Oh43/fmt_pan_TE_lib.fasta \
    -g maize/B73Oh43/filtered_B73.EDTA.TEanno.gff3 \
    -t maize/B73Oh43/final_taxonomy_B73.tsv \
    -1 maize/B73Oh43/L001_paired_out_1.fq \
    -2 maize/B73Oh43/L001_paired_out_2.fq \
    -p 16 \
    -m temp2 \
    -o /home/hirschc1/menar060/programs/mcclintock/mcclintock/maizetest1/
