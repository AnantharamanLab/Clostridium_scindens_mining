# Steps for downloading, mining, and analyses of Clostridium Scindens genomes

### Step 1. Downloading human gut microbiome datasets
Genomes from human gut microbiome datasets were downloaded from nine different sources as follows: 32,277 genomes were downloaded from Zeng et al. 2022, 1,200 genomes from Wilkinson et al. 2020, 120 genomes classified as _Clostridium scindens_ from Almeida et al. 2020, 1,381 genomes from Tamburini et al. 2021, 154,723 genomes from Pasolli et al. 2019, 4,997 genomes from Merrill et al. 2022 (PRJEB49206), 2,914 genomes from Lemos et al. 2022, 4,497 genomes from Gounot et al. 2022, and 31 genomes from NCBI. 

### Step 2. Identification and Classification of Clostridium Scindens Genomes
The GTDB-Tk (version 2.1.1) classify workflow (classify_wf) was run on all 202,140 genomes (Chaumeil et al. 2019), which resulted in the identification of 224 Clostridium scindens genomes. All 14 shell scripts for running these analyses (with the commands) are provided here (run_gtdbtk*.sh). Genome completeness was evaluated using CheckM v1.1.6 (Parks et al. 2015). The command used for checkM is provided in the shell script 'run_checkm_all_c_scindens_genomes.sh'. 

### Step 3. Dereplication of Clostridium Scindens Genomes
From these 224 genomes, 66 genomes were obtained after dereplication by running the dRep (version 3.4.0) dereplicate workflow (-comp 50 -pa 0.99 -sa 0.99). The drep command is provide in the shell script 'run_drep_all_c_scindens_genomes_v2.sh'.

### Step 4. Generate HMM Profiles
Experimentally-verified amino acid sequences for the proteins BaiA_2, BaiCD, BaiE, BaiF, BaiG, BaiH, BaiI, BaiJ, BaiK, BaiN, BaiP, DesA, DesB, 12alpha-HSDH, 12beta-HSDH, 3alpha-HSDH, 3beta-HSDH, 7alpha-HSDH, and 7beta-HSDH were used to generate HMM profiles. In order to create the protein-protein alignments needed to generate HMM profiles, muscle (5.1.linux64) was used with default parameters to align all amino acid sequences for each of the proteins. This alignment was converted to stockholm format using the esl-reformat function of the Easel package (version 0.48), which is provided with HMMER (version 3.3.2)." in the Generate HMM Profiles section. The alignments were then used with the hmmbuild function of the HMMER (version 3.3.2) package to generate the HMM profiles. 

### Step 5. Create Trusted Cutoffs
To generate trusted cutoffs for each of the proteins, one amino acid sequence for each of the proteins was extracted and queried against the NCBI nr protein database using the NCBI blastp suite. For each protein, the sequences for the top 500 hits from the BLAST output were downloaded. The previously-generated HMM profiles were queried against the obtained BLAST sequences for each protein sequence using hmmsearch with default parameters. The score used as a trusted cutoff was identified based on the largest changes in score from the hmmsearch outputs. The average of the two scores that constitute the largest drop in number were averaged to generate the trusted cutoffs. For 12alpha-HSDH, there was no clear large drop in score identified from the hmmsearch outputs, so no trusted cutoff was added to the HMM profile. For BaiH and BaiB, there were two large drops in score consecutively, so these three score values were averaged to generate the trusted cutoff. 

###  Step 6. Identify Protein Sequences in _C. scindens_ Genomes
The 224 identified _C. scindens_ genomes were translated into amino acid sequences using Prodigal (version 2.6.3). The generated HMM profiles were queried against the amino acid sequences for the 224 genomes using hmmsearch of the HMMER package with the flag --cut_tc.

All commands used in these analyses are provided in shell scripts in the scripts folder. Additional custom python scripts used for cleaning blast outputs and conversion of gff to fasta files are also provided in the same folder.

##### References
1. Zeng, S. et al. A compendium of 32,277 metagenome-assembled genomes and over 80 million genes from the early-life human gut microbiome. Nat Commun 13, 5139 (2022).
2. Wilkinson, T. et al. 1200 high-quality metagenome-assembled genomes from the rumen of African cattle and their relevance in the context of sub-optimal feeding. Genome Biology 21, 229 (2020).
3. Almeida, A. et al. A unified catalog of 204,938 reference genomes from the human gut microbiome. Nat Biotechnol 39, 105–114 (2021).
4. Tamburini, F. B. et al. Short- and long-read metagenomics of urban and rural South African gut microbiomes reveal a transitional composition and undescribed taxa. Nat Commun 13, 926 (2022).
5. Pasolli, E. et al. Extensive Unexplored Human Microbiome Diversity Revealed by Over 150,000 Genomes from Metagenomes Spanning Age, Geography, and Lifestyle. Cell 176, 649-662.e20 (2019).
6. Carter, M. M. et al. Ultra-deep sequencing of Hadza hunter-gatherers recovers vanishing gut microbes. Cell 186, 3111-3124.e13 (2023).
7. Lemos, L. N. et al. Large Scale Genome-Centric Metagenomic Data from the Gut Microbiome of Food-Producing Animals and Humans. Sci Data 9, 366 (2022).
8. Gounot, J.-S. et al. Genome-centric analysis of short and long read metagenomes reveals uncharacterized microbiome diversity in Southeast Asians. Nat Commun 13, 6044 (2022).
9. Chaumeil, P-S et al. GTDB-Tk: a toolkit to classify genomes with the Genome Taxonomy Database, Bioinformatics, 36(6), 1925–1927 (2020).
10. Parks DH et al. CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Res. 25(7):1043-55 (2016).







