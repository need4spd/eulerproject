#!/usr/bin/perl

use strict;
use warnings;
use 5.012;

sub primefactors {
    
    my $num = shift @_;
    
    my $start_num = 2;
    my @prime_numbers = ();
    
    my $quota = 0;
    my $rest = 0;
    
    while (1) {
        $quota = $num / $start_num;
        $rest = $num % $start_num;
        
        if ($rest == 0) {
            push @prime_numbers, $start_num;
            ($start_num, $num) = (2, $quota);
        } else {
            $start_num+=1;
        }
        
        if ($quota == 1 and $rest == 0) {
            last;
        }
    }
    
    @prime_numbers;
}

sub by_num {
    if ($a < $b) { -1 }
    elsif ($a > $b) { 1 }
    else { 0 }
}

my @prime_numbers = primefactors(600851475143);

my @sorted = reverse sort by_num @prime_numbers;

print $sorted[0];