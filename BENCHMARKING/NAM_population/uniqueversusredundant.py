#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from collections import defaultdict

# Directory containing your _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize a dictionary to store coordinate counts across files
coordinate_count = defaultdict(int)

# List all _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.endswith('_ALL.bed')]

# Count occurrences of each coordinate across all files
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            # Extract relevant fields (chrom, start, end) and create a unique key
            fields = line.strip().split('\t')
            if len(fields) >= 3:
                coord_key = f"{fields[0]}:{fields[1]}-{fields[2]}"  # chr:start-end format
                coordinate_count[coord_key] += 1

# Function to determine redundancy status
def get_redundancy_status(coord_key):
    count = coordinate_count[coord_key]
    if count == 1:
        return 'unique'
    else:
        return f'redundant_in_{count}'

# Update BED files with redundancy status and write to new files
for bed_file in bed_files:
    output_lines = []
    output_file = os.path.join(directory, f"updated_{bed_file}")  # New file name

    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 3:
                coord_key = f"{fields[0]}:{fields[1]}-{fields[2]}"
                redundancy_status = get_redundancy_status(coord_key)
                # Append the status as an additional column
                output_lines.append(f"{line.strip()}\t{redundancy_status}\n")
            else:
                output_lines.append(line)  # Add lines that don't match the expected format

    # Write updated lines to the new output file
    with open(output_file, 'w') as f:
        f.writelines(output_lines)

print("Updated files have been written with redundancy status.")


# In[4]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize counters for unique and redundant entries
unique_counts = []
redundant_counts = []
genotype_names = []

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    unique_count = 0
    redundant_count = 0
    
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                if redundancy_status == 'unique':
                    unique_count += 1
                elif redundancy_status.startswith('redundant_in'):
                    redundant_count += 1
    
    unique_counts.append(unique_count)
    redundant_counts.append(redundant_count)
    # Extract the genotype name from the file name (e.g., Oh43 from updated_Oh43_ALL.bed)
    genotype_name = bed_file.split('_')[1]  # Assuming format: updated_GenotypeName_ALL.bed
    genotype_names.append(genotype_name)

# Create the plot
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(genotype_names))

# Plotting unique and redundant counts
plt.bar(index, unique_counts, bar_width, label='Unique', color='#117733')
plt.bar([i + bar_width for i in index], redundant_counts, bar_width, label='Redundant', color='#DDCC77')

# Adding labels and title
plt.xlabel('Genotypes', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Unique vs Redundant Entries Across Genotypes', fontsize=14)
plt.xticks([i + bar_width / 2 for i in index], genotype_names, rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()


# In[5]:


import os
import matplotlib.pyplot as plt

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize lists for proportions
unique_proportions = []
redundant_proportions = []
genotype_names = []

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    unique_count = 0
    redundant_count = 0
    
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                if redundancy_status == 'unique':
                    unique_count += 1
                elif redundancy_status.startswith('redundant_in'):
                    redundant_count += 1
    
    total_count = unique_count + redundant_count
    
    if total_count > 0:
        unique_proportions.append(unique_count / total_count)
        redundant_proportions.append(redundant_count / total_count)
    else:
        unique_proportions.append(0)
        redundant_proportions.append(0)

    # Extract the genotype name from the file name
    genotype_name = bed_file.split('_')[1]  # Assuming format: updated_GenotypeName_ALL.bed
    genotype_names.append(genotype_name)

# Create the plot
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(genotype_names))

# Plotting unique and redundant proportions
plt.bar(index, unique_proportions, bar_width, label='Unique Proportion', color='#117733')
plt.bar([i + bar_width for i in index], redundant_proportions, bar_width, label='Redundant Proportion', color='#DDCC77')

# Adding labels and title
plt.xlabel('Genotypes', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.title('Proportion of Unique vs Redundant Entries Across Genotypes', fontsize=14)
plt.xticks([i + bar_width / 2 for i in index], genotype_names, rotation=45, ha='right')
plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()


# In[6]:


import os
import matplotlib.pyplot as plt

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize lists for proportions
unique_proportions = []
redundant_proportions = []
genotype_names = []

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    unique_count = 0
    redundant_count = 0
    
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                if redundancy_status == 'unique':
                    unique_count += 1
                elif redundancy_status.startswith('redundant_in'):
                    redundant_count += 1
    
    total_count = unique_count + redundant_count
    
    if total_count > 0:
        unique_proportions.append(unique_count / total_count)
        redundant_proportions.append(redundant_count / total_count)
    else:
        unique_proportions.append(0)
        redundant_proportions.append(0)

    # Extract the genotype name from the file name
    genotype_name = bed_file.split('_')[1]  # Assuming format: updated_GenotypeName_ALL.bed
    genotype_names.append(genotype_name)

# Create the plot
plt.figure(figsize=(10, 6))
index = range(len(genotype_names))

# Plotting stacked bars for unique and redundant proportions
plt.bar(index, unique_proportions, label='Unique Proportion', color='#117733')
plt.bar(index, redundant_proportions, bottom=unique_proportions, label='Redundant Proportion', color='#DDCC77')

# Adding labels and title
plt.xlabel('Genotypes', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.title('Proportion of Unique vs Redundant Entries Across Genotypes', fontsize=14)
plt.xticks(index, genotype_names, rotation=45, ha='right')
plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()


# In[1]:


import os
import matplotlib.pyplot as plt

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/updated'

# Initialize lists for proportions
unique_proportions = []
redundant_proportions = []
genotype_names = []

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    unique_count = 0
    redundant_count = 0
    
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                
                # Filter for lines that contain TP_ or FN_
                if 'TP_' in line or 'FN_' in line:
                    if redundancy_status == 'unique':
                        unique_count += 1
                    elif redundancy_status.startswith('redundant_in'):
                        redundant_count += 1
    
    total_count = unique_count + redundant_count
    
    if total_count > 0:
        unique_proportions.append(unique_count / total_count)
        redundant_proportions.append(redundant_count / total_count)
    else:
        unique_proportions.append(0)
        redundant_proportions.append(0)

    # Extract the genotype name from the file name
    genotype_name = bed_file.split('_')[1]  # Assuming format: updated_GenotypeName_ALL.bed
    genotype_names.append(genotype_name)

# Create the plot
plt.figure(figsize=(10, 6))
index = range(len(genotype_names))

# Plotting stacked bars for unique and redundant proportions
plt.bar(index, unique_proportions, label='Unique Proportion', color='#CC6677')
plt.bar(index, redundant_proportions, bottom=unique_proportions, label='Redundant Proportion', color='#882255')

# Adding labels and title
plt.xlabel('Genotypes', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.title('Proportion of Unique vs Redundant Entries Across Genotypes (TP_ and FN_ only)', fontsize=14)
plt.xticks(index, genotype_names, rotation=45, ha='right')
plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()


# In[8]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize a dictionary to count redundant categories
redundant_counts = defaultdict(int)

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                
                # Count occurrences of redundancy categories
                if redundancy_status.startswith('redundant_in'):
                    # Extract the number after 'redundant_in_'
                    num = int(redundancy_status.split('_')[-1])
                    redundant_counts[num] += 1

# Prepare data for plotting
x_labels = list(range(1, 26))  # X-axis labels from 1 to 25
y_counts = [redundant_counts.get(i, 0) for i in x_labels]  # Get counts or 0 if not present

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(x_labels, y_counts, color='#CC6677')

# Adding labels and title
plt.xlabel('Redundancy Category (1 to 25)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Counts of Redundant Entries by Category', fontsize=14)
plt.xticks(x_labels)  # Set x-ticks to be the redundancy categories
plt.tight_layout()

# Show the plot
plt.show()


# In[9]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize dictionaries to count unique and redundant categories
redundant_counts = defaultdict(int)
unique_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                
                # Count occurrences of redundancy categories
                if redundancy_status.startswith('redundant_in'):
                    # Extract the number after 'redundant_in_'
                    num = int(redundancy_status.split('_')[-1])
                    redundant_counts[num] += 1
                elif redundancy_status == 'unique':
                    unique_count += 1  # Count unique entries

# Prepare data for plotting
x_labels = list(range(1, 26))  # X-axis labels from 1 to 25
y_counts = [redundant_counts.get(i, 0) for i in x_labels]  # Get counts or 0 if not present

# Add unique counts to the first category (redundant_in_1)
y_counts[0] += unique_count  # Add unique count to the first category

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(x_labels, y_counts, color='#CC6677')

# Adding labels and title
plt.xlabel('Redundancy Category (1 to 25)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Counts of Unique and Redundant Entries by Category', fontsize=14)
plt.xticks(x_labels)  # Set x-ticks to be the redundancy categories
plt.tight_layout()

# Show the plot
plt.show()


# In[10]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize dictionaries to count unique and redundant categories
redundant_counts = defaultdict(int)
unique_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                
                # Count occurrences of redundancy categories
                if redundancy_status.startswith('redundant_in'):
                    # Extract the number after 'redundant_in_'
                    num = int(redundancy_status.split('_')[-1])
                    redundant_counts[num] += 1
                elif redundancy_status == 'unique':
                    unique_count += 1  # Count unique entries

# Prepare data for plotting
x_labels = list(range(1, 26))  # X-axis labels from 1 to 25
y_counts = [redundant_counts.get(i, 0) for i in x_labels]  # Get counts or 0 if not present

# Add unique counts to the first category (redundant_in_1)
y_counts[0] += unique_count  # Add unique count to the first category

# Calculate total entries for proportion
total_entries = sum(y_counts)

# Calculate proportions
if total_entries > 0:
    proportions = [count / total_entries for count in y_counts]
else:
    proportions = [0] * len(y_counts)

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(x_labels, proportions, color='#CC6677')

# Adding labels and title
plt.xlabel('Redundancy Category (1 to 25)', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.title('Proportion of Unique and Redundant Entries by Category', fontsize=14)
plt.xticks(x_labels)  # Set x-ticks to be the redundancy categories
plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
plt.tight_layout()

# Show the plot
plt.show()


# In[22]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize dictionaries to count unique and redundant categories
redundant_counts = defaultdict(int)
unique_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there's at least one redundancy status
                redundancy_status = fields[-1]  # Last field is redundancy status
                
                # Count occurrences of redundancy categories
                if redundancy_status.startswith('redundant_in'):
                    # Extract the number after 'redundant_in_'
                    num = int(redundancy_status.split('_')[-1])
                    redundant_counts[num] += 1
                elif redundancy_status == 'unique':
                    unique_count += 1  # Count unique entries

# Prepare data for plotting
x_labels = list(range(2, 26))  # X-axis labels from 2 to 25
x_labels.insert(0, 'unique')  # Insert 'unique' as the first label
x_labels = [str(x) for x in x_labels]  # Convert all labels to strings to avoid type errors
y_counts = [redundant_counts.get(i, 0) for i in range(1, 26)]  # Get counts for 1 to 25

# Add unique counts to the first category (redundant_in_1)
y_counts[0] += unique_count  # Add unique count to the first category

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(x_labels, y_counts, color='#CC6677')

# Adding labels and title
plt.xlabel('Redundancy Category', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Counts of Unique and Redundant Entries by Category', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()


# In[7]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize dictionaries to count TP and FP occurrences for each redundancy category
tp_counts = defaultdict(int)
fp_counts = defaultdict(int)
unique_tp_count = 0
unique_fp_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            print(f"Fields for line in {bed_file}: {fields}")
            if len(fields) >= 4:  # Ensure there are at least five columns
                tp_fp_status = fields[3]  # Fourth column has TP_ or FP_ information
                redundancy_status = fields[4]  # Fifth column is redundancy status

                # Debug: Check if TP_ or FP_ entries are found
                if tp_fp_status.startswith('TP_') or tp_fp_status.startswith('FP_'):
                    print(f"Found {tp_fp_status} with redundancy status: {redundancy_status}")

                # Count occurrences of TP_ and FP_ lines separately based on redundancy status
                if tp_fp_status.startswith('TP_'):
                    if redundancy_status.startswith('redundant_in'):
                        try:
                            num = int(redundancy_status.split('_')[-1])
                            tp_counts[num] += 1
                            # Debug: Confirm redundancy category for TP_
                            print(f"TP_ entry with redundancy category {num}")
                        except ValueError:
                            print(f"Skipping TP_ line due to unexpected redundancy format: {redundancy_status}")
                    elif redundancy_status == 'unique':
                        unique_tp_count += 1
                        print(f"Unique TP_ entry found")
                elif tp_fp_status.startswith('FP_'):
                    if redundancy_status.startswith('redundant_in'):
                        try:
                            num = int(redundancy_status.split('_')[-1])
                            fp_counts[num] += 1
                            # Debug: Confirm redundancy category for FP_
                            print(f"FP_ entry with redundancy category {num}")
                        except ValueError:
                            print(f"Skipping FP_ line due to unexpected redundancy format: {redundancy_status}")
                    elif redundancy_status == 'unique':
                        unique_fp_count += 1
                        print(f"Unique FP_ entry found")

# Debug: Check final counts
print("TP Counts:", dict(tp_counts))
print("FP Counts:", dict(fp_counts))
print("Unique TP Count:", unique_tp_count)
print("Unique FP Count:", unique_fp_count)

# Prepare data for plotting
x_labels = list(range(1, 26))  # Redundancy categories from 1 to 25
tp_y_counts = [unique_tp_count] + [tp_counts.get(i, 0) for i in x_labels]  # Counts for TP, with unique as the first entry
fp_y_counts = [unique_fp_count] + [fp_counts.get(i, 0) for i in x_labels]  # Counts for FP, with unique as the first entry

# Debug: Check prepared data for plotting
print("TP Y Counts:", tp_y_counts)
print("FP Y Counts:", fp_y_counts)

# Convert labels to strings for readability and add "unique" label at the start
x_labels_str = ['unique'] + [str(x) for x in x_labels]

# Create the plot
plt.figure(figsize=(12, 6))
bar_width = 0.35  # Width of the bars

# Generate positions for each bar group
x = range(len(x_labels_str))
tp_bar = plt.bar([i - bar_width / 2 for i in x], tp_y_counts, width=bar_width, color='#44AA99', label='TP')
fp_bar = plt.bar([i + bar_width / 2 for i in x], fp_y_counts, width=bar_width, color='#88CCEE', label='FP')

# Adding labels and title
plt.xlabel('Redundancy Category', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Counts of TP and FP Entries by Redundancy Category', fontsize=14)
plt.xticks(x, x_labels_str, rotation=45)  # Rotate x-axis labels for better readability
plt.legend()

plt.tight_layout()
plt.show()


# In[10]:


import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize dictionaries to count TP and FP occurrences for each redundancy category
tp_counts = defaultdict(int)
fp_counts = defaultdict(int)
unique_tp_count = 0
unique_fp_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 5:  # Ensure there are at least five columns
                tp_fp_status = fields[3]  # Fourth column contains potential TP_ or FP_ info
                redundancy_status = fields[4]  # Fifth column is redundancy status

                # Check if TP_ or FP_ appears anywhere in the fourth column
                if 'TP_' in tp_fp_status:
                    if redundancy_status.startswith('redundant_in'):
                        try:
                            num = int(redundancy_status.split('_')[-1])
                            tp_counts[num] += 1
                        except ValueError:
                            continue
                    elif redundancy_status == 'unique':
                        unique_tp_count += 1
                elif 'FP_' in tp_fp_status:
                    if redundancy_status.startswith('redundant_in'):
                        try:
                            num = int(redundancy_status.split('_')[-1])
                            fp_counts[num] += 1
                        except ValueError:
                            continue
                    elif redundancy_status == 'unique':
                        unique_fp_count += 1

# Prepare data for plotting
x_labels = list(range(1, 26))  # Redundancy categories from 1 to 25
tp_y_counts = [unique_tp_count] + [tp_counts.get(i, 0) for i in x_labels]  # Counts for TP, with unique as the first entry
fp_y_counts = [unique_fp_count] + [fp_counts.get(i, 0) for i in x_labels]  # Counts for FP, with unique as the first entry

# Convert labels to strings for readability and add "unique" label at the start
x_labels_str = ['unique'] + [str(x) for x in x_labels]

# Create the plot
plt.figure(figsize=(12, 6))
bar_width = 0.35  # Width of the bars

# Generate positions for each bar group
x = range(len(x_labels_str))
tp_bar = plt.bar([i - bar_width / 2 for i in x], tp_y_counts, width=bar_width, color='#44AA99', label='TP')
fp_bar = plt.bar([i + bar_width / 2 for i in x], fp_y_counts, width=bar_width, color='#88CCEE', label='FP')

# Adding labels and title
plt.xlabel('Redundancy Category', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Counts of TP and FP Entries by Redundancy Category', fontsize=14)
plt.xticks(x, x_labels_str, rotation=45)  # Rotate x-axis labels for better readability
plt.legend()

plt.tight_layout()
plt.show()


# In[12]:


import os
from collections import defaultdict

# Directory containing your updated _ALL.bed files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Initialize counters for TP and FN occurrences across all files
tp_total_count = 0
fn_total_count = 0
fp_total_count = 0

# List all updated _ALL.bed files in the directory
bed_files = [f for f in os.listdir(directory) if f.startswith('updated_') and f.endswith('_ALL.bed')]

# Process each updated BED file
for bed_file in bed_files:
    with open(os.path.join(directory, bed_file), 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure there are at least four columns
                tp_fp_status = fields[3]  # Fourth column contains potential TP_ or FN_ info

                # Count occurrences of TP_ and FN_
                if 'TP_' in tp_fp_status:
                    tp_total_count += 1
                elif 'FN_' in tp_fp_status:
                    fn_total_count += 1
                elif 'FP_' in tp_fp_status:
                    fp_total_count += 1

# Display total counts
print("Total TP_ entries:", tp_total_count)
print("Total FN_ entries:", fn_total_count)
print("Total FP_ entries:", fp_total_count)


# In[1]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store data for plotting
genotypes = []
fp_counts = []

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Debug: Print the count of FPs for each file
        print(f"File {updated_file_path}: FPs = {fp_count}")
        
        # Add the genotype number (i + 1) and the FP count to the lists
        genotypes.append(i + 1)  # Genotype number (1 through 25)
        fp_counts.append(fp_count)

# Check if any data was collected
if not fp_counts:
    print("No FPs found or no data to plot.")
else:
    # Create a bar plot of FPs for each genotype
    plt.figure(figsize=(10, 6))
    plt.bar(genotypes, fp_counts, color='lightcoral')

    # Add labels and title
    plt.xlabel('Genotype')
    plt.ylabel('Number of FPs')
    plt.title('Number of False Positives (FPs) for Each Genotype')

    # Optionally, label each bar with its FP count
    for i in range(len(fp_counts)):
        plt.text(genotypes[i], fp_counts[i] + 1, str(fp_counts[i]), ha='center', fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[ ]:




