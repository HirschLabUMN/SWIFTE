#TIP_finder output proccessing
#merge overlapping read windows into coordinates
module load bedtools
cat Oh43-vs-ALL* > Oh43-vs-ALL.sort.bed
sort -V -k1,1 -k2,2 Oh43-vs-ALL.sort.bed > fixed.Oh43-vs-ALL.sort.bed
bedtools merge -i fixed.Oh43-vs-ALL.sort.bed > merged_windows_Oh43-vs-ALL.sort.bed

mkdir results/
cd results/
cp ../merged_windows_Oh43-vs-ALL.sort.bed .
ln -s /home/hirschc1/menar060/programs/input_data/maize/B73v5_genes.bed
ln -s /home/hirschc1/menar060/programs/input_data/maize/filtered_B73.EDTA.TEanno.gff3
awk 'BEGIN{ FS = OFS = "\t" } { print $0,"TIP_finder_"NR"_CM"}' merged_windows_Oh43-vs-ALL.sort.bed > named.merged_windows_Oh43-vs-ALL.sort.bed
