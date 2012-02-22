#!/usr/bin/perl

use strict;
use warnings;

open PRB, "<", "euler_18_problem.txt";

my %a;
my $key=14;
while(defined(my $line=<PRB>)) {
    chomp($line);
    
    my @temp = split /\s+/, $line;
    
    my $size = @temp;    
    print "Size : $size, Array : @temp \n";
    $a{$key}=[@temp];
    $key-=1;
}

foreach my $row ((0..13)) {
    foreach my $col ((0..13-$row)) {
        
        my @t1=$a{$row}[$col];
        print "row : $row, col : $col, array : @t1 \n";
        
        my $first_sum = $a{$row}[$col] + $a{$row+1}[$col];
        my $second_sum = $a{$row}[$col+1] + $a{$row+1}[$col];
        
        my @t = ($first_sum, $second_sum);
        @t = reverse sort {$a <=> $b} @t;    
        my $max_of_two = $t[0];
        
        print "max_of_two : $max_of_two \n";
        
        $a{$row+1}[$col] = $max_of_two;
    }
    
    print join(" ",$a{$row+1}),"\n";
    #print "$a{$row+1}";
}

