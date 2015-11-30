#!/usr/bin/python

#gene_locations.py takes in one .txt file of positions resulting in a motif hit
#and a .gbk file with genome + annotations of gene characterization
#*USES: Biopython, SeqIO lib: http://biopython.org/wiki/SeqIO

import os
import sys, Bio, getopt
from Bio import SeqIO

def gene_locations(gbk, posns, motif):
    # using biopython to parse through gbk file
    gbank = SeqIO.read(open(gbk, "r"), 'genbank')
    #data ouput
    genes = [] #no characterization of gene --> empty string pasted in
    start_end_site = []
    product = []
    #while loop to parse through gbk data; adds genes, product,
    # start + end site per annotation in CDS.
    infile_motif = open(posns, "r")
    motif_posn = infile_motif.readline()
    #checking each motif, and if there is a hit in the gbk data.
    while motif_posn != "":
        #while loop to traverse through gbank data:
	i = 0
        while i < len(gbank.features):
            feature = gbank.features[i]
	    if feature.type == "CDS":
              #print feature.qualifiers['codon_start']
              #print int(motif_posn) + len(motif) - int(feature.qualifiers['codon_start'][0])
              idx1 = str(feature.location).find("[")
              idx2 = str(feature.location).find(":")
              codon = str(feature.location)[idx1 + 1:idx2]
              posn = int(motif_posn) + len(motif) - int(codon)
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


def main(argv):
  gbk = ''
  positions = ''
  motif = ''
  try:
      opts, args = getopt.getopt(argv,"hg:p:m:",["genbank-file=","positions-file=","motif="])
  except getopt.GetoptError:
      print 'biopy_gene_location.py -g <genbank-file> -p <positions-file> -m <motif>'
      sys.exit(2)
  for opt, arg in opts:
     if opt == '-h':
        print 'biopy_gene_location.py -g <genbank-file> -p <positions-file> -m <motif>'
        sys.exit()
     elif opt in ("-g", "--genbank-file"):
        gbk = arg
     elif opt in ("-p", "--positions-file"):
        positions = arg
     elif opt in ("-m", "--motif"):
        motif = arg
  gene_locations(gbk, positions, motif)

if __name__ == "__main__":
   main(sys.argv[1:])



