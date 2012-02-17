#!/usr/bin/perl

use strict;
use warnings;

sub is_prime_number {
    my($num) = @_;
    
    my $t=2;
    
    while ($t <= $num) {
        my $rest = $num % $t;
        
        if ($rest==0 and $t==$num) {
            return 1;
        } elsif ($rest == 0 and $t != $num) {
            return 0;
        } else {
            $t+=1;
        }
        
    }
    
    0;
}

sub get_prime_number {
    my($offset) = @_;
    my $target_num = 2;
    my $number_of_prime_num = 0;
    
    while (1) {
        my $r = is_prime_number($target_num);
        
        if ($r) {
            $number_of_prime_num+=1;
            
            if ($number_of_prime_num == $offset) {
                return $target_num;
            }
        }
        
        $target_num+=1;
    }
    
    return $target_num;
}

my $r = &get_prime_number(10001);
print $r."\n";