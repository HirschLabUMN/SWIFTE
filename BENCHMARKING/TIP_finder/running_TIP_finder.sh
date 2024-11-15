#!/bin/bash

#SBATCH --time=96:00:00
#SBATCH --mem=1900g
#SBATCH -p ag2tb
#SBATCH -N 1
#SBATCH -n 120
#SBATCH -J TIP_finder_B73Oh43
#SBATCH -o TIP_finder_B73Oh43.o%j
#SBATCH -e TIP_finder_B73Oh43.e%j
#SBATCH --mail-user=menar060@umn.edu
#SBATCH --mail-type=ALL
cd /home/hirschc1/menar060/programs/TIP_finder/maize/
source activate tip_finder2
module load parallel

parallel -j 10 --joblog TIP_finder_B73vOh43_bychr_progress.log --workdir $PWD <<FIL
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr1 -t chr1 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr1.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr1_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr2 -t chr2 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr2.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr2_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr3 -t chr3 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr3.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr3_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr4 -t chr4 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr4.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr4_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr5 -t chr5 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr5.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr5_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr6 -t chr6 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr6.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr6_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr7 -t chr7 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr7.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr7_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr8 -t chr8 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr8.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr8_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr9 -t chr9 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr9.fa -w /home/hirschc1/menar060/programs/TIP_finder/maize/chr9_reference_genome_B73_10kbwindows.bed -m 350 -a blast
mpirun -np 12 -hosts= python /home/hirschc1/menar060/programs/TIP_finder/TIP_finder.py -f /home/hirschc1/menar060/programs/TIP_finder/maize/read_files.txt -o out_chr10 -t chr10 -b /home/hirschc1/menar060/programs/TIP_finder/maize/fmt_pan_TE_lib -l /home/hirschc1/menar060/programs/TIP_finder/maize/split/chr10.fa-w /home/hirschc1/menar060/programs/TIP_finder/maize/chr10_reference_genome_B73_10kbwindows.bed -m 350 -a blast
FIL
scontrol show job $SLURM_JOB_ID

