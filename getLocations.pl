use Bio::SeqIO;
# get command-line arguments, or die with a usage statement
my $usage         = "x2y.pl infile infileformat outfile outfileformat motif\n";
my $infile        = shift or die $usage;
my $infileformat  = shift or die $usage;
my $outfile       = shift or die $usage;
my $outfileformat = shift or die $usage;
my $motif 	  = shift or die $usage;
my $resultfile 	  = shift or die $usage; 


# create one SeqIO object to read in,and another to write out
my $seq_in = Bio::SeqIO->new(
                             -file   => "<$infile",
                             -format => $infileformat,
                             );
my $seq_out = Bio::SeqIO->new(
                              -file   => ">$outfile",
                              -format => $outfileformat,
                              );
 
# write each entry in the input file to the output file
while (my $inseq = $seq_in->next_seq) {
    $seq_out->write_seq($inseq);
}
# open up fasta file, read in sequence lines and print as one line
open my $fastafh, '<', $outfile;
open my $outfastafh, '>', "$outfile.fa";
my $seq = <$fastafh>;
while($seq = <$fastafh>){
  chomp($seq);
  print $outfastafh $seq;
}
print $outfastafh "\n";
close $fastafh;
`rm $outfile`; # remove temp file
close $outfastafh;
# read in file with fasta seqence as one line
open my $infile, '<', "$outfile.fa";
$seq = <$infile>;
chomp($seq);
close my $infile;
`rm $outfile.fa`;# remove temp file
# parse seqence, search and print to results file each hit of motif
my $offset = 0;
my $result = index($seq, $motif, $offset);
open my $resultfh, ">", $resultfile;
while($result != -1){
	print $resultfh $result + 1 . "\n";
	$offset = $result + 1;
	$result = index($seq, $motif, $offset);
}
close $resultfh;
