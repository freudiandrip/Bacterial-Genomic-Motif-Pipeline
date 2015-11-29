'''
gene_locations.py takes in one .txt file of positions resulting in a motif hit
and a .gbk file with genome + annotations of gene characterization
*USES: Biopython, SeqIO lib: http://biopython.org/wiki/SeqIO
'''

import os
import sys, Bio
from Bio import SeqIO

def gene_locations(gbk, posns, motif):
    # using biopython to parse through gbk file
    gbank = SeqIO.read(open(gbk, "r"), 'genbank')
    #data ouput
    genes = [] #no characterization of gene --> empty string pasted in
    start_end_site = []
    product = []
    i = 0
    #while loop to parse through gbk data; adds genes, product,
    # start + end site per annotation in CDS.
    infile_motif = open(posns, "r")
    motif_posn = infile_motif.readline()
    #checking each motif, and if there is a hit in the gbk data.
    while motif != "":
        #while loop to traverse through gbank data:
        while gbank.features != []:
            feature = gbank.features[0]
            posn = len(motif) - int(feature.qualifiers['codon_start'][0])
            if posn <= 200 and posn > 0:
            #grabbing gbank features from ADT storage.
            genes.append(feature.qualifiers['gene'][0])
            start_end_site.append(feature.location)
            product.append(feature.qualifiers['product'][0])
            #moving on to the next entry in gbank
            i += 1
        #moving on to next motif in positions file
        motif_posn = infile_motif.readline()
    #done reading the motif file.
    infile_motif.close()
    #writing results into output file with gene, CDS region, product.
    outfile = open("gene-locations.txt", "w")
    #extracting info from list to output file.
    for i in range(len(genes)):
        #writes out info related per motif hit.
        outfile.write('motif hit: ' + str(i+1) + '\n')
        outfile.write('gene: ' + str(genes[i]) + '\n')
        outfile.write('start / end site: ' + str(start_end_site[i]) + '\n')
        outfile.write('product: ' + str(product[i]) + '\n')
    #file writing complete
    outfile.close()




