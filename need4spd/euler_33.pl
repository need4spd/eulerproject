#10n + i / 10i + d = n/d
#9nd = 10in - di
#i = remove num, d=bunmo, n=bunja
# 0 < i < 10

my $multi_of_d=1;
my $multi_of_n=1;

foreach my $i ((1..9)) {
    foreach my $n ((1..9)) {
        foreach my $d (($n+1..9)) {
            if (9*$n*$d == (10*$i*$n) - ($i*$d)) {
                my $t = 10*$i+$d;
                my $t2 = 10*$n+$i;
                
                print "n : $n, d : $d, i : $i \n";
                
                $multi_of_d = $multi_of_d * $t;
                $multi_of_n = $multi_of_n * $t2
                
            }
        }
    }
}

my $result = $multi_of_d / $multi_of_n;
print "$multi_of_d, $multi_of_n, $result \n";
