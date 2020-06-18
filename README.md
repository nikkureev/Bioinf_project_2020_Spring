# Bioinf_project_2020_Spring

**Aegilops taushi repeatome research**

Agriculural plants have a lot of repetitive DNA in their genome.
Aegilops taushi have 4.3 Gb in length and almost 84% of it's genome sequence represented by transposons.
The most dispersed type of those sequences is LTR (Long Terminal Repeat - 66% of hole genome).

At the begining we had sequencing reslts (NovaSeq Illumina) of two samples of Aegilops taushi of different origin.
The main aim of the research was to determinate the reason of repetitive sequences enreachment and it's influence on plants.

Our main objects represented below:
* to investigate reads quality by using FastQC
* reads quality correction by Trimmomatic in PE-mode
* using Repeat Explorer with TAREAN in Comparative mode for clustering reads to find repeats
* using DANTE to find revertase and integrase domains in found clusters
* building phylogenetic trees using DANTE output
* statistic analysis using TAREAN output
* comparing reads proportion by each sample in same clusters
* making conclusions

Using Repeat Explorer output we obtained statistics about reads distribution among repeat types.
It turned out that Ty1/copia is the most numerous repeat type in our samples.
It belongs to Class II transposon family. Using R Studio we built a barplot.
![screenshot of sample](https://github.com/nikkureev/Bioinf_project_2020_Spring/blob/master/Barplot.png?raw=true)

Also we had statistics about distribution of reads from different samples in same clusters.
Here the dotplot built by R Studio which represent reads distribution.
![screenshot of sample](https://github.com/nikkureev/Bioinf_project_2020_Spring/blob/master/Dotplot.png?raw=true)

Using Geneious tool we built phylogenetic trees.
We used reverse transcriptase and integrase domains for distinguishing does clusters with same annotated groups have same domain structure. 

Tree based on INT domain.
![screenshot of sample](https://github.com/nikkureev/Bioinf_project_2020_Spring/blob/master/INT_tree.png?raw=true)

Tree based on RT domain.
![screenshot of sample](https://github.com/nikkureev/Bioinf_project_2020_Spring/blob/master/RT_tree.png?raw=true)

Based on the dotplot and barplot results we cannot conclude that we have significant differences between two samples.
To make sure do we have interesting clusters we decided to use Mann-Witeny statistical test.
We had a table consist of numbers of reads of two samples and we used it to run test.

