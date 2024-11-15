#TEfinder output processing
sort TEinsertions.bed

mkdir results/
cd results/

cp ../sorted.TEinsertions.bed .
ln -s /home/hirschc1/menar060/programs/input_data/Arabidopsis/final/TAIR10_GFF3_genes.gff.bed.genes.bed
#ln -s /home/hirschc1/menar060/programs/input_data/maize/B73v5_genes.bed 

ln -s /home/hirschc1/menar060/programs/input_data/Arabidopsis/final/filtered_TAIR10_GCF_000001735.4.fasta.mod.EDTA.TEanno.gff3
#ln -s /home/hirschc1/menar060/programs/input_data/maize/filtered_B73.EDTA.TEanno.gff3

awk 'BEGIN{ FS = OFS = "\t" } { print $0,"TEfinder_"NR"_CM"}' sorted.TEinsertions.bed > named.sorted.TEinsertions.bed
#awk 'BEGIN{ FS = OFS = "\t" } { print $0,"TEfinder_"NR"_CM"}' sorted.TEinsertions.all.bed > named.sorted.TEinsertions.bed

#intersect reference TEs
bedtools intersect -wo -a filtered_TAIR10_GCF_000001735.4.fasta.mod.EDTA.TEanno.gff3 -b named.sorted.TEinsertions.bed -f 0.9 -r > intersect_referenceTEs.txt
#bedtools intersect -wo -a filtered_B73.EDTA.TEanno.gff3 -b named.sorted.TEinsertions.bed -f 0.9 -r > intersect_referenceTEs.txt


#intersect reference genes
bedtools intersect -a named.sorted.TEinsertions.bed -b TAIR10_GFF3_genes.gff.bed.genes.bed -c | awk '$9==1' > intersect_genes.txt
#bedtools intersect -a named.sorted.TEinsertions.bed -b B73v5_genes.bed -c | awk '$9==1' > intersect_genes.txt

#within 1kb of a gene
bedtools window -w 1000 -a named.sorted.TEinsertions.bed -b TAIR10_GFF3_genes.gff.bed.genes.bed -c | awk '$9!=0' > 1kb_window_of_genes.txt
#bedtools window -w 1000 -a named.sorted.TEinsertions.bed -b B73v5_genes.bed -c | awk '$9!=0' > 1kb_window_of_genes.txt

cut -f 8 intersect_genes.txt > filterout.txt
grep -f filterout.txt 1kb_window_of_genes.txt -v > within_1kb_but_not_in_gene.txt
rm filterout.txt
rm 1kb_window_of_genes.txt
#outside 1kb of a gene
bedtools window -w 1000 -a named.sorted.TEinsertions.bed -b TAIR10_GFF3_genes.gff.bed.genes.bed -c | awk '$9==0' > outside_1kb_window_of_genes.txt
bedtools window -w 1000 -a named.sorted.TEinsertions.bed -b  B73v5_genes.bed -c | awk '$9==0' > outside_1kb_window_of_genes.txt
