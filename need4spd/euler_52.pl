use strict;
use warnings;

sub is_permutations {
    my ($a, $b) = @_;
     
    #print "$a, $b \n";
    my @s_a = split //, $a;
    @s_a = sort @s_a;
    my $a_str = join "", @s_a;
     
    my @s_b = split //, $b;
    @s_b = sort @s_b;
    my $b_str = join "", @s_b;

    
    #print "@s_a, @s_b \n";      
    if ($a_str == $b_str) {
        return 1;
    } else {
        return 0;
    }
}

my $n = 125874;
while (1) {
    
    if (is_permutations($n, $n*2) and is_permutations($n, $n*3) and is_permutations($n, $n*4) and is_permutations($n, $n*5) and is_permutations($n, $n*6)) {
        print "n=$n";
        last;
    }
    
    $n += 1;
}