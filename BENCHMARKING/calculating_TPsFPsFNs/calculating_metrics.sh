#!/bin/bash
#benchmark

cd /home/hirschc1/menar060/programs/results/benchmark
ln -s /home/hirschc1/menar060/programs/TEfinder/TEfinder/results/100bpwindow/100bpchange.named.sorted.TEinsertions.bed
ln -s /home/hirschc1/menar060/programs/results/Manisha_calls_Oh43.bed
ln -s /home/hirschc1/menar060/programs/mcclintock/mcclintock/maizetest1/L001_paired_out_1/results/temp2/results/100bp_window/TEMP2.nonreference.named.output_center.bed
ln -s /home/hirschc1/menar060/programs/TIP_finder/maize/results/results/100bp_window/TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed
ln -s /home/hirschc1/menar060/programs/results/SWIFTE_calls.bed

#Category 4 & 5 TIP annotations removed from original file
grep 'Category_3' -v output_file_Oh43.tsv > notTEequalsSV_Oh43.bed

#adjusted coords of SWIFTE calls, expand 100bp and take middle coords
/home/hirschc1/menar060/programs/results/benchmark/get_window.sh SWIFTE_calls.bed
#add name to each SWIFTE call
awk 'BEGIN{OFS="\t"} {$6 = "SWIFTE_" NR "_CM"; print}' SWIFTE_calls_center.bed > SWIFTE_calls_center_with_ID.bed

#getting num of TP, FP and FN before any other filtering
module load bedtools

##TEfinder
bedtools intersect -a 100bpchange.named.sorted.TEinsertions.bed -b Manisha_calls_Oh43.bed | cut -f 8 | sort | uniq  |wc -l
echo "TEfinder # of TP: 1213"
bedtools intersect -a 100bpchange.named.sorted.TEinsertions.bed -b Manisha_calls_Oh43.bed -v | cut -f 8 | sort | uniq  |wc -l
echo "TEfinder # of FP: 85781"
bedtools intersect -a Manisha_calls_Oh43.bed -b 100bpchange.named.sorted.TEinsertions.bed -v | cut -f 6 | sort | uniq | wc -l
echo "TEfinder # of FN:10025"

##TEMP2
bedtools intersect -a TEMP2.nonreference.named.output_center.bed -b Manisha_calls_Oh43.bed | cut -f 7 | sort | uniq | wc -l
echo "TEMP2 # of TP: 610"
bedtools intersect -a TEMP2.nonreference.named.output_center.bed -b Manisha_calls_Oh43.bed -v | cut -f 7 | sort | uniq | wc -l
echo "TEMP2 # of FP: 1463"
bedtools intersect -a Manisha_calls_Oh43.bed -b TEMP2.nonreference.named.output_center.bed -v | cut -f 6 | sort | uniq | wc -l
echo "TEMP2 # of FN: 10616"

##TIP_finder
bedtools intersect -a TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed -b Manisha_calls_Oh43.bed | cut -f 4 | sort | uniq | wc -l
echo "TIP_finder # of TP: 655"
bedtools intersect -a TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed -b Manisha_calls_Oh43.bed -v | cut -f 4 | sort | uniq | wc -l
echo "TIP_finder # of FP: 71968"
bedtools intersect -a Manisha_calls_Oh43.bed -b TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed -v | cut -f 6 | sort | uniq | wc -l
echo "TIP_finder # of FN: 10568"

##SWIF-TE
bedtools intersect -a SWIFTE_calls_center_with_ID.bed -b Manisha_calls_Oh43.bed  | cut -f 6 | sort |  uniq | wc -l
echo "SWIF-TE # of TP: 1438"
bedtools intersect -a SWIFTE_calls_center_with_ID.bed -b Manisha_calls_Oh43.bed -v  | cut -f 6 | sort |  uniq | wc -l
echo "SWIF-TE # of FP: 4397"
bedtools intersect -a Manisha_calls_Oh43.bed -b SWIFTE_calls_center_with_ID.bed -v | cut -f 6 | sort | uniq | wc -l
echo "SWIF-TE # of FN: 9787"



###FILTERING: counting num of FP calls from each output that are in unalignable sequence and in Category 4 and 5 TE SV's (not TE=SVs). Will subsract this from total num of calls to reduce FP
#TEfinder
bedtools intersect -a 100bpchange.named.sorted.TEinsertions.bed -b unalignable_regions_sorted.bed | cut -f 8 | sort | uniq | wc -l
echo "TEfinder # of FP in unalignable sequence: 2292"
bedtools intersect -a 100bpchange.named.sorted.TEinsertions.bed -b notTEequalsSV_Oh43.bed | cut -f 8 | sort | uniq | wc -l
echo "TEfinder # of FP in non TE=SV: 2802"

#TIP_finder
bedtools intersect -a TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed -b Manisha_calls_Oh43.bed | cut -f 4 | sort | uniq | wc -l
echo "TIP_finder # FP in unalignable sequence: 655"
bedtools intersect -a TIP_finder_named.merged_windows_Oh43-vs-ALL.sort_center.bed -b notTEequalsSV_Oh43.bed | cut -f 4 | sort | uniq | wc -l
echo "TIP_finder # FP in non TE=SV: 517"


#TEMP2
bedtools intersect -a TEMP2.nonreference.named.output_center.bed -b unalignable_regions_sorted.bed | cut -f 7 | sort | uniq | wc -l
echo "TEMP2 # FP in unalignable sequence: 18"
bedtools intersect -a TEMP2.nonreference.named.output_center.bed -b notTEequalsSV_Oh43.bed | cut -f 7 | sort | uniq | wc -l
echo "TEMP2 # FP in non TE=SV: 444"

#SWIF-TE
bedtools intersect -a SWIFTE_calls_center_with_ID.bed -b unalignable_regions_sorted.bed | cut -f 6 | sort | uniq | wc -l
echo "SWIF-TE # FP in unalignable sequence: 24"
bedtools intersect -a SWIFTE_calls_center_with_ID.bed -b notTEequalsSV_Oh43.bed | cut -f 6 | sort| uniq | wc -l
echo "SWIF-TE # FP in non TE=SV: 570"

