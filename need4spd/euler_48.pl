use strict;
use warnings;
use Math::BigInt;

my $n = Math::BigInt->bzero();
foreach my $i ((1..1000)) {
    my $t = Math::BigInt->new($i);
    $t->bpow($t);
    $n->badd($t);
}

my $n_str = $n->bstr();
my $n_str_length = length $n_str;

my $r = substr $n_str, $n_str_length - 10, 10;
print "r=$r";