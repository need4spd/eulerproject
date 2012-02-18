#!/usr/bin/perl

use strict;
use warnings;

sub number_of_prime_factors {
    my ($num) = @_;
    
    if ($num == 1) {
        return 1;
    }
    
    my $start_num = 2;
    my %exponent_hash;
    
    my $quota = 0;
    my $rest = 0;
    
    while (1) {
        $quota = $num / $start_num;
        $rest = $num % $start_num;
        
        if ($rest == 0) {
            if (exists $exponent_hash{$start_num}) {
                $exponent_hash{$start_num} = $exponent_hash{$start_num} + 1;
            } else {
                $exponent_hash{$start_num} = 1;
            }
            
            ($start_num, $num) = (2, $quota);
        } else {
            $start_num += 1;
        }
        
        if ($quota == 1 and $rest == 0) {
            last;
        }
    }
    
    my @v = values %exponent_hash;
    my $r = 1;
    foreach (@v) {
        $r = $r * ($_ + 1);
    }
    
    return $r;
}

my $i = 1;
my $result = 0;

while (1) {
    $result+=$i;
    $i+=1;
    
    my $number_of_prime = &number_of_prime_factors($result);
    
    if ($number_of_prime >= 500) {
        print $result;
        last;
    }
}