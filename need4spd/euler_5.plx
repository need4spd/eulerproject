#!/usr/bin/perl

use strict;
use warnings;

my @number_list = (1..20);

my $num = 1;

while (1) {
    my $is_search = 1;
    
    foreach my $n (@number_list) {
        my $r = $num % $n;
        
        if ($r != 0) {
            $is_search = 0;
            $num+=1;
            last
        }
    }
    
    if ($is_search) {
        print $num."\n";
        last;
    }
}