#!/bin/bash

# Define arrays of filenames
sv_files=(
    "unique_TEequalsSV_B97.tsv.bed"
    "unique_TEequalsSV_CML103.tsv.bed"
    "unique_TEequalsSV_CML228.tsv.bed"
    "unique_TEequalsSV_CML247.tsv.bed"
    "unique_TEequalsSV_CML277.tsv.bed"
    "unique_TEequalsSV_CML322.tsv.bed"
    "unique_TEequalsSV_CML333.tsv.bed"
    "unique_TEequalsSV_CML52.tsv.bed"
    "unique_TEequalsSV_CML69.tsv.bed"
    "unique_TEequalsSV_HP301.tsv.bed"
    "unique_TEequalsSV_Il14H.tsv.bed"
    "unique_TEequalsSV_Ki11.tsv.bed"
    "unique_TEequalsSV_Ki3.tsv.bed"
    "unique_TEequalsSV_Ky21.tsv.bed"
    "unique_TEequalsSV_M162W.tsv.bed"
    "unique_TEequalsSV_M37W.tsv.bed"
    "unique_TEequalsSV_Mo18W.tsv.bed"
    "unique_TEequalsSV_Ms71.tsv.bed"
    "unique_TEequalsSV_NC350.tsv.bed"
    "unique_TEequalsSV_NC358.tsv.bed"
    "unique_TEequalsSV_Oh43.tsv.bed"
    "unique_TEequalsSV_Oh7B.tsv.bed"
    "unique_TEequalsSV_P39.tsv.bed"
    "unique_TEequalsSV_Tx303.tsv.bed"
    "unique_TEequalsSV_Tzi8.tsv.bed"
)

knobs_files=(
    "B97_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML103_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML228_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML247_paired_toB73_genomic.clean.remove_knobs.bed"
    "CML277_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML322_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML333_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "CML52_single_toB73_genomic.clean.remove_knobs.bed"
    "CML69_paired_toB73_genomic.clean.remove_knobs.bed"
    "HP301_single_toB73_genomic.sam.15x.sorted.sam.inserts.txt.clean.bed"
    "Il14H_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "Ki11_single_toB73_genomic.sam.15x.sorted.sam.inserts.txt.clean.bed"
    "Ki3_paired_toB73_genomic.clean.remove_knobs.bed"
    "Ky21_paired_toB73_genomic.clean.remove_knobs.bed"
    "M162W_single_toB73_genomic.sam.15x.sorted.sam.inserts.txt.clean.bed"
    "M37W_single_toB73_genomic.sam.15x.sorted.sam.inserts.txt.clean.bed"
    "Mo18W_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "Ms71_paired_toB73_genomic.clean.remove_knobs.bed"
    "NC350_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "NC358_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "Oh43_paired_toB73_genomic.clean.remove_knobs.bed"
    "Oh7B_single_toB73_genomic.sam.15x.sorted.clean.remove_knobs.bed"
    "P39_paired_toB73_genomic.clean.remove_knobs.bed"
    "Tx303_paired_toB73_genomic.clean.remove_knobs.bed"
    "Tzi8_paired_toB73_genomic.clean.remove_knobs.bed"
)

# Iterate over the indices of sv_files and knobs_files simultaneously
for ((i=0; i<${#sv_files[@]}; i++)); do
    # Extract line name from the filename
    line_name=$(basename "${sv_files[$i]}" .tsv.bed)
    line_name=${line_name#unique_TEequalsSV_}

    # Perform bedtools intersect with options
    bedtools window -w 100 -a "${sv_files[$i]}" -b "${knobs_files[$i]}" -v |awk -v line_name="$line_name" 'BEGIN {OFS="\t"} {$5="FN_"NR; printf "%s\t%s\t%s\t", $1, $2, $3; for (i=4; i<=NF; i++) printf "%s%s", $i, (i==NF ? ORS : ";")}' > "${line_name}_${j+1}_FN.bed"
    bedtools window -w 100 -a "${knobs_files[$i]}" -b "${sv_files[$i]}" -u | awk -v line_name="$line_name" 'BEGIN {OFS="\t"} {$5="TP_"NR; printf "%s\t%s\t%s\t", $1, $2, $3; for (i=4; i<=NF; i++) printf "%s%s", $i, (i==NF ? ORS : ";")}' > "${line_name}_${j+1}_TP.bed"
    bedtools window -w 100 -a "${knobs_files[$i]}" -b "${sv_files[$i]}" -v |awk -v line_name="$line_name" 'BEGIN {OFS="\t"} {$5="FP_"NR; printf "%s\t%s\t%s\t", $1, $2, $3; for (i=4; i<=NF; i++) printf "%s%s", $i, (i==NF ? ORS : ";")}' > "${line_name}_${j+1}_FP.bed"
    cat "${line_name}_${j+1}_FN.bed" "${line_name}_${j+1}_TP.bed" "${line_name}_${j+1}_FP.bed" | sort -k1,1V -k2,2n > "${line_name}_${j+1}ALL.bed"
    rm "${line_name}_${j+1}_FN.bed" 
    rm "${line_name}_${j+1}_TP.bed" 
    rm "${line_name}_${j+1}_FP.bed"
done

