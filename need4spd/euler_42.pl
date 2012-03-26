use strict;
use warnings;
use Math::Complex;
use List::MoreUtils qw(first_index);
 
open PRB, "euler_42_words.txt";
 
my $names_str;
while(defined(my $line=<PRB>)) {
    chomp($line);
    $names_str = $line;
}
 
$names_str =~ s/\"//g;
 
my @names_list=split /,/, $names_str;

my @alpha_list=('A'..'Z');

sub getNameScore {
    
    my ($name) = @_;
    
    my $char_score_sum = 0;
    foreach my $byte (split //, $name) {
        my $char_score = first_index {$_ eq $byte} @alpha_list;
        #print "byte : $byte , char_score : $char_score \n";        
        $char_score_sum = $char_score_sum + $char_score + 1;
    }
    
    return $char_score_sum;
}

sub isTriangleNumber {
    my ($n) = @_;
    
    my $temp_n = $n * 2;
    my $start_num = int(sqrt($temp_n)) - 1;
    
    while(1) {
        my $s = $start_num**2 + $start_num;
        if ($temp_n == $s) {
            return 1;
        }
        
        if ($temp_n < $s) {
            return 0;
        }
        
        $start_num += 1;
    }
}

my $cnt_of_result = 0;

foreach my $name (@names_list) {
    my $name_score = getNameScore($name);
    
    #print "$name_score \n";
    if (isTriangleNumber($name_score)) {
        $cnt_of_result += 1;
    }
}

print "$cnt_of_result";