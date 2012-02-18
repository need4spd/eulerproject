#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#my $a = Math::BigInt->new(2)->bpow(1000)->bstr();
my $a=2**1000;

my @l = split //, $a;

my $r;
foreach (@l) {
    $r += $_;
}

print $r;
