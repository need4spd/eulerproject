use strict;
use warnings;

my $limit = 999999;
my $result = 0;

foreach my $n ((3..$limit)) {
    my $temp = 0;
    
    foreach my $c (split //, $n) {
        if ($c == 0) {
            $temp += 1;
        } else {
            my $fact_temp = 1;
            foreach my $d (1..$c) {
                $fact_temp = $fact_temp * $d;
            }
            
            $temp += $fact_temp;
        }
    }
    
    if ($n == $temp) {
        $result += $n;
    }
}

print "$result";
