#!/usr/bin/env python
# coding: utf-8

# In[2]:


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





# In[5]:


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


# In[8]:


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

