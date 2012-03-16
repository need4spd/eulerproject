use strict;
use warnings;

sub isPalidrome {
    my ($n) = @_;
    
    my $reverse_n = reverse $n;
    
    return $reverse_n == $n;
}

my $result = 0;

foreach my $n ((0..1000000)) {
    
    if (!isPalidrome($n)) {
        next;
    }
    
    if ((substr $n, 0, 1) == 0) {
        next;
    }
    
    my $n_2 = sprintf("%b", $n);
    
    if (!isPalidrome($n_2)) {
        next;
    }
    
    $result+=$n;
}

print "$result";