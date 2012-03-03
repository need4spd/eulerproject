use strict;
use warnings;
use List::Util qw (sum);

my $limit = (9**5)*6;
my @r_list = ();

foreach my $n ((2..$limit)) {
    my $sum=0;
    
    foreach my $c (split //, $n) {
        $sum = $sum + ($c**5);
    }
    
    if ($sum == $n) {
        push @r_list, $n
    }
}

my $r = sum @r_list;
print "$r";
