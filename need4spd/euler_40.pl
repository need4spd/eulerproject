my $s = "";
foreach my $n ((0..300000)) {
    $s=$s.$n;
    
    if (length $s > 1000000) {
        last;
    }
}


my @l = split //, $s;
my $result = $l[1] * $l[10] * $l[100] * $l[1000] * $l[10000] * $l[100000] * $l[1000000];

print "$result \n";