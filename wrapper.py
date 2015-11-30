#!/usr/bin/python

import sys, getopt, os

def main(argv):
  genbankfile = ''
  resultsfile = ''
  motif = ''
  outfile = ''
  try:
      opts, args = getopt.getopt(argv,"hg:r:m:",["genbank-file=","results-file=","motif="])
  except getopt.GetoptError:
      print 'pipeline.py -g <genbank-file> -r <results-file> -m <motif>'
      sys.exit(2)
  for opt, arg in opts:
     if opt == '-h':
        print 'pipeline.py -g <genbankfile> -r <results-file> -m <motif>'
        sys.exit()
     elif opt in ("-g", "--genbank-file"):
        genbankfile = arg
     elif opt in ("-r", "--results-file"):
        resultsfile = arg
     elif opt in ("-m", "--motif"):
        motif = arg
  print 'Genbank file is :', genbankfile
  print 'Results file is :', resultsfile
  print 'Motif is :', motif
  os.system("perl getLocations.pl " + genbankfile + " genbank testfasta fasta " + motif + " " + resultsfile + ".posns")
  print 'Genbank File Parsed for Motif Matches'
  # Insert call to second script here
  os.system("python biopy_gene_locations.py -g "+ genbankfile + " -p " + resultsfile + ".posns -m " + motif + " -o " + resultsfile + ".txt")
  print 'Results Tabulated - Cleaning up'
  os.system("rm " + resultsfile + ".posns")
  print 'Done - Code available at https://github.com/sherbert-lemon/Bacterial-Genomic-Motif-Pipeline' 

if __name__ == "__main__":
   main(sys.argv[1:])
