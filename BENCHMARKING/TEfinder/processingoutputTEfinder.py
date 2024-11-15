#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:03:48 2023

@author: clairemenard
"""

#processing new output format
import pandas as pd
import numpy as np
#TEfinder results parse
#sort TE insertions bed file first
TEfinder_outputfile = pd.read_csv("named.sorted.TEinsertions.bed", sep='\t', header =None)
TEfinder_outputfile.columns  = ['chr', 'start', 'stop', 'TE_family', 'score', 'strand', 'info', 'program_ID']

'''
TAIR_GFF = pd.read_csv("TAIR_TE.gff3",sep='\t', header=None)
TAIR_GFF.columns = ["chr", "EDTA", "Superfamily", "start", "stop", "score", "strand", "phase", "attributes"]
TAIR_GFF.attributes.str.split(";", expand=True)
'''
TIPs_refTEs_intersect = pd.read_csv("intersect_referenceTEs.txt", sep='\t', header=None)
TIPs_refTEs_intersect.columns = ["chr", "EDTA", "Superfamily", "start", "stop", "score", "strand", "phase", "attributes", "chr_x", "start_x", "stop_x", "family_x", "score_x", "strand_x", "extra_x", "program_ID","num_bp_overlap"]

TIPs_genes_intersect =  pd.read_csv("intersect_genes.txt", sep='\t', header=None)
TIPs_genes_intersect_1kbwindow =  pd.read_csv("within_1kb_but_not_in_gene.txt", sep='\t')
TIPs_genes_intersect_outsidewindow = pd.read_csv("outside_1kb_window_of_genes.txt", sep='\t')
header1 = ['chr', 'start', 'stop', 'TE_family', 'num_of_reads_mapped', 'score', 'info', 'program_ID', 'num_of_intersects']
TIPs_genes_intersect.columns = header1
TIPs_genes_intersect_1kbwindow.columns = header1
TIPs_genes_intersect_outsidewindow.columns = header1

import gffpandas as gffpd
TAIR_GFF3_GFFPD = gffpd.read_gff3('filtered_B73.EDTA.TEanno.gff3')
TAIR_GFF3 = TAIR_GFF3_GFFPD.attributes_to_columns()
Family_dict = TAIR_GFF3.set_index('Name').to_dict()['Classification']
Family_dict_small = TEfinder_outputfile['TE_family']
filtered_TAIR_GFF3 = TAIR_GFF3[TAIR_GFF3['Name'].isin(Family_dict_small)]


merged1 = pd.merge(TEfinder_outputfile, filtered_TAIR_GFF3, left_on=('TE_family'), right_on=('Name'))
full_df = merged1[['chr', 'start_x', 'stop', 'TE_family', 'score_x', 'strand_x', 'program_ID','info', 'type','Classification', 'Method']].drop_duplicates(subset=('program_ID'))
TIP_ref_list = list(TIPs_refTEs_intersect['program_ID'])
full_df['reference'] = np.where(full_df['program_ID'].isin(TIP_ref_list), True, False)

TIP_gene_list = list(TIPs_genes_intersect['program_ID'])
full_df['in_gene'] = np.where(full_df['program_ID'].isin(TIP_gene_list), True, False)

TIP_1kbgene_list =list(TIPs_genes_intersect_1kbwindow['program_ID'])
full_df['within_1kb_of_gene'] = np.where(full_df['program_ID'].isin(TIP_1kbgene_list), True, False)

TIP_outsidegenic_list = list(TIPs_genes_intersect_outsidewindow['program_ID'])
full_df['outside_genic_region'] = np.where(full_df['program_ID'].isin(TIP_outsidegenic_list), True, False)


cols = ['chr', 'start', 'stop', 'TE_family', 'score', 'strand',
       'program_ID', 'info', 'type', 'Classification', 'Method', 'reference',
       'in_gene', 'within_1kb_of_gene', 'outside_genic_region']
full_df = full_df.rename(columns={'start_x':'start', 'score_x':'score', 'strand_x':'strand'})
full_df = full_df[cols]



full_df['start'] = full_df['start'].astype(int)
full_df['stop'] = full_df['stop'].astype(int)
full_df['program_name'] = "TEfinder"
full_df.to_csv("TEfinder.output", sep='\t')


duplicated_fams_output = pd.read_csv("duplicated_fams.tsv", sep='\t')
duplicated_fams_output2  = pd.read_csv("duplicated_fams_2.tsv", sep='\t')
duplicated_fams_output3  = pd.read_csv("duplicated_fams_3.tsv", sep='\t')
