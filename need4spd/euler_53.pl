sub fact {
    my ($n) = @_;
    
    if ($n == 1) {
        return 1
    }
    
    my $result = 1;
    foreach my $d ((1..$n)) {
        $result = $result * $d;
    }
    
    return $result;
}

sub get_number_of_cases {
    my ($n, $r) = @_;
    
    my $result = fact($n) / (fact($r) * fact($n-$r));
    return $result;
}

my $cnt = 0;

foreach my $n ((23..100)) {
    foreach my $r ((1..$n-1)) {
        if (get_number_of_cases($n, $r) > 1000000) {
            $cnt += 1;
        }
    }
}

print "$cnt";