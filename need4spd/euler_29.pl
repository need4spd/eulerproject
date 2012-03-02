use strict;
use warnings;
use Set::Light;
use Math::BigInt;

my $r = Set::Light->new();

foreach my $a ((2..100)) {
    foreach my $b ((2..100)) {
        my $temp = Math::BigInt->new($a);
        $temp->bpow($b);
        print "$temp \n";
        $r->insert($temp);
    }
}

my $size = $r->size();

print "$size";