use strict;
use warnings;
use Math::Complex;

sub is_pentagonal {
    my ($n) = @_;
    $n = abs $n;
    my $p = (sqrt(1 + 24 *$n) + 1) / 6;
    
    return $p == int $p;
}

my @pent_list=qw (1);
my $i = 0;
my $not_found = 1;

while ($not_found) {
    $i += 1;
    my $penta_n = $i * (3*$i - 1) / 2;
    push @pent_list, $penta_n;
    
    foreach my $j ((2..$#pent_list - 1)) {
        if (&is_pentagonal($pent_list[$i] - $pent_list[$j]) and
            &is_pentagonal($pent_list[$i] + $pent_list[$j])) {
            print scalar($pent_list[$i] - $pent_list[$j]);
            $not_found = 0;
            last;
        }
    }
}