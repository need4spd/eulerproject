#!/usr/bin/perl

use strict;
use warnings;

sub fib_up_to {
    my $maxnum = shift @_;
    
    my $i1 = 1;
    my $i2 = 1;
    
    my @fib_list=();
    
    while ($i1 <= $maxnum) {
        push @fib_list, $i1;
        
        ($i1, $i2) = ($i2, $i1+$i2);
    }
    
    @fib_list;
}

my @result_list=fib_up_to(4000000);

my $sum = 0;
foreach my $num (@result_list) {
    if ($num%2 == 0) {
        $sum+=$num;
    }
}

print $sum;