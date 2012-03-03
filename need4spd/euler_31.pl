my $n=0;

foreach my $p1 ((0..200)) {
    foreach my $p2 ((0..100)) {
        if (($p1+2*$p2) % 5 != 0) {
            next;
        }
        
        foreach my $p5 ((0..40)) {
            foreach my $p10 ((0..20)) {
                foreach my $p20 ((0..10)) {
                    if (($p1+2*$p2+5*$p5+10*$p10+20*$p20) % 50!= 0) {
                        next;
                    }
                    
                    foreach my $p50 ((0..4)) {
                        foreach my $p100 ((0..2)) {
                            foreach my $p200 ((0..1)) {
                                if (($p1+2*$p2+5*$p5+10*$p10+20*$p20+50*$p50+100*$p100+200*$p200) == 200) {
                                    $n+=1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

print "$n";