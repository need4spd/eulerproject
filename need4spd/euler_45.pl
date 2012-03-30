use strict;
use warnings;

use Set::Scalar;

my $t_n_set = Set::Scalar->new;
my $p_n_set = Set::Scalar->new;
my $h_n_set = Set::Scalar->new;

foreach my $n ((1..100000)) {
    $t_n_set->insert($n * ($n+1)/2);
    $p_n_set->insert($n*(3*$n-1)/2);
    $h_n_set -> insert($n*(2*$n-1));
}

my $r = $t_n_set->intersection($p_n_set);
$r = $r -> intersection($h_n_set);

print "$r";