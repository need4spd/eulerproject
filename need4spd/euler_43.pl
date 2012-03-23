use strict;
use warnings;

use List::Permutor;

my $perm = new List::Permutor qw /0 1 2 3 4 5 6 7 8 9/;

my %rule = (1=>2, 2=>3, 3=>5, 4=>7, 5=>11, 6=>13, 7=>17);

my $sum_of_result = 0;

while (my @p = $perm->next) {
    my $s = join "", @p;
    
    my $is_right = 1;
    
    foreach my $k (keys %rule) {
        unless ((substr $s, $k, 3) % $rule{$k} == 0) {
            $is_right = 0;
            last;
        }
    }
    
    if ($is_right) {
        $sum_of_result += $s;
    }
}

print "$sum_of_result";