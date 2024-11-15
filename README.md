# SWIF-TE

SWIF-TE (Short-read Whole-genome Insertion Finder for Transposable Elements) is a powerful tool designed to identify transposable element insertions (TIPs) using short-read data.
<img src="SWIF-TE_final.png" alt="Example Image">
## Features

-   **Memory Efficiency**: SWIF-TE works by loading in small chunks of sequence from a SAM file at a time, becoming much more memory efficient than other tools.
-   **Flexibility**: Customize SWIF-TE to suit your species by including a soft-clipping cutoff (default is 40 for 150-bp reads).
-   **Speed**: Experience lightning-fast performance, even with large, complex genomes. Easy to scale to tens or hundreds of individuals.

## Getting Started

To begin using SWIF-TE, follow these simple steps:

1.  **Download**: Clone this repository.
    -   `git clone <link>`

    -   `cd SWIFTEv35/`
2.  **Installation**: Follow the installation instructions provided on the website to install SWIF-TE on your system.

    -   `unzip SWIFTEv35.zip`

    -   `chmod +x SWIFTEv35`

3.  **Test if it works**: Once installed, launch SWIF-TE to start exploring its features and capabilities.

    -   `./SWIFTEv35`

        -   If you get a shared library error, could you execute the command below and send me the output so I can see what libraries need adding the following.

            -   `ldd SWIFTEv35`

        -   Generally missing shared libraries (.so) just need to be dropped into the SWIFTE Libs folder (or installed at the system level).

## Usage

### Data Prep

-   **Genome**
    -   The reference genome and a repeat library (which can be generated with repeatModeler) for the reference need to be indexed. Our aligner of choice is bowtie2. Others may work, but have not been tested.
        -   build genome index
            -   `bowtie2-build Thal_genome.fa Thal`
        -   build repeat database index
            -   `bowtie2-build athaTEref_RU.lib Rep`
-   **Reads**
    -   SWIF-TE has been built for 1x150nt Illumnia reads. It will work down to 1x100nt reads but will lose sensitivity. We haven't tested longer Illumnia reads but those should also work. If you have paired-end reads, you can concatenate both ends to a single-end file but need to make sure the read names are different (\*see notes).
-   **Trimming**
    -   Reads need to be trimmed. We chose \_\_\_ , but any should work.
        -   `cutadapt -a AGATCGGAAGAG -q 20 -m 50 -o reads.fastq input.fastq`
-   **Aligning to genome**
    -   If the reads are up to 3% diverged from the reference, the command below should work. If there is more divergence, change ---local to --very-sensitivite-local. Assuming 4 threads and reads are named reads.fastq
        -   `bowtie2 -p 4 -x Thal -U reads.fastq -S genomic.sam --local`
-   Aligning to the repeat database
    -   If the reads are up to 3% diverged from the reference, the command below should work. If there is more divergence, change ---local to --very-sensitivite-local. Assuming 4 threads and reads are named reads.fastq
        -   `bowtie2 -p 4 -x Rep -U reads.fastq -S rpt.sam --local`

### Running SWIF-TE

`./SWIFTEv35 genomic.sam rpt.sam`

-   Can also define the soft-clip threshold (default is 40). Here is an example:

    -   `./SWIFTEv35 genomic.sam rpt.sam 40,40`

**Output**

-   The output file name will be reported if the process completes successfully. The output consists of the following columns:

| chr/Scaffold                                                           | Raw_pos                                         | TE_ID                                                               | Align_info                                                    | Final_position                                                | TE_ID_score                                                                                                                                   |
|------------|------------|------------|------------|------------|------------|
| Name of the reference genome scaffold where the TE insert is predicted | Raw alignment location of the read (do not use) | The ID of the TE that has been inserted (comes from the TE library) | A combination of cigar strings for alignments and strand info | The 1-based position of the TE insert in the reference genome | A score that can be used to prioritize the identification of the TE if different reads disagree on the TE identification at the same location |

: Table: Example output of SWIF-TE

-   The raw output data can be best viewed in genome order:

    -   `sort -k1V,1 -k5,5n <output_file_name>`
    -   Best practice: run ./clean_SWIFTE.sh to update header with necessary info, filter for read count support (default is 5)

**Example data**

1.  Access example data files:

    1.  `cd example_data/`
    2.  `gunzip rpt.sam.gz`
    3.  `gunzip genomic.sam.gz`
    4.  'cd ..'

2.  Run SWIF-TE with these files to make sure it's working correctly.

    1.  `./SWIFTEv35 example_data/genomic.sam example_data/rpt.sam`
    2.  `sort -k1,1 -k2,2n genomic.sam.inserts.txt`

3.  Expected output:

    | Position | TE        |
    |----------|-----------|
    | 1000000  | TNAT1A    |
    | 2000000  | AT9NMU1   |
    | 3000000  | ATLINE1A  |
    | 4000000  | ATENSPM8  |
    | 5000000  | ATENSPM9  |
    | 6000000  | ATENSPM4  |
    | 7000000  | ATENSPM5  |
    | 8000000  | ATENSPM6  |
    | 9000000  | ATENSPM7  |
    | 10000000 | ATENSPM1  |
    | 11000000 | ATENSPM2  |
    | 12000000 | ATENSPM3  |
    | 13000000 | VANDAL20  |
    | 14000000 | ATTIRX1D  |
    | 15000000 | ATTIRX1C  |
    | 16000000 | ATHILA    |
    | 17000000 | ATCOPIA28 |
    | 18000000 | ATCOPIA29 |
    | 19000000 | ATCOPIA26 |
    | 20000000 | ATCOPIA27 |
    | 21000000 | ATCOPIA24 |
    | 22000000 | ATCOPIA25 |
    | 23000000 | ATCOPIA22 |
    | 24000000 | ATCOPIA23 |
    | 25000000 | ATCOPIA20 |
    | 26000000 | ATCOPIA21 |
    | 27000000 | VANDALNX1 |
    | 28000000 | ATHPOGO   |
    | 29000000 | VANDAL17  |

    : Expected reference position of TE inserts in the read data.

### Notes

-   You can rename reads to be guaranteed unique names with something like:

    -   `awk {if(NR % 4 == 1) {print "\@" NR};if(NR % 4 == 2){print \$1};if(NR % 4 ==3){print"+" };if(NR % 4 == 0){print\$1}} input.fastq > input_renamed.fastq`

## Support

If you encounter any issues or have questions about SWIF-TE, please email (menar060@umn.edu) or submit a Github ticket!

## Feedback

We value your feedback! Help us improve SWIF-TE by sharing your thoughts and suggestions with us. Send your feedback to menar060@umn.edu.
## Collaborators

Thank you to everyone who helped write, develop and benchmark SWIF-TE. Special thanks to Adrian Platts and Nathan Catlin at MSU.


------------------------------------------------------------------------
