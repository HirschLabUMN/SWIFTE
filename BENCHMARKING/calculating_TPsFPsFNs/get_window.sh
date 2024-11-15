#!/bin/bash

# Check if input file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 input.bed"
    exit 1
fi

input_file="$1"
output_file="${input_file%.bed}_center.bed"

# Calculate the 100-bp center for each entry and update start and stop positions
awk 'BEGIN{OFS="\t"} {center=int(($2+$3)/2); $2=center-50; $3=center+50; print}' "$input_file" > "$output_file"

echo "Updated BED file with center positions saved to $output_file"


