#!/usr/bin/perl

use strict;
use warnings;
use Math::Complex;

sub is_prime {
    (my $n) = @_;
    
    if ($n == 2) {
        return 1;
    } elsif ($n % 2 == 0) {
        return 0;
    }
    
    my $i = 3;
    my $range = sqrt($n) + 1;
    
    while ($i < $range) {
        if ($n % $i == 0) {
            return 0;
        }
        
        $i+=1;
    }
    
    return 1;
}

my $num = 2;
my $sum_of_prime = 0;

while (1) {
    if (is_prime($num)) {
        $sum_of_prime+=$num;
    }
    
    $num+=1;
    
    if ($num == 2000000) {
        last;
    }
}

print $sum_of_prime;