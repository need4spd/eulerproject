#!/usr/bin/perl

use strict;
use warnings;

sub sum_of_square {
    my(@num_list) = @_;
    
    my $result = 0;
    
    foreach my $num (@num_list) {
        my $t = $num**2;
        $result += $t;
    }
    
    $result;
}

sub square_of_sum {
    my(@num_list) = @_;
    
    my $result = 0;
    
    foreach my $num (@num_list) {
        $result+=$num;
    }
    
    $result**2;
}

my $r1 = sum_of_square((1..100));
my $r2 = square_of_sum((1..100));

print ($r2 - $r1);