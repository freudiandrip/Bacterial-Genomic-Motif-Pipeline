#!/usr/bin/python

#gene_locations.py takes in one .txt file of positions resulting in a motif hit
#and a .gbk file with genome + annotations of gene characterization
#*USES: Biopython, SeqIO lib: http://biopython.org/wiki/SeqIO

import os
import sys, Bio, getopt
from Bio import SeqIO

def gene_locations(gbk, posns, motif, output, rangestart, rangeend):
    # using biopython to parse through gbk file
    gbank = SeqIO.read(open(gbk, "r"), 'genbank')
    #data ouput
    genes = [] #no characterization of gene --> empty string pasted in
    start_end_site = []
    product = []
    motifs = []
    #while loop to parse through gbk data; adds genes, product,
    # start + end site per annotation in CDS.
    infile_motif = open(posns, "r")
    motif_posn = infile_motif.readline()
    #checking each motif, and if there is a hit in the gbk data.
    while motif_posn != "":
        i = 0
        #while loop to traverse through gbank data:
        while i < len(gbank.features):
            feature = gbank.features[i]
            #indexing for the start codon for gene
            if feature.type == "CDS":
                idx1 = str(feature.location).find("[")
                idx2 = str(feature.location).find(":")
                codon = str(feature.location)[idx1 + 1:idx2]
                posn = int(motif_posn) + len(motif) - int(codon)
            #only want genes if 200 away from a motif
                if posn <= int(rangeend) and posn > int(rangestart):
            #grabbing gbank features from ADT storageself
                   genes.append(feature.qualifiers['gene'][0])
                   start_end_site.append(feature.location)
                   motifs.append(motif_posn.rstrip())
                   if 'product' in feature.qualifiers:
                     product.append(feature.qualifiers['product'][0])
                   else:
                     product.append("-")
            #moving on to the next entry in gbank
            i += 1
        #moving on to next motif in positions file
        motif_posn = infile_motif.readline()
    #done reading the motif file.
    infile_motif.close()
    #writing results into output file with gene, CDS region, product.
    outfile = open(output, "w")
    #first column of the outfile.
    outfile.write('hit #:\t' 'motif position:\t' + 'gene:\t' + 'start_end_site:\t' + 'product:\n')
    #extracting info from list to output file.
    for i in range(len(genes)):
    #writes out info related per motif hit.
        outfile.write(str(i+1) + '\t')
        outfile.write(str(motifs[i]) + '\t')
        outfile.write(str(genes[i]) + '\t')
        outfile.write(str(start_end_site[i]) + '\t')
        outfile.write(str(product[i]) + '\n')
    #file writing complete
    outfile.close()


def main(argv):
    gbk = ''
    positions = ''
    motif = ''
    outfile = ''
    try:
        opts, args = getopt.getopt(argv,"hg:p:m:o:",["genbank-file=","positions-file=","motif=","outfile="])
    except getopt.GetoptError:
        print 'biopy_gene_location.py -g <genbank-file> -p <positions-file> -m <motif> -o <outfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'biopy_gene_location.py -g <genbank-file> -p <positions-file> -m <motif> -o <outfile>'
            sys.exit()
        elif opt in ("-g", "--genbank-file"):
            gbk = arg
        elif opt in ("-p", "--positions-file"):
            positions = arg
        elif opt in ("-m", "--motif"):
            motif = arg
        elif opt in ("-o", "--outfile"):
            outfile = arg
    gene_locations(gbk, positions, motif, outfile,0, 200)

if __name__ == "__main__":
   main(sys.argv[1:])



