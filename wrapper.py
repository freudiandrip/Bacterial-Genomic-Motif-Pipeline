#!/usr/bin/python

import sys, getopt, os

def main(argv):
  genbankfile = ''
  resultsfile = ''
  motif = ''
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
  os.system("perl getLocations.pl " + genbankfile + " genbank testfasta fasta " + motif + " " + resultsfile)
  # Insert call to second script here
if __name__ == "__main__":
   main(sys.argv[1:])
