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
It belongs to Class II transposon family.
![screenshot of sample](https://github.com/nikkureev/Bioinf_project_2020_Spring/blob/master/Barplot.png?raw=true)
