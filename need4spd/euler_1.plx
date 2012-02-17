#!/usr/bin/perl

use strict;
use warnings;

my $result=0;

for my $num ((1..999)) {
    if ($num%3 ==0 or $num%5==0) {
        $result+=$num;
    }
}

print $result;
