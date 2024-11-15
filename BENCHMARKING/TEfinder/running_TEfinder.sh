#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --mem=400g
#SBATCH --tmp=400g
#SBATCH --job-name=TEfinder
#SBATCH -D /home/hirschc1/menar060/programs/TEfinder/TEfinder/
#SBATCH -p ag2tb
#SBATCH --mail-type=ALL
#SBATCH --mail-user=menar060@umn.edu

cd /home/hirschc1/menar060/programs/TEfinder/TEfinder/

module load bowtie2/2.3.4.1
module load samtools/1.9
module load bedtools/2.29.2
module load picard-tools/2.25.6
module load bwa

cut -f 9 filtered_B73.EDTA.TEanno.gff3 | cut -d ';' -f 2 | cut -d '=' -f 2 > B73.EDTA.TEnames.txt

bwa index B73_chrs.fa

cat L001_paired_out_1.fq | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > L001_paired_out_1.sorted.fastq
cat L001_paired_out_2.fq | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > L001_paired_out_2.sorted.fastq

bwa mem -t 16 B73_chrs.fa L001_paired_out_1.sorted.fastq L001_paired_out_2.sorted.fastq > Oh43B73_fast.bam  
java -jar /panfs/roc/msisoft/picard/2.25.6/picard.jar
java -jar /panfs/roc/msisoft/picard/2.25.6/picard.jar AddOrReplaceReadGroups \
    I=Oh43B73_fast.bam \
    O=Oh43B73_fast_fixed.bam \
    RGID=Oh43 \
    RGLB=LIB \
    RGPL=illumina \
    RGPU=unit1 \
    RGSM=Oh43

source activate TEfinder
bash TEfinder -alignment Oh43B73_fast_fixed.REF_chr1.bam -fa chr1.fa -gtf filtered_B73.EDTA.TEanno.gff3 -te xaa -maxHeapMem 400000 -workingdir out_xaa -picard /panfs/roc/msisoft/picard/2.25.6/picard.jar -intermed yes 
