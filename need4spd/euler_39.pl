my %r=();

foreach my $a ((1..1000)) {
    foreach my $b ((1..1000)) {
        foreach my $c ((1..1000)) {
            
            if ($a + $b + $c > 1000) {
                last;
            }
            
            my $temp = $a**2 + $b**2;
            if ($c**2 == $temp) {
                my $p = $a + $b + $c;
                
                if ($r{$p}) {
                    $r{$p} = $r{$p} + 1;
                } else {
                    $r{$p} = 1;
                }
            }
            
        }
    }
}

@max_keys = sort {$r{$b} <=> $r{$a}} keys %r;

print "@max_keys \n";
print $max_keys[0];

