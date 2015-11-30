# Bacterial Genomic Motif Pipeline:

The pipeline consists of a series of scripts that ultimately characterizes a given motif with the nearest closest gene downstream from the position, protein product, and the CDS, with respect to each hit per a given bacterial genome.

Usage example:

python wrapper.py -g FullEColi.gbff -r ResultsFile -m ATCGTGT
