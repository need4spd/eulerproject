use strict;
use warnings;
use bigint;

sub fib {
    my ($n) = @_;
    
    my ($a, $b) = (0, 1);
    
    foreach (0..$n) {
        ($a, $b) = ($b, $a+$b);
    }
    
    return $a;
}


my $n = 1;
while(1) {
    my $r = fib($n);
    my $l = length($r); 
    print "$l \n";
    if ($l == 1000) {
        print "$n";
        last;
    }
    
    $n+=1;
}