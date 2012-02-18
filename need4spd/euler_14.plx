#!/usr/bin/perl

use strict;
use warnings;

sub a {
    my ($num) = @_;
    return $num/2;
}

sub b {
    my ($num) = @_;
    return (3*$num)+1;
}

my $target_num = 1000000;
my $loop_cnt = 1;

my $biggest_loop_cnt = 0;
my $biggest_loop_cnt_num = 0;

my $r = $target_num;

while (1) {
    if ($r % 2 == 0) {
        $r = &a($r);
    } else {
        $r = &b($r);
    }
    
    $loop_cnt+=1;
    
    if ($r == 1) {
        if ($biggest_loop_cnt < $loop_cnt) {
            $biggest_loop_cnt = $loop_cnt;
            $biggest_loop_cnt_num = $target_num;
        }
        
        $loop_cnt = 1;
        $target_num-=1;
        $r = $target_num;
    }
    
    if ($target_num == 1) {
        last;
    }
}

print $biggest_loop_cnt_num;