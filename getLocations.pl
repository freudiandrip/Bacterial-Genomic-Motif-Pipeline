use Bio::SeqIO;
# get command-line arguments, or die with a usage statement
my $usage         = "x2y.pl infile infileformat outfile outfileformat motif\n";
my $infile        = shift or die $usage;
my $infileformat  = shift or die $usage;
my $outfile       = shift or die $usage;
my $outfileformat = shift or die $usage;
my $motif 	  = shift or die $usage; 

print $motif . "\n";

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
open my $fastafh, '<', $outfile;
open my $outfastafh, '>', "$outfile.fa";
while(my $seq = <$fastafh>){
  chomp($seq);
  print $outfastafh $seq;
}
print $outfastafh "\n";
close $fastafh;
close $outfastafh;
open my $infile, '<', "$outfile.fa";
my $seq = <$infile>;
chomp($seq);
close my $infile;
my $offset = 0;
my $result = index($seq, $motif, $offset);
while($result != -1){
	print "$result\n";
	$offset = $result + 1;
	$result = index($seq, $motif, $offset);
}

