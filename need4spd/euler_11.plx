#!/usr/bin/perl

use strict;
use warnings;

open PRB, "euler_11_prb.txt";

#my @a=();
my %a;
my $key=0;
while(defined(my $line=<PRB>)) {
    chomp($line);
    
    my @temp = split /\s+/, $line;
    print "@temp \n";
    
    $a{$key}=[@temp];
    $key+=1;
}

my $max = 0;
foreach my $i ((0..16)) {
    foreach my $j ((0..16)) {
        my $horizontal = $a{$i}[$j] *  $a{$i}[$j+1] * $a{$i}[$j+2] *  $a{$i}[$j+3];
        my $vertical = $a{$i}[$j] * $a{$i+1}[$j] * $a{$i+2}[$j] * $a{$i+3}[$j];
        my $right_diag = $a{$i}[$j] *  $a{$i+1}[$j+1] * $a{$i+2}[$j+2] *  $a{$i+3}[$j+3];
        my $left_diag = $a{$i}[$j+3] *  $a{$i+1}[$j+2] * $a{$i+2}[$j+1] *  $a{$i+3}[$j];
        
        my @t = ($horizontal, $vertical, $right_diag, $left_diag);
        @t = reverse sort {$a <=> $b} @t;    
        my $iteration_max = $t[0];
        
        if ($max < $iteration_max) {
            $max = $iteration_max;
        }
    }
}

print $max;


