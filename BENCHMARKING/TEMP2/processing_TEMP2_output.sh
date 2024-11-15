mkdir results/
cd results/
cp ../L001_paired_out_1_temp2_nonredundant.bed .
awk 'NR!=1 {print}' L001_paired_out_1_temp2_nonredundant.bed | awk 'BEGIN{ FS = OFS = "\t" } { print $0,"TEMP2_"NR"_CM"}' >named.output.bed
