#!/usr/bin/perl

use strict;
use warnings;
use bigint;

my $factorial_result = 1;

foreach ((1..100)) {
    $factorial_result = $factorial_result * $_;
}

my @l = split //, $factorial_result;

my $r;

foreach (@l) {
    $r+=$_;
}

print $r;