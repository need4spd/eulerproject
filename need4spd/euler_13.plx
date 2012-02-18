#!/usr/bin/perl

use strict;
use warnings;

open PRB, "euler_13_problem.txt";

my $num;
while(defined(my $line=<PRB>)) {
    chomp($line);
    
    $num+=$line;
}

my $result = substr($num, 0, 10);
print $result;