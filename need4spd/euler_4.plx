#!/usr/bin/perl

use strict;
use warnings;

sub is_symmetry_num {
    my($num) = @_;
    
    my $reversed_num = scalar reverse $num;
    
    if ($reversed_num == $num) {
        return 1;
    } else {
        return 0;
    }
}

my @target1 = (1..1000);
my @target2 = (1..1000);

my $biggest_num = 0;

foreach my $num1 (@target1) {
    foreach my $num2 (@target2) {
        my $a = $num1 * $num2;
        
        if (is_symmetry_num($a) and $biggest_num < $a) {
            $biggest_num = $a;
        }
    }
}

print $biggest_num;