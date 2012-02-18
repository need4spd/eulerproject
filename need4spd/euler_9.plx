#!/usr/bin/perl
use strict;
use warnings;

my $n = 1;
my $m = 2;

while (1) {
    my $r = ($m**2) + ($m*$n);
    
    if ($r == 500) {
        print $m, $n;
        last;
    }
    
    $m+=1;
    if ($m == 500) {
        $n+=1;
        $m=$n+1;
    }
}

my $a=($m**2) - ($n**2);
my $b=2*$m*$n;
my $c=($m**2) + ($n**2);

print "a=$a , b=$b, c=$c \n";
my $d = $a*$b*$c;
print "result=$d";