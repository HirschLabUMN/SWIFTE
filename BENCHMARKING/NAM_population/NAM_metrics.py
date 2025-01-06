#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from collections import defaultdict

# Function to count occurrences of TP, FN, FP
def count_occurrences(filename):
    tp_count = 0
    fn_count = 0
    fp_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
    
    return tp_count, fn_count, fp_count

# Function to calculate metrics
def calculate_metrics(tp_count, fn_count, fp_count):
    precision = tp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    sensitivity = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if precision + sensitivity > 0 else 0
    fdr = fp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    pod = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    
    return precision, sensitivity, f1_score, fdr, pod

# Directory containing BED files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'

# Loop through each file
results = defaultdict(dict)
for filename in os.listdir(directory):
    if filename.endswith('_ALL.bed'):
        filepath = os.path.join(directory, filename)
        tp_count, fn_count, fp_count = count_occurrences(filepath)
        precision, sensitivity, f1_score, fdr, pod = calculate_metrics(tp_count, fn_count, fp_count)
        
        results[filename] = {
            'Precision': precision,
            'Sensitivity': sensitivity,
            'F1 Score': f1_score,
            'FDR': fdr,
            'POD': pod
        }

# Print results
for filename, metrics in results.items():
    print(f"Metrics for {filename}:")
    print(f"Precision: {metrics['Precision']:.2f}")
    print(f"Sensitivity: {metrics['Sensitivity']:.2f}")
    print(f"F1 Score: {metrics['F1 Score']:.2f}")
    print(f"FDR: {metrics['FDR']:.2f}")
    print(f"POD: {metrics['POD']:.2f}")
    print()


# In[ ]:





# In[2]:


import os
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Function to count occurrences of TP, FN, FP
def count_occurrences(filename):
    tp_count = 0
    fn_count = 0
    fp_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
    
    return tp_count, fn_count, fp_count

# Function to calculate metrics
def calculate_metrics(tp_count, fn_count, fp_count):
    precision = tp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    sensitivity = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if precision + sensitivity > 0 else 0
    fdr = fp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    pod = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    
    return precision, sensitivity, f1_score, fdr, pod

# Directory containing BED files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/'

# Loop through each file
results = defaultdict(dict)
for filename in os.listdir(directory):
    if filename.endswith('_ALL.bed'):
        filepath = os.path.join(directory, filename)
        tp_count, fn_count, fp_count = count_occurrences(filepath)
        precision, sensitivity, f1_score, fdr, pod = calculate_metrics(tp_count, fn_count, fp_count)
        
        results[filename] = {
            'Precision': precision,
            'Sensitivity': sensitivity,
            'F1 Score': f1_score,
            'FDR': fdr,
            'POD': pod
        }

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Get file names and metrics
file_names = list(results.keys())
metrics = ['Precision', 'Sensitivity', 'F1 Score', 'FDR', 'POD']

# Prepare data for plotting
bar_width = 0.15
index = np.arange(len(file_names))

for i, metric in enumerate(metrics):
    values = [results[file][metric] for file in file_names]
    ax.bar(index + i * bar_width, values, bar_width, label=metric)

# Formatting
ax.set_xlabel('Files')
ax.set_ylabel('Scores')
ax.set_title('Metrics for Each BED File')
ax.set_xticks(index + bar_width * (len(metrics) / 2 - 0.5))
ax.set_xticklabels(file_names, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()


# In[6]:


import os
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Function to count occurrences of TP, FN, FP
def count_occurrences(filename):
    tp_count = 0
    fn_count = 0
    fp_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
    
    return tp_count, fn_count, fp_count

# Function to calculate metrics
def calculate_metrics(tp_count, fn_count, fp_count):
    precision = tp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    sensitivity = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if precision + sensitivity > 0 else 0
    fdr = fp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    pod = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    
    return precision, sensitivity, f1_score, fdr, pod

# Directory containing BED files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/'

# Loop through each file
results = defaultdict(dict)
file_names = []
genotypes = []

for filename in os.listdir(directory):
    if filename.endswith('_ALL.bed'):
        filepath = os.path.join(directory, filename)
        tp_count, fn_count, fp_count = count_occurrences(filepath)
        precision, sensitivity, f1_score, fdr, pod = calculate_metrics(tp_count, fn_count, fp_count)
        
        genotype = filename.split('_')[0]  # Extract genotype from filename
        results[genotype] = {
            'Precision': precision,
            'Sensitivity': sensitivity,
            'F1 Score': f1_score,
            'FDR': fdr,
            'POD': pod
        }
        file_names.append(filename)
        genotypes.append(genotype)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Prepare data for plotting
bar_width = 0.15
index = np.arange(len(genotypes))

for i, metric in enumerate(['Precision', 'Sensitivity', 'F1 Score', 'FDR', 'POD']):
    values = [results[genotype][metric] for genotype in genotypes]
    ax.bar(index + i * bar_width, values, bar_width, label=metric)

# Formatting
ax.set_xlabel('Genotypes')
ax.set_ylabel('Scores')
ax.set_title('Metrics for Each Genotype')
ax.set_xticks(index + bar_width * (len(['Precision', 'Sensitivity', 'F1 Score', 'FDR', 'POD']) / 2 - 0.5))
ax.set_xticklabels(genotypes, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()


# In[4]:


import os
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Function to count occurrences of TP, FN, FP
def count_occurrences(filename):
    tp_count = 0
    fn_count = 0
    fp_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
    
    return tp_count, fn_count, fp_count

# Function to calculate metrics
def calculate_metrics(tp_count, fn_count, fp_count):
    precision = tp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    sensitivity = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if precision + sensitivity > 0 else 0
    fdr = fp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    pod = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    
    return precision, sensitivity, f1_score, fdr, pod

# Directory containing BED files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/'

# Loop through each file
results = defaultdict(dict)
file_names = []
genotypes = []

for filename in os.listdir(directory):
    if filename.endswith('_ALL.bed'):
        filepath = os.path.join(directory, filename)
        tp_count, fn_count, fp_count = count_occurrences(filepath)
        precision, sensitivity, f1_score, fdr, pod = calculate_metrics(tp_count, fn_count, fp_count)
        
        genotype = filename.split('_')[0]  # Extract genotype from filename
        results[genotype] = {
            'Precision': precision,
            'Sensitivity': sensitivity,
            'F1 Score': f1_score,
            'FDR': fdr,
            'POD': pod
        }
        file_names.append(filename)
        genotypes.append(genotype)

# Define colors for each metric
colors = ["#332288", "#117733", "#DDCC77", "#CC6677", "#AA4499"]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Prepare data for plotting
bar_width = 0.15
index = np.arange(len(genotypes))

metrics = ['Precision', 'Sensitivity', 'F1 Score', 'FDR', 'POD']
for i, metric in enumerate(metrics):
    values = [results[genotype][metric] for genotype in genotypes]
    ax.bar(index + i * bar_width, values, bar_width, label=metric, color=colors[i % len(colors)])

# Formatting
ax.set_xlabel('Genotypes')
ax.set_ylabel('Scores')
ax.set_title('Metrics for Each Genotype')
ax.set_xticks(index + bar_width * (len(metrics) / 2 - 0.5))
ax.set_xticklabels(genotypes, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()


# In[9]:


import os
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Function to count occurrences of TP, FN, FP
def count_occurrences(filename):
    tp_count = 0
    fn_count = 0
    fp_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
    
    return tp_count, fn_count, fp_count

# Function to calculate metrics
def calculate_metrics(tp_count, fn_count, fp_count):
    precision = tp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    sensitivity = tp_count / (tp_count + fn_count) if tp_count + fn_count > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if precision + sensitivity > 0 else 0
    fdr = fp_count / (tp_count + fp_count) if tp_count + fp_count > 0 else 0
    return precision, sensitivity, f1_score, fdr

# Directory containing BED files
directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/'

# Loop through each file
results = defaultdict(dict)
file_names = []
genotypes = []

for filename in os.listdir(directory):
    if filename.endswith('_ALL.bed'):
        filepath = os.path.join(directory, filename)
        tp_count, fn_count, fp_count = count_occurrences(filepath)
        precision, sensitivity, f1_score, fdr = calculate_metrics(tp_count, fn_count, fp_count)
        
        genotype = filename.split('_')[0]  # Extract genotype from filename
        results[genotype] = {
            'Precision': precision,
            'Sensitivity': sensitivity,
            'F1 Score': f1_score,
            'FDR': fdr
        }
        file_names.append(filename)
        genotypes.append(genotype)

# Define colors for each metric
colors = ["#332288", "#117733", "#DDCC77", "#CC6677"]

# Plotting
fig, ax = plt.subplots(figsize=(5, 5))  # Adjust figure size to 5x5 inches

# Set font size to 12 pt
plt.rcParams.update({'font.size': 12})

# Prepare data for plotting
bar_width = 0.15
index = np.arange(len(genotypes))

metrics = ['Precision', 'Sensitivity', 'F1 Score', 'FDR']
for i, metric in enumerate(metrics):
    values = [results[genotype][metric] for genotype in genotypes]
    ax.bar(index + i * bar_width, values, bar_width, label=metric, color=colors[i % len(colors)])

# Formatting
ax.set_xlabel('Genotypes')
ax.set_ylabel('Scores')
ax.set_xticks(index + bar_width * (len(metrics) / 2 - 0.5))
ax.set_xticklabels(genotypes, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()


# In[1]:


import glob

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Initialize a variable to keep track of the cumulative number of FPs
cumulative_fp_count = 0

# Process each file
for updated_file_path in updated_files:
    with open(updated_file_path, 'r') as file:
        # Read each line and check if 'FP_' is in the line
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Add the count of FPs in this file to the cumulative count
        cumulative_fp_count += fp_count

# Output the cumulative FP count
print(f"Cumulative number of FPs across all files: {cumulative_fp_count}")


# In[2]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Initialize lists to store data for plotting
genotypes = []
fp_counts = []

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Add the genotype number (i + 1) and the FP count to the lists
        genotypes.append(i + 1)  # Genotype number (1 through 25)
        fp_counts.append(fp_count)

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


# In[4]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

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


# In[5]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store data for plotting
genotypes = []
cumulative_fp_counts = []

# Initialize cumulative FP count
cumulative_fp_count = 0

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Update cumulative FP count
        cumulative_fp_count += fp_count
        
        # Add the genotype number (i + 1) and the cumulative FP count to the lists
        genotypes.append(i + 1)  # Genotype number (1 through 25)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_fp_counts:
    print("No FPs found or no data to plot.")
else:
    # Create a cumulative plot of FPs for each genotype
    plt.figure(figsize=(10, 6))
    plt.plot(genotypes, cumulative_fp_counts, marker='o', color='lightcoral', linestyle='-', linewidth=2)

    # Add labels and title
    plt.xlabel('Genotype')
    plt.ylabel('Cumulative Number of FPs')
    plt.title('Cumulative Number of False Positives (FPs) as More Genotypes Are Added')

    # Optionally, label each point with its cumulative FP count
    for i in range(len(cumulative_fp_counts)):
        plt.text(genotypes[i], cumulative_fp_counts[i] + 1, str(cumulative_fp_counts[i]), ha='center', fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[6]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store data for plotting
genotypes = []
cumulative_fp_counts = []

# Initialize cumulative FP count
cumulative_fp_count = 0

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Update cumulative FP count
        cumulative_fp_count += fp_count
        
        # Add the genotype number (i + 1) and the cumulative FP count to the lists
        genotypes.append(i + 1)  # Genotype number (1 through 25)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_fp_counts:
    print("No FPs found or no data to plot.")
else:
    # Create a bar plot of cumulative FPs for each genotype
    plt.figure(figsize=(10, 6))
    plt.bar(genotypes, cumulative_fp_counts, color='lightcoral')

    # Add labels and title
    plt.xlabel('Genotype')
    plt.ylabel('Cumulative Number of FPs')
    plt.title('Cumulative Number of False Positives (FPs) as More Genotypes Are Added')

    # Optionally, label each bar with its cumulative FP count
    for i in range(len(cumulative_fp_counts)):
        plt.text(genotypes[i], cumulative_fp_counts[i] + 1, str(cumulative_fp_counts[i]), ha='center', fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[7]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store data for plotting
file_numbers = []
cumulative_fp_counts = []

# Initialize cumulative FP count
cumulative_fp_count = 0

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Update cumulative FP count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1) and the cumulative FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_fp_counts:
    print("No FPs found or no data to plot.")
else:
    # Create a bar plot of cumulative FPs for each file
    plt.figure(figsize=(10, 6))
    plt.bar(file_numbers, cumulative_fp_counts, color='lightcoral')

    # Add labels and title
    plt.xlabel('Number of Files')
    plt.ylabel('Cumulative Number of FPs')
    plt.title('Cumulative Number of False Positives (FPs) as More Files Are Added')

    # Optionally, label each bar with its cumulative FP count
    for i in range(len(cumulative_fp_counts)):
        plt.text(file_numbers[i], cumulative_fp_counts[i] + 1, str(cumulative_fp_counts[i]), ha='center', fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[8]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store data for plotting
file_numbers = []
cumulative_fp_counts = []

# Initialize cumulative FP count
cumulative_fp_count = 0

# Process each file and count FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Count FPs in the file
        fp_count = sum(1 for line in file if 'FP_' in line)
        
        # Update cumulative FP count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1) and the cumulative FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_fp_counts:
    print("No FPs found or no data to plot.")
else:
    # Create a bar plot of cumulative FPs for each file
    plt.figure(figsize=(10, 6))
    plt.bar(file_numbers, cumulative_fp_counts, color='lightcoral')

    # Add labels and title
    plt.xlabel('Number of Files')
    plt.ylabel('Cumulative Number of FPs')
    plt.title('Cumulative Number of False Positives (FPs) as More Files Are Added')

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[1]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store cumulative data for plotting
file_numbers = []
cumulative_tp_counts = []
cumulative_fn_counts = []
cumulative_fp_counts = []

# Initialize cumulative counts
cumulative_tp_count = 0
cumulative_fn_count = 0
cumulative_fp_count = 0

# Process each file and count TPs, FNs, and FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        tp_count = 0
        fn_count = 0
        fp_count = 0
        # Count TPs, FNs, and FPs in the file
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
        
        # Debugging: Print the counts for each file
        print(f"File {updated_file_path}: TP count = {tp_count}, FN count = {fn_count}, FP count = {fp_count}")
        
        # Update cumulative counts
        cumulative_tp_count += tp_count
        cumulative_fn_count += fn_count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1), cumulative TP count, FN count, and FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_tp_counts.append(cumulative_tp_count)
        cumulative_fn_counts.append(cumulative_fn_count)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_tp_counts or not cumulative_fn_counts or not cumulative_fp_counts:
    print("No TPs, FNs, or FPs found or no data to plot.")
else:
    # Create a cumulative plot of TP, FN, and FP counts for each file
    plt.figure(figsize=(10, 6))

    # Plot cumulative TPs, FNs, and FPs with updated colors
    plt.plot(file_numbers, cumulative_tp_counts, label='Cumulative TPs', color='#117733', marker='o')
    plt.plot(file_numbers, cumulative_fn_counts, label='Cumulative FNs', color='#DDCC77', marker='o')
    plt.plot(file_numbers, cumulative_fp_counts, label='Cumulative FPs', color='#CC6677', marker='o')

    # Add labels and title
    plt.xlabel('Number of Files')
    plt.ylabel('Cumulative Count')
    plt.title('Cumulative Count of TPs, FNs, and FPs Across Files')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[4]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store cumulative data for plotting
file_numbers = []
cumulative_tp_counts = []
cumulative_fn_counts = []
cumulative_fp_counts = []

# Initialize cumulative counts
cumulative_tp_count = 0
cumulative_fn_count = 0
cumulative_fp_count = 0

# Process each file and count TPs, FNs, and FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        tp_count = 0
        fn_count = 0
        fp_count = 0
        # Count TPs, FNs, and FPs in the file
        for line in file:
            if 'TP_' in line:
                tp_count += 1
            elif 'FN_' in line:
                fn_count += 1
            elif 'FP_' in line:
                fp_count += 1
        
        # Debugging: Print the counts for each file
        print(f"File {updated_file_path}: TP count = {tp_count}, FN count = {fn_count}, FP count = {fp_count}")
        
        # Update cumulative counts
        cumulative_tp_count += tp_count
        cumulative_fn_count += fn_count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1), cumulative TP count, FN count, and FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_tp_counts.append(cumulative_tp_count)
        cumulative_fn_counts.append(cumulative_fn_count)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_tp_counts or not cumulative_fn_counts or not cumulative_fp_counts:
    print("No TPs, FNs, or FPs found or no data to plot.")
else:
    # Set font size for all text elements
    plt.rcParams.update({'font.size': 12})

    # Create a cumulative plot of TP, FN, and FP counts for each file
    plt.figure(figsize=(5, 5))  # Set figure size to 3.5 by 5 inches

    # Plot cumulative TPs, FNs, and FPs with updated colors
    plt.plot(file_numbers, cumulative_tp_counts, label='Cumulative TPs', color='#117733', marker='o')
    plt.plot(file_numbers, cumulative_fn_counts, label='Cumulative FNs', color='#DDCC77', marker='o')
    plt.plot(file_numbers, cumulative_fp_counts, label='Cumulative FPs', color='#CC6677', marker='o')

    # Add labels and title
    plt.xlabel('Number of Genotypes')
    plt.ylabel('Cumulative Count')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[1]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/updated'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store cumulative data for plotting
file_numbers = []
cumulative_tp_counts = []
cumulative_fn_counts = []
cumulative_fp_counts = []

# Initialize cumulative counts
cumulative_tp_count = 0
cumulative_fn_count = 0
cumulative_fp_count = 0

# Process each file and count TPs, FNs, and FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        # Use sets to keep track of unique coordinates or identifiers for TP, FN, and FP
        tp_set = set()
        fn_set = set()
        fp_set = set()
        
        # Count unique TPs, FNs, and FPs in the file
        for line in file:
            if 'TP_' in line:
                # Extract unique identifier or coordinate (for example, use the first three columns as a key)
                identifier = line.split()[0:3]  # Assuming chr, start, stop are in columns 0, 1, 2
                tp_set.add(tuple(identifier))  # Add the identifier as a tuple to the set
            elif 'FN_' in line:
                identifier = line.split()[0:3]  # Assuming chr, start, stop are in columns 0, 1, 2
                fn_set.add(tuple(identifier))  # Add the identifier as a tuple to the set
            elif 'FP_' in line:
                identifier = line.split()[0:3]  # Assuming chr, start, stop are in columns 0, 1, 2
                fp_set.add(tuple(identifier))  # Add the identifier as a tuple to the set
        
        # Update the cumulative counts using the sizes of the sets (unique entries)
        tp_count = len(tp_set)
        fn_count = len(fn_set)
        fp_count = len(fp_set)
        
        # Debugging: Print the counts for each file
        print(f"File {updated_file_path}: TP count = {tp_count}, FN count = {fn_count}, FP count = {fp_count}")
        
        # Update cumulative counts
        cumulative_tp_count += tp_count
        cumulative_fn_count += fn_count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1), cumulative TP count, FN count, and FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_tp_counts.append(cumulative_tp_count)
        cumulative_fn_counts.append(cumulative_fn_count)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_tp_counts or not cumulative_fn_counts or not cumulative_fp_counts:
    print("No TPs, FNs, or FPs found or no data to plot.")
else:
    # Set font size for all text elements
    plt.rcParams.update({'font.size': 12})

    # Create a cumulative plot of TP, FN, and FP counts for each file
    plt.figure(figsize=(5, 5))  # Set figure size to 3.5 by 5 inches

    # Plot cumulative TPs, FNs, and FPs with updated colors
    plt.plot(file_numbers, cumulative_tp_counts, label='Cumulative TPs', color='#117733', marker='o')
    plt.plot(file_numbers, cumulative_fn_counts, label='Cumulative FNs', color='#DDCC77', marker='o')
    plt.plot(file_numbers, cumulative_fp_counts, label='Cumulative FPs', color='#CC6677', marker='o')

    # Add labels and title
    plt.xlabel('Number of Genotypes')
    plt.ylabel('Cumulative Count')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[3]:


import glob
import matplotlib.pyplot as plt

# Define the directory and pattern for the updated genotype files
updated_files_directory = '/home/hirschc1/menar060/programs/splitreader_maize_3/aMizeNG33/Oh43_retest/updated'
updated_files_pattern = updated_files_directory + '/updated_*_ALL.bed'  # Correct file pattern

# Get a list of all updated files matching the pattern
updated_files = glob.glob(updated_files_pattern)

# Debug: Check how many files are found
print(f"Files found: {len(updated_files)}")
print(f"Files: {updated_files[:25]}")  # Display the first 25 files

# Initialize lists to store cumulative data for plotting
file_numbers = []
cumulative_tp_counts = []
cumulative_fn_counts = []
cumulative_fp_counts = []

# Initialize cumulative counts
cumulative_tp_count = 0
cumulative_fn_count = 0
cumulative_fp_count = 0

# Initialize a dictionary to track seen identifiers and their classifications
seen_identifiers = {}

# Process each file and count TPs, FNs, and FPs
for i, updated_file_path in enumerate(updated_files[:25]):  # Process first 25 files
    with open(updated_file_path, 'r') as file:
        tp_set = set()
        fn_set = set()
        fp_set = set()
        
        # Count unique TPs, FNs, and FPs in the file
        for line in file:
            identifier = tuple(line.split()[0:3])  # Unique identifier (chr, start, stop)
            
            if 'TP_' in line:
                # If this identifier was previously FN, move it from FN to TP
                if identifier in seen_identifiers and seen_identifiers[identifier] == 'FN':
                    fn_set.remove(identifier)
                    cumulative_fn_count -= 1
                tp_set.add(identifier)
                seen_identifiers[identifier] = 'TP'
            elif 'FN_' in line:
                # If this identifier was previously TP, keep it as TP, otherwise add it as FN
                if identifier not in seen_identifiers:
                    fn_set.add(identifier)
                    seen_identifiers[identifier] = 'FN'
            elif 'FP_' in line:
                fp_set.add(identifier)
        
        tp_count = len(tp_set)
        fn_count = len(fn_set)
        fp_count = len(fp_set)
        
        # Update the cumulative counts
        cumulative_tp_count += tp_count
        cumulative_fn_count += fn_count
        cumulative_fp_count += fp_count
        
        # Add the file number (i + 1), cumulative TP count, FN count, and FP count to the lists
        file_numbers.append(i + 1)  # File number (1 through 25)
        cumulative_tp_counts.append(cumulative_tp_count)
        cumulative_fn_counts.append(cumulative_fn_count)
        cumulative_fp_counts.append(cumulative_fp_count)

# Check if any data was collected
if not cumulative_tp_counts or not cumulative_fn_counts or not cumulative_fp_counts:
    print("No TPs, FNs, or FPs found or no data to plot.")
else:
    # Set font size for all text elements
    plt.rcParams.update({'font.size': 12})

    # Create a cumulative plot of TP, FN, and FP counts for each file
    plt.figure(figsize=(5, 3))  # Set figure size to 3.5 by 5 inches

    # Plot cumulative TPs, FNs, and FPs with updated colors
    plt.plot(file_numbers, cumulative_tp_counts, label='Cumulative TPs', color='#44AA99', marker='o')
    plt.plot(file_numbers, cumulative_fn_counts, label='Cumulative FNs', color='#88CCEE', marker='o')
    plt.plot(file_numbers, cumulative_fp_counts, label='Cumulative FPs', color='#AA4499', marker='o')

    # Add labels and title
    plt.xlabel('Number of Genotypes')
    plt.ylabel('Cumulative Count')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


# In[ ]:




