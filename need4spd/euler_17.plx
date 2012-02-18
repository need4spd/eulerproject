#!/usr/bin/perl

use strict;
use warnings;

my %alpha_hash = (1=>"one",
2=>"two",
3=>"three",
4=>"four",
5=>"five",
6=>"six",
7=>"seven",
8=>"eight",
9=>"nine",
10=>"ten",
11=>"eleven",
12=>"twelve",
13=>"thirteen",
14=>"fourteen",
15=>"fifteen",
16=>"sixteen",
17=>"seventeen",
18=>"eighteen",
19=>"nineteen",
20=>"twenty",
30=>"thirty",
40=>"forty",
50=>"fifty",
60=>"sixty",
70=>"seventy",
80=>"eighty",
90=>"ninety");

my $sum_of_word_len=0;

foreach my $x ((1..1000)) {
    if ($x > 0 and $x <=20) {
        $sum_of_word_len+=length ($alpha_hash{$x});

        print "a=$alpha_hash{$x}, sum_of_word_len=$sum_of_word_len \n";
            
    } elsif ($x > 20 and $x <= 99) {
        my $t = substr($x, 0, 1);
        my $o = substr($x, 1, 1);
        my $key = $t."0";
        
        my $temp1 = $alpha_hash{$key};
        my $temp2 = $alpha_hash{$o};
        
        my $sum_of_len = 0;
        
        if ($o == 0) {
            $sum_of_len = length($temp1);
            $sum_of_word_len+=$sum_of_len;
        } else {
            $sum_of_len = length ($temp1) + length ($temp2);
            $sum_of_word_len+=$sum_of_len;
            
            $alpha_hash{$x} = $temp1.$temp2;
        }
        
        print "t=$t, o=$o, key=$key, temp1=$temp1, temp2=$temp2, sum_of_len=$sum_of_len, sum_of_word_len=$sum_of_word_len \n";
        
    } elsif ($x > 99 and $x < 1000) {
        my $h = substr($x, 0, 1);
        my $t = int(substr($x, 1, 2));
        
        my $temp1 = $alpha_hash{$h};
        my $temp2 = "hundred";
        my $temp3 = $alpha_hash{$t};
        
        my $sum_of_len = 0;
        
        if ($t == 0) {
            $sum_of_len = length ($temp1) + length ($temp2);
            $sum_of_word_len+=$sum_of_len;
        } else {
            $temp2 = "hundredand";
            $sum_of_len = length ($temp1) + length ($temp2) + length ($temp3);
            $sum_of_word_len += $sum_of_len;
        }
        
        print "h=$h, t=$t, temp1=$temp1, temp2=$temp2, temp3=$temp3, sum_of_len=$sum_of_len, sum_of_word_len=$sum_of_word_len \n";
        
    } else {
        $sum_of_word_len += length ("onethousand");
    }
}

print $sum_of_word_len;