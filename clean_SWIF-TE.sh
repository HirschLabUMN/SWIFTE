#!/bin/bash

# Default values
input_file=""
read_count_min=5

# Parse command line options
while getopts ":i:c:" opt; do
  case ${opt} in
    i ) input_file=$OPTARG;;
    c ) read_count_min=$OPTARG;;
    \? ) echo "Usage: $0 -i <input_file> -c <read_count_min>"
         exit 1;;
    : ) echo "Invalid option: $OPTARG requires an argument"
        exit 1;;
  esac
done
shift $((OPTIND -1))

# Check if input file is provided
if [ -z "$input_file" ]; then
  echo "Error: Input file is not provided"
  echo "Usage: $0 -i <input_file> -c <read_count_min>"
  exit 1
fi

# Generate output file name
output_file="${input_file}.clean.bed"

# Generate a unique name for temporary file
tname=$(echo `date +%s` $$ | sed -e 's/ /./g')

# Remove header from input file and save to temporary file
tail -n +2 "$input_file" > "$tname"

# Update the header
header="scaffold/chr\tinsertion_start\tinsertion_stop\tTE_information"

# Print updated header
#echo -e "$header"

# Sort the modified input file based on columns
sort -k1V,1 -k5,5n "$tname" | \

# Read the modified input file line by line and process
awk -v f2="$2" -v f3="$3" -v f4="$4" -v count_filter="$read_count_min" '
    BEGIN {
        pL2=0;
        pL3=0;
        pL4=0;
        if(f2>0) { pL2=f2 };
        if(f3>0) { pL3=f3 };
        if(f4>0) { pL4=f4 };
        kCH=$1;
        kPOS=$5;
        kCNT=1;
        kMXSC=$6;
        kID=$3;
        kMN=$5;
        kMX=$5;
        kST=$5
    } 
    {
        if($1!=kCH || $5-kPOS>15 || $5-kST>50) {
            if(kMXSC>=pL2 && kCNT>=pL3 && (kMX-kMN)>=pL4 && kCNT>=count_filter) {
                print kCH "\t" kMN-1 "\t" kMX "\tID=" kID ";Count=" kCNT ";TSD_length=" kMX-kMN "\t" kMXSC "\t+"
            };
            kST=$5;
            kCH=$1;
            kPOS=$5;
            kCNT=1;
            kMXSC=$6;
            kID=$3;
            kMN=$5;
            kMX=$5
        } else {
            kCNT++;
            if($6>kMXSC) { kMXSC=$6; kID=$3 };
            if($5<kMN) { kMN=$5 };
            if($5>kMX) { kMX=$5 };
            kPOS=$5
        }
    }' > "$output_file"

# Remove the temporary file
rm "$tname"

echo "Output file $output_file has been created."

